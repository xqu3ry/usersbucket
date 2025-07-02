import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init()
def telegram_check(username):
    url = f"https://t.me/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')

        
        title_block = soup.find("div", class_="tgme_page_title")
        if title_block:
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Telegram: @{username} exists.")
        else:
            return False
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Telegram error: {e}")
        return False


