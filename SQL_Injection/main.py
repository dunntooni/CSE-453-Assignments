def genQuery(username, password):
    sql = f"SELECT * FROM table WHERE user = '{username}' AND userPassword = '{password}'"
    return sql

def genQueryWeak(username, password):
    sql = ""
    return sql

def genQueryStrong(username, password):
    sql = ""
    return sql

def testValid(queryGenerator):
    print("\tTESTING VALID INPUTS")
    print("\t********************")

    test_cases = [("ValidUsername", "Valid_Password")]
    for test in test_cases:
        print(f"\tUsername: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

def testTautology(queryGenerator):
    print("\tTESTING TAUTOLOGY ATTACKS")
    print("\t*************************")

    test_cases = [("ValidUsername", "Valid_Password")]
    for test in test_cases:
        print(f"\tUsername: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

def testUnion(queryGenerator):
    print("\tTESTING UNION ATTACKS")
    print("\t*********************")

    test_cases = [("ValidUsername", "Valid_Password")]
    for test in test_cases:
        print(f"\tUsername: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

def testAddState(queryGenerator):
    print("\tTESTING ADD STATE ATTACKS")
    print("\t*************************")

    test_cases = [("ValidUsername", "Valid_Password")]
    for test in test_cases:
        print(f"\tUsername: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"\tSQL statement is:    {sql}")
    print("")

def testComment(queryGenerator):
    print("\tTESTING COMMENT ATTACKS")
    print("\t***********************")

    test_cases = [("ValidUsername", "Valid_Password")]
    for test in test_cases:
        print(f"\tUsername: {test[0]}  Password: {test[1]}")
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