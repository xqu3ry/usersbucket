import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote
from colorama import init, Fore, Style
init()

def ahmia_search(query):
    
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://ahmia.fi/search/?q={query}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select("ol.searchResults li.result")
        
        all_onion_results = []
        for result in results:
            link_tag = result.select_one("a[href*='redirect_url=']")
            desc_tag = result.select_one("p")
            if not link_tag:
                continue

            href = link_tag.get("href")
            parsed = urlparse(href)
            qs = parse_qs(parsed.query)
            redirect_url = unquote(qs.get("redirect_url", [""])[0])

            if ".onion" in redirect_url:
                description = desc_tag.text.strip() if desc_tag else "No description"
                all_onion_results.append((redirect_url, description))

        total = len(all_onion_results)
        if total == 0:
            print(" ┗" + "[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " Nothing was found.")
        else:
            print(f" ┗" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Found {total} onion-links, showing first {min(5, total)}.")
            for i, (url, desc) in enumerate(all_onion_results[:5], 1):
                print(Fore.LIGHTBLUE_EX + f"   {i}" + Style.RESET_ALL + f": URL - {url}")
                print(f"      Description - {desc}")
            

    except Exception as e:
        print(" ┗" + "[" + Fore.RED + "!" + Style.RESET_ALL + "]" + f"Error: {str(e)}" + f" \n(" + Fore.LIGHTCYAN_EX + "In most cases, you dont have Internet connection" + Style.RESET_ALL + ")")
