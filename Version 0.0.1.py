"""
Game (Name TBD)
By: Brandon Cunningham
Version 0.0.1
This is just supposed to preform the simple calculations necessary for the final program.
This is going to be the backbone of the final program, but contains no graphics.
Start Date: 10/1/2018
Finish Date: 10/1/2018
"""


def calculate(row, col, board):
    if board[row][col]==0:
        num=board[row-1][col]
        num+=board[row+1][col]
        num += board[row][col+1]
        num += board[row][col-1]
    """This code is for implementing the ability to 'X' out an opponents tile in future versions"""
    #elif board[row][col]==None:
    #else:
        #num=-1*board[row][col]
    if num==0:
        num=1
    board[row][col]=num
    return board

def inputs():
    """Temporary input method, will later change to graphics and mouse clicking"""
    while True:
        row=int(input("Enter row number between 1 and 6: "))
        col=int(input("Enter column number between 1 and 6: "))
        if row<7 and row>0 and col>0 and col<7:
            break
    return row, col


def initialize_board():
    """future ability to choose whatever board size you want"""
    #width=int(input"Enter playable board width, between 2 and 15: ")
    #height=int(input"Enter playable board height, between 2 and 15: ")
    #w, h = width+2, height+2
    w, h = 7, 7
    board = [[0 for x in range(w)] for y in range(h)]
    for x in range(w):
        board[x][0] = 1
        board[x][h-1] = 1
        board[0][x] = 1
        board[w-1][x] = 1
    spots=(w-1)*(h-1)
    return board, spots


def draw_board():
    pass


def get_input():
    pass
    #return row, col


def checker(board):
    for x in range(w-1):
        for y in range(h-1):
            if board[x+1][y+1]==0:
                return True
    return False


def end(P1score, P2score):
    Print("Game over\nPlayer 1: " + str(P1score) + "\nPlayer 2: " + str(P2score))
    if P1score > P2score:
        print("Player 1 wins")
    elif P1score < P2score:
        print("Player 2 wins")
    else:
        print("It's a Tie")


def main():
    turn=0
    P1score = 0
    P2score = 0
    (board, spots)=initialize_board()
    check=True
    while check:
        (row, col)=inputs()
        board=calculate(row, col, board)
        if turn%2==0:
            P1score+=board[row][col]
        else:
            P2score+=board[row][col]
        turn+=1
        if turn%2==0:
            print("Player 1: " + str(P1score)+"\nPlayer 2: "+str(P2score))
        if turn>=spots:
            check=checker(board)
    end(P1score, P2score)


main()
exit()