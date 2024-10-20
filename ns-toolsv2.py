# Importing requirements
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
print ("|-------------------------- TOOL NAME : NS-TOOLSV2 ------------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| ")
print ("—————————————————————————————————————————————————————————————————————————————————")
print (" ")
print("Welcome",name)
print ("\033[91m")

# Get a time and date
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
    print("| 21. Flames                                                             |")
    print("| 22. Wifijam                                                            |")
    print("| 23. Instagram Autoreporting tool                                       |")
    print("| 24. DDOS Attack                                                        |")
    print("| 25. facebook bruteforce tool                                           |")
    print("|  b. Back the tool                                                      |")
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

# choice ns to exit
    elif choice == 'ns':
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("exit ")

# choice b back the tools
    elif choice =='b':
      time.sleep(1)
      os.system("python3 ns-tools.py")

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
      os.system("python3 ns-tools.py ")


# press other wrong key return this tools
    else:
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 ns-tools.py ")



if __name__ == "__main__":
    main()
