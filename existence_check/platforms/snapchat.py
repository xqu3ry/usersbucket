import requests
from colorama import init, Fore, Style
init()
def snapchat_check(username):
    
    try:
        url = f"https://www.snapchat.com/add/{username.strip()}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Snapchat: @{username} exists.")
            
        else:
            return False
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Snapchat error: {e}")
