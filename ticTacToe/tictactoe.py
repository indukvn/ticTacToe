#displays game board
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

game_still_on = True
current_player = "X"
winner = None


def play_game():

    display_game_board()
    while game_still_on:

        #check for current_player input
        handle(current_player)

        #check if game is over or not
        check_if_game_on()

        #shifting the turn to next player
        flip_player()

    #checking for winner
    if winner == 'X' or winner == 'O':
        print(f"Congratulations + {winner} + has wont the game!")
    elif winner == None:
        print("It's a draw!")


#to display the game_board
def display_game_board():
    print('\n')
    print(game_board[0] + ' | ' + game_board[1] + ' | ' + game_board[2] + "    1 | 2 | 3")
    print('---------')
    print(game_board[3] + ' | ' + game_board[4] + ' | ' + game_board[5] + "    4 | 5 | 6")
    print('---------')
    print(game_board[6] + ' | ' + game_board[7] + ' | ' + game_board[8] + "    7 | 8 | 9")
    print('\n')


#to handle the player
def handle(player):
    print(player + "'s turn.")

    spot = input("Choose a value from 1-9: ")

    valid = False
    while not valid:

        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("Hey, enter a value from range 1-9: ")
        spot = int(spot) - 1

        if game_board[spot] == '-':
            valid = True
        else:
            print("Oops! Entered invalid spot.")

    game_board[spot] = player
    display_game_board()


def check_if_game_on():
    check_winner()
    check_tie()


#check for winner
def check_winner():
    global winner

    row_winner = check_rows()
    col_winner = check_cols()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


#matched row wise
def check_rows():
    global game_still_on

    row1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row1 or row2 or row3:
        game_still_on = False
    elif row1:
        return game_board[0]
    elif row2:
        return game_board[3]
    elif row3:
        return game_board[6]
    else:
        return None


#matched column wise
def check_cols():
    global game_still_on

    col1 = game_board[0] == game_board[3] == game_board[6] != "-"
    col2 = game_board[1] == game_board[4] == game_board[7] != "-"
    col3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if col1 or col2 or col3:
        game_still_on = False
    elif col1:
        return game_board[0]
    elif col2:
        return game_board[1]
    elif col3:
        return game_board[2]
    else:
        return None


#matched diagonally
def check_diagonal():
    global game_still_on

    diag1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diag2 = game_board[2] == game_board[4] == game_board[6] != "-"

    if diag1 or diag2:
        game_still_on = False
    elif diag1:
        return game_board[0]
    elif diag2:
        return game_board[2]
    else:
        return None


#check for tie
def check_tie():
    global game_still_on

    if '-' not in game_board:
        game_still_on = False
        return True
    else:
        return False


#shift player
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


#start game
play_game()
