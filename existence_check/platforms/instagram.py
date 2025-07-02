import instaloader
import os
import contextlib
from instaloader.exceptions import ProfileNotExistsException, ConnectionException
from colorama import init, Fore, Style
init()
@contextlib.contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
            yield

def instagram_check(username):
    loader = instaloader.Instaloader()
    try:
        with suppress_output():
            instaloader.Profile.from_username(loader.context, username)
        print(f" ┣" + "[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + f" Instagram: @{username} exists.")
    except (ProfileNotExistsException, ConnectionException):
        return False
    except Exception:
        return False
