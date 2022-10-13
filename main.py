import re

canon_dir = "/users/joe/test/test.txt"


def displayMenu():
    # comment
    return


def canonicalize(url):
    x = re.sub("(?<!\.)\.[\/\\\\]", "", url)
    return x


def isHomograph():
    return


def compareNonHomographs():
    return


def compareHomographs():
    return

if __name__ == '__main__':
    print(canonicalize("./././.././test.txt"))
    print(canonicalize(".\.\././test.txt"))