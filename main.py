import configparser
import argparse
from colorama import init, Fore, Style
init()


config = configparser.ConfigParser()
config.read('config.ini')



def main():
    
    help_username = "Username"

    parser = argparse.ArgumentParser(description="UsersBucket - username investigation tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search
    parser_all = subparsers.add_parser("all", help="Search for all")
    parser_all.add_argument("username", help=help_username)
    
    parser_leaks = subparsers.add_parser("leaks", help="Search only for leaks module")
    parser_leaks.add_argument("username", help=help_username)

    parser_exis = subparsers.add_parser("exis", help="Check username existence on different platforms")
    parser_exis.add_argument("username", help=help_username)
    
    parser_darknet = subparsers.add_parser("darknet", help="Search only for darknet module")
    parser_darknet.add_argument("username", help=help_username)
    
    parser_pastes = subparsers.add_parser("pastes", help="Search username only in pastes")
    parser_pastes.add_argument("username", help=help_username)
    
    parser_vars = subparsers.add_parser("vars", help="Mutate username to other variants")
    parser_vars.add_argument("username", help=help_username)
    
    parser_clearnet = subparsers.add_parser("clearnet", help="Search in clearnet searchers")
    parser_clearnet.add_argument("username", help=help_username)
    
    parser_help = subparsers.add_parser("help", help="Show help message")
    
    args = parser.parse_args()

    
    
    if config.getboolean('VISUAL', 'show_banner'):
            try:
                with open('banner.txt', 'r', encoding='utf-8') as file:
                    art = file.read()
                    print(Style.BRIGHT + art + Style.RESET_ALL)
            except FileNotFoundError:
                print("[" + Fore.RED + "!" + Style.RESET_ALL + "]" + Fore.YELLOW + " File ascii_art.txt not found." + Style.RESET_ALL)
            except Exception as e:
                print(f"[" + Fore.RED + "!" + Style.RESET_ALL + "]" + Fore.YELLOW + f"Error: {e}" + Style.RESET_ALL)
    
    if config.getboolean('VISUAL', 'show_warning'):
        print(Fore.YELLOW + """
   ^     Your decision to use this utility is entirely your own.
  /!\\    If your use of this utility causes any harm, you alone will be responsible.
 /___\\   All information is taken from public sources.
"""+ Style.RESET_ALL)
    
    match args.command:
        
        case "exis":

            if config.getboolean('EXISTENCE_CHECK', 'existence_check'):
                from existence_check.platforms_check import platforms_check
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Checking username existence on platforms..." + Style.RESET_ALL)
                print(" ┃")
                platforms_check(args.username)
                print(f" ┗" + "[" + Fore.YELLOW + "*" + Style.RESET_ALL + "] Done.")
        
        case "all":
        
        
            if config.getboolean('EXISTENCE_CHECK', 'existence_check'):
                from existence_check.platforms_check import platforms_check
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Checking username existence on platforms..." + Style.RESET_ALL)
                print(" ┃")
                platforms_check(args.username)
                print(f" ┗" + "[" + Fore.YELLOW + "*" + Style.RESET_ALL + "] Done.")
            
            if config.getboolean('CLEARNET_SEARCH', 'google_search'):
                from search_systems.google_search import google_search
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in google..." + Style.RESET_ALL)
                print(" ┃")
                google_search(f"intext:{args.username} | intitle:{args.username}")
            
            if config.getboolean('DARKNET_SEARCH', 'ahmia_search'):
                from darknet_search.ahmia import ahmia_search
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in darknet through ahmia..." + Style.RESET_ALL)
                print(" ┃")
                ahmia_search(args.username)
            
            
            if config.getboolean('BREACH_SEARCH', 'breachdirectory_search'):
                from breach_search.breachsearch import breachdirectory_func
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in data leaks through Breachdirectory source..." + Style.RESET_ALL)
                print(" ┃")
                breachdirectory_func(args.username)
        
            if config.getboolean('BREACH_SEARCH', 'proxynova_search'):
                from breach_search.breachsearch import proxynova_func
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in data leaks through Proxynova source..." + Style.RESET_ALL)
                print(" ┃")
                proxynova_func(args.username)

            if config.getboolean('BREACH_SEARCH', 'hudsonrock_search'):
            
                from breach_search.breachsearch import hudsonrock_func
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in stealer logs through Hudsonrock source..." + Style.RESET_ALL)
                print(" ┃")
                hudsonrock_func(args.username)

            
        
            if config.getboolean('PASTES_SEARCH', 'pastebin_search'):
                from pastes_search.pastebin import pastebin_search
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in pastes through PsbDmp..." + Style.RESET_ALL)
                print(" ┃")
                pastebin_search(args.username)
        
        case "leaks":
            
            if config.getboolean('BREACH_SEARCH', 'breachdirectory_search'):
                from breach_search.breachsearch import breachdirectory_func
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in data leaks through Breachdirectory source..." + Style.RESET_ALL)
                print(" ┃")
                breachdirectory_func(args.username)
        
            if config.getboolean('BREACH_SEARCH', 'proxynova_search'):
                from breach_search.breachsearch import proxynova_func
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in data leaks through Proxynova source..." + Style.RESET_ALL)
                print(" ┃")
                proxynova_func(args.username)

            if config.getboolean('BREACH_SEARCH', 'hudsonrock_search'):
            
                from breach_search.breachsearch import hudsonrock_func
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in stealer logs through Hudsonrock source..." + Style.RESET_ALL)
                print(" ┃")
                hudsonrock_func(args.username)        

        case "darknet":
            
            if config.getboolean('DARKNET_SEARCH', 'ahmia_search'):
                
                from darknet_search.ahmia import ahmia_search
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in darknet through ahmia..." + Style.RESET_ALL)
                print(" ┃")
                ahmia_search(args.username)

        case "pastes":
            
            if config.getboolean('PASTES_SEARCH', 'pastebin_search'):
                from pastes_search.pastebin import pastebin_search
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in pastes through PsbDmp..." + Style.RESET_ALL)
                print(" ┃")
                pastebin_search(args.username)
        
        case "vars":

            if config.getboolean('MUTATIONS', 'username_variations'):
                from username_mutations.username_variations import username_variations
                variants = username_variations(args.username)
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Generating username variations..." + Style.RESET_ALL)
                print(" ┗━>")
                for v in variants[:20]: 
                    print("    " + v)
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + f" Total generated: {len(variants)} variants.")
        
        case "clearnet":

            if config.getboolean('CLEARNET_SEARCH', 'google_search'):
                from search_systems.google_search import google_search
                print("[" + Fore.YELLOW + "*" + Style.RESET_ALL + "]" + Fore.YELLOW + " Searching in google..." + Style.RESET_ALL)
                print(" ┃")
                google_search(f"intext:{args.username} | intitle:{args.username}")
        
        
        
        case "help":

            print("""
                  
Specify one of these functions:
                  
 - help - show this help message.
 - all - search for all modules.
 - leaks - search only for leaks
 - exis - check username existence on different platforms.
 - vars - mutate username to other variations
 - pastes - search username in pastes
 - darknet - search username in darknet
 - clearnet
Examples:

   >_ python main.py help
                  
   >_ python main.py all <username>
""")



if __name__ == "__main__":
    main()