import numpy as np

def create_board():
    return np.zeros((5, 5))
    1
def print_board(board):
    print(board)


def piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, row, col):
    if board[row][col] == 0 :
        return True


def check_winner(board, piece):
    count =0
    for a in range(5):
        for b in range(5):
            if (board[a][b] == piece):
                count=count+1
        if count>=4 :
            return True       

    
    for c in range(5):
        for r in range(5):
            if (board[r][c] == piece):
                count=count+1
        if count>=4 :
            return True  


    for r in range(2):
        for c in range(2):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
            if all(board[r+3-i][c+i] == piece for i in range(4)):
                return True

    return False

board = create_board()

game_over = True
turn = 2
while  game_over:

    print_board(board)

    player = turn % 2 + 1
    print("Player",player)

    row = int(input("Enter row : "))
    col = int(input("Enter column : "))

    if is_valid_location(board, row, col)==True:
        piece(board, row, col, player)

        if check_winner(board, player):
            print("Player ",player, "win!")
            game_over = False

        turn += 1
    else:
        print("try again\n")