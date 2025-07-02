import requests
from colorama import init, Fore, Style
init()
def hudsonrock_func(username):
    
    i = 0

    url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username?username={username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        

        
        stealers = data.get("stealers", [])
        if not stealers:
            print(f" ┗" + "[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " No infostealer data found.")
            return

        print(f" ┗" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Found {len(stealers)} infostealer record(s), showing first 5:")
        
        for entry in stealers[:5]:
            i += 1
            
            
            print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + f": Computer - {entry.get('computer_name')}")
            print(f"      OS - {entry.get('operating_system')}")
            print(f"      Malware Path - {entry.get('malware_path')}")
            print(f"      Compromised - {entry.get('date_compromised')}")
            print(f"      IP - {entry.get('ip')}")
            
            
            antiviruses = entry.get('antiviruses')
            if isinstance(antiviruses, list):
                antiviruses_str = ', '.join(antiviruses)
            else:
                antiviruses_str = antiviruses or "None"

            print(f"      Antiviruses - {antiviruses_str}")
            
            
            print(f"      Corp Services - {entry.get('total_corporate_services')}")
            print(f"      User Services - {entry.get('total_user_services')}")

            print("      Top Passwords:")
            for passwd in entry.get("top_passwords", []):
                print(f"        - {passwd}")

            print("      Top Logins:")
            for login in entry.get("top_logins", []):
                print(f"        - {login}")
            
            

    except Exception as e:
        print(f" ┗" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f" Error: {e}" + f" \n(" + Fore.LIGHTCYAN_EX + "In most cases, you dont have Internet connection" + Style.RESET_ALL + ")")