import requests
from colorama import init, Fore, Style
init()

def breachdirectory_func(username):

    url = "https://api.breachdirectory.org/rapidapi-IscustemTaingtowItrionne"
    
    params = {
        "func": "auto",
        "term": username    }
    
    headers = {
        "Accept": "application/json"
    }

    try:
    
        response = requests.get(url, headers=headers, params=params)

        if response.ok:
        
            data = response.json()

            if "result" in data and isinstance(data["result"], list) and data["result"]:
                breaches = data["result"][:5]
                print(f" ┗" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f"Found {data.get('found', len(breaches))} entries, showing first 5:")
            
                for i, entry in enumerate(breaches, 1):
                
                    print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + f": Email - {entry.get('email')}")
                    print(f"      Password: {entry.get('password')}")
                    print(f"      SHA1: {entry.get('sha1')}")
                    print(f"      Hash: {entry.get('hash')}")
                    print(f"      Hash Password: {entry.get('hash_password')}")
                    print(f"      Source: {entry.get('sources')}")
        
            else:
            
                print(" ┗" + "[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " Entries Not Found.")
    
    except Exception as e:
        
        print(" ┗" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Error: {str(e)}" + f" \n(" + Fore.LIGHTCYAN_EX + "In most cases, you dont have Internet connection" + Style.RESET_ALL + ")")

