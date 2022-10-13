from collections import UserString
import re

canon_dir = "/users/joe/test/test.txt"


def displayMenu():
    userInput = ""
    while(userInput != "M" and userInput != "A"):
        userInput = input(
            "Please input 'M' to manually input a file path or 'A' to automatically execute the test cases: ")
        userInput = userInput.upper()
    return userInput


def canonicalize(url):
    x = re.sub("(?<!\.)\.[\/\\\\]", "", url)
    return x


def isHomograph(f1, f2):
    return True


def compareNonHomographs(f1, f2):
    return


def compareHomographs(f1, f2):
    return


def compareTwoFilePaths():
    print(canonicalize("./././.././test.txt"))
    print(canonicalize(".\.\././test.txt"))
    file1 = input("Input the name of the first file: ")
    file2 = input("Input the name of the second file: ")
    file1 = canonicalize(file1)
    file2 = canonicalize(file2)
    print(file1)
    print(file2)

    homograph = isHomograph(file1, file2)

    if homograph == True:  # This logic might not be correct. Feel free to revise if it isn't.
        compareHomographs(file1, file2)
    else:
        compareNonHomographs(file1, file2)


def executeTestCases():
    return


if __name__ == '__main__':
    userInput = displayMenu()
    if userInput == "A":
        executeTestCases()
    else:
        compareTwoFilePaths()
