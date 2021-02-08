from termcolor import colored
import colorama  # Require install (pip install colorama)
colorama.init()


def logo():
    print(colored('''          __  ___  _ _  __  ___  _  _  ___   __  ___ 
         / _||_ _|| | ||  \| __|| \| ||_ _| |  \| o )
         \_ \ | | | U || o ) _| | \\\\ | | |  | o ) o \\
         |__/ |_| |___||__/|___||_|\_| |_|  |__/|___/''', 'blue', attrs=['bold']))


def print_menu():
    print(colored('''
+——————————————————————[  MAIN MENU  ]—————— Lab no. 2 ——————+
|    1. Read CSV-file    4. Add Student      7. Quit         │
|    2. Show JSON-data   5. Remove Student                   │
|    3. Save to File     6. Search Student                   │
+————————————————————————————————————————————————————————————+''', 'magenta'))


def remove_menu():
    print(colored('''
+————————————————————[  Remove Student  ]————————————————————+
|    [list] Show list again   [exit] Go back to main menu    │
+————————————————————————————————————————————————————————————+''', 'magenta'))


def add_menu():
    print(colored('''
+——————————————————————[  Add Student  ]—————————————————————+
|      1. Add another student   2. Go back to main menu      │
+————————————————————————————————————————————————————————————+''', 'magenta'))


def search_menu():
    print(colored('''
+————————————————————[  Search Student  ]————————————————————+
|         1. Search again   2. Go back to main menu          │
+————————————————————————————————————————————————————————————+''', 'magenta'))


def add_header():
    print(colored('''
+——————————————————————[  Add Student  ]—————————————————————+''', 'blue'))


def search_header():
    print(colored('''
+—————————————————————[  Search Student  ]———————————————————+''', 'blue'))


def search_result():
    print(colored('''
+—————————————————————[  Search Results  ]———————————————————+''', 'cyan'))

