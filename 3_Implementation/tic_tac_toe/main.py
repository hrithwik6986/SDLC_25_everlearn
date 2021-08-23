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


