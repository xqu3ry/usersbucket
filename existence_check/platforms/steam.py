import requests
from colorama import init, Fore, Style
init()
def steam_check(username):
    url = f"https://steamcommunity.com/id/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = requests.get(url, headers=headers, timeout=5)
        html = r.text.lower()

        if "the specified profile could not be found" in html:
            return False

        print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Steam: @{username} exists.")

    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Steam error: {e}")


