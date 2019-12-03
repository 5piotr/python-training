import os

board = {1:' ',2:' ',3:' ',
         4:' ',5:' ',6:' ',
         7:' ',8:' ',9:' '}

def printBoard(board):
    os.system('cls')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |   ')

def printRules():
    os.system('cls')
    print('   |   |   ')
    print(' 7 | 8 | 9')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' 4 | 5 | 6')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' 1 | 2 | 3')
    print('   |   |   ')

def checkBoard(board,turn):
    if(board[1]==board[2]==board[3]==turn or
       board[4]==board[5]==board[6]==turn or
       board[7]==board[8]==board[9]==turn or
       board[1]==board[4]==board[7]==turn or
       board[2]==board[5]==board[8]==turn or
       board[3]==board[6]==board[9]==turn or
       board[1]==board[5]==board[9]==turn or
       board[3]==board[5]==board[7]==turn):
        return 1
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and
         board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and
         board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        return 0
    else:
        return -1

def clearBoard(board):
    board[1] = ' '
    board[2] = ' '
    board[3] = ' '
    board[4] = ' '
    board[5] = ' '
    board[6] = ' '
    board[7] = ' '
    board[8] = ' '
    board[9] = ' '
    

play = True
printRules()
print('Witamy w grze kółko i krzyżyk')
print('Rozpoczyna gracz z symbolem "X"')
turn = 'X'

while play:
    while True:
        try:
            position = int(input('gdzie postawić ' + turn + '? '))
            if position in range(1,10) and board[position] == ' ':
                break
            else:
                print('to miejsce jest zajęte')
        except:
            print('podaj właściwą wartość')
    board[position] = turn
    printBoard(board)

    check = checkBoard(board,turn)
    if(check == 1):
        print('Wygrywa gracz z symbolem ' + turn + ' !!!')
    if(check == 0):
        print('Remis !!!')
    if(check == 1 or check == 0):
        while True:
            question = input('Czy chcecie zagrać jeszcze raz? (y/n) ')
            if (question == 'y' or question == 'n'):
                break
            else:
                print('Jeżeli tak wpisz "y", jeżeli nie wpisz "n"')
        if question == 'n':
            play = False
        elif question == 'y':
            printRules()
            clearBoard(board)
            turn = 'X'
    if(check == -1):
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    
input('press enter to continue...')
