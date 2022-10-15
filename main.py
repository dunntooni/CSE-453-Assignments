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
    canon = re.sub("[\/\\\\]+", "\\\\",
                   filepath)  # This ugly bit of regex turns all instances of multiple \ or / into a single \
    canon = re.sub("(?<!\.)\.\\\\", "",
                   canon)    # This deletes all instances of ".\"

    # Split the string into a list and parse it
    list = re.split("[\/\\\\]", canon)
    # We're using forward slashes to avoid having to do escapes and getting confused
    path_pieces = ["users", "bob"]
    isFirst = True
    for item in list:
        if isFirst:
            isFirst = False
            if item == '..':
                path_pieces.pop()

            else:
                path_pieces = []
                if item != "c:":
                    path_pieces.append(item)
        else:
            if item == "..":
                if(len(path_pieces) > 0):
                    path_pieces.pop()
            else:
                if item != "c:":
                    path_pieces.append(item)
    filepath = "\\".join(path_pieces)
    filepath = "C:\\" + filepath
    return filepath


def isHomograph(f1, f2):
    return canonicalize(f1) == canonicalize(f2)


def compareNonHomographs():
    nonHomographFileNames = open("non-homographs.txt", "r")
    print("\nRunning tests on non-homographs.txt...")
    isError = False
    for filename in nonHomographFileNames:
        filename = filename.replace('\n', '')
        isNonHomograph = not isHomograph(filename, canon_dir)
        if isNonHomograph == False:
            print("Error: ", filename, " is a homograph with ", canon_dir,)
            isError = True
    if isError:
        print("One or more lines were homographs. Test failed.")
    else:
        print("No errors detected. Success!")


def compareHomographs():
    homographFileNames = open("homographs.txt", "r")
    print("\nRunning tests on homographs.txt...")
    isError = False
    for filename in homographFileNames:
        filename = filename.replace('\n', '')
        isAHomograph = isHomograph(filename, canon_dir)
        if isAHomograph == False:
            print("ERROR:", filename, "is not a homograph with", canon_dir)
            isError = True
    if isError:
        print("One or more lines were not homographs. Test failed.")
    else:
        print("No errors detected. Success!")


def compareTwoFilePaths():
    file1 = input("Input the name of the first file: ")
    file2 = input("Input the name of the second file: ")
    homograph = isHomograph(file1, file2)

    if homograph == True:
        print(file1, " and ", file2, " are homographs.")
    else:
        print(file1, " and ", file2, " are not homographs.")


if __name__ == '__main__':
    userInput = displayMenu()
    if userInput == "A":
        # Test cases for homographs.
        compareHomographs()
        compareNonHomographs()
    else:
        compareTwoFilePaths()
