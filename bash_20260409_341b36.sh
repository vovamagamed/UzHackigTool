# MD5 kraking
hashcat -m 0 -a 0 hash.txt wordlists/rockyou.txt

# NTLM kraking
hashcat -m 1000 -a 0 hash.txt wordlists/rockyou.txt

# SHA256 kraking
hashcat -m 1400 -a 0 hash.txt wordlists/rockyou.txt