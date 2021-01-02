import string
from datetime import datetime
import random
from cryptography.fernet import Fernet
import time
import getpass


users = {"User": "Password"}
pass_key = "123456"


class Password:
    def __init__(self):
        pass

    def get_pwLNS(self, length=10):
        self.pw = string.ascii_lowercase + string.digits + string.punctuation
        return ''.join(random.choice(self.pw) for i in range(length))

    def get_pwNL(self, length=10):
        self.pw = string.ascii_lowercase + string.digits
        return ''.join(random.choice(self.pw) for i in range(length))

    def get_pwOL(self, length=10):
        self.pw = string.ascii_lowercase + string.ascii_uppercase
        return ''.join(random.choice(self.pw) for i in range(length))

    def get_date(self):
        return datetime.now().strftime('|%Y-%m-%d |%H:%M:%S')


class Encryption:
    def __init__(self):
        pass

    def encrypt(self):
        fern = open("C:/Users/zydmu/OneDrive/Desktop/Key/Key.txt", "rb")
        key = fern.read()
        cipher = Fernet(key)
        filename = "C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt"
        with open(filename, 'rb') as f:
            file = f.read()
            encrypted_text = cipher.encrypt(file)
        with open(filename, 'wb')as ef:
            ef.write(encrypted_text)


class Decryption:
    def __init__(self):
        pass

    def decryption(self):
        key_pass = getpass.getpass(prompt='Key:', stream=None)
        if key_pass == "123456":
            fkey = open("C:/Users/zydmu/OneDrive/Desktop/Key/Key.txt", "rb")
            key = fkey.read()
            cipher = Fernet(key)
            with open('C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt', 'rb')as df:
                encrypted_data = df.read()

            decrypted_file = cipher.decrypt(encrypted_data)

            with open("C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt", "wb")as df:
                df.write(decrypted_file)
        else:
            print("Incorrect Key!")
            quit()


def login():
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ', stream=None)
    while username in users.keys() and users[username] == password:
        print("\n" + "~"*5)
        print("Login Successful!")
        print("What would you like to do?")
        print("q -> quit program")
        print("c -> create and store password")
        print("e -> encrypt password")
        print("d -> decrypt password")
        print("v -> view password list")
        input1 = input(":")

        if input1 == "q":
            quit()

        if input1 == "c":
            print("     What type of password do you prefer?")
            print("OL -> only letters (not safest, but easiest to remember)")
            print("NL -> numbers and letters (safer, but harder to remember)")
            print("LNS -> letters, numbers and signs (safest option but hardest to remember)")
            input2 = input(":")
            if input2 == "OL":
                p3 = Password()
                pas1 = p3.get_pwOL()
                serv1 = input("Service: ")
                date = p3.get_date()
                print("Your password for " + serv1 + " is: " + pas1)
                print("ALWAYS REMEMBER TO ENCRYPT YOUR PASSWORDS!!!")
                filename = "C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt"
                with open(filename, 'a')as ef:
                    ef.write("\n")
                    ef.write(serv1 + ": " + pas1 + (" " * 82) + date)
                    ef.close()
            elif input2 == "NL":
                p4 = Password()
                pas2 = p4.get_pwNL()
                serv2 = input("Service: ")
                date = p4.get_date()
                print("Your password for " + serv2 + " is: " + pas2)
                print("ALWAYS REMEMBER TO ENCRYPT YOUR PASSWORDS!!!")
                filename = "C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt"
                with open(filename, 'a')as ef:
                    ef.write("\n")
                    ef.write(serv2 + ": " + pas2 + (" " * 82) + date)
                    ef.close()

            elif input2 == "LNS":
                p5 = Password()
                pas3 = p5.get_pwLNS()
                serv3 = input("Service: ")
                date = p5.get_date()
                print("Your password for " + serv3 + " is: " + pas3)
                print("ALWAYS REMEMBER TO ENCRYPT YOUR PASSWORDS!!!")
                filename = "C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt"
                text1 = serv3 + ": " + pas3 + (" " * 82) + date
                with open(filename, 'a')as ef:
                    ef.write("\n")
                    ef.write(text1)
                    ef.close()

        if input1 == "e":
            p4 = Encryption()
            p4.encrypt()
            print("Passwords successfully encrypted!")

        if input1 == "d":
            p5 = Decryption()
            p5.decryption()
            print("Successfully decrypted! Remember to encrypt your passwords after every session!!!")

        if input1 == "v":
            project = open("C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt", "r")
            print(project.read())
            project.close()

    else:
        print("Wrong username or password! Try again in 3 seconds...")
        time.sleep(3)
        login()


login()
