sys_user_name = "admin"
sys_user_password = "123456"

while True:

    user_name = input("Enter username:")
    
    if user_name != sys_user_name:
        print("Incorrect username, please try again.")

    elif user_name == sys_user_name:
        user_password = input("Enter password:")
        if user_password == sys_user_password:
            print("Login successful!")
            break
        else:
            print("Incorrect password, please try again.")