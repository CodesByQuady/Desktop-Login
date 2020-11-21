#Deskstop Login Program

print('Before signing into the system, you must create a vaild user login and password.')
valid_users = {} #Empty dictionary allows the results to be fully customizable.
def user_login():
    print('Create a username, it can be letters and numbers.')
    create_user = input('Username: ')
    print(create_user, 'has been created by the user')
    while True: #This while loop will keep asking the user for a password until it meets the criteria.
        print("""
In order to complete the sign up process, you must create a password.
Password must at least 8 characters long.
Password must also include letters and numbers.
""")
        password = input()
        if len(password) < 8: #This condition runs if the length of the password is lower than 8.
            print('Password is not long enough. Try Again.')
            continue

        elif password.isalpha(): #This condition will run if the user doesn't enter a number with their password.
            print('Password must include letters and numbers. Try Again.')
            continue
        elif password.isalnum() and len(password) >= 8: #This line of code has two conditions, which will be ran if both are true.
            print("""
Password meets criteria.
Rebooting.....
""")
            valid_users[create_user] = password #This line of code will create a Username/Password pair for the empty dictionary.
            break

        elif password == '': #This condition is ran if the user presses enter without typing anything.
            print('Password cannot be an empty space. Try Again.')
            continue
        
        else: #This line of code is if the customer entered a special character (i.e !, @, #, $).
            print("""
No need for special chartacters, just letters and numbers.
""")
            continue
    print("SYSTEM DESKTOP".center(35, '='))
    print("""
System is rebooted, please sign into the database to finish changes.
""")
    while True: #This line of code will be ran once the user completes the accoiunt creation.
        login_ID = input('Enter Username: ')
        if login_ID not in valid_users.keys(): #If the login_ID is not found inside of the valid_user, then the program will keep asking for the proper login ID.
            print("""
User cannot be found, enter a vaild username.
""")
            continue
        else: #This code is ran when the login_ID matches the the user's created username from earlier.
            print(login_ID, 'is found in the database, now enter your paassword.')
            break
    while True: #This loop is ran after the login_ID is found inside of dictionary.
        password_attempt = input('Enter Your Password: ')
        if password_attempt == valid_users[create_user]: #The program will end after the correct password is entered.
            print("""
Username and password are correct, welcome to the database.
""")
            break
        else: #This will keep asking the user to enter it's password until it's correct.
            print("""
The password you entered is incorrect, try again.
""")
            continue

user_login()
