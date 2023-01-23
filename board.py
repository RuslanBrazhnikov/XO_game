board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

win_con = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))


def draw_board():
    global board
    for i in range(3):
        print(f'{board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]}')


def get_board():
    global board
    return board


def set_board(position: int, mark: str):
    global board
    board[int(position) - 1] = mark
