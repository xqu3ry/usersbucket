import requests
from colorama import init, Fore, Style
init()
def mastodon_check(username: str):
    
    try:
        response = requests.get(
            "https://mastodon.social/api/v1/accounts/lookup",
            params={"acct": username.strip()},
            headers={"User-Agent": "MastoChecker/1.0"},
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Mastodon: @{username} exists.")
            
        else:
            return False
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Mastodon error: {e}")
