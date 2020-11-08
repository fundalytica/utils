import sys

def valid_arg_count(count = 2):
    if len(sys.argv) != count:
        return False

    return True

