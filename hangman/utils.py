import os

# 0. Clearing the console between guesses
def clear():
  os.system("clear")


# 1. Validating user input
def validate_input(letter, guessed_letters):

  """
  Ensures user provides a valid letter guess. True if valid and false if invalid. 

  letter: String 
  guessed_letters: list (of Strings)

  returns: Boolean 
  """

  valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  return letter not in guessed_letters and letter in valid_letters


# 3. Checking if the guessed letter is in the target word
def find_all_occurrences(letter, target_word):
  indices = []
  i = 0
  letter = letter.lower()
  while i !=-1:
    # find the letter in the target word, searching from index i onward.
    i = target_word.lower().find(letter, i)
    if i != -1:
      indices.append(i)
      i+=1
  return indices

# 4. Showing the state of the game to the user (display_word)
def update_display_word(letter, occurrences, display_word):
  new_word = display_word
  for index in occurrences:
    new_word = new_word[:index] + letter + new_word[index+1:]
  return new_word

def print_hangman(strikes_remaining):
  if strikes_remaining >= 6:
    print(
      """
       ----.
      |   
      |
      |
      |
      -----
      """
    )
  elif strikes_remaining == 5:
    print(
      """
       ----.
      |    O
      |
      |
      |
      -----
      """
    )
  elif strikes_remaining == 4:
    print(
      """
       ----.
      |    O
      |    |
      |
      |
      -----
      """
    )
  elif strikes_remaining == 3:
    print(
      """
       ----.
      |    O
      |    |
      |   / 
      |
      -----
      """
    )
  elif strikes_remaining == 2:
    print(
      """
       ----.
      |    O
      |    |
      |   / \\
      |
      -----
      """
    )
  elif strikes_remaining == 1:
    print(
      """
       ----.
      |    O
      |   -|
      |   / \\
      |
      -----
      """
    )
  elif strikes_remaining == 0:
    print(
      """
       ----.
      |    O
      |   -|-
      |   / \\
      |
      -----
      """
    )

# 5. Updating the screen at the end of the turn
def update_screen(strikes_remaining, display_word, guessed_letters):
  # Print the hangman 
  print_hangman(strikes_remaining)

  # Print the display word 
  print(display_word)
  
  # Let user know how many strikes they have left 
  print("You have " + str(strikes_remaining) + " strikes remaining.\n")
  # Print the letters they have already guessed 

  print("You have guessed " + str(guessed_letters) + ".")