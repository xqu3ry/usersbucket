import requests
from colorama import init, Fore, Style
init()
def tumblr_check(username):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    urls = [
        f"https://{username}.tumblr.com/",
        f"https://www.tumblr.com/{username}"
    ]

    for url in urls:
        try:
            r = requests.get(url, headers=headers, timeout=5)
            html = r.text.lower()

            if r.status_code == 404 or "there's nothing here" in html or "page not found" in html:
                continue

            
            print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Tumblr: @{username} exists.")
            break
        except requests.RequestException:
            continue

    return False



