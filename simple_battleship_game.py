# Import randint
from random import randint

# Make the board
board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print("LET'S PLAY BATTLESHIP!")
print()
print_board(board)
print()
print("Each O on this 5x5 grid represents one spot in the ocean.")
print("I have hidden my battleship in one of these spots.")
print("Let's see if you can sink it by guessing exactly where it is hidden in four attempts!")
print("You have a 16% chance of winning, so good luck!")
print()

# Picks where the battleship is located
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print("Guess which row and column I have hidden it in. The rows are numbered from 1-5 going down, while the columns are numbered going from left to right.")
print()

# For loop
# Prints which turn player is on
# Asks player to input their guess
for turn in range(4):
  print('Turn', turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

# Checks input and gives response
  if (guess_row - 1) == ship_row and (guess_col - 1) == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row - 1][guess_col - 1] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row - 1][guess_col - 1] = "X"
    if turn == 3:
      print('GAME OVER')
      print('The answer was ' + str(ship_row + 1) + ', ' + str(ship_col + 1))
      board[ship_row][ship_col] = '!'
  
  # Prints new board for player
    print_board(board)