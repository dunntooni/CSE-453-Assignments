import re

# This function will take users input as is and plug it into the SQL statement 
def genQuery(username, password):
    return f"SELECT * FROM users WHERE userName = \'{username}\' AND userPassword = \'{password}\'"

# This function runs user input through a blacklist of characters and removes characters that could prove problematic
# We decided to allow the space character.
# the Following characters are removed: ; - ' " = *
def genQueryWeak(username, password):
    username = re.sub("[;\-\'\"=*]", "", username)
    password = re.sub("[;\-\'\"=*]", "", password)
    return f"SELECT * FROM users WHERE userName = \'{username}\' AND userPassword = \'{password}\'"

# The strong mitigation will compare the inputed username and password against known usernames and passwords. If it doesn't
# match any existing usernames or passwords, the whole input is rejected as bad input.
def genQueryStrong(username, password):
    #In a real system, these would be grabbed from a database in the background. For this purpose this is fine
    knownUsernames = ["ValidUsername", "Erick", "ikeypoo", "jimbob"]
    knownPasswords = ["Valid_Password", "coolEpicPassword97", "DankchickyNuggies_1", "password"]
    
    #If the username matches a known username, allow it to be plugged in to the sql statement 
    sqlUsername = ""
    if username in knownUsernames:
        sqlUsername = username

    #If the password matches a known password, allow it to be plugged in to the sql statement
    sqlPassword = ""
    if password in knownPasswords:
        sqlPassword = password

    #Plug in the accepted input to the SQL statement and make the query
    return f"SELECT * FROM users WHERE userName = \'{sqlUsername}\' AND userPassword = \'{sqlPassword}\'"

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testValid(queryGenerator):
    print("\tTESTING VALID INPUTS")
    print("\t********************")

    test_cases = [("ValidUsername", "Valid_Password"),
                  ("ikeypoo", "coolEpicPassword97"),
                  ("Erick", "DankchickyNuggies_1"),
                  ("jimbob", "password")]
    for test in test_cases:
        print(f"\tTesting with inputs: Username = \"{test[0]}\"  Password = \"{test[1]}\"")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testTautology(queryGenerator):
    print("\tTESTING TAUTOLOGY ATTACKS")
    print("\t*************************")

    test_cases = [("bob", "none' OR 'x' = 'x"), 
                  ("ikeypoo", "password' OR 'password lol' = 'password lol"), 
                  ("Erick", "asdf' OR 'blackTv_123' = 'blackTv123"),
                  ("jimbob", "hopeIsDescending' OR '1' = '1")]
    for test in test_cases:
        print(f"\tTesting with inputs: Username = \"{test[0]}\"  Password = \"{test[1]}\"")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testUnion(queryGenerator):
    print("\tTESTING UNION ATTACKS")
    print("\t*********************")

    test_cases = [("bob", "gobbledygook' UNION SELECT * FROM users;--"), 
                  ("ikeypoo", "gabbagoo' UNION SELECT * FROM authData;--"),
                  ("Erick", "main_admin' UNION SELECT * FROM users;--"),
                  ("jimbob", "valjean' UNION SELECT * FROM authData;--")]
    for test in test_cases:
        print(f"\tTesting with inputs: Username = \"{test[0]}\" Password = \"{test[1]}\"")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testAddState(queryGenerator):
    print("\tTESTING ADD STATE ATTACKS")
    print("\t*************************")

    test_cases = [("Erick", "asdf' ; INSERT INTO users (userName, userPassword) VALUES ('Erick', '6969'); -- "), 
                  ("regular_joe", "password'; DROP TABLE users;--"),
                  ("ikeypoo", "funnypasswordhaha'; INSERT INTO authData (userName, accessLevel) VALUES ('ikeypoo', 'Admin'); --"),
                  ("jimbob", "trumpCard'; DROP TABLE authData;--")]
    for test in test_cases:
        print(f"\tTesting with inputs:  Username = \"{test[0]}\" Password \"{test[1]}\"")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testComment(queryGenerator):
    print("\tTESTING COMMENT ATTACKS")
    print("\t***********************")

    test_cases = [("Root'; --", "nothing_lol"), 
                  ("BestUser';--", "You've been hacked!"),
                  ("Erick';--", "Sucks to be you XD"),
                  ("jimbob';--", "Monologue Time")]
    for test in test_cases:
        print(f"\tTesting with inputs: Username = \"{test[0]}\"  Password = \"{test[1]}\"")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

if __name__ == '__main__':
    #For these inputs, the input should be plugged into the SQL query as is, allowing exploitation.
    print("TESTING NO MITIGATION:")
    print("*"*22 +"\n")
    testValid(genQuery)
    testTautology(genQuery)
    testUnion(genQuery)
    testAddState(genQuery)
    testComment(genQuery)

    #For this round of testing, Weak mitigation should remove problematic characters from input and put remaining characters in query
    print("TESTING WEAK MITIGATION:")
    print("************************\n")
    testValid(genQueryWeak)
    testTautology(genQueryWeak)
    testUnion(genQueryWeak)
    testAddState(genQueryWeak)
    testComment(genQueryWeak)

    #For this round of testing, strong mitigation compares user input to known acceptable input and disallow unknown input 
    print("TESTING STRONG MITIGATION:")
    print("**************************\n")
    testValid(genQueryStrong)
    testTautology(genQueryStrong)
    testUnion(genQueryStrong)
    testAddState(genQueryStrong)
    testComment(genQueryStrong)