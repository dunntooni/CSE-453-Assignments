import re

# This function will take users input as is and plug it into the SQL statement 
def genQuery(username, password):
    return f"SELECT * FROM users WHERE userName = \'{username}\' AND userPassword = \'{password}\'"

# 
def genQueryWeak(username, password):
    username = re.sub("[;\-\'\"=*]", "", username)
    password = re.sub("[;\-\'\"=*]", "", password)
    return f"SELECT * FROM users WHERE userName = \'{username}\' AND userPassword = \'{password}\'"

def genQueryStrong(username, password):
    usernameList = ["ValidUsername", "Erick", "ikeypoo"]
    username = ["a","b", ...]
    passwordList = []
    
    sql = ""
    return sql

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testValid(queryGenerator):
    print("\tTESTING VALID INPUTS")
    print("\t********************")

    test_cases = [("ValidUsername", "Valid_Password"),
                  ("ikeypoo", "coolEpicPassword97"),
                  ("Erick", "DankchickyNuggies_1")]
    for test in test_cases:
        print(f"\tTesting with inputs Username: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testTautology(queryGenerator):
    print("\tTESTING TAUTOLOGY ATTACKS")
    print("\t*************************")

    test_cases = [("bob", "none' OR 'x' = 'x"), 
                  ("ikeypoo", "password' OR 'password lol' = 'password lol"), 
                  ("Erick", "asdf' OR 'blackTv_123' = 'blackTv123"),]
    for test in test_cases:
        print(f"\tTesting with inputs Username: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testUnion(queryGenerator):
    print("\tTESTING UNION ATTACKS")
    print("\t*********************")

    test_cases = [("bob", "gobbledygook' UNION SELECT * FROM users;--"), 
                  ("ikeypoo", "gabbagoo' UNION SELECT * FROM authData;--"),
                  ("Erick", "main_admin' UNION SELECT * FROM users;--")]
    for test in test_cases:
        print(f"\tTesting with inputs Username: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testAddState(queryGenerator):
    print("\tTESTING ADD STATE ATTACKS")
    print("\t*************************")

    test_cases = [("Erick", "asdf' ; INSERT INTO users (userName, userPassword) VALUES ('Erick', '6969'); -- "), 
                  ("regular_joe", "password'; DROP TABLE users;--"),
                  ("ikeypoo", "funnypasswordhaha'; INSERT INTO authData (userName, accessLevel) VALUES ('ikeypoo', 'Admin'); --")]
    for test in test_cases:
        print(f"\tTesting with inputs Username: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

#This implementation requires the mitigation function be passed in as a parameter. This can be any mitigation function
def testComment(queryGenerator):
    print("\tTESTING COMMENT ATTACKS")
    print("\t***********************")

    test_cases = [("Root'; --", "nothing_lol"), 
                  ("BestUser';--", "You've been hacked!"),
                  ("Erick';--", "Sucks to be you XD")]
    for test in test_cases:
        print(f"\tTesting with inputs Username: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

if __name__ == '__main__':
    print("TESTING NO MITIGATION:")
    print("*"*22 +"\n")
    testValid(genQuery)
    testTautology(genQuery)
    testUnion(genQuery)
    testAddState(genQuery)
    testComment(genQuery)

    print("TESTING WEAK MITIGATION:")
    print("************************\n")
    testValid(genQueryWeak)
    testTautology(genQueryWeak)
    testUnion(genQueryWeak)
    testAddState(genQueryWeak)
    testComment(genQueryWeak)

    print("TESTING STRONG MITIGATION:")
    print("**************************\n")
    testValid(genQueryStrong)
    testTautology(genQueryStrong)
    testUnion(genQueryStrong)
    testAddState(genQueryStrong)
    testComment(genQueryStrong)