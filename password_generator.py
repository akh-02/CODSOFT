# importing the random and string modules
import string
import random
 
# storing all characters in lists 
lw_case = list(string.ascii_lowercase)
up_case = list(string.ascii_uppercase)
digit = list(string.digits)
special_char = list(string.punctuation)
characters = lw_case + up_case + digit + special_char


# \u0332 is used to underline the contents that precedes it
print()
print("\u0332".join("Hello! This is password generator!"))
print()

# taking user input for the number of characters
length = int(input("Please enter the length of the password: "))
password=""
for i in range (0,length):
    password+="".join(random.choice(characters))
print("The desired password is ",password)