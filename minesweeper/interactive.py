from Game import Game
from render import render

game = Game(16, 16, 40)

while not game.is_game_over():
    print(render(game))
    cmd = input("Reveal(r) or flag(f) what cell, with the x and y coordinates? e.g. r 0 4: ")
    cmds = cmd.split()
    if len(cmds) > 3 or len(cmds) < 3:
        print("Invalid command")
        continue
    try:
        cmds[1] = int(cmds[1])
        cmds[2] = int(cmds[2])
    except ValueError:
        print("Invalid coordinate")
        continue
    if cmds[0] == "r":
        game.reveal(cmds[1], cmds[2])
    if cmds[0] == "f":
        game.toggle_flag(cmds[1], cmds[2])
