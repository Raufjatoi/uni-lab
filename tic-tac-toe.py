import sys
import random

board = ['-','-','-','-','-','-','-','-','-']
p1 = ''
p2 = ''

def player_won(s):
    if (   (board[0] == s and board[1] == s and board[2] == s)
        or (board[3] == s and board[4] == s and board[5] == s)
        or (board[6] == s and board[7] == s and board[8] == s)
        or (board[0] == s and board[3] == s and board[6] == s)
        or (board[1] == s and board[4] == s and board[7] == s)
        or (board[2] == s and board[5] == s and board[8] == s)
        or (board[0] == s and board[4] == s and board[8] == s)
        or (board[2] == s and board[4] == s and board[6] == s)):
        return True
    else:
        return False

def draw():
    for item in board:
        if item == '-':
            return False
    return True

def board_display ():
    print('Current board is : ')
    count= 0
    for i in range (len(board)):
        print(board[i], end =' ')
        count +=1
        if count%3 == 0:
            print()

def update(idx,val):
    board[idx]= val

def playgame ():
    print( " Tic tac toe game :: Rauf :: ")
    board_display()
    global p1, p2
    p1 = input('Choose ("O" or "X" ): ')
    if p1 == 'O':
        p2 = 'X'
    elif p1 == 'X':
        p2 = 'O'
    else:
        print('Invalid input choose "O" or "X": ') 
        exit(0)
        
    turn=random.randrange(1,2)
    while not (player_won(p1) or player_won(p2) or draw()):
        if turn == 1:
            move = int(input('Enter your move between 0-8: '))
            update(move,p1)
            board_display()
            turn=2
            if player_won(p1):
                print('Player one has won. Congratulations!')
                break
        if turn == 2:
            move = int(input('Enter your move: 0 to 8: '))
            update(move,p2)
            board_display()
            turn=1
            if player_won(p2):
                print('Congratulations! You won.')
                break

playgame()
