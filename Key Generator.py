from cryptography.fernet import Fernet

# Put this somewhere safe!
key = Fernet.generate_key()
with open("Safe location for your key", "wb") as s:
    s.write(key)
