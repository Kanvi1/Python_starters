from cryptography.fernet import Fernet


# def write_key():
#     key  = Fernet.generate_key();
#     with open('key.key','wb') as f:
#         f.write(key)

# write_key()

def load_key():
    with open('key.key','rb') as f:
        return f.read()

key = load_key()
fer = Fernet(key)
master_pwd = input("What is the master password? ")

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