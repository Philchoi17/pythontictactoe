import random


def print_board(board):
    print('\n'*100)
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

test = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# print_board(test)


def player_input():
    
    condition = True
    
    while condition:
        marker = input('Do you want to be X\'s or O\'s? ').upper()
        if marker == 'X':
            
            return ('X', 'O')
        else:
            
            return ('O', 'X')
    
def place_marker(board, marker, position):
    
    board[int(position)] = marker

def win_check(board, mark):
    if board.count(mark) >= 3:
        if board[1] == mark and board[2] == mark and board[3] == mark:
            return True
        elif board[4] == mark and board[5] == mark and board[6] == mark:
            return True
        elif board[7] == mark and board[8] == mark and board[9] == mark:
            return True
        elif board[1] == mark and board[4] == mark and board[7] == mark:
            return True
        elif board[2] == mark and board[5] == mark and board[8] == mark:
            return True
        elif board[3] == mark and board[6] == mark and board[9] == mark:
            return True
        elif board[1] == mark and board[5] == mark and board[9] == mark:
            return True
        elif board[3] == mark and board[5] == mark and board[7] == mark:
            return True
        else:
            print("in here")
            return False

def choose_first():
    
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    
#     if board[position] == ' ':
#         return True
#     else:
#         return False
    
    return board[position] == ' '

def full_board_check(board):
    
    if ' ' in board:
        return False
    else:
        return True

def player_choice(board):
    
    condition = True
    positions = '123456789'
    
    while condition:
        choice = input('what position is your next move?')
        condition = False
        if choice in positions:
            if board[int(choice)] == ' ':
                return choice
        else:
            return False

def replay():
    condition = True
    while condition:
        again_play = input('wanna play again?[Y/N]')
        if again_play.upper() == 'Y' or again_play.upper() == 'F':
            condition = False
            if again_play.upper() == 'Y':
                return True
            elif again_play.upper() == 'N':
                return False

print('Welcome to Tic Tac Toe!')

while True:
    
    #play the game
    the_board = [' ']*10
    
    player1_marker , player2_marker = player_input() 
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play?[Y/N] ').upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        
        if turn == 'Player 1':
            print_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                print_board(the_board)
                print('player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    print_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
            
        
        else:
            
            print_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                print_board(the_board)
                print('player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    print_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
    
    
    
    if not replay():
        break
        

    
    
    
