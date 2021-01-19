# Range of acceptable inputs
board = [' ' for x in range(10)]


# function for Entering letter and matching them to positions
def insert_letter(letter, pos):
    board[pos] = letter


def free_space(pos):
    return board[pos]


def full_board(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def win_conditions(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


# function for Printing out the board on CMD
def print_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')


# function for making moves on the board
def player_moves():
    play = True
    while play:
        move = input("Enter a number from 1 to 9 to  play")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    play = False
                    insert_letter('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 and 9")
        except:
            print("Please type a number")


# function for computer moves
def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if win_conditions(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


# function for random selection for computer
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


# main game function
def main_game():
    print("Welcome to TIC TAC TOE board game")
    print_board(board)
    while not (full_board(board)):
        if not (win_conditions(board, 'O')):
            player_moves()
            print_board(board)
        else:
            print("Sorry, You Lost!")

            break
        if not (win_conditions(board, 'X')):
            move = computerMove()
            if move == 0:
                print("Tie game")
            else:
                insert_letter('O', move)
                print("Computer has played on ", move)
                print_board(board)
        else:
            print("You Win!!")
            break

    if full_board(board):
        print("The game is a tie")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main_game()
    else:
        break