# import requirements
import os
import time
import datetime

# Create a banne NS HACK
print ("\033[92m")
print ("\033[92m")

def banner():
    os.system("clear ")
    print("""
████          ██|  █████████████ ██      ██            ██|        ██████████   ██        ██|
████         ██|   ██|            ██      ██         ██ ██|      ██|            ██      ██|
██||██       ██|    ██|            ██      ██       ██  ██|     ██|             ██     ██|
██| |██     ██|     ██|_________  ██████████       ██   ██|   ██|                ██   ██|
██|  |██    ██|      ████████████|  ██|    |██     ████████|   ██|                ████|
██|   |██  ██|                 ██|   ██|     |██  ██|     ██|    ██|              ██||██|
██|    |██ ██|                  ██|  ██|     |██ ██|      ██|      ██|_______      ██| |██|
██|     |██|          ████████████|  ██|     |██ ██|       ██|       ████████|      ██|  |██|

""")

# getting a user name
banner()
name = input("What can i call you ? :")

# Create a Description
banner()
print ("_________________________________________________________________________________")
print ("|--------------------------- author :  NS HACK ----------------------------------| ")
print ("|-------------------------- TOOL NAME : NS-TOOLS --------------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| ")
print ("—————————————————————————————————————————————————————————————————————————————————")
print (" ")
print("Welcome",name)
print ("\033[91m")


def display_time():
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), end='\r')
        time.sleep(1)

# Create a MENU OPTIONS
def display_menu():
    print ("\033[92m")
    print(display_time())
    print ("\033[91m")
    print("_________________________________________________________________________ ")
    print("| Options:                                                               | ")
    print("| 1. Password generator (CUPP)                                           | ")
    print("| 2. Phishing attacks (zphisher)                                         | ")
    print("| 3. Start Mtasploit                                                     | ")
    print("| 4. Jump Location (Auto tor ip changer)                                 | ")
    print("| 5. Advanced Hack Via Wifi(Phonesploit-pro)                             | ")
    print("| 6. Kali linux root in Terminal                                         | ")
    print("| 7. Instant Phishing (Lord Phish)                                       | ")
    print("| 8. The Lazy Script Powerful Tool                                       | ")
    print("| 9. Instagram information gathering (OSINT)                             | ")
    print("| 10. Web and Web applications Tools (pureblood)                         | ")
    print("| 11. Hack instagram account (instainsane)                               | ")
    print("| 12. Password generator Best tool (W-list-gen)                          | ")
    print("| 13. URL Hider                                                          | ")
    print("| 14. Hack instagram account V2 (hackinsagram)                           | ")
    print("| 15. Wifi password attack (wifite)                                      | ")
    print("| 16. Calculator                                                         | ")
    print("| 17. URL Hider V2(FACAD1NG)                                             | ")
    print("| 18. Lock Screen Password Cracking (CILOCKS)                            | ")
    print("| 19. Create a ransomware <apk> (SARA)                                   |")
    print("| 20. Create a malware <apk> (METASPLOIT)                                |")
    print("|  m. more tools                                                         |")
    print("| ns. Exit                                                               | ")
    print("——————————————————————————————————————————————————————————————————————————  ")
print("")
print("")

# Get choice from script user
def get_user_choice():
    choice = input("Enter your choice: ")
    return choice

# Excute choices
def main():
    display_menu()
    choice = get_user_choice()

# choice 1 password generator
    if choice == '1':
      os.system("clear")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 cupp/cupp.py -i ")

# choice 2 phishing attacks
    elif choice == '2':
      os.system("clear")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("cd zphisher ")
      os.system("chmod +x zphisher/zphisher.sh ")
      os.system("bash zphisher/zphisher.sh ")

# choice 3 start metaspoloit
    elif choice == '3':
      os.system("clear" )
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("msfconsole ")

# choice 4 jump location
    elif choice == '4':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 Auto_Tor_IP_changer/autoTOR.py ")

# choice 5 Hack via wifi
    elif choice == '5':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 PhoneSploit-Pro/phonesploitpro.py ")

# choice 6 start kali linux
    elif choice == '6':
      os.system("clear")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("bash start-kali.sh ")

# choice 7 Instant phishing
    elif choice == '7':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("bash LordPhish/setup.sh ")
      os.system("bash LordPhish/lord.sh ")

# choice 8 The lazy script powerful tool
    elif choice == '8':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("bash lscript/l ")

# choice 9 Instagram information gathering by osint
    elif choice == '9':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("pip3 install instaloader ")
      os.system("python3 IG-OSINT-V2/ig.py ")

# choice 10 pureblood web and webapplication tool
    elif choice == '10':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 https-github.com-cr4shcod3-pureblood/pureblood.py ")

# choice 11 instagram password cracking
    elif choice == '11':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("bash instainsane/instainsane.sh ")

# choice 12 best password generator
    elif choice == '12':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 W-list-gen/wlistgen.py ")

# choice 13 URL Hider
    elif choice == '13':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 URLHider/URLHider.py ")

# choice 14 instagram password cracking
    elif choice == '14':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("bash hackinsagram/haxter.sh ")

# choice 15 wifi password cracking
    elif choice == '15':
      os.system("clear ")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("wifite ")

# choice 16 calculator
    elif choice == '16':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 calculator.py ")

# choice 17 URL Hider v2
    elif choice == '17':
      os.system("clear")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 Facad1ng/facad1ng.py ")

# choice 18 Lock Screen password cracking
    elif choice == '18':
      os.system("clear")
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("bash CiLocks/cilocks")

# choice 19 create a ransomware
    elif choice == '19':
      os.system("clear")
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 SARA/install.sh ")
      os.system("python3 SARA/sara.py ")

# choice 20 create a malware apk
    elif choice == '20':
     banner()
     time.sleep(1)
     os.system("clear")
     os.system("python3 autohack.py")

# choice m more tools
    elif choice == 'm':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 ns-toolsv2.py")

# choice ns to exit
    elif choice == 'ns':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("exit ")

# press any key return this tool
    elif 'press any key':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 ns-tools.py ")


# press other wrong key return this tools
    else:
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 ns-tools.py ")



if __name__ == "__main__":

     main()

