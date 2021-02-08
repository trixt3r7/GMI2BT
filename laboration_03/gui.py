from termcolor import colored
import colorama  # Require install (pip install colorama)
colorama.init()

def logo():
    print(colored('''
              __ __  ___  _ _  _  ___   ___  ___ 
             |  \  \| . || | || || __> | . \| . >
             |     || | || ' || || _>  | | || . \\
             |_|_|_|`___'|__/ |_||___> |___/|___/''', 'blue', attrs=['bold']))


def print_menu():
    print(colored('''
+——————————————————————[  MAIN MENU  ]—————— Lab no. 3 ——————+
|    1. Search Movie         3. Detailed Movie Information   │
|    2. 10 Latest Searches   4. QUIT                         │
+————————————————————————————————————————————————————————————+''', 'magenta'))


def previous_header():
    print(colored('''
+———————————————————[  10 Latest Searches  ]—————————————————+''', 'blue'))


def search_header():
    print(colored('''
+——————————————————————[  Search Movie  ]————————————————————+''', 'blue'))


def movie_list_header():
    print(colored('''
+———————————————————————[  Movie List  ]—————————————————————+''', 'blue'))


def movie_info_header():
    print(colored('''
+———————————————————[  Movie Information  ]——————————————————+''', 'blue'))


def hr_header():
    print(colored('''+————————————————————————————————————————————————————————————+''', 'blue'))
