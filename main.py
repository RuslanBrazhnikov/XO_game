import board
import game

game.set_player_names()

while True:
    if game.game_turn():
        break
