# Protecting Your Linux Server Against Brute Force Attacks 😎

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/5b28386e-9544-4e6b-b9a2-ca1ddfafa0c0" />

This will be a short introduction followed by a practical guide for different scenarios.

Recently, one of my servers experienced a resource overload and was automatically shut down. While investigating the issue and reviewing the logs, I noticed that the server was constantly being targeted by brute force attacks from different hosts attempting to guess passwords for both the **root** account and a custom user account.

Some individual hosts attempted more than **8,000 login attempts** within less than a month. 🙂

Even though direct root login from the Internet was already disabled, I decided to strengthen the server's security even further by configuring SSH properly and installing **Fail2Ban**.

---

# Useful Commands to Check Your Server for Brute Force Attempts

### Check successful logins

The output should normally contain only your own IP address.

```bash
sudo grep "Accepted" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq
```

### Check failed password login attempts sorted by number of attempts

```bash
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```

---

# Scenario 1

## You do not log in as the **root** user using a password and want to disable this option completely.

```bash
sudo grep -q "^PermitRootLogin" /etc/ssh/sshd_config && \
{ sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config && echo "Replaced: PermitRootLogin yes -> no"; } || \
{ echo "PermitRootLogin no" | sudo tee -a /etc/ssh/sshd_config && echo "Added: PermitRootLogin no"; } && \
sudo systemctl restart ssh.service && echo "SSH restarted successfully."
```

---

# Scenario 2

## You want to continue logging in directly as **root**, but protect your server against brute force password attacks.

This scenario is slightly more complicated, and the recommended approach is to switch to **SSH key authentication**.

### 1. Generate SSH keys on your local computer

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

---

### 2. Connect to the remote server you want to protect and add your **public key** (rsa_key.pub)

```bash
mkdir -p ~/.ssh

echo "PASTE YOUR PUBLIC SSH KEY HERE" >> ~/.ssh/authorized_keys

chmod -R go= ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

---

### 3. Disable password authentication

```bash
sudo grep -q "^PasswordAuthentication" /etc/ssh/sshd_config && \
{ sudo sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && echo "Replaced: PasswordAuthentication yes -> no"; } || \
{ echo "PasswordAuthentication no" | sudo tee -a /etc/ssh/sshd_config && echo "Added: PasswordAuthentication no"; }
```

---

### 4. Disable challenge-response authentication

```bash
sudo grep -q "^ChallengeResponseAuthentication" /etc/ssh/sshd_config && \
{ sudo sed -i 's/^ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && echo "Replaced: ChallengeResponseAuthentication yes -> no"; } || \
{ echo "ChallengeResponseAuthentication no" | sudo tee -a /etc/ssh/sshd_config && echo "Added: ChallengeResponseAuthentication no"; }
```

---

### 5. Enable public key authentication

```bash
sudo grep -q "^PubkeyAuthentication" /etc/ssh/sshd_config && \
{ echo "PubkeyAuthentication is already enabled"; } || \
{ echo "PubkeyAuthentication yes" | sudo tee -a /etc/ssh/sshd_config && echo "Added: PubkeyAuthentication yes"; }
```

---

### 6. Restart the SSH service

```bash
sudo systemctl restart ssh.service && echo "SSH restarted successfully."
```

---

### 7. Verify the current SSH configuration

```bash
grep "^PasswordAuthentication" /etc/ssh/sshd_config

grep "^ChallengeResponseAuthentication" /etc/ssh/sshd_config

grep "^PubkeyAuthentication" /etc/ssh/sshd_config
```

---

### 8. Check that no additional SSH configuration files override your settings

```bash
cat /etc/ssh/sshd_config.d/*.conf
```

If any of these files override your SSH configuration, modify or remove those parameters as shown above.

If you are using **Termius**, simply import your **private SSH key** into the connection settings and specify the username you use to log in. The password field is no longer needed.

---

# Installing Fail2Ban

### 1. Update your packages

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 2. Install Fail2Ban

```bash
sudo apt install fail2ban -y
```

---

### 3. Create a copy of the default configuration

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

---

### 4. Edit the configuration

```bash
sudo nano /etc/fail2ban/jail.local
```

---

### 5. Modify the **[sshd]** section

If you are using the default SSH port **22**, there is no need to change it.

```ini
# Permanent ban
bantime = -1

# Time window for counting failed attempts
findtime = 10m

# Number of failed attempts before banning
maxretry = 5
```

---

### 6. Restart the Fail2Ban service

```bash
sudo systemctl restart fail2ban
```

---

# Useful Commands

### Check Fail2Ban status

```bash
sudo systemctl status fail2ban
```

---

### View banned IP addresses

```bash
sudo fail2ban-client status sshd
```
