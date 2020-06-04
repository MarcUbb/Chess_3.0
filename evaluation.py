import constants
from matplotlib import pyplot as plt

def evaluate():
    print("White:", constants.WINS_WHITE, "Black:", constants.WINS_BLACK, "DRAWS:", constants.DRAWS, "Moves:", constants.MOVES, "Average Moves:", constants.MOVES_AVERAGE)
    print_board()
    results()

def results():

    constants.X.append(constants.ROUND_COUNT)
    constants.WINS_WHITE_PLOT.append(constants.WINS_WHITE)
    constants.WINS_BLACK_PLOT.append(constants.WINS_BLACK)
    constants.DRAWS_PLOT.append(constants.DRAWS)
    constants.MOVES_PLOT.append(constants.MOVES)

    constants.MOVES_AVERAGE = 0
    i = 0
    while i < len(constants.MOVES_PLOT):
        constants.MOVES_AVERAGE += constants.MOVES_PLOT[i]
        i += 1
    constants.MOVES_AVERAGE = round(float(constants.MOVES_AVERAGE) / float(len(constants.MOVES_PLOT)), 3)

    constants.MOVES_AVERAGE_PLOT.append(constants.MOVES_AVERAGE)



    if len(constants.X) % constants.UPDATE_FREQUENCY == 0:
        print("longest match:", max(constants.MOVES_PLOT), "shortest match:", min(constants.MOVES_PLOT))
        plt.clf()
        plt.plot(constants.X, constants.WINS_WHITE_PLOT, label = "WINS_WHITE")
        plt.plot(constants.X, constants.WINS_BLACK_PLOT, label = "WINS_BLACK")
        plt.plot(constants.X, constants.DRAWS_PLOT, label = "DRAWS")
        plt.plot(constants.X, constants.MOVES_PLOT, label = "MOVES")
        plt.plot(constants.X, constants.MOVES_AVERAGE_PLOT, label="MOVES_AVERAGE")
        plt.legend()
        plt.show()

def print_board():
    print_board = []

    i = 0
    while i < len(constants.BOARD.fields):
        print_board.append([])
        j = 0
        while j < len(constants.BOARD.fields[i]):
            print_board[i].append([constants.BOARD.fields[i][j].figure_team, constants.BOARD.fields[i][j].figure_type])
            j += 1
        i += 1

    i = 0
    while i < len(print_board):
        print(print_board[i])
        i += 1