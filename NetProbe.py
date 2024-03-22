from scapy.all import *
from colorama import Fore

red = Fore.RED
yellow = Fore.YELLOW
reset = Fore.RESET


print(f'''{red}
::::    ::: :::::::::: ::::::::::: :::::::::  :::::::::   ::::::::  :::::::::  :::::::::: 
:+:+:   :+: :+:            :+:     :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:        
:+:+:+  +:+ +:+            +:+     +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+        
+#+ +:+ +#+ +#++:++#       +#+     +#++:++#+  +#++:++#:  +#+    +:+ +#++:++#+  +#++:++#   
+#+  +#+#+# +#+            +#+     +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+        
#+#   #+#+# #+#            #+#     #+#        #+#    #+# #+#    #+# #+#    #+# #+#        
###    #### ##########     ###     ###        ###    ###  ########  #########  ########## 
      
                                                                     {yellow} GITHUB: StarStark07
                                                                      MadeBy: Piyush Kumar {reset}\n''')

def ftp_exploitation(pkt):
    if pkt.haslayer('TCP') and pkt.haslayer(Raw):
        if pkt['TCP'].dport == 21 or pkt['TCP'].sport == 21:
            if b'USER' in pkt[Raw].load or b'PASS' in pkt[Raw].load:
                return True
    return False

def ssh_brute_force(pkt):
    if pkt.haslayer('TCP') and pkt.haslayer(Raw):
        if pkt['TCP'].dport == 22 or pkt['TCP'].sport == 22:
            if b'ssh' in pkt[Raw].load.lower():
                return True
    return False

def telnet_spoofing(pkt):
    if pkt.haslayer('TCP') and pkt.haslayer(Raw):
        if pkt['TCP'].dport == 23 or pkt['TCP'].sport == 23:
            return True
    return False

def snmp_attack(pkt):
    if pkt.haslayer('SNMP'):
        return True
    return False

def rip_attack(pkt):
    if pkt.haslayer('RIP'):
        return True
    return False

def smtp_attack(pkt):
    if pkt.haslayer('TCP') and pkt.haslayer(Raw):
        if pkt['TCP'].dport == 25 or pkt['TCP'].sport == 25:
            return True
    return False

def dns_attack(pkt):
    if pkt.haslayer('DNS'):
        return True
    return False

def syn(pkt):
    if pkt.haslayer('TCP') and pkt['TCP'].flags == 2:
        return True
    return False

num_packets = int(input("Enter the number of packets to scan: "))
packets = sniff(count=num_packets)

ftp_count = ssh_count = telnet_count = snmp_count = rip_count = smtp_count = dns_count = syn_count = unknown_count = 0

for pkt in packets:
    if ftp_exploitation(pkt):
        ftp_count += 1
    elif ssh_brute_force(pkt):
        ssh_count += 1
    elif telnet_spoofing(pkt):
        telnet_count += 1
    elif snmp_attack(pkt):
        snmp_count += 1
    elif rip_attack(pkt):
        rip_count += 1
    elif smtp_attack(pkt):
        smtp_count += 1
    elif dns_attack(pkt):
        dns_count += 1
    elif syn(pkt):
        syn_count += 1
    else:
        unknown_count += 1


print("    <== Attack Detection Results ==>")
print(f"FTP Exploitation Attack: {ftp_count}")
print(f"SSH Brute Force Attack: {ssh_count}")
print(f"Telnet Spoofing: {telnet_count}")
print(f"SNMP Attack: {snmp_count}")
print(f"RIP Attack: {rip_count}")
print(f"SMTP Attack: {smtp_count}")
print(f"DNS Attack: {dns_count}")
print(f"SYN Packets: {syn_count}")
print(f"Unknown Packets: {unknown_count}")
