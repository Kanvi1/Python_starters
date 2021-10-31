import os, base64
from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# def write_key():
#     key  = os.urandom(16)
#     with open('key.key','wb') as f:
#         f.write(key)

# write_key()

def load_key():
    with open('key.key','rb') as f:
        return f.read()


# Get master password
master_pwd = input("What is the master password? ")

# Generate key from master password
salt = load_key()
kdf = PBKDF2HMAC(hashes.SHA256,length=32,salt=salt,iterations=100000)
key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
fer = Fernet(key)

def view():
    with open('paswords.txt','r') as f:
        for line in f.readlines():
            user, pwd = line.rstrip().split("|")
            print("User: " + user + " , Password: " + fer.decrypt(pwd.encode()).decode())

def add():
    user = input("Username: ")
    pwd = input("Password: ")
    with open('paswords.txt','a') as f:
        f.write(user + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    choice = input("Add a password or view? (a/v/q:quit): ")

    if(choice =='a'):
        add();
    elif choice == 'v':
        view()
    elif choice == 'q':
        quit()
    else:
        print("Invalid choice! Please choose again.")