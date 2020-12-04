import os
import sys
import json
import pathlib
from distutils import util

import pandas as pd
from colorama import Style
from pympler import asizeof

# user confirmation prompt
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

# running from terminal
def terminal():
    return sys.stdin.isatty()

def file_path(file):
    return pathlib.Path(file).parent.absolute()

def file_name(file):
    return os.path.splitext(file)[0]

def file_extension(file):
    return os.path.splitext(file)[1]

# obj pretty printing (converts into json)
def obj_print(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

# color print
def cprint(text, color):
    print(f'{color}{text}{Style.RESET_ALL}')

# data size in mb
def mbsize(data):
    return f'{(asizeof.asizeof(data) / 1024 / 1024):.2f} MB'

# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#from-timestamps-to-epoch
def pd_ts_to_unix_ts(pd_ts):
    return (pd_ts - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

