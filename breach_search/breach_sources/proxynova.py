import requests
from colorama import init, Fore, Style
init()

def proxynova_func(username):
    
    
    
    url = "https://api.proxynova.com/comb"
    params = {
        "query": username,
        "start": 0,
        "limit": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        try:
            data = response.json()
            lines = data.get("lines", [])

            i = 1
            if lines:
                
                print(f" ┗[" + Fore.GREEN + "+" + Style.RESET_ALL + f"] Found {len(lines)} entr{'y' if len(lines) == 1 else 'ies'}:")
                for line in lines:
                    print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + ": " + line)
                    i += 1
            else:
                print(f" ┗[" + Fore.RED + "-" + Style.RESET_ALL + "] No entries found.")

        except ValueError:
            print(f" ┗" + "[" + Fore.RED + "!" + Style.RESET_ALL + "] Failed to parse JSON.")
            print("   Raw response:", response.text[:100])

    except Exception as e:
        print(f" ┗[" + Fore.RED + "!" + Style.RESET_ALL + f"] Error: {e}")
        print(" (" + Fore.LIGHTCYAN_EX + "In most cases, you don't have Internet connection" + Style.RESET_ALL + ")")
