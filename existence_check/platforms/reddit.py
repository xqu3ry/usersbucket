import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init()
def reddit_check(username):
    url = f"https://www.reddit.com/user/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"  
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text().lower()

        if "nobody on reddit goes by that name" in text:
            return False
        elif "this account has been suspended" in text:
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Reddit: @{username} banned")
        else:
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Reddit: @{username} exists.")
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Reddit error: {e}")


