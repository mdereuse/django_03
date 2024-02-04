import sys
from antigravity import geohash


class WrongNumberArguments(Exception):
    def __init__(self):
        self.args = ("Ce programme prend trois arguments en parametres.",)


def main():
    args = sys.argv[1:]
    if len(args) != 3:
        raise WrongNumberArguments
    try:
        a = float(args[0])
        b = float(args[1])
        c = args[2].encode("utf-8")
    except ValueError as e:
        raise e
    else:
        geohash(a, b, c)


if __name__ == "__main__":
    try:
        main()
    except (WrongNumberArguments, ValueError) as e:
        print(e)
