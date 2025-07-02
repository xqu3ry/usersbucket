from itertools import product
from colorama import init, Fore, Style
init()

def username_variations(username):
    leet_map = {
        'a': ['a', '4', '@'],
        'b': ['b', '8'],
        'e': ['e', '3'],
        'i': ['i', '1', '!'],
        'l': ['l', '1', '|'],
        'o': ['o', '0'],
        's': ['s', '5', '$'],
        't': ['t', '7'],
        'g': ['g', '9'],
        'z': ['z', '2'],
        'c': ['c', '('],
        'h': ['h', '#'],
        'x': ['x', '%']
    }

    
    replacements = [leet_map.get(char.lower(), [char]) for char in username]

    
    variants = set(''.join(chars) for chars in product(*replacements))

    return list(variants)





