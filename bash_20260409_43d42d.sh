# 1. Homebrew o'rnatish (agar yo'q bo'lsa)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Kerakli paketlar
brew install git python3

# 3. Tool'ni o'rnatish
git clone https://github.com/CyberRazor/UzHackingTool.git
cd UzHackingTool
pip3 install -r requirements.txt
python3 uz_hacking_tool.py