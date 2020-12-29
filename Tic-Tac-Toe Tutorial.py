#Each comment explains before the code
#Board display
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

#Spaces/seperator in between moves
def display_board():
    print('            Play Positions')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '     1 | 2 | 3')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '     4 | 5 | 6')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '     7 | 8 | 9')
#Misc
game_still_going = True
winner = None
current_player = 'X'

#Tic-Tac-toe game play order flow(order of operations)
def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == 'X' or winner =='O':
        print(winner + ' won!')
    elif winner == None:
        print('Tie!')

#Turn basex2d placement code
def handle_turn(player):

    print(player +'\'s turn!')
    position = input('Choose a position from 1 through 9: ')
    valid = False
    while not valid:
        #Sets what input is allowed // while loop prevents from continuing unless given righ input
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Invalid input. Choose a position from 1 through 9: ')
        #Subtracted 1 from position to make it easier for user to play since 0=1 for player
        position = int(position) - 1
        #This prevents from overwriting a spot that's already taken
        if board[position] == "_":
            valid = True
        else:
            print('You can\'t go there. Go again!')
    board[position] = player
    display_board()

#Checks if game still in play
def check_if_game_over():
    check_for_winner()
    check_for_tie()

#Checks if player Won
def check_for_winner():
    #Adding global links it together
    global winner
    row_winner = check_rows()
    coloumn_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


#Checks if any blank space in the game
def check_rows():
    #Adding global links it together
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    #Adding global links it together
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != '_'
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #Adding global links it together
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != '_'
    diagonal_2 = board[6] == board[4] == board[2] != '_'
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

#Checks if player tie
def check_for_tie():
    #Adding global links it together
    global game_still_going
    if '_' not in board:
        game_still_going = False
    return

#Changes turn to other player
def flip_player():
    #Adding global links it together
    global current_player
#Changes from X to O per turn
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()
