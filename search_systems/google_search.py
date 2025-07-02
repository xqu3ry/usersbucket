from googlesearch import search
from colorama import init, Fore, Style
init()

def google_search(query, num_results=5, lang="en"):
    try:
        results = list(search(query, num_results=num_results, lang=lang))
        
        if not results:
            print(" ┗" + "[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " Nothing was found.")
        else:
            print(f" ┗" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f"Found ? links:")
            for i, url in enumerate(results, 1):
                print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + f": {url}")

        
        for i in range(len(results)+1, num_results+1):
            print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + f": <empty>")

        return results
    except Exception as e:
        print(" ┗" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Error: {str(e)}" + f" \n(" + Fore.LIGHTCYAN_EX + "In most cases, you have been blocked" + Style.RESET_ALL + ")")
        return []


