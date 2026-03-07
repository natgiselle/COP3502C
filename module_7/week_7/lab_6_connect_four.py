


'''
def initialize_board(num_rows, num_cols):

This will take in the num_row and num_cols from user input 
and this will set each spot in the list to “-”. 
A 2D character list with each spot set to be “-” will be returned.
'''
def initialize_board(num_rows, num_cols):
    board = []
    for r in range(num_rows):
        row = []
        for c in range (num_cols):
            row.append('-')
        board.append(row)
    return board


'''
def print_board(board):

This will take in the 2D character list for the board and print the board.
'''
def print_board(board):
    for row in reversed(board):
        for c in range(len(row)):
            if c == len(row) - 1:
                print(row[c], end="")
            else:
                print(row[c], end=" ")
        print()


'''
def insert_chip(board, col, chip_type):

This will take in the 2D character list for the board.
This function places the token ('x' or 'o' denoted as 'chip_type')
in the column that the user has chosen. Will find the 
next available spot in that column if there are already tokens there.
The index of the row that the token is placed in is returned.
'''
def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row # return row inside of the if statement because the only row needed is where the chip is placed

'''
def check_if_winner(board, col, row, chip_type)
This will take in the 2D character list for the board.
After a token is added, checks whether the token in this location,
of the specified chip type, creates four in a row.
Will return True if someone won, and False otherwise.

Hint: Implement the methods in this order.
'''

def check_if_winner(board, col, row, chip_type):
    # vertical
    count = 1

    r = row - 1
    while r >= 0 and board[r][col] == chip_type:
        count += 1
        r -= 1

    r = row + 1
    while r < len(board) and board[r][col] == chip_type:
        count += 1
        r += 1

    if count >= 4:
        return True

    # horizontal
    count = 1

    c = col - 1
    while c >= 0 and board[row][c] == chip_type:
        count += 1
        c -= 1

    c = col + 1
    while c < len(board[0]) and board[row][c] == chip_type:
        count += 1
        c += 1

    return count >= 4



if __name__ == "__main__":
        num_rows = int(input("What would you like the height of the board to be?"))
        num_cols = int(input("What would you like the length of the board to be?"))
        board = initialize_board(num_rows,num_cols)
        print_board(board)
        print()
        chip_type_p1 = 'x'
        chip_type_p2 = 'o'
        print(f"Player 1: {chip_type_p1}")
        print(f"Player 2: {chip_type_p2}")

        p1_turn = True
        p2_turn = False
        stop = False

        while stop == False:
            print()
            if p1_turn:
                col_p1 = int(input("Player 1: Which column would you like to choose?"))
                row_p1 = insert_chip(board, col_p1, chip_type_p1)
                p1_turn = False
                p2_turn = True
                print_board(board)

                if check_if_winner(board, col_p1, row_p1, chip_type_p1):
                    print()
                    print("Player 1 won the game!")
                    stop = True
                elif '-' not in sum(board, []):
                    print()
                    print("Draw. Nobody wins.")
                    stop = True


            elif p2_turn:
                col_p2 = int(input("Player 2: Which column would you like to choose?"))
                row_p2 = insert_chip(board, col_p2, chip_type_p2)
                p1_turn = True
                p2_turn = False
                print_board(board)

                if check_if_winner(board, col_p2, row_p2,chip_type_p2):
                    print()
                    print("Player 2 won the game!")
                    stop = True
                elif '-' not in sum(board, []):
                    print()
                    print("Draw. Nobody wins.")
                    stop = True