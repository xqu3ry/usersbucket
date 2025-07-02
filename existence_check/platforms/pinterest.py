import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init()
def pinterest_check(username):
    url = f"https://www.pinterest.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        title_tag = soup.title

        if not title_tag or not title_tag.string:
            return False  

        title = title_tag.string.strip().lower()

        if "page not found" in title or "not found" in title:
            return False
        print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Pinterest: @{username} exists.")
    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Pinterest error: {e}")

