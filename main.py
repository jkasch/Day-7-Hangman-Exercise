from replit import clear

import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

#Create blanks
display = []
guess_list = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()  
    if guess in guess_list:
      print(guess + " was alreaedy guessed. Guess again.")
      continue
    else:
      guess_list.append(guess)
      print(guess_list)
    clear()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(guess + " is not in the word.")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The solution is {chosen_word}.")

    print(f"{' '.join(display)}")
  
    if "_" not in display:
        end_of_game = True
        print("You win! Great job!")

    print(stages[lives])