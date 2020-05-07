def get_option():
    print("Welcome to PassGen2.0")
    print("Select an option by entering the numeric value:")
    print("1) Generate a new password")
    print("2) Encrypt a password")
    print("3) Decrypt a password")
    user_inp = input("Enter choice: ")

    return user_inp    

def get_random_password(alpha):
    from random import randint, choices

    password_length = randint(12, 16)
    password = choices(alpha, k=password_length)

    return "".join(password)

def get_encrypted(alpha, plaintext):
    from random import choices

    return "".join(char + "".join(choices(alpha, k=10)) for char in plaintext)

def get_decrypted(encrypted_plaintext):
    return encrypted_plaintext[::11]    

def do_again():
    import sys

    print("Would you like to go back to the main menu?")
    x = input("y/n: ")
    if x == 'y':
        get_option()
    else:
        print("Have a nice day!")
        sys.exit()  

def main():
    import string

    alpha = string.digits + string.ascii_letters + string.punctuation

    password = get_random_password(alpha)
    encrypted = get_encrypted(alpha, password)
    decrypted = get_decrypted(encrypted)

    user_inp = get_option()

    if user_inp == "1" :
        print(f'Password: {password}')
    elif user_inp == "2" :
        print(f'Encrypted: {encrypted}')
    elif user_inp == "3" :    
        print(f'Decrypted: {decrypted}')
    else :
        print("Invalid Input") 

    do_again()


if __name__ == "__main__":
    main()