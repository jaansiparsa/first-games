import os

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_board(board):

  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print('----------')
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print('----------')
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Takes in an index where player wants to place piece 
# Returns True if valid index. Returns False if invalid index 

def validate(player_index):
  if index not in range(0,9):
    return False
  elif board[player_index] != ' ':
    return False 
  else:
    return True 

def update_board(index,turn):
  if turn % 2 == 0:
    board[index] = "X"
  else:
    board[index] = "O"

def is_game_over():
  if (board[0] == board[1] == board[2]) and board[0] != " ":
    return True
  elif (board[3] == board[4] == board[5]) and board[3] != " ":
    return True
  elif (board[6] == board[7] == board[8]) and board[7]!= " ":
    return True
  elif (board[0] == board[3] == board[6]) and board[3]!= " ":
    return True
  elif (board[1] == board[4] == board[7]) and board[1]!= " ":
    return True
  elif (board[2] == board[5] == board[8]) and board[2]!= " ":
    return True
  elif (board[0] == board[4] == board[8]) and board[0]!= " ":
    return True
  elif (board[2] == board[4] == board[6]) and board[2]!= " ":
    return True
  else:
    return False

def print_game_over_message(turn):
  if turn == 9:
    print("It is a tie. Good job")
  elif turn % 2 == 0:
    print("Player 1 wins!")
  else:
    print("Player 2 wins!")

turn = 0
while turn < 9:

  # print the current board 
  print_board(board)

  # Ask the player for a spot or index to place their piece 
  index = int(input("Where do you want to place your piece?\n"))

  # Validate the input 
  # reasons for invalid input 
    # any number that isn't 0 through 8 
    # if the spot is already occupied
  while validate(index) == False:
    index = int(input("You can't go there, try again >:( \n"))
   
  # Update the board 
  update_board(index, turn)

  if is_game_over():
    break
  
  turn = turn + 1
  
print_game_over_message(turn)
