import re

def valid_symbol(symbol):
    STOCK_SYMBOL_PATTERN = "[A-Z]{1,4}((\.){1}[A|B]{1}){0,1}$"

    pattern = re.compile(STOCK_SYMBOL_PATTERN)
    match = pattern.match(symbol)

    if match is None:
        return False

    return True