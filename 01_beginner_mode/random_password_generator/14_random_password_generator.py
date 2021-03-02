#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get the password requirements
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_pwd = "" 
for i in range(0, nr_letters):
  letters_pwd += letters[random.randint(0, len(letters)-1)]

numbers_pwd = ""
for i in range(0, nr_numbers):
  numbers_pwd += numbers[random.randint(0, len(numbers)-1)]

symbols_pwd = ""
for i in range(0, nr_symbols):
  symbols_pwd += symbols[random.randint(0, len(symbols)-1)]

password1 = letters_pwd+numbers_pwd+symbols_pwd
print("Your password is: " + password1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password2 = list(password1)
random.shuffle(password2)
password2 = ''.join(password2)
print("Random password is: " + password2)
