# SSH Brute Force Automation Tool 🔐

A powerful and educational SSH brute force automation tool with a custom wordlist generator.  
Created for **ethical hacking learning**, **red team practice**, and **interview portfolio demonstration**.

## 🚀 Features

- ✅ Automatic target-specific password wordlist generation
- ✅ Options to include symbols, numbers, and strong (Google-style) passwords
- ✅ SSH brute force attack using Paramiko
- ✅ Auto dependency installation (Rust, pip tools, Paramiko)
- ✅ Works on **Termux**, **Linux**, **Kali**, **Windows**
---
## 📜 Usage Instructions
python required ⛓️‍💥

---

For Termux:

This tool not suitable for termux 
so check out my page (github.com/p4cket-hunt3r)There 
is a new repository name : bruteforce 2 (only for termux)


---
For linux:

This tool will automatically install all required dependencies before execution.
If the automatic installation fails, please follow the steps below to install manually:

```

sudo apt update
sudo apt install build-essential libssl-dev python3-dev rustc -y
pip install --upgrade pip setuptools wheel
pip install cryptography
pip install paramiko

```
---

windows:
install automatically ✅

manually installation:


```

pip install --upgrade pip setuptools wheel
pip install cryptography
pip install paramiko



```

**or**


Download and install from:

```
https://visualstudio.microsoft.com/visual-cpp-build-tools/

```


---

#run

---

linux:

Give permission if needed
After:-

```

python ssh_bruteforce_tool.py

```




windows:

```

python ssh_bruteforce_tool.py

```


⚠️ Legal Disclaimer:

For educational and authorized use only.

👤 Author:

```

p4cket-hunt3r

```
```
https://github.com/p4cket-hunt3r

```


