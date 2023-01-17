from replit import clear
from artSA import logo
#HINT: You can call clear() to clear the output in the console.
again = True
dict = {}
highest_bidder = ""
highest_bid = 0
print(logo)
print("Werlcome to the secret auction program")

while again:
  name = str(input("What is your name? "))
  bid = int(input("What is your bid? $"))
  yn_bool = str(input("Are there any other bidders? Type 'yes' or 'no'"))
  clear()
  if yn_bool == "no":
    again = False
  dict[name] = bid

for key in dict:
  if dict[key] > highest_bid:
    highest_bid = dict[key]
    highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")