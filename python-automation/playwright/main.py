from playwright.sync_api import sync_playwright
import time
import os

# Sanitized Playwright Browser Extension Workflow
#
# This script is based on a real browser automation workflow.
# All URLs, selectors, extension names, credentials, and business-specific logic
# have been replaced with generic placeholders for portfolio demonstration.
#
# Purpose:
# - launch Chromium with a browser extension
# - initialize extension session
# - authenticate on a web portal
# - handle extension popups
# - execute JavaScript for dynamic UI elements
# - monitor dashboard metrics
# - save metric history to a file

BROWSER_EXTENSION_PATH = os.path.abspath("browser_extension")
USER_DATA_DIR = os.path.abspath("user_data")

AUTH_DATA_FILE = "auth_data.txt"
EXTENSION_PASSWORD = "ExampleStrongPassword123!"
METRICS_FILE = "metrics_history.txt"

PORTAL_URL = "https://portal.example.com/"


def fill_authentication_fields(page, auth_values):
    """Fill authentication fields on the browser extension recovery/import screen."""
    try:
        values = auth_values.split()

        for index, value in enumerate(values[:12]):
            selector = f"#auth-word-{index}"
            page.fill(selector, value)

        return True

    except Exception as error:
        print(f"Error while filling authentication fields: {error}")
        return False


def initialize_browser_extension(browser):
    """Initialize browser extension session using generic placeholder selectors."""
    page = browser.wait_for_event("page")

    print("Waiting for browser extension page...")
    page.wait_for_load_state("load")

    page.wait_for_selector("#terms-checkbox", timeout=30000)
    page.click("#terms-checkbox")

    page.click("[data-testid='import-extension-session']")
    page.click("[data-testid='analytics-no-thanks']")

    with open(AUTH_DATA_FILE, "r", encoding="utf-8") as file:
        auth_data = file.read().strip()

    page.wait_for_selector("#auth-word-0", timeout=30000)
    fill_authentication_fields(page, auth_data)

    page.click("[data-testid='confirm-auth-data']")

    page.fill("(//input[@class='password-input'])[1]", EXTENSION_PASSWORD)
    page.fill("(//input[@class='password-input'])[2]", EXTENSION_PASSWORD)

    page.click("[data-testid='accept-extension-terms']")
    page.click("[data-testid='create-extension-session']")
    page.click("[data-testid='onboarding-complete']")

    page.click("[data-testid='pin-extension-next']")
    page.click("[data-testid='pin-extension-done']")


def authenticate_portal(page, browser):
    """Authenticate on a protected web portal using browser extension flow."""
    page.goto(PORTAL_URL)
    page.wait_for_load_state("load")

    page.wait_for_selector("text=Start Registration", timeout=30000)
    page.click("text=Start Registration")
    print("Started registration workflow")

    page.wait_for_selector(".connect-with-extension-button", timeout=30000)
    page.click(".connect-with-extension-button")
    print("Clicked connect with extension button")

    page.locator(".extension-provider-item").first.click()
    print("Selected browser extension provider")

    page.wait_for_load_state("load")

    popup_page = browser.wait_for_event("page", timeout=30000)
    time.sleep(5)
    popup_page.wait_for_selector("[data-testid='confirm-btn']", timeout=30000)
    popup_page.click("[data-testid='confirm-btn']")

    time.sleep(3)
    page.wait_for_selector(".select-environment-button", timeout=30000)
    page.click(".select-environment-button")

    popup_page = browser.wait_for_event("page", timeout=30000)
    time.sleep(5)
    popup_page.wait_for_selector("[data-testid='confirmation-submit-button']", timeout=30000)
    popup_page.click("[data-testid='confirmation-submit-button']")

    popup_page = browser.wait_for_event("page", timeout=30000)
    time.sleep(5)
    popup_page.wait_for_selector("[data-testid='confirm-footer-button']", timeout=30000)
    popup_page.click("[data-testid='confirm-footer-button']")

    time.sleep(3)
    page.wait_for_load_state("load")

    page.wait_for_selector("text=Continue", timeout=30000)
    page.click("text=Continue")

    time.sleep(5)

    page.evaluate(
        """
        var interval = setInterval(function() {
            var element = document.querySelector('[data-testid="background-action-button"]');
            if (element) {
                element.click();
            }
        }, 5000);
        """
    )


def get_dashboard_metric(page):
    """Read metric value from the dashboard."""
    selector = "[data-testid='dashboard-metric-value']"
    element = page.locator(selector)
    return element.inner_text().strip() if element else None


def save_metric_to_file(page):
    """Save current dashboard metric value to a log file."""
    metric_value = get_dashboard_metric(page)

    if metric_value:
        with open(METRICS_FILE, "a", encoding="utf-8") as file:
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Metric value: {metric_value}\n")

        print(f"Saved metric value: {metric_value}")


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch_persistent_context(
            USER_DATA_DIR,
            headless=False,
            args=[
                f"--disable-extensions-except={BROWSER_EXTENSION_PATH}",
                f"--load-extension={BROWSER_EXTENSION_PATH}",
            ],
        )

        initialize_browser_extension(browser)

        page = browser.new_page()
        authenticate_portal(page, browser)

        while True:
            save_metric_to_file(page)
            time.sleep(5)


if __name__ == "__main__":
    main()
