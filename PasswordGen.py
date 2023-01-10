# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random as rd

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numlet = int(input("How many latters would you like in your password?\n"))
numsym = int(input("How many symbols would you like in yoour password?\n"))
numnum = int(input("How many numbers would you like in your password?\n"))
password_list = []
password = ''

for char in range(1, numlet+1):
    password_list.append(rd.choice(letters))
for char in range(1, numsym+1):
    password_list.append(rd.choice(symbols))
for char in range(1, numnum+1):
    password_list.append(rd.choice(numbers))
    
rd.shuffle(password_list)

for char in password_list:
    password += char

print(f'Here is your password: {password}')
