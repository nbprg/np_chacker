import requests
import os, sys
if sys.platform.startswith('win'):
        os.system('cls')
else:
        os.system('clear')

banner = f">    Nodepay Get Token By user pass\n>    Telegram Channel : @cryp2xyz\n>    Youtube Channel  : @nbprg"
print(banner)
print('-' * 40)
print('\033[0;32mNote : accaunts format is `email|pass` \nSave accaunts in accaunts.txt \033[0m')
print('-' * 40)
api_key = input('Put Captcha Api key: ')
print('-' * 40)

def get_token():
    while True:
         json_data = {
            'username': api_key
         }
         response = requests.get('https://cryptohubnp.pythonanywhere.com/get_captcha',json=json_data).json()
         if response['success']:
              print(f'Captcha token get successful')
              return response['token']
         else:time.sleep(0.5)

def login_acccaunts(email, password, captcha_token):
   try:
       json_data = {
           'user': email,
           'password': password,
           'remember_me': True,
           'recaptcha_token': captcha_token
       }
       headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.nodepay.ai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
       }
       url = "https://api.nodepay.ai/api/auth/login"
       response = requests.post(url,headers=headers,json=json_data,timeout=10)
       response.raise_for_status()
       return response.json()
   except Exception as e:
       return 'Error to requests or json'

accaunts_list = open('accaunts.txt','r').read().splitlines()

for accaunt in accaunts_list:
    email, password = accaunt.split('|')
    print('Try to login accaunt :',email)
    captcha_token = get_token()
    token_data = login_acccaunts(email, password, captcha_token)
    try:
         token = response_data['data']['token']
         open('token.txt','a').write(token+'\n')
         print('Token Saved Successfull ')
    except:
       print(f'\033[0;31mFailed to get Token : {email} \033[0m')
    print('-' * 40)
