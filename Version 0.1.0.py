"""
Game (Name TBD)
By: Brandon Cunningham
Version 0.1.0

Start Date: 10/3/2018
Finish Date: 10/11/2018

This version made some minor improvements on the backend compared to the previous version, but the main improvement is
the addition of any sort of graphics.
"""



import turtle as t
#t.speed(0)
t.tracer(0,0)
t.ht()

"""
All numbers must stick within a 20 by 40 rectangle
the starting coordinates for 1 digit number is (40,30) from left hand corner
The starting and ending position of each of these numbers will be the bottom left hand corner of their rectangles
They will all start facing the right side wall and end the same direction
"""
def num1():
    x = t.xcor()
    y = t.ycor()
    t.down()
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(40)
    t.left(135)
    t.forward(14)
    t.up()
    t.goto(x,y)
    t.right(225)


def num2():
    x=t.xcor()
    y=t.ycor()
    t.down()
    t.forward(20)
    t.backward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.up()
    t.left(180)
    t.goto(x,y)


def num3():
    x = t.xcor()
    y = t.ycor()
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.up()
    t.goto(x, y)
    t.left(180)

def num4():
    x = t.xcor()
    y = t.ycor()
    t.up()
    t.forward(17)
    t.left(90)
    t.down()
    t.forward(40)
    t.left(150)
    t.forward(34)
    t.left(120)
    t.forward(20)
    t.up()
    t.goto(x, y)


def num5():
    x = t.xcor()
    y = t.ycor()
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.up()
    t.goto(x, y)


def num6():
    x = t.xcor()
    y = t.ycor()
    t.down()
    for x in range(4):
        t.forward(20)
        t.left(90)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.up()
    t.goto(x, y)


def num7():
    x = t.xcor()
    y = t.ycor()
    t.down()
    t.goto(t.xcor()+20, t.ycor()+40)
    t.backward(20)
    t.up()
    t.goto(x, y)


def num8():
    x = t.xcor()
    y = t.ycor()
    t.down()
    for x in range(4):
        t.forward(20)
        t.left(90)
    t.left(90)
    t.forward(20)
    t.right(90)
    for x in range(4):
        t.forward(20)
        t.left(90)
    t.up()
    t.goto(x, y)


def num9():
    x = t.xcor()
    y = t.ycor()
    t.down()
    t.forward(20)
    t.left(90)
    t.forward(40)
    for z in range(3):
        t.left(90)
        t.forward(20)
    t.up()
    t.goto(x, y)


def plus():
    x = t.xcor()
    y = t.ycor()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.down()
    t.forward(20)
    t.backward(10)
    t.right(90)
    t.backward(10)
    t.forward(20)
    t.up()
    t.goto(x, y)


def num0():
    x = t.xcor()
    y = t.ycor()
    t.down()
    for x in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.up()
    t.goto(x, y)


def calculate(row, col, board):
    x=True
    while x:
        if board[row][col] == 0:
            num = board[row - 1][col]
            num += board[row + 1][col]
            num += board[row][col + 1]
            num += board[row][col - 1]
            x=False
        else:
            print("for now you can't choose a position that has already been chose, please try again")
            (row, col) = inputs()
    """This code is for implementing the ability to 'X' out an opponents tile in future versions"""
    #elif board[row][col]==None:
    #else:
    #num=-1*board[row][col]
    if num==0:
        num=1
    board[row][col]=num
    return board

def inputs():
    """Temporary input method, will later change to graphics and mouse clicking.
    Or at least that is the plan, pygame was not working and I unfortunately
    may not be able to get it implemented in time.
    """
    while True:
        row=int(input("Enter row number between 1 and 5: "))
        col=int(input("Enter column number between 1 and 5: "))
        if row<6 and row>0 and col>0 and col<6:
            break
        else:
            print("invalid input")
    return row, col


def initialize_board():
    """future ability to choose whatever board size you want, may not be implimented """
    #width=int(input"Enter playable board width, between 2 and 15: ")
    #height=int(input"Enter playable board height, between 2 and 15: ")
    #w, h = width+2, height+2
    w, h = 5, 5
    board = [[0 for x in range(w)] for y in range(h)]
    for x in range(w):
        board[x][0] = 1
        board[x][h-1] = 1
        board[0][x] = 1
        board[w-1][x] = 1
    spots=(w-1)*(h-1)
    t.setworldcoordinates(-30, -30, (w*100)+30, (h*100)+30)
    return board, spots


def draw_board(w, h):
    t.up()
    t.home()
    t.right(90)
    for x in range(0, w+1):
        t.goto(x*100, 0)
        t.down()
        t.backward(h*100)
        t.up()
    t.left(90)
    for x in range(0, h+1):
        t.goto(0, x * 100)
        t.down()
        t.forward(w * 100)
        t.up()
    t.home()
    corners()
    t.goto(0, (h-1)*100)
    corners()
    t.goto((w-1)*100, 0)
    corners()
    t.goto((w-1)*100, (h-1)*100)
    corners()
    t.home()


def draw_1s(w, h):
    for x in range(1, w-1):
        t.goto((x*100)+40, 30)
        num1()
        t.goto((x * 100) + 40, (h*100)-70)
        num1()
    for x in range(1, h-1):
        t.goto(40, (x*100)+30)
        num1()
        t.goto((w*100)-60, (x * 100) + 30)
        num1()
    t.update()

def corners():
    """
    Draws the black corners in the game
    """
    t.down()
    t.fillcolor('black')
    t.begin_fill()
    for x in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.up()


def draw_number(row, col, num):
    """Will print the score onto the drawn board"""
    t.up()
    t.goto(row*100, col*100)
    num=str(num)
    if len(num)==1:
        one_digit(num)
    elif len(num)==2:
        two_digit(num)
    elif len(num)==3:
        three_digit(num)
    else:
        more_digit()
    t.update()

def one_digit(num):
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.right(90)
    draw_char(num)


def two_digit(num):
    t.forward(28)
    t.left(90)
    t.forward(30)
    t.right(90)
    draw_char(num[0])
    t.forward(34)
    draw_char(num[1])


def three_digit(num):
    t.forward(16)
    t.left(90)
    t.forward(30)
    t.right(90)
    draw_char(num[0])
    t.forward(34)
    draw_char(num[1])
    t.forward(34)
    draw_char(num[2])

def more_digit():
    t.forward(4)
    t.left(90)
    t.forward(30)
    t.right(90)
    num9()
    t.forward(34)
    num9()
    t.forward(34)
    num9()
    t.forward(34)
    plus()


def draw_char(char):
    if char == '1':
        num1()
    elif char == '2':
        num2()
    elif char == '3':
        num3()
    elif char == '4':
        num4()
    elif char == '5':
        num5()
    elif char == '6':
        num6()
    elif char == '7':
        num7()
    elif char == '8':
        num8()
    elif char == '9':
        num9()
    else:
        num0()

def get_input():
    pass
    #return row, col


def checker(board):
    for x in range(len(board)-1):
        for y in range(len(board[0])-1):
            if board[x+1][y+1]==0:
                return True
    return False


def end(P1score, P2score):
    print("Game over\nPlayer 1: " + str(P1score) + "\nPlayer 2: " + str(P2score))
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
    draw_board(len(board), len(board[0]))
    draw_1s(len(board), len(board[0]))
    while checker(board):
        if turn%2==0:
            print("Player 1's Turn")
        else:
            print("Player 2's turn")
        (row, col)=inputs()
        board=calculate(row, col, board)
        if turn%2==0:
            P1score+=board[row][col]
            t.pencolor('red')
        else:
            P2score+=board[row][col]
            t.pencolor('blue')
        draw_number(row, col, board[row][col])
        turn+=1
        if turn%2==0:
            print("Player 1: " + str(P1score)+"\nPlayer 2: "+str(P2score))
    end(P1score, P2score)
    t.done()


main()
exit()
