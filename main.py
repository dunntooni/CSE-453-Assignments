from collections import UserString
import re

canon_dir = "C:/users/bob/test.txt"


def displayMenu():
    userInput = ""
    while(userInput != "M" and userInput != "A"):
        userInput = input(
            "Please input 'M' to manually input a file path or 'A' to automatically execute the test cases: ")
        userInput = userInput.upper()
    return userInput


def canonicalize(filepath):
    # Sanitize the inputted file
    filepath = filepath.lower()
    canon = re.sub("[\/\\\\]+", "\\\\", filepath) # This ugly bit of regex turns all instances of multiple \ or / into a single \
    canon = re.sub("(?<!\.)\.\\\\", "", canon)    # This deletes all instances of ".\"

    # Split the string into a list and parse it
    list = re.split("[\/\\\\]", canon)
    newURL = ["users", "bob"] # We're using forward slashes to avoid having to do escapes and getting confused
    isFirst = True
    for item in list:
        if isFirst:
            isFirst = False
            if item == '..':
                newURL.pop()
            else:
                newURL = []
                newURL.push(item)
        else:
            if item == "..":
            
            else:
                

    print(list)
    return canon

def isHomograph(f1, f2):
     return canonicalize(f1) == canonicalize(f2)

def compareNonHomographs(f1, f2):
    return


def compareHomographs(f1, f2):
    return


def compareTwoFilePaths():
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
