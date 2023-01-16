import hangman_art as ha
import hangman_words as hw
import random as rd
from replit import clear

empty_list = []
lives = 6
print(ha.logo)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = rd.choice(hw.word_list)

for char in range(0, len(chosen_word)):
  empty_list.append('-')
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while '-' in empty_list and lives > 0:
  guess = input('Guess a letter: ').lower()
  clear()
 #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  for char in range(0,len(chosen_word)):
    if guess == chosen_word[char]:
      empty_list[char] = guess
  print(empty_list)
  if  guess not in empty_list:
    lives -= 1
    print(f'You guessed {guess}, which is not in the word. You lose a life')
  print(ha.stages[lives])

if lives == 0:
  print('You Lose')
else:
  print('You win')