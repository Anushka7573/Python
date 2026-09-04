import random
import string

password = {}

# load existing passwords from file

try:
    with open('passwords.txt', 'r') as file:
        for line in file:
            website, pwd = line.strip().split(':') # strip removes whitespace and newline characters & split separates the website and password by the colon
            password[website] = pwd
except:
    pass

def generate_password(length=12):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + "-+&*^%$#@!"
    password = "".join(random.choice(characters) for i in range(length))
    return password

while True:
        print("------Password Manager App------")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. View Passwords")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            site = input("Enter website name: ")
            pwd = input("Enter password :")
            password[site] = pwd

            with open('passwords.txt', 'a') as file:
                file.write(f"{site}:{pwd}\n")

                print("Password saved successfully!")


        elif choice == 2:
            if not password:
                print("No passwords found!")
            else:
                for site, pwd in password.items():
                    print(site, ":", pwd)

        elif choice == 3:
            print ("Generating a random password...", generate_password())                    

        elif choice == 4:
            print("Ok Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")