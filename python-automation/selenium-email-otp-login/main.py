from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from imapclient import IMAPClient
import pyzmail
import time
import re
from datetime import datetime, timezone
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import threading


print("Waiting 15 seconds before starting the browser automation...")
time.sleep(15)

LOGIN_URL = "https://portal.example.com/login"

CODE_WAIT_TIMEOUT = 180
FUTURE_ALLOWANCE_SECONDS = 14400


def load_email_env():
    env_path = ".env.email"
    config = {}

    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

        print(f"[INFO] Loaded email configuration from {env_path}")

    else:
        print(f"[INFO] {env_path} was not found. Please enter email settings manually.")
        print("[INFO] For Gmail, use an App Password instead of your regular account password.")

        config["EMAIL"] = input("Email: ").strip()
        config["EMAIL_PASSWORD"] = input("Email App Password: ").strip()
        config["IMAP_SERVER"] = input("IMAP server [imap.gmail.com]: ").strip() or "imap.gmail.com"

        port = input("IMAP port [993]: ").strip()
        config["IMAP_PORT"] = int(port) if port else 993

        config["IMAP_FOLDER"] = input("IMAP folder [INBOX]: ").strip() or "INBOX"

        with open(env_path, "w", encoding="utf-8") as file:
            file.write(f"EMAIL={config['EMAIL']}\n")
            file.write(f"EMAIL_PASSWORD={config['EMAIL_PASSWORD']}\n")
            file.write(f"IMAP_SERVER={config['IMAP_SERVER']}\n")
            file.write(f"IMAP_PORT={config['IMAP_PORT']}\n")
            file.write(f"IMAP_FOLDER={config['IMAP_FOLDER']}\n")

        print(f"[INFO] Email configuration saved to {env_path}")

    return config


def get_new_verification_code_after_action(ts_after_action, max_age_seconds=120):
    """
    Search for a new verification email received after the web action timestamp.
    """

    with IMAPClient(IMAP_SERVER, port=IMAP_PORT, ssl=True) as client:
        client.login(EMAIL, EMAIL_PASSWORD)
        client.select_folder(IMAP_FOLDER)

        start_time = time.time()
        tried_relaxed_filter = False

        while time.time() - start_time < CODE_WAIT_TIMEOUT:
            messages = client.search(["ALL"])
            now = datetime.now(timezone.utc)
            found_valid_email = False

            for uid in reversed(messages):
                envelope = client.fetch([uid], ["ENVELOPE"])[uid][b"ENVELOPE"]
                msg_date = envelope.date.replace(tzinfo=timezone.utc)

                age = (now - msg_date).total_seconds()
                future_delta = (msg_date - now).total_seconds()
                after_action_delta = msg_date.timestamp() - ts_after_action

                subject = envelope.subject.decode() if envelope.subject else ""

                print(
                    f"UID: {uid}, Subject: {subject}, Date: {msg_date}, "
                    f"Age: {age}, ΔafterAction={after_action_delta}, Δfuture={future_delta}"
                )

                if future_delta > FUTURE_ALLOWANCE_SECONDS:
                    continue

                is_recent_after_action = msg_date.timestamp() > ts_after_action and age <= max_age_seconds
                is_recent_relaxed = tried_relaxed_filter and age <= 600

                if is_recent_after_action or is_recent_relaxed:
                    found_valid_email = True

                    raw_message = client.fetch([uid], ["BODY[]"])[uid][b"BODY[]"]
                    message = pyzmail.PyzMessage.factory(raw_message)

                    email_subject = message.get_subject()

                    if "verification code" in email_subject.lower() or "code" in email_subject.lower():
                        text = None

                        if message.text_part:
                            text = message.text_part.get_payload().decode(message.text_part.charset)

                        elif message.html_part:
                            text = message.html_part.get_payload().decode(message.html_part.charset)

                        if text:
                            match = re.search(r"\b(\d{6})\b", text)

                            if match:
                                code = match.group(1)
                                print(f"[OK] Verification code found: {code}")
                                return code

            if not found_valid_email:
                print("[INFO] No valid verification emails found after the web action.")

            if not tried_relaxed_filter and time.time() - start_time > 60:
                print("[INFO] Expanding search filter to emails from the last 10 minutes.")
                tried_relaxed_filter = True

            time.sleep(1)

        print("[WARN] Verification code was not found within the timeout.")
        return None


def print_latest_email_info():
    """
    Print diagnostic information about the latest email in the inbox.
    """

    print("=== Latest Email Information ===")

    with IMAPClient(IMAP_SERVER, port=IMAP_PORT, ssl=True) as client:
        client.login(EMAIL, EMAIL_PASSWORD)
        client.select_folder(IMAP_FOLDER)

        messages = client.search(["ALL"])

        if not messages:
            print("[WARN] Inbox is empty.")
            return

        latest_uid = messages[-1]
        envelope = client.fetch([latest_uid], ["ENVELOPE"])[latest_uid][b"ENVELOPE"]

        msg_date = envelope.date.replace(tzinfo=timezone.utc)
        subject = envelope.subject.decode() if envelope.subject else ""

        print(f"UID: {latest_uid}")
        print(f"Subject: {subject}")
        print(f"Date UTC: {msg_date}")
        print(f"Timestamp: {msg_date.timestamp()}")
        print("===============================")


def get_latest_code_from_subject():
    """
    Extract a 6-digit verification code from the latest email subject.
    """

    with IMAPClient(IMAP_SERVER, port=IMAP_PORT, ssl=True) as client:
        client.login(EMAIL, EMAIL_PASSWORD)
        client.select_folder(IMAP_FOLDER)

        messages = client.search(["ALL"])

        if not messages:
            print("[WARN] Inbox is empty.")
            return None

        latest_uid = messages[-1]
        envelope = client.fetch([latest_uid], ["ENVELOPE"])[latest_uid][b"ENVELOPE"]

        subject = envelope.subject.decode() if envelope.subject else ""

        match = re.match(r"^(\d{6})", subject.strip())

        if match:
            return match.group(1)

        print(f"[WARN] Verification code was not found in subject: {subject}")
        return None


config = load_email_env()

EMAIL = config.get("EMAIL", "")
EMAIL_PASSWORD = config.get("EMAIL_PASSWORD", "")
IMAP_SERVER = config.get("IMAP_SERVER", "imap.gmail.com")
IMAP_PORT = int(config.get("IMAP_PORT", 993))
IMAP_FOLDER = config.get("IMAP_FOLDER", "INBOX")


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get(LOGIN_URL)

wait = WebDriverWait(driver, 30)


login_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-button"))
)
print("[OK] Login button found.")
login_button.click()
print("[OK] Login button clicked.")


email_input = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email'][name='email']"))
)
print("[OK] Email input found.")
email_input.clear()
email_input.send_keys(EMAIL)
print("[OK] Email entered.")


continue_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'].primary-action"))
)
print("[OK] Continue button found.")

ts_before_continue = time.time()

continue_button.click()
print("[OK] Continue button clicked.")


print("[INFO] Waiting 30 seconds for the verification email...")
time.sleep(30)

code = get_latest_code_from_subject()

if code:
    print(f"[OK] Verification code from email subject: {code}")

    otp_inputs = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[aria-label^='One time password input']")
        )
    )

    if len(otp_inputs) >= 6:
        for index, digit in enumerate(code):
            otp_inputs[index].clear()
            otp_inputs[index].send_keys(digit)

        print("[OK] Verification code entered into OTP fields.")

    else:
        print("[WARN] Not all OTP input fields were found.")

else:
    print("[WARN] Failed to find verification code in the latest email subject.")


def delayed_quit(driver_instance, delay=60):
    time.sleep(delay)
    driver_instance.quit()


threading.Thread(target=delayed_quit, args=(driver, 60), daemon=True).start()
