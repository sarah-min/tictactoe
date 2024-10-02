# create a new board
def new_board():
    return [[0,0,0], [0,0,0], [0,0,0]]

# print current state of board
def print_board(board):
    # print x-coords
    print("    0   1   2   ")
    # print board
    a = 0
    for i in board:
        print("  -------------")
        print(a, end=" ")
        a += 1
        print("|", end =" ")
        # 0 = blank, 1 = x, 2 = o
        for j in i:
            if j == 0:
                print("-", end=" | ")
            elif j == 1:
                print("x", end=" | ")
            elif j == 2:
                print("o", end=" | ")
        print()
    print("  -------------")

# get move coordinates
def get_x():
    x = input("What is your move's x-coordinate: ")
    x = int(x)
    while x > 2:
        print("Error: invalid input -- must be less than 2")
        x = input("What is your move's x-coordinate: ")
        x = int(x)
    return x

def get_y():
    y = input("What is your move's y-coordinate: ")
    y = int(y)
    while y > 2:
        print("Error: invalid input -- must be less than 2")
        y = input("What is your move's y-coordinate: ")
        y = int(y)
    return y

# make move if user 1's turn
def user1_move(x, y, board):
    board[y][x] = 1
    return board

# make move if user 2's turn
def user2_move(x, y, board):
    board[y][x] = 2
    return board

# check if move being made is ok
def valid_move(x, y, board):
    if (board[x][y] == 0):
        return True
    return False

# check for win
def check_win(board):
    # check all possible lines of 3
    if ( board[0][0] == board[1][0] and board[1][0] == board[2][0] ):
        return board[0][0]
    elif ( board[0][1] == board[1][1] and board[1][1] == board[2][1] ):
        return board[0][1]
    elif ( board[0][2] == board[1][2] and board[1][2] == board[2][2] ):
        return board[0][2]
    elif ( board[0][0] == board[0][1] and board[0][1] == board[0][2] ):
        return board[0][0]
    elif ( board[1][0] == board[1][1] and board[1][1] == board[1][2] ):
        return board[1][0]
    elif ( board[2][0] == board[2][1] and board[2][1] == board[2][2] ):
        return board[2][0]
    elif ( board[0][0] == board[1][1] and board[1][1] == board[2][2] ):
        return board[0][0]
    elif ( board[0][2] == board[1][1] and board[1][1] == board[2][0] ):
        return board[0][2]
    else:
        return 0


def main():
    board = new_board()
    print_board(board)
    turn_count = 1

    while (turn_count <= 9):
        if (turn_count % 2 == 1):
            print("\nPlayer 1:")
        else:
            print("\nPlayer 2: ")
        x = get_x()
        y = get_y()
        # test move validity (if there's smth in that space already)
        if valid_move(x, y, board):
            # odd counts = user 1
            if (turn_count % 2 == 1):
                board = user1_move(x, y, board)
            # even counts = user 2
            else:
                board = user2_move(x, y, board)
        else: 
            print("That spot is already taken")
            turn_count -= 1

        # check for a win
        w = check_win(board)
        if w != 0:
            print_board(board)
            print("Player", w, "wins!")
            break

        print()
        print_board(board)
        turn_count += 1


if __name__ == "__main__":
    main()