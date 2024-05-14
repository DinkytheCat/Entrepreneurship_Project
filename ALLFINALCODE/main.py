from cipher import AES256
from Manager import PasswordManager
import os

def fetchMasterKey():
    masterKey = b'GT1DFpQhbd1w9afJWjTJUKqDWL7sDm+ruS3qCgdkqBE='
    return masterKey

def fetchSecret():
    return "textToMatch"

def prompt_menu():
    os.system("clear")
    print("1. Find Password")
    print("2. Add Password")
    print("3. Delete Password")
    print("4. Press to Exit")

    print("\nChoice: ", end="")
    choice = int(input())
    return choice

def delete_password(password_manager, passwords, encrypter):
    app = input("Application Name: ")
    for entry in passwords:
        if app == encrypter.decrypt(entry[0]):
            confirm = input(f"Are you sure want to delete '{app}' [y/n]: ")

            if confirm == "y":
                del passwords[passwords.index(entry)]
                password_manager.save(passwords)
                print("Password Successfully Deleted.")  
            break
    input("Press Any Key to Continue.")

def add_password(password_manager, passwords, encrypter):
    app = input("Application Name: ")
    password = input("Password: ")

    passwords.append([encrypter.encrypt(app ).decode(), encrypter.encrypt(password).decode()])
    password_manager.save(passwords)
    input("Password Successfully Added. Press Any Key to Continue.")

def find_password(passwords, encrypter):
    app = input("Application Name: ")
    for entry in passwords:
        if app in encrypter.decrypt(entry[0]):
            print("\n-----------------------------------------")
            print(f"Application: {encrypter.decrypt(entry[0])}")
            print(f"Password: {encrypter.decrypt(entry[1])}")
    input("Press Any Key to Continue.")

password_manager = PasswordManager("passwords.txt")
passwords = password_manager.read()
already_loggedIn = False

while True:
    if not already_loggedIn:
        masterPassword = input("Enter Master Password:")

        encrypter = AES256(masterPassword)

        if encrypter.encrypt(fetchSecret()) != fetchMasterKey():
            input("Password Incorrect. Press Any Key to Continue")
            continue
        else:
            already_loggedIn = True

   # display the menu and get the choice
    choice = prompt_menu()

    if choice < 1 or choice > 4:
        input("Choice needs to be a number from 1-4. Press Any Key to Continue.")
        continue
    elif choice == 1:
        find_password(passwords, encrypter)
    elif choice == 2:
        add_password(password_manager, passwords, encrypter)
    elif choice == 3:
        delete_password(password_manager, passwords, encrypter)    
    else:
        print("Exiting the Password Manager.") 
        exit(0)       
