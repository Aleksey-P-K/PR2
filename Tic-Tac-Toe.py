# Tic-Tac-Toe Game
def row_winner(board):
    is_equal = []
    for row in board:
        is_equal_row = []
        for char in row:
            if char == row[len(row) - 1] and char != ' ':
                is_equal_row.append(True)
            else:
                is_equal_row.append(False)
        is_equal.append(is_equal_row)
    is_equal2 = []
    for row in is_equal:
        if False in row:
            is_equal2.append(False)
        else:
            is_equal2.append(True)
    return True in is_equal2


def column_winner(board):
    return row_winner([list(x) for x in zip(*board)])


def diagonal_winner(board):
    for row in range(len(board)):
        all_equal = True
        if board[row][row] != board[0][0] or board[row][row] == ' ':
            all_equal = False
            break
    for row in range(len(board)):
        all_equal_1 = True
        if board[row][len(board) - 1 - row] != board[0][len(board) - 1] \
                or board[row][len(board) - 1 - row] == ' ':
            all_equal_1 = False
    return all_equal or all_equal_1


def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)


def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'


def play_move(board, player,):
    success_move = False
    while not (success_move):
        row = input(f'{player} row: ')
        collom = input(f'{player} collom: ')
        if row.isdigit() and collom.isdigit() and\
                int(row) <= board_size and int(collom) <= board_size\
                and board[int(row) - 1][int(collom) - 1] == ' ':
            row = int(row)
            collom = int(collom)
            board[row - 1][int(collom) - 1] = player
            success_move = True
        else:
            print("Wrong move!")
    print(format_board(board))


def make_board(size):
    return [[' '] * size for _ in range(size)]


def print_winner(player):
    print(f'{player} wins!')


def print_draw():
    print("It's a draw!")


def draw(board):
    is_draw = []
    for row in board:
        if not (' ' in row):
            is_draw.append(True)
    if len(is_draw) == len(board):
        return True


def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    end_game = False
    current_player = player1
    last_player = player2
    while not end_game:
        if winner(board):
            print_winner(last_player)
            end_game = True
        elif draw(board):
            print_draw()
            end_game = True
        else:
            if current_player == player1:
                play_move(board, current_player)
                current_player = player2
                last_player = player1
            else:
                play_move(board, current_player)
                current_player = player1
                last_player = player2

success_input = False
print('Welcome to the Tic-Tac-Toe Game')
while not success_input:
    board_size_raw = input(f'Please enter board size: ')
    if board_size_raw.isdigit():
        success_input = True
        board_size = int(board_size_raw)
    else:
        print('Wrong size!')

play_game(board_size, 'X', 'O')