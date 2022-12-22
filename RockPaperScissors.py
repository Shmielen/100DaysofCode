# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors"))
randchoice = random.randint(0,2)
choices = [rock, paper, scissors]

print(f"You chose {choices[choice]}")
print(f"The computer chose {choices[randchoice]}")

if choice == 0:
    if randchoice == 0:
        print("You Draw")
    elif randchoice == 1:
        print("You Lose")
    else:
        print("You Win")
elif choice == 1:
    if randchoice == 0:
        print("You Win")
    elif randchoice == 1:
        print("You Draw")
    else:
        print("You Lose")
else:
    if randchoice == 0:
        print("You Lose")
    elif randchoice == 1:
        print("You Win")
    else:
        print("You Draw")


