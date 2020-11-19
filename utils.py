from distutils import util
def confirm(question, default='no'):
    if default is None:
        prompt = " [y/n] "
    elif default == 'yes':
        prompt = " [Y/n] "
    elif default == 'no':
        prompt = " [y/N] "
    else:
        raise ValueError(f"Unknown setting '{default}' for default.")

    while True:
        try:
            resp = input(question + prompt).strip().lower()
            if default is not None and resp == '':
                return default == 'yes'
            else:
                return util.strtobool(resp)
        except ValueError:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

from colorama import Style
def cprint(text, color):
    print(f'{color}{text}{Style.RESET_ALL}')

import sys
def terminal():
    return sys.stdin.isatty()

import json
def pprint(obj):
    return json.dumps(obj, indent=4, sort_keys=True)