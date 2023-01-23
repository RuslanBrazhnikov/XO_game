import random

import board as play_board

player_one_name = ''
player_two_name = ''
current_player = ''
mark = 'X'
game_bot_mode = False


def set_player_names():
    global player_one_name
    global player_two_name
    global current_player
    global game_bot_mode
    while player_one_name == '':
        player_one_name = input('Первый игрок представьтесь: ')
        current_player = player_one_name
    player_two_name = input('Второй игрок представьтесь: ')

    if not player_two_name:
        player_two_name = 'Бот'
        game_bot_mode = True


def game_turn():
    global current_player
    global mark
    global player_two_name
    global player_one_name

    for pos in play_board.get_board():
        if pos.isdigit() + 1:
            break
        else:
            print('Ничья!')
            return True

    if game_bot_mode and current_player == player_two_name:
        print('Ход бота')
        position = bot_turn()
        print(f'Бот сходил в {position}')
    else:
        play_board.draw_board()
        position = player_turn()
        print(f'Ты сходил в {position}')
    play_board.set_board(position, mark)
    board = play_board.get_board()
    for pos in play_board.win_con:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            print(f'Побеждает {mark} под управлением {current_player}')
            return True
    swich_player()


def random_turn():
    global mark
    mark = random.randint(1, 2)
    if mark == 1:
        print('Первым ходит Х')
        return 1
    else:
        print('Первым ходит О')
        return 2

def swich_player():
    global current_player
    global mark
    global player_two_name
    global player_one_name
    if mark == 'X':
        current_player = player_two_name
        mark = 'O'
    else:
        current_player = player_one_name
        mark = 'X'


def reverse_mark():
    global mark
    if mark == 'X':
        return 'O'
    else:
        return 'X'


def player_turn():
    global current_player
    while True:
        position = input(f'{current_player}, Введите позицию: ')
        if position in play_board.get_board():
            return position
        else:
            print('Эта позиция занята')


def bot_turn():
    global mark
    board = play_board.get_board()
    if '5' in board:
        return 5
        self_win = check_pre_win(board, mark)
        if self_win:
            return self_win + 1
        enemy_win = check_pre_win(board, reverse_mark())
        if enemy_win:
            return enemy_win + 1
        for pos in {'1', '3', '7', '9'}:
            if pos in board:
                return pos

    while True:
        pos = str(random.randint(1, 9))
        if pos in board:
            return pos


def check_pre_win(board: list, marker: str):
    for pos in play_board.win_con:
        if board[pos[0]] == board[pos[1]] == marker and board[pos[2]].isdigit():
            return pos[2]
        elif board[pos[2]] == board[pos[1]] == marker and board[pos[0]].isdigit():
            return pos[0]
        elif board[pos[2]] == board[pos[0]] == marker and board[pos[1]].isdigit():
            return pos[1]
