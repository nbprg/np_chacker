import cloudscraper
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

banner = f"""
>    Nodepay Multipole Accaunt Check
>    Telegram Channel : @cryp2xyz
>    Youtube Channel  : @nbprg
----------------------------------------
\033[0;32mNote : save nodepay token in 
token.txt & save token one by one \033[0m
----------------------------------------"""


def headers(token):
    hs = {
    'authority': 'api.nodepay.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'referer': 'https://app.nodepay.ai/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    if token:
         hs['authorization'] = f'Bearer {token}'
         hs['origin'] = 'https://app.nodepay.ai'
    return hs

def get_proff_humand_badge_info(token):
    try:
       params = ''
       heade = headers(token)
       scraper = cloudscraper.create_scraper()
       response = scraper.get('https://api.nodepay.ai/api/medal/all', params=params, headers=heade)
       for i in response.json()['data']:
            if i['name'] == "Proof of Humanhood":
                return (i['status']).replace('_',' ').capitalize()
    except Exception as e:
       return 'Failed to check'

def chack_wallet_status(token):
     try:
        params = ''
        scraper = cloudscraper.create_scraper()
        head = headers(token)
        response = scraper.get('https://api.nodepay.ai/api/wallet/status', params=params, headers=head).json()
        data = response['data']
        content = f"wallet : {data['wallet_address']}\nEmail  : {data['email']}\nStatus : {(data['status']).capitalize()}"
        return content
     except:
        return 'Wallet Staus : error to check'

def get_ballence_info(token):
   try:
      params = ''
      json_data = {}
      scraper = cloudscraper.create_scraper()
      head = headers(token)
      response = scraper.post('https://api.nodepay.ai/api/auth/session', params=params, headers=head, json=json_data).json()
      balance = response['data']['balance']['total_collected']
      return str(balance)
   except:
      return 'Prossess Error'


def airdrop_status(token):
  try:
     params = ''
     scraper = cloudscraper.create_scraper()
     head = headers(token)
     response = scraper.get('https://api.nodepay.ai/api/season/airdrop-status', params=params, headers=head).json()
     status = response['data']['is_eligible']
     airdrop_status = "Not Eligible"
     if status:
          airdrop_status = "Eligible For Airdrop"
     try:
        total_tokens = (response['data']['season1_tokens'] or 0) + (response['data']['season2_tokens'] or 0)
     except:
        total_tokens = 'Count error'
     return f'Airdrop Status : {airdrop_status}\nTokens : {total_tokens}'
  except:
     return 'Airdrop Status : Requests failed'


def token_to_info(token):
     print("Total Points :",get_ballence_info(token))
     print("Humanhood Badge :",get_proff_humand_badge_info(token))
     print(chack_wallet_status(token))
     print(airdrop_status(token))

def main():
     clear_console()
     print(banner)
     captha_api_token = 'token.txt'
     token_list = open(captha_api_token,'r').read().splitlines()
     for token in token_list:
         token_to_info(token)
         print('----------------------------------------')
     print('All Accaunt Check Complete ')
     input('Press Enter To Exit ');exit()

main()
