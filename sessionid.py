import requests
from user_agent import generate_user_agent
import time
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

tok = input(Back.RED + 'ENTER YOUR token Bot : ')
io = input(Back.YELLOW + 'ENTER YOUR ID : ')
os.system('clear')

email = input(Back.RED + 'ENTER YOUR Username or Email IG : ')
psw = input(Back.GREEN + 'ENTER YOUR Password : ')

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.8',
    'content-length': '303',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=ZQZC9QAEAAG9NicS3jBHkYqHlp8C; ig_nrcb=1; ig_did=AC6A65E6-8577-4CDE-8F3F-4B24D5787A91; datr=D0MGZZ_cUrCctc7jPE92HUgb; csrftoken=NYaOlpVmXUwzESZVfuFOYqbJ0gHzcvks',
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'user-agent': str(generate_user_agent()),
    'viewport-width': '808',
    'x-asbd-id': '129477',
    'x-csrftoken': 'NYaOlpVmXUwzESZVfuFOYqbJ0gHzcvks',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1008686036',
    'x-requested-with': 'XMLHttpRequest',
}

timestamp = str(time.time()).split('.')[0]
data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{psw}',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': email,
}

response = requests.post(url, headers=headers, data=data)
if "userId" in response.text:
    tanji = response.cookies.get("sessionid", "No session ID found")
    print(f'Your Session ID Instagram >> {tanji}')
    tlg = f'''
    Your Session ID >> {tanji}
    BY >> @seedhe_maut
    '''
    requests.get("https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(io)+"&text="+str(tlg))
    print(tlg)
    with open("Meow.txt", "a") as x:
        x.write(f"Your Session >> {tanji}\n")
else:
    print(response.text)
