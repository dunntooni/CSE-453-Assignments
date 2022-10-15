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
    canon = re.sub("[\/\\\\]+", "\\\\", filepath)  # This ugly bit of regex turns all instances of multiple \ or / into a single \

    # Split the string into a list and parse it. Each list item should be a directory or a relative filepath directive
    list = re.split("[\/\\\\]", canon)
    
    # This is what we are assuming the current working directory is. i.e. "c:\users\bob"
    path_pieces = ["users", "bob"]
    
    # we need to do a special check with the first item to see if we're dealing with a relative or absolute filepath
    isFirst = True
    for item in list:
        #The first item is a special case and we use it to determine if the filepath is absolute or relative
        if isFirst:
            isFirst = False
            # relative file path where we move back a directory
            if item == '..':
                path_pieces.pop()

            # relative file path so we want to stay in the current directory
            elif item == ".":
                continue
            
            # absolute filepath so we need to start from root
            else:
                path_pieces = []
                # we add the root directory at the end to the canonized version so we don't want duplicates
                if item != "c:":
                    path_pieces.append(item)
        else:
            # go up a directory level
            if item == "..":
                # we can't go back a directory if we're already at root
                if(len(path_pieces) > 0):
                    path_pieces.pop()
            
            # ./ case we remain in current directory
            elif item == ".":
                continue
            
            # add another directory or filename to the filepath
            else:
                # we add the root directory at the end to the canonized version so we don't want duplicates
                if item != "c:":
                    path_pieces.append(item)
    
    # frankenstein our filepath together 
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
