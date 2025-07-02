import requests
from colorama import init, Fore, Style
init()
def github_check(username):
    url = f"https://github.com/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Github: @{username} exists.")
        elif r.status_code == 404:
            return False
        
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Github error: {e}")
        return False


