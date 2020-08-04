import time
import random
import string
from datetime import datetime
from cryptography.fernet import Fernet


users = {"User": "Password"}

pass_key = "123456"


def pas(length=12):
    p = string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(p) for i in range(length))


pw = pas()


def view():
    project = open("enter location where your passwords are stored, C:/Users/ etc...", "r")
    print(project.read())
    project.close()


def encrypt_pass():
    fern = open("enter location for your key, C:/Users/ etc...", "rb")
    key = fern.read()
    cipher = Fernet(key)
    filename = "enter location where your passwords are stored, C:/Users/ etc..."
    with open(filename, 'rb')as f:
        e_file = f.read()
    encrypted_file = cipher.encrypt(e_file)
    with open(filename, 'wb')as ef:
        ef.write(encrypted_file)


def decrypt_pass():
    key_pass = input("Key: ")
    if key_pass == "123456":
        fkey = open("enter location for your key, C:/Users/ etc...", "rb")
        key = fkey.read()
        cipher = Fernet(key)
        with open('enter location where your passwords are stored, C:/Users/ etc...', 'rb')as df:
            encrypted_data = df.read()

        decrypted_file = cipher.decrypt(encrypted_data)

        with open("enter location where your passwords are stored, C:/Users/ etc...", "wb")as df:
            df.write(decrypted_file)
    else:
        print("Incorrect Key!")
        decrypt_pass()


def login():
    username = input("Username: ")
    password = input("Password: ")
    while username in users.keys() and users[username] == password:
        print("\n" + "~"*5)
        print("Login Successful!")
        print("What would you like to do?")
        print("q -> quit program")
        print("c -> create and store password")
        print("e -> encrypt password")
        print("d -> decrypt password")
        print("v -> view password list")
        input_ = input(":")

        if input_ == "q":
            quit()
        if input_ == "c":
            print("Password for " + username + " is: " + pw)
            with open("enter location where you want to store passwords like C:/Users/ etc...", "a") as s:
                s.write("\n")
                s.write(username + " : " + pw + datetime.now().strftime(' |%Y-%m-%d |%H:%M:%S'))
                s.close()
        if input_ == "e":
            encrypt_pass()
            print("Password successfully encrypted!")
        if input_ == "d":
            decrypt_pass()
            print("Password has been decrypted!\n       ---Remember to encrypt password before closing the program!!!")
        if input_ == "v":
            view()
    else:
        print("Wrong username or password! Try again in 3 seconds...")
        time.sleep(3)
        login()


login()
