import random

from hangman.utils import (
  clear,
  validate_input, 
  find_all_occurrences, 
  update_display_word, 
  update_screen,
  print_hangman
  )

""" 
 TODO: Create Constants 
  * word to guess 
  * strikes allowed
"""

#1. Create a list of words, then randomly choose a word to be the target word, store it to a constant called TARGET_WORD 

#2. Create a constant called STRIKES 

target_words = ['xylophone', 'python', 'giraffe', 'passionfruit', 'architect', 'snickerdoodle', 'airplane', 'desktop' 'rainbow', 'hamburger', 'cookie', 'boutique', 'dictionary', 'suitcase']

RANDOM_WORD = random.choice(target_words)

STRIKES = 5

def play_game():

  """
    TODO: Create game state variables 
      * strikes_remaining 
      * guessed_letters 
      * display word
  """
  strikes_remaining = STRIKES

  guessed_letters = []

  display_word = "_" * len(RANDOM_WORD)
  """ 
    TODO: Update the while condition of the game loop
  """
  print("The word is " + str(len(RANDOM_WORD)) + " letters long.\n")
  
  while strikes_remaining > 0 and "_" in display_word:
    #update screen

    update_screen(strikes_remaining, display_word, guessed_letters)

    # guess a letter 
    guessed_letter = input("Which letter would you like to guess?\n")

    clear()

    # Check if the input is valid
    """
      TODO: Check if input is valid
    """
    if validate_input(guessed_letter, guessed_letters): # if input is valid 

      """
        TODO: Keep track of guessed letter
      """
      # Add guessed letter to the list of guessed letters
      guessed_letters.append(guessed_letter)
      # Check if the guessed letter is in the target word
      if guessed_letter in RANDOM_WORD:
        # Get the indices of the occurences 
        indices = find_all_occurrences(guessed_letter, RANDOM_WORD)
        # Update the display word to add the guessed letter 
        display_word = update_display_word(guessed_letter, indices, display_word)

      else:
        # Use a strike 
        strikes_remaining = strikes_remaining - 1
        print("Wrong letter. You have " + str(strikes_remaining) + " strikes remaining\n")
    else:
      print('Invalid guess. Try again')
      

  """
    TODO: Print result of the game 
  """
  if "_" not in display_word:
    print("Congrats!!! You won!")
  else:
    print("Boooo!! Try harder next time.")

# Play the game
play_game()