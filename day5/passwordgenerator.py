#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#password = ""
#for letter in range(0,nr_letters):
  ##below is incredibily prone to mistake as you need to figured out the end range vs random.choice is just that
#  password += letters[random.randint(0,51)].append
#for symbol in range(0,nr_symbols):
#  password += random.choice(symbols)
#for number in range(0,nr_numbers):
#  password += random.choice(password)
#print(password)
password_list = []
#look like you dont have to use different variable like letter, symbol, but can use the same one. 
for letter in range(0,nr_letters):
  password_list.append(random.choice(letters))
for symbol in range(0,nr_symbols):
  password_list += random.choice(symbols)
for number in range (0,nr_numbers):
  password_list.append(random.choice(numbers))
#print(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your password is: {password}")
