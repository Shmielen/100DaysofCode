#Number Guessing Game Objectives:
from NGart import logo
import random as rd
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


number = rd.randint(1, 100)
easy = 10
hard = 5
guess = 0

print(logo)
print("Welcome to the number Guessing Game!\n")
print("Im thinking of a number between 1 and 100")

tries = input("Choose a difficuly. Type easy or hard: ")

if tries == "easy":
  tries = easy
else:
  tries = hard

while guess != number and tries > 0:
  print(f"You have {tries} attaempts remainging to guess the number")

  tries -= 1
  guess = int(input("Make a guess: "))

  if guess == number:
    print("You win")
    break
  else:
    if guess > number:
      print("Too High")
    else:
      print("Too low")

if tries == 0:
  print("You have run out of attempts")