print("Welcome to tic tac toe!")


def play():
    user1 = 0
    while not 0 < int(user1) < 10:
        user1 = int(input("Type a number between 1 and 9: "))
    if board[user1 - 1] == '-':
        board[user1 - 1] = playerSign
        switchPlayer()
        checkWin(board)
    else:
        print("Spot is taken, try again")
    boardPrint(board)

    user2 = 0
    while not 0 < int(user2) < 10:
        user2 = int(input("Type a number between 1 and 9: "))
    if board[user2 - 1] == '-':
        board[user2 - 1] = playerSign
        switchPlayer()
        checkWin(board)
    else:
        print("Spot is taken, try again")
    boardPrint(board)


def exit_game():
    global board, isRunning
    ext = input('Type exit if you want to quit playing, or play if you want to play again: ')
    if ext == 'exit':
        exit()
    elif ext == 'play':
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
        isRunning = True
        return play()
    else:
        exit()


winner = None
isRunning = True
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
playerSign = 'X'


def boardPrint(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_____")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_____")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print('\n')


def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True


def checkWin(board):
    global isRunning
    if checkRow(board):
        boardPrint(board)
        print(f"the winner is {winner}")
        return exit_game()

    elif checkColumn(board):
        boardPrint(board)
        print(f"the winner is {winner}")
        return exit_game()

    elif checkDiagonal(board):
        boardPrint(board)
        print(f"the winner is {winner}")
        return exit_game()

    elif '-' not in board:
        boardPrint(board)
        print('The game is a tie')
        return exit_game()


def switchPlayer():
    global playerSign
    if playerSign == 'X':
        playerSign = 'O'
    else:
        playerSign = 'X'


while isRunning:
    play()
exit_game()
