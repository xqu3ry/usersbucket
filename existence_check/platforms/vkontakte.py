import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init()
def vkontakte_check(username):
    url = f"https://vk.com/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "ru-RU,ru;q=0.9"
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)

        if r.status_code == 404:
            return False

        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string.strip().lower() if soup.title else ""

        if "страница заблокирована" in title:
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Vkontakte: @{username} blocked.")

        print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Vkontakte: @{username} exists.")

    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Vkontakte error: {e}")


