# ----------------Gloable Variables---------------------

# Game board
board = [
  "-","-","-",
  "-","-","-",
  "-","-","-",]

# Decor Wrap
def decor(func):
    def wrap():
        print("=======================================================")
        func()
        print("=======================================================")
    return wrap

@decor
def text_wrap():
    print("Hello world!")

# Text_wrap();

# If game is still going
game_still_going = True

# Who Won? Or Tie?
winner = None

# Whos turn is it
current_player = "X"

# Display Board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play game of Tic Tac Toe
def play_game():

  # Didplay initial board
  display_board()

  # While the game is still going
  while game_still_going:

    # Handle a single turn of an arbitaty player
    handle_turn(current_player)

    # Check if the game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # The game has ended
  if winner =="X" or winner == "O":
    print()
    print(winner + " WON.")
    print()
  elif winner == None:
    print()
    print("Tie.")
    print()

# Handle a single turn of an arbitrary player
def handle_turn(player):
  print()
  print(player + "'s turn.")
  print()
  position = input("Choose a position from 1-9: ")
  print()

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
      print()

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You cant go there. Go again!")
      print()

  board[position] = player

  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():

  # Setup global Variables
  global winner

  # Check rows
  row_winner = check_rows()
  # Check columns
  column_winner = check_columns()
  # Check diagonals
  diagonal_winner = check_diagonals()

  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

def check_rows():
  # Setup global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return to winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
 # Setup global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any columns does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return to winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  # Setup global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"
  # If any diagonals does have a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
  # Return to winner (X or O)
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return

def check_if_tie():
  # Check if a tie game
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  # Global variables we next
  global current_player
  # if the current player was x, then change it to O
  if current_player == "X":
    current_player = "O"
    # If the current player was O, Then change it to X
  elif current_player == "O":
    current_player = "X"
  return

def yes_or_no():
    # Continue Game
    YesNo = input("Yes or No?")
    YesNo = YesNo.lower()
    if(YesNo == "yes"):
        return 1
    elif(YesNo == "no"):
        return 0
    else:
        return yes_or_no()

play_game()

# Thanks for playimg
