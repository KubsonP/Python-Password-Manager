# Python-Password-Manager
This project is meant to create, store and encrypt your passwords. I used fernet instead of hashing for the sole purpose of ability to decrypt the password if needed. Option 
which hashing doesn`t have. Hashing is of course safer thanks to that, but I wanted to have the ability to check the passwords.

Before running the program you need to create folder for storing your passwords and another folder for your key!

If you're running Pass Manager in OOP in PyCharm you need to check the "Emulate terminal in output console" bracket in configuration for getpass module to work.
In terminal it works without issues.
