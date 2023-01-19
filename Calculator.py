from art import logo
from replit import clear

operators = ["+", "-", "*","/"]
numbers = [0,1,2,3,4,5,6,7,8,9]
print(logo)
a = float(input("Whats the first number? "))
b = 0
# for char in operators:
#   print(char)
again = True

def add(a, b):
  """Prints the sum of two numbers"""
  n = a
  a = n + b
  print(f"{n} + {b} = {a}")
  return a

def subtract(a, b):
  """Prints the minus of two numbers"""
  n = a
  a = n - b
  print(f"{n} - {b} = {a}")
  return a

def multiply(a, b):
  """Prints the product of two numbers"""
  n = a
  a = n * b
  print(f"{n} * {b} = {a}")
  return a

def divide(a, b):
  """Prints the division of two numbers"""
  n = a
  a = n / b
  print(f"{n} / {b} = {a}")
  return a

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
  
while again:
  for char in operators:
    print(char)
  op = input("Pick an operator ")
  if op not in operators:
    print("Ïnvalid Operator")
  else:
    b = float(input("Whats the next number? "))
    if op == operators[0]:
      a = operations[operators[0]](a,b)
    if op == operators[1]:
      a = operations[operators[1]](a, b)
    if op == operators[2]:
      a = operations[operators[2]](a, b)
    if op == operators[3]:
      a = operations[operators[3]](a, b)
      
  if input("Would you like to carry on ") == "n":
    clear()
    again = False