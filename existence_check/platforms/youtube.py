import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init()
def youtube_check(username):
    url = f"https://www.youtube.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string.strip().lower() if soup.title else ""

        if "404" in title or "not found" in title:
            return False
        print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Youtube: @{username} exists.")
        
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Youtube error: {e}")

