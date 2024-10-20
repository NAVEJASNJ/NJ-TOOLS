
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


# Create a Description
banner()
print ("_________________________________________________________________________________")
print ("|--------------------------- author :  NS HACK ----------------------------------| ")
print ("|-------------------------- TOOL NAME : INSTA REPORT ----------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| ")
print ("—————————————————————————————————————————————————————————————————————————————————")
print (" ")
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
    print("| IR. Instagram Auto Reporting tool                                      | ")
    print("|  S. Create a session id                                                |")
    print("|  b. Back ns-tools                                                      |")
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

# choice IR instagram reporting tool
    if choice == 'IR':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 instagramreporttool.py")

# choice S create a session I'D
    elif choice =='S':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 sessionid.py ")

# choice b Back ns-tools
    elif choice == 'b':
      banner()
      time.sleep(1)
      os.system("clear")
      os.system("python3 ns-tools.py")


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
      os.system("python3 instareport.py ")


# press other wrong key return this tools
    else:
      banner()
      time.sleep(1)
      os.system("clear ")
      os.system("python3 instareport.py ")



if __name__ == "__main__":
    main()

