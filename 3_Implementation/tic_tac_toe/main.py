board = [' ' for i in range(10)]


def print_board(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3])
    print("---------")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("---------")
    print(" " + board[7] + "| " + board[8] + "| " + board[9])


def insert_alphabet(alphabet, pos):
    board[pos] = alphabet


def free_space(pos):
    return board[pos] == " "


def winner(bot, alpha):
    return ((bot[7] == alpha and bot[8] == alpha and bot[9] == alpha) or
            (bot[4] == alpha and bot[5] == alpha and bot[6] == alpha) or
            (bot[1] == alpha and bot[2] == alpha and bot[3] == alpha) or
            (bot[1] == alpha and bot[4] == alpha and bot[7] == alpha) or
            (bot[2] == alpha and bot[5] == alpha and bot[8] == alpha) or
            (bot[3] == alpha and bot[6] == alpha and bot[9] == alpha) or
            (bot[1] == alpha and bot[5] == alpha and bot[9] == alpha) or
            (bot[3] == alpha and bot[5] == alpha and bot[7] == alpha))

def user_move():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0:
                if move < 10:
                    if free_space(move):
                        run = False
                        insert_alphabet("x", move)
                    else:
                        print("Sorry this space is occupied")
                else:
                    print("Please type the number within the range")
            else:
                print("Please type the number within the range")
        except:
            print("Please type a number. ")


def computer_move():
    possible_moves = [x for x, alphabet in enumerate(board) if alphabet == ' ' and x != 0]
    move = 0
    for alphabet in ['o', 'x']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = alphabet
            if winner(board_copy, alphabet):
                move = i
                return move
    corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners.append(i)
    if len(corners) > 0:
        move = select_random(corners)
        return move
    if 5 in possible_moves:
        move = 5
        return move
    edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = select_random(edges)
    return move

def select_random(li):
 import random
 ln = len(li)
 r = random.randrange(0, ln)
 return li[r]


def board_full(board):
 if board.count(" ") > 1:
    return False
 else:
    return True


def main():
 print("WELCOME TO TIC TAC TOE!!!")
 print_board(board)
 while not(board_full(board)):
    if not(winner(board, "o")):
        user_move()
        print_board(board)
    else:
        print("Sorry, computer won the game!!!")
        break
    if not(winner(board, "x")):
        move = computer_move()
        if move == 0:
            print("Tie game")
        else:
            insert_alphabet("o", move)
            print("Computer placed an 'o' in position", move, ":")
            print_board(board)
    else:
        print("Congo!!!!!!!! you won the game")
        break
    if board_full(board):
        print("Tie game")


main()