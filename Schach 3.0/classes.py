

class Field:
    def __init__(self, line, collum, figure_team, figure_type):
        self.active = False
        self.pos_x = collum
        self.pos_y = line

        self.figure_moved = False
        self.figure_team = figure_team                                  #0-none 1-white 2-black
        self.figure_type = figure_type                                  #0-none 1-pawn 2-rook 3-knight 4-bishop 5-queen 6-king
        self.move_pattern = pattern_generator(figure_type,figure_team)
        self.rochade_flag = 0

class Board:
    def __init__(self, start_pos, x_pos):
        self.fields = fields_fill(start_pos, x_pos)





def fields_fill(start_pos,x_pos):
    fields = [[] for _ in range(len(start_pos))]

    i = 0
    while i < len(start_pos):
        j = 0
        while j < len(start_pos[i]):
            fields[i].append(Field(i, j + x_pos, start_pos[i][j][0], start_pos[i][j][1]))
            j += 1
        i += 1
    return fields


def pattern_generator(figure_type, figure_team):

    pawn_white = [[0, -1],
                  [0, -2],
                  [1, -1],
                  [-1, -1]]

    pawn_black = [[0, 1],
                  [0, 2],
                  [1, 1],
                  [-1, 1]]

    rook = [[0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [0, 7],
            [1, 0],
            [2, 0],
            [3, 0],
            [4, 0],
            [5, 0],
            [6, 0],
            [7, 0],
            [0, -1],
            [0, -2],
            [0, -3],
            [0, -4],
            [0, -5],
            [0, -6],
            [0, -7],
            [-1, 0],
            [-2, 0],
            [-3, 0],
            [-4, 0],
            [-5, 0],
            [-6, 0],
            [-7, 0]]

    bishop = [[1, 1],
              [2, 2],
              [3, 3],
              [4, 4],
              [5, 5],
              [6, 6],
              [7, 7],
              [1, -1],
              [2, -2],
              [3, -3],
              [4, -4],
              [5, -5],
              [6, -6],
              [7, -7],
              [-1, -1],
              [-2, -2],
              [-3, -3],
              [-4, -4],
              [-5, -5],
              [-6, -6],
              [-7, -7],
              [-1, 1],
              [-2, 2],
              [-3, 3],
              [-4, 4],
              [-5, 5],
              [-6, 6],
              [-7, 7]]

    knight = [[2, 1],
              [2, -1],
              [-2, 1],
              [-2, -1],
              [1, 2],
              [-1, 2],
              [1, -2],
              [-1, -2]]

    king = [[0, 1],
            [0, -1],
            [1, 0],
            [1, 1],
            [1, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1]]

    queen = rook + bishop

    if (figure_type == 0):
        return 0
    elif (figure_type == 1 and figure_team == 1):
        return pawn_white

    elif (figure_type == 1 and figure_team == 2):
        return pawn_black

    elif (figure_type == 2):
        return rook

    elif (figure_type == 3):
        return knight

    elif (figure_type == 4):
        return bishop

    elif (figure_type == 5):
        return queen

    elif (figure_type == 6):
        return king

    else:
        print("ERROR IN PATTERN_GENERATOR")