import random
import string
import sys
import pyperclip

my_pass = []

print("!-------Random Password Generator-------!")
pass_length = int(input("Enter Passwrd Length: "))

if pass_length < 8 or pass_length > 20:
    print("Do Your Password Minimum Length 8 or Maximum 20")
    sys.exit()
else:
    pass_list = string.ascii_letters + string.digits + string.punctuation
    for a in range(pass_length):
        my_pass.append(random.choice(pass_list))


    string_pass = "".join(my_pass)
    print(f"Generated Password : {string_pass}")

    choice_copy = input(f"Do You Want To Copy Your Password? {string_pass}:    ")
    if choice_copy.lower() == "yes":
        pyperclip.copy(string_pass)
        print("Your Password Has Been Copied!")

