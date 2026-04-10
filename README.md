# UzHackigTool
<div align="center">
  
# 🛠️ UzHackingTool v5.0


<img width="1907" height="986" alt="Снимок экрана 2026-04-10 213912" src="https://github.com/user-attachments/assets/c0d102fb-7705-4afe-9677-5048a3e7b020" />




<img src="https://raw.githubusercontent.com/CyberRazor/UzHackingTool/main/logo.png" alt="UzHackingTool Logo" width="200">

**O'zbekistonning eng kuchli penetration testing vositalar to'plami**

[![Version](https://img.shields.io/badge/Version-5.0-green.svg)](https://github.com/CyberRazor/UzHackingTool)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20Windows-red.svg)](https://github.com/CyberRazor/UzHackingTool)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/CyberRazor/UzHackingTool)](https://github.com/CyberRazor/UzHackingTool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/CyberRazor/UzHackingTool)](https://github.com/CyberRazor/UzHackingTool/network)
[![GitHub issues](https://img.shields.io/github/issues/CyberRazor/UzHackingTool)](https://github.com/CyberRazor/UzHackingTool/issues)

**Muallif: Cyber Razor**

[![Telegram](https://img.shields.io/badge/Telegram-@CyberRazor-0088cc)](https://t.me/CyberRazor)
[![YouTube](https://img.shields.io/badge/YouTube-Cyber%20Razor-ff0000)](https://youtube.com/@cyberrazor)
[![GitHub](https://img.shields.io/badge/GitHub-CyberRazor-333333)](https://github.com/CyberRazor)

</div>

---

## 📌 Loyiha haqida

**UzHackingTool** - Cyber Razor tomonidan yaratilgan, **20+** professional pentesting vositalarini bir joyda jamlagan kuchli platforma. Bu tool yordamida siz:

- ✅ Phishing hujumlarini simulyatsiya qilish
- ✅ Wi-Fi tarmoqlar xavfsizligini tekshirish
- ✅ Web aplikatsiyalar zaifliklarini aniqlash
- ✅ DNS, IP va Whois ma'lumotlarini olish
- ✅ SQL injeksiya va DDOS hujumlarini test qilish
- ✅ Hash parollarni (rockyou wordlist bilan) kraking
- ✅ Va yana ko'plab funksiyalar...

### ⭐ Asosiy xususiyatlar

| Xususiyat | Tavsif |
|-----------|--------|
| 🎨 **GUI + CLI** | Ikkala rejimda ishlash imkoniyati |
| 🔧 **20+ vosita** | Eng mashhur pentesting tool'lar |
| 📡 **Wi-Fi Hacking** | Wifite + Rockyou wordlist bilan |
| 🔐 **Hash Cracking** | John/Hashcat + 14M parol bazasi |
| 🌍 **Cross-platform** | Linux, Termux, Windows, macOS |
| 🚀 **Avtomatik o'rnatish** | Bir buyruq bilan hamma narsa |
| 📊 **Real-time ma'lumot** | IP geolocation, DNS lookup |
| 🛡️ **Xavfsiz** | Faqat ta'lim va test uchun |

---

## 🚀 Tezkor o'rnatish

### 📱 Termux (Android) uchun

```bash
# 1. Paketlarni yangilash
pkg update && pkg upgrade -y

# 2. Kerakli paketlarni o'rnatish
pkg install git python -y

# 3. Tool'ni yuklab olish
git clone https://github.com/CyberRazor/UzHackingTool.git

# 4. Papkaga o'tish
cd UzHackingTool

# 5. O'rnatish skriptini ishga tushirish
bash setup.sh

# 6. Dasturni ishga tushirish
python3 uz_hacking_tool.py

💻Kali-linux
# 1. Repositoriyani klonlash
git clone https://github.com/CyberRazor/UzHackingTool.git

# 2. Papkaga o'tish
cd UzHackingTool

# 3. Bajarish huquqini berish
chmod +x setup.sh install.sh

# 4. O'rnatish
sudo bash setup.sh

# 5. Dasturni ishga tushirish
python python_2026.py

# Yoki GUI versiya uchun
python3 uz_hacking_tool.py --gui
🪟 Windows uchun
# 1. Python o'rnating: https://www.python.org/downloads/
# 2. Git o'rnating: https://git-scm.com/download/win
# 3. Komanda qatorida (Admin sifatida):

git clone https://github.com/CyberRazor/UzHackingTool.git
cd UzHackingTool
python -m pip install -r requirements.txt
python uz_hacking_tool.py
🐧 macOS uchun
# 1. Homebrew o'rnatish (agar yo'q bo'lsa)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Kerakli paketlar
brew install git python3

# 3. Tool'ni o'rnatish
git clone https://github.com/CyberRazor/UzHackingTool.git
cd UzHackingTool
pip3 install -r requirements.txt
python3 uz_hacking_tool.py


🎮 Qanday ishlatish?
python3 uz_hacking_tool.py


Menyu ko'rinishi:
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         UzHackingTool v5.0                                     ║
║                      Cyber Razor tomonidan ishlab chiqilgan                     ║
╚═══════════════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════════════

[01] 🔧 Kerakli paketlar & Yangilanish
[02] 🎣 Phishing Tool (Zphisher)
[03] 📷 WebCam Hack (SayCheese)
[04] 🔍 Subdomain Scaner (Subfinder)
[05] 📧 Email Bomber
[06] 💥 DDOS Hujum (Hammer)
[07] 📍 IP Ma'lumot (IP-Tracer)
[08] 🔌 Port Scaner (Nmap)
[09] 💉 SQL Injeksiya (sqlmap)
[10] 📡 Wi-Fi Tarmoq xavfsizligi
[11] 🔓 Wi-Fi Hack (Wifite + Rockyou)
[12] 🔐 Hash Cracking (John/Hashcat)
[13] 📺 Qanday ishlatish? (Video)
[14] 🗑️ Yuklangan dasturlarni o'chirish
[15] 🌐 DNS Lookup
[16] 📋 Whois ma'lumot
[17] 🗺️ Geolocation
[18] 🖥️ GUI Rejimi
[00] 🚪 Chiqish

═══════════════════════════════════════════════════════════════════════════════

UzHackingTool ➜ 
