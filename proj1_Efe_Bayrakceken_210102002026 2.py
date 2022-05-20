my_name = "Efe Bayrakceken"
my_id = "210102002026"
my_email = "e.bayrakceken2021@gtu.edu.tr"

import random
def generate(row, column):
    count=0
    board=[]
    for i in range(row):
        board.append(list(range(row*column))[count:(count+column)])
        count+=column
        
    return board

def shuffle(board, times=20):
    moves=""
    times_prev=times
    while times!=0:
        moves+=move_random(board)
        times-=1
    if is_solved(board)==True:
        for i in moves[::-1]:
            if i=="U":
                move(board, "D")
            if i=="D":
                move(board, "U")
            elif i=="L":
                move(board, "R")
            elif i=="R":
                move(board, "L")
        
        moves=shuffle(board, times_prev)
    return moves
    
        
def reset(board):
    row=len(board[0])
    column=len(board)
    board.clear()
    for i in range(column):    
        board.append(generate(column, row)[i])
        
def is_valid(board):
    row=len(board[0])
    column=len(board)
    testboard=[]
    board_raw=list(range(0, row*column))
    # print(board_raw)
    while len(testboard)!=len(board_raw):
        for i in range(0,column):    
            for j in range(0,row):
                for n in board_raw:
                    if board[i][j] not in board_raw:
                        return False
                testboard.append(board[i][j])
                
                #     (testboard)
        testboard.sort()
        if testboard!=board_raw:
            return False                    
    return True

def is_solved(board):
    row=len(board[0])
    column=len(board)
    testboard=[]
    board_raw=list(range(0, row*column))
    # print(board_raw)
    while len(testboard)!=len(board_raw):
        for i in range(0,column):    
            for j in range(0,row):
                for n in board_raw:
                    if board[i][j] not in board_raw:
                        return False
                testboard.append(board[i][j])
                
                # print(testboard)
        if testboard!=board_raw:
            return False                    
    return True


def get_board_size(board):
    row=len(board)
    column=len(board[0])
    return row, column

def find_zero(board):
    for i in board:
        if 0 in i:
            return (board.index(i), board[board.index(i)].index(0))
    

def move_right(board, check_only=False):
    y, x= find_zero(board)
    if x==len(board[0])-1:
        return 0
    if check_only==False:
        board[y][x],board[y][x+1]=board[(y)][x+1], board[(y)][x]
    return 1

def move_left(board, check_only=False):
    y, x= find_zero(board)
    if x==0:
        return 0
    if check_only==False:
        board[y][x],board[y][x-1]=board[(y)][x-1], board[(y)][x]
    return 1

def move_up(board, check_only=False):
    y, x= find_zero(board)
    if y==0:
        return 0
    if check_only==False:
        board[y][x],board[(y-1)][x]=board[(y-1)][x], board[(y)][x]
    return 1

def move_down(board, check_only=False):
    y, x= find_zero(board)
    if y==len(board)-1:
        return 0
    
    if check_only==False:
        board[y][x],board[(y+1)][x]=board[(y+1)][x], board[(y)][x]
    return 1


def move_random(board):
    valids=[]
    if move_up(board, True)==1:
        valids.append("U")
        
    if move_down(board, True)==1:
        valids.append("D")
        
    if move_left(board, True)==1:
        valids.append("L")
        
    if move_right(board, True)==1:
        valids.append("R")

    rand=random.choice(valids)
    move(board, rand)
    return rand

def move(board, moves):
    x=0
    y=0
    for i in range(len(board)):
        if board[i].count(0)>0:
            for j in range(len(board[i])):
                if board[i][j]==0:
                    x=j
                    y=i
    for i in moves:
        if i in ["U", "u"]:
            move_up(board)
            y-=1
        elif i in ["D","d"]:
            move_down(board)
            y+=1
        elif i in ["L","l"] :
            move_left(board)
            x-=1
        elif i in ["R","r"]:
            move_right(board)
            x+=1
                
def rotate(board):
    board_copy=board[:]
    empty=[]
    board_rotated=[]
    for _ in range(len(board[0])):
        board_rotated.append(empty[:])
    
    for i in range(len(board[0])):
        for j in range(len(board)):
            board_rotated[i].append(board_copy[j][i])
        board_rotated[i].reverse()
    # print(board_rotated)
    return board_rotated
        

def print_board(board):
    matrix=""
    count=0
    for i in board:
        for j in board[count]:
            matrix+=str(j)+"\t"
        count+=1
        matrix+="\n"
        
    print(matrix)
    
def play(board, moves):
    count=0
    if is_valid(board)!=1:
        return -2
    if len(moves)==0:
        return -1
    for i in moves:
        if is_solved(board)==1:
            return count
        count+=1
        move(board, i)
    if is_solved(board)==1:
        return count
    if count==len(moves) and count!=1:
        return -1
        
def play_interactive(board=None):
    if board==None:
        print("Please type the puzzle size")
        row=int(input("Row number:"))
        column=int(input("Column number:"))
        a=generate(row, column)
        shuffle(a)
        board=a
    if is_valid(board)!=1:
        return "", -2
    print_board(board)
    if is_solved(board)==True:
        return "", 0
    moves=""
    count=0
    while is_solved(board)!=True:
        curr_move=input("Move: ")
        if curr_move in ["Q","q"]:
            return moves, -1
        elif curr_move not in ["m", "M"]:
            move(board, curr_move)
        else:
            move_random(board)
        moves+=curr_move
        count+=1
        print_board(board)
    return moves, count


