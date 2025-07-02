import requests
from colorama import init, Fore, Style
init()

def facebook_check(username):
    url = f"https://www.facebook.com/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"  
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        page = response.text.lower()

        error_signatures = [
            "this content isn't available",
            "the link you followed may be broken",
            "page isn't available"
        ]

        if any(sig in page for sig in error_signatures):
            return False  
        print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Facebook: @{username} exists.")  

    except Exception as e:
        print(f" ┣" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Facebook error: {e}")
        return False

