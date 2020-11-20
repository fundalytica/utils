from utils import utils

from colorama import Fore

import pandas as pd

# read data frame
def df_read(file, sort=False, verbose=False):
    csv = utils.file_extension(file) == '.csv'

    if verbose:
        utils.cprint('\n[ DataFrame Read ]', Fore.GREEN)
        utils.cprint(file, Fore.CYAN)

    try:
        if csv:
            df = pd.read_csv(file, index_col='date')
        else:
            df = pd.read_pickle(file)

        if sort:
            df.sort_index(inplace=True)
        if verbose:
            print(f'\n{df}')
    except IOError as e:
        if verbose:
            utils.cprint('> File Not Found', Fore.RED)
        return None
    except pd.errors.EmptyDataError as e:
        if verbose:
            utils.cprint('> Empty Data', Fore.RED)
        return None

    return df

# write data frame
def df_write(df, file, sort=False, verbose=False):
    csv = utils.file_extension(file) == '.csv'
    print(utils.file_extension(file))

    if verbose:
        utils.cprint('\n[ DataFrame Write ]', Fore.GREEN)
        utils.cprint(file, Fore.CYAN)

    if sort:
        df.sort_index(inplace=True)

    if csv:
        df.to_csv(file)
    else:
        df.to_pickle(file)

    if verbose:
        utils.cprint('> OK', Fore.MAGENTA)