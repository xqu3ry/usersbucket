import requests
from colorama import init, Fore, Style
init()

def pastebin_search(username):
    url = f"https://psbdmp.cc/api/v3/search/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if not data:
            print(" ┗" + "[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " Entries Not Found.")
            return

        print(f" ┗" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Found {len(data)} entries, showing first 5:")

        i = 0
        for i, item in enumerate(data[:5], start=1):
            
            print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + f": ID - {item.get('id')}")
            print(f"      Time - {item.get('time')}")
            print(f"      Lenght - {item.get('length')} байт")
            text_snippet = item.get('text', '')[:200].replace('\r', '').replace('\n', ' ')
            print(f"      Text fragment - {text_snippet}...")
            print(f"      Link - https://pastebin.com/{item.get('id')}")
            

    except Exception as e:
        print(" ┗" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f" Error: {str(e)}" + f" \n(" + Fore.LIGHTCYAN_EX + "In most cases, you dont have Internet connection" + Style.RESET_ALL + ")")


