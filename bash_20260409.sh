#!/bin/bash

# ==============================================
# UzHackingTool - Avtomatik o'rnatish skripti
# Cyber Razor tomonidan
# ==============================================

set -e

# Ranglar
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

clear
echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║              UzHackingTool - O'rnatish skripti                ║"
echo "║                   Cyber Razor tomonidan                       ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Papkalarni yaratish
mkdir -p Tools wordlists logs

# Kerakli paketlarni o'rnatish
echo -e "${YELLOW}[1/4] Kerakli paketlar o'rnatilmoqda...${NC}"

if command -v apt &> /dev/null; then
    sudo apt update
    sudo apt install -y git python3 python3-pip curl wget nmap aircrack-ng hashcat john tor
elif command -v pkg &> /dev/null; then
    pkg update -y
    pkg install -y git python python-pip curl wget nmap tor
elif command -v pacman &> /dev/null; then
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm git python python-pip curl wget nmap aircrack-ng hashcat john tor
fi

# Python paketlari
echo -e "${YELLOW}[2/4] Python paketlar o'rnatilmoqda...${NC}"
pip3 install --upgrade pip
pip3 install requests colorama dnspython python-whois customtkinter pillow

# Bajarish huquqi
echo -e "${YELLOW}[3/4] Bajarish huquqi berilmoqda...${NC}"
chmod +x uz_hacking_tool.py
chmod +x install.sh

# Rockyou wordlist
echo -e "${YELLOW}[4/4] Rockyou wordlist tekshirilmoqda...${NC}"
if [ ! -f wordlists/rockyou.txt ]; then
    echo -e "${YELLOW}Rockyou wordlist yuklanmoqda...${NC}"
    wget -O wordlists/rockyou.txt.gz https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt.gz 2>/dev/null || \
    wget -O wordlists/rockyou.txt https://downloads.skullsecurity.org/passwords/rockyou.txt.bz2 2>/dev/null
    
    if [ -f wordlists/rockyou.txt.gz ]; then
        gunzip wordlists/rockyou.txt.gz
    elif [ -f wordlists/rockyou.txt.bz2 ]; then
        bunzip2 wordlists/rockyou.txt.bz2
        mv wordlists/rockyou.txt wordlists/rockyou.txt 2>/dev/null
    fi
fi

echo -e "${GREEN}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║              ✅ O'RNATISH MUVAFFAQIYATLI! ✅                   ║"
echo "║                                                               ║"
echo "║   Dasturni ishga tushirish:                                   ║"
echo "║   python3 uz_hacking_tool.py                                  ║"
echo "║                                                               ║"
echo "║   GUI versiya:                                                ║"
echo "║   python3 uz_hacking_tool.py --gui                            ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"