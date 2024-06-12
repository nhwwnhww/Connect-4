# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name:
# Student Number: 47981739

# ----------------

# Write your classes and functions here

def num_hours() -> float :
   """
   return how much time spend on this assignment
   """
   return 15.3

def generate_initial_board() -> list[str]:
   """
   Generate an inital empty game board

   Return: A empty game board 
   ['--------', 
    '--------',
    '--------', 
    '--------', 
    '--------', 
    '--------',
    '--------', 
    '--------']
   """
   list = ['--------', '--------', '--------', '--------', '--------', '--------',
'--------', '--------']
   return list

def is_column_full(column: str) -> bool:
   """
   Check if a column on the game board is full

   Parameters:
   column(str): a string representing a column on the game board

   Returns:
   bool: True if the column is full, False otherwise
   
   """
   if BLANK_PIECE in column:
       return False
   return True

def is_column_empty(column: str) -> bool:
   """
   Check if a column on the game board is empty

   Parameters:
   column(str): a string representing a column on the game board

   Returns:
   bool: True if the column is empty, False otherwise
   
   """
   for x in column:
       if (x == PLAYER_1_PIECE or x ==PLAYER_2_PIECE):
           return False
   return True

def display_board(board: list[str]) -> None:
   """
   Display the game board

   Parameters:
   board(list[str]): a list representing the game board

   Returns -> None

   
   """
   temp_str = ""
   bottom_line = " "
   for c in range(BOARD_SIZE):
       bottom_line = bottom_line + str(c+1) + " "
       temp_str += COLUMN_SEPARATOR
       for r in board:
           temp_str += r[c] + COLUMN_SEPARATOR
       temp_str += "\n"
   temp_str += bottom_line
   print (temp_str)
   pass


def check_input(command: str) -> bool:
   """
   Check if the input command is valid

   Parameters:
   command(str): The input command to be checked

   Returns:
   bool: True if the input command is valid, False otherwise

   """
   # check empty
   if (command == ''):
       print(INVALID_FORMAT_MESSAGE)
       return False
   #check command length
   if len(command) > 2:
       print(INVALID_FORMAT_MESSAGE)
       return False

   F_char = command[0]
   # use check list to check the command (for fisrt char)
   if not (F_char in "aArRhHqQ"):
       print(INVALID_FORMAT_MESSAGE)
       return False
   # check for invalid command like 'a','r'
   elif (len(command)==1):
       if (F_char in "hHqQ"):
           return True
       else:
            print(INVALID_FORMAT_MESSAGE)
            return False
   # check the second char if the command has a length of 2
   elif (len(command)==2):
       # check the command to aviod some command like 'h1','q3'
       if (F_char in "hHqQ"):
            print(INVALID_FORMAT_MESSAGE)
            return False
       else:
            S_char = command[1]
            # check for the number
            if not(1 <= int(S_char) <= BOARD_SIZE):
                print(INVALID_COLUMN_MESSAGE)
                return False
   
   return True


def get_action() -> str:
    """
   get a valid action command from user


   Returns:
   str: A valid action command entered by user
   
   """
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        #check function
        if (check_input(command)):
            return command
    

def add_piece(board: list[str], piece: str, column_index: int) -> bool:
   """
   add a new piece to the specified column of the board

   Parameters:
   board (list[str]): The game board
   piece (str): The game piece to be added ('X' or 'O')
   column_index (int): the index of the column where the piece is to be added

   Returns:
   bool: True if the piece is successfully added, False otherwise

   If the column is full, the game will print full column messgae
   
   """
   column = board[column_index]
   if (is_column_full(column)):
       print(FULL_COLUMN_MESSAGE)
       return False
   count = 0
   for i in column:
       count+=1
       if (i == PLAYER_1_PIECE or i == PLAYER_2_PIECE):
           #get the row number for this column to replace the '-'
           count -= 1
           break
   
   # replace '-' to piece
   list_column = list(column)
   list_column[count-1] = piece
   new_column = "".join(list_column)
   
   # update board
   board[column_index] = new_column
   return True

def remove_piece(board: list[str], column_index: int) -> bool:
   """
   remove a piece from the specified column of the board

   Parameters:
   board (list[str]): The game board
   piece (str): The game piece to be removed ('X' or 'O')
   column_index (int): the index of the column where the bottem piece is to be removed

   Returns:
   bool: True if the piece is successfully removed, False otherwise

   If the column is removed, the game will print empty column messgae
   
   """
#    get the target column
   column = board[column_index]
#    check if empty
   if is_column_empty(column):
       print(EMPTY_COLUMN_MESSAGE)
       return False
#    compare whether X or O is the first char
   new_column = ''.join((BLANK_PIECE,column))
    #    update board
   board[column_index] = new_column[:-1]
   return True

def check_win(board: list[str]) -> Optional[str]:
    """
   Check if a player has won the game by getting four pieces in a row (horizontally, vertically, or diagonally).

   Parameters:
   board (list[str]): the game board

   Returns:
   Optional[str]: the winning player's piece (if a win is detected, None otherwise)
   """

    result = None

    # Check horizontal lines
    for row in board:
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] and row[i] != BLANK_PIECE:
                if (result == None):
                    result = row[i]
                elif (result != row[i]):
                    return BLANK_PIECE
    
    # Check vertical lines
    for col in range(len(board[0])):
        for i in range(len(board) - 3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] and board[i][col] != BLANK_PIECE:
                if (result == None):
                    result = board[i][col]
                elif (result != board[i][col]):
                    return BLANK_PIECE
    
    # Check diagonal lines (top-left to bottom-right)
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != BLANK_PIECE:
                if (result == None):
                    result = board[i][j]
                elif (result != board[i][j]):
                    return BLANK_PIECE
    
    # Check diagonal lines (bottom-left to top-right)
    for i in range(3, len(board)):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] and board[i][j] != BLANK_PIECE:
                if (result == None):
                    result = board[i][j]
                elif (result != board[i][j]):
                    return BLANK_PIECE
    return result

def play_game() -> None:
   """
    generate the initial game board

   The main game loop, 
   include player moves, 
   display te game board, 
   check for wins or draw, 
   and provide help and quit option

   Return -> None
   
   """
   #display the initial board
   board = generate_initial_board()
   current_player = PLAYER_1_PIECE
   display_board(board)
   print(PLAYER_1_MOVE_MESSAGE)
   while True:
        
        action = get_action()

        # help command
        if (action[0] in 'hH'):
            print(HELP_MESSAGE)
            display_board(board)
            if (current_player == PLAYER_1_PIECE):
                print(PLAYER_1_MOVE_MESSAGE)
            else:
                print(PLAYER_2_MOVE_MESSAGE)
            continue

        # quit game command
        if (action[0] in 'qQ'):
            break

        if (action[0] in 'aA'):
            if not(add_piece(board,current_player,int(action[1])-1)):
                continue
            display_board(board)
        elif (action[0] in 'rR'):
            if not(remove_piece(board,int(action[1])-1)):
                continue
            display_board(board)

        # swap player and print out move message
        if check_win(board) == None:
            if (current_player == PLAYER_1_PIECE):
                current_player = PLAYER_2_PIECE
            else:
                current_player = PLAYER_1_PIECE

            if (current_player == PLAYER_1_PIECE):
                print(PLAYER_1_MOVE_MESSAGE)
            else:
                print(PLAYER_2_MOVE_MESSAGE)
            continue

        
        # check win
        if (check_win(board) == BLANK_PIECE):
            print(DRAW_MESSAGE)
        elif (check_win(board)==PLAYER_1_PIECE):
            print(PLAYER_1_VICTORY_MESSAGE)
        elif (check_win(board)==PLAYER_2_PIECE):
            print(PLAYER_2_VICTORY_MESSAGE)
        break
   pass

def main() -> None:
   """
   The main function
   
   start the game and allow player to replay a new game
   """
   while True:
       play_game()
       replay = input(CONTINUE_MESSAGE)
       # check if player want to replay the game
       if (replay == "y"):
           continue
       else:
           break

if __name__ == "__main__":
   main()
