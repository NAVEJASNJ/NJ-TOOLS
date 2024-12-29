# Importing requirements
import os
import time
import datetime

r = "\033[91m"
y = "\033[93m"
v = "\033[94m"
g = "\033[92m"

# Create a banne NAVE
print ("\033[92m")

def banner():
    os.system("clear ")
    print("""
                 ████          ██     ██      ██        ██   ██████  
                 ████         ██     ██ ██     ██      ██    ██           
                 ██ ██       ██      ██  ██    ██      ██    ██          
                 ██  ██     ██      ██   ██     ██    ██     ████        
                 ██   ██    ██      ████████    ██    ██     ██
                 ██    ██  ██      ██     ██     ██  ██      ██
                 ██     ████       ██      ██    ██  ██      ██       
                 ██     ██        ██       ██      ██        ██████   
""")

# getting a user name
banner()
name = input("What can i call you ? :")

# Create a Description
banner()
print ("_________________________________________________________________________________")
print ("|--------------------------- author :  NAVE -- ----------------------------------| ")
print ("|-------------------------- TOOL NAME : NAVE-TOOLSV2 ----------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| ")
print ("—————————————————————————————————————————————————————————————————————————————————")
print (" ")
print("Welcome",name)

# Get a time and date
def display_time():
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), end='\r')
        time.sleep(1)

# Create a MENU OPTIONS
def display_menu():
    print("Date and time")
    print(display_time())
    print(g+"_________________________________________________________________________ ")
    print(g+"| Tools options:                                                         | ")
    print(g+"| 21.",y+" Flames                                                   ",g+"        |")
    print(g+"| 22.",y+" Wifijam                                                  ",g+"        |")
    print(g+"| 23.",y+" Instagram Autoreporting tool                             ",g+"        |")
    print(g+"| 24.",y+" DDOS Attack                                              ",g+"        |")
    print(g+"| 25.",y+" facebook bruteforce tool                                 ",g+"        |")
    print(g+"|  b.",y+" Back the tool                                            ",g+"        |")
    print(g+"| n .",y+" Exit                                                     ",g+"        | ")
    print(g+"——————————————————————————————————————————————————————————————————————————  ")
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

# choice 21 Flames
    if choice == '21':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 flames.py")

# choice 22 WifiJam
    elif choice == '22':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 wifijam.py")

# choice 23 Instagram auto reporting tool
    elif choice == '23':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 instareport.py ")

# choice n to exit
    elif choice == 'n':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("exit ")

# choice b back the tools
    elif choice =='b':
      time.sleep(1)
      os.system("python3 nave-tools.py")

# choice 24 DDOS ATTACK
    elif choice == '24':
      time.sleep(1)
      os.system("python2 GAMKERS-DDOS/GAMKERS-DDOS.py")

# choice 25 facebook bruteforce tool
    elif choice == '25':
      time.sleep(1)
      print("After run this tool type 'help' for tools guiding")
      os.system("python2 Firecrack/firecrack.py")

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
