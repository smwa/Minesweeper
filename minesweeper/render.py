from Game import Game

def render(game: Game):
    output = "    "
    width = game.width
    counter = 0
    for i in range(width):
        if i < 10:
            output += " {} ".format(i)
        elif i < 100:
            output += " {}".format(i)
        elif i < 1000:
            output += "{}".format(i)
        else:
            raise Exception("TUI renderer does not support a width greater than 1000")
    output += "\n"
    for cell in game.cells:
        if counter % width == 0:
            height = int(counter / width)
            if height < 10:
                output += "{}   ".format(height)
            elif height < 100:
                output += "{}  ".format(height)
            elif height < 1000:
                output += "{} ".format(height)
            elif height < 10000:
                output += "{}".format(height)
            else:
                raise Exception("TUI renderer does not support a height greater than 10,000")
        if not cell.is_revealed:
            if cell.is_flagged:
                output += "[M]"
            else:
                output += "[ ]"
        else:
            if cell.is_mine:
                output += "[X]"
            else:
                output += "[{}]".format(cell.number_of_neighboring_mines)
        counter += 1
        if counter % width == 0:
            output += "\n"
    if game.did_win:
        output += "You won\n"
    if game.did_lose:
        output += "You lost\n"
    return output
