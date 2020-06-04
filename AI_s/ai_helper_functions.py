############################################################################
#                     USEFUL FUNCTIONS FOR YOUR AI                         #
############################################################################

def reset_markers(board):   # deactivates all fields on a board
    for i in board.fields:
        for f in i:
            f.active = False
            f.rochade_flag = 0

def check_for_check(board, team):   # checks if a given team is in check
    for i in board.fields:
        for f in i:
            if f.figure_team != team:
                mark_move_pattern(f, board)
            if f.figure_team == team and f.figure_type == 6 and f.active == True:
                return True
    return False

def get_positioning(board): # returns positioning on a board in initialisation form (to generate a copy board for example)
    positioning = []
    i = 0
    while i < board.fields:
        positioning.append([])
        j = 0
        while j < board.fields[i]:
            positioning[i].append([board.fields[i][j].figure_team, board.fields[i][j].figure_type])
            j += 1
        i += 1
    return positioning




########################### MOVE PATTERN ##########################

def mark_move_pattern(field,board):  # activates al fields a given figure can be moved to
    field.move_pattern = pattern_generator(field.figure_type, field.figure_team)  #allways reload Moveset so we can later delete unavailable Moves
    if field.figure_team == 0 or field.figure_type == 0:
        return 0

    else:

        i = 0
        while i < len(field.move_pattern):
            move_pos_x = field.pos_x + field.move_pattern[i][0]
            move_pos_y = field.pos_y + field.move_pattern[i][1]
            if move_pos_x >= 0 and move_pos_x < 8 and move_pos_y >= 0 and move_pos_y < 8:
                if board.fields[move_pos_y][move_pos_x].figure_team != field.figure_team:
                    board.fields[move_pos_y][move_pos_x].active = True
            i += 1
    # print(field.move_pattern) # for testing. please delete this line if its still there
    applyFigureMovementRules(field, board)


## Set of characteristic moveset treatments for each type of figure ##

def applyFigureMovementRules(field, board):  # Switch for the selection of Figuretype
    if field.figure_type == 0:
        print("no Figure given!")
    elif field.figure_type == 1:
        pawnMoveSet(field, board)
    elif field.figure_type == 4:
        bishopMoveSet(field, board)
    elif field.figure_type == 3:
        knightMoveSet(field, board)
    elif field.figure_type == 2:
        rookMoveSet(field, board)
    elif field.figure_type == 5:
        queenMoveSet(field, board)
    elif field.figure_type == 6:
        kingMoveSet(field, board)
    else:
        print("wrong FigType given WTF?!")


def pawnMoveSet(field, board):
    if field.figure_team == 1:  # white pawn
        # check if it has moved
        if field.pos_y != 6 and field.pos_y - 2 >= 0:  # Figure has moved?
            board.fields[field.pos_y - 2][field.pos_x].active = False
        else:
            if field.pos_y - 2 >= 0:
                if board.fields[field.pos_y - 1][field.pos_x].figure_type != 0:  # is someone in Front of Figure
                    board.fields[field.pos_y - 2][field.pos_x].active = False
                if board.fields[field.pos_y - 2][field.pos_x].figure_type != 0:  # is someone two in Front of Figure
                    board.fields[field.pos_y - 2][field.pos_x].active = False

        # check if it can kill someone
        if field.pos_x - 1 >= 0:
            if board.fields[field.pos_y - 1][field.pos_x - 1].figure_team != 2:  # can pawn kill a Figure to the 'left' of its view
                board.fields[field.pos_y - 1][field.pos_x - 1].active = False
        if field.pos_x + 1 < 8:
            if board.fields[field.pos_y - 1][field.pos_x + 1].figure_team != 2:  # can pawn kill a Figure to the 'right' of its view
                board.fields[field.pos_y - 1][field.pos_x + 1].active = False
        if board.fields[field.pos_y - 1][field.pos_x].figure_team == 2:  # when someone is in front of pawn, he cant kill or move there
            board.fields[field.pos_y - 1][field.pos_x].active = False


    elif field.figure_team == 2:  # black pawn
        # check if it has moved
        if field.pos_y != 1 and field.pos_y + 2 < 8:  # Figure has moved?
            board.fields[field.pos_y + 2][field.pos_x].active = False
        else:
            if field.pos_y + 2 < 8:
                if board.fields[field.pos_y + 1][field.pos_x].figure_type != 0:  # is someone in Front of Figure
                    board.fields[field.pos_y + 2][field.pos_x].active = False
                if board.fields[field.pos_y + 2][field.pos_x].figure_type != 0:  # is someone two in Front of Figure
                    board.fields[field.pos_y + 2][field.pos_x].active = False

        # check if it can kill someone
        if field.pos_x - 1 >= 0 and field.pos_y + 1 < 8:
            if board.fields[field.pos_y + 1][field.pos_x - 1].figure_team != 1:  # can pawn kill a Figure to the 'left' of its view
                board.fields[field.pos_y + 1][field.pos_x - 1].active = False
        if field.pos_x + 1 < 8 and field.pos_y + 1 < 8:
            if board.fields[field.pos_y + 1][field.pos_x + 1].figure_team != 1:  # can pawn kill a Figure to the 'right' of its view
                board.fields[field.pos_y + 1][field.pos_x + 1].active = False
        if field.pos_y + 1 < 8:
            if board.fields[field.pos_y + 1][field.pos_x].figure_team == 1:  # when someone is in front of pawn, he cant kill or move there
                board.fields[field.pos_y + 1][field.pos_x].active = False


def bishopMoveSet(field, board):
    checkDirection(field, board, -1, 1)
    checkDirection(field, board, 1, 1)
    checkDirection(field, board, 1, -1)
    checkDirection(field, board, -1, -1)


def knightMoveSet(field, board):
    pass  # The knight has no specialmoves


def rookMoveSet(field, board):
    checkDirection(field, board, 1, 0)
    checkDirection(field, board, -1, 0)
    checkDirection(field, board, 0, 1)
    checkDirection(field, board, 0, -1)


def queenMoveSet(field, board):
    checkDirection(field, board, 1, 0)
    checkDirection(field, board, -1, 0)
    checkDirection(field, board, 0, 1)
    checkDirection(field, board, 0, -1)
    checkDirection(field, board, -1, 1)
    checkDirection(field, board, 1, 1)
    checkDirection(field, board, 1, -1)
    checkDirection(field, board, -1, -1)


def kingMoveSet(field, board):
    if not field.figure_moved:
        if not board.fields[field.pos_y][field.pos_x - 4].figure_moved and board.fields[field.pos_y][field.pos_x - 1].figure_type == 0 and board.fields[field.pos_y][field.pos_x - 2].figure_type == 0 and board.fields[field.pos_y][field.pos_x-3].figure_type == 0:
            board.fields[field.pos_y][field.pos_x - 2].active = True
            board.fields[field.pos_y][field.pos_x - 2].rochade_flag = 1
        if not board.fields[field.pos_y][field.pos_x + 3].figure_moved and board.fields[field.pos_y][field.pos_x + 1].figure_type == 0 and board.fields[field.pos_y][field.pos_x + 2].figure_type == 0:
            board.fields[field.pos_y][field.pos_x + 2].active = True
            board.fields[field.pos_y][field.pos_x + 2].rochade_flag = 2

def rochade(field, board, direction):
    if direction == 1: # left
        board.fields[field.pos_y][field.pos_x-2].figure_team = 0
        board.fields[field.pos_y][field.pos_x-2].figure_type = 0
        board.fields[field.pos_y][field.pos_x+1].figure_team = field.figure_team
        board.fields[field.pos_y][field.pos_x+1].figure_type = 2
    elif direction == 2: # right
        board.fields[field.pos_y][field.pos_x+1].figure_team = 0
        board.fields[field.pos_y][field.pos_x+1].figure_type = 0
        board.fields[field.pos_y][field.pos_x-1].figure_team = field.figure_team
        board.fields[field.pos_y][field.pos_x-1].figure_type = 2
    else: print("no rochade direction given. ERROR")


def checkDirection(field, board, x,y):  # treats the problem, that a figure can't move behind another figure when it's in the way
    foundFigure = False
    i = 1
    while field.pos_x + i * x >= 0 and field.pos_x + i * x < 8 and field.pos_y + i * y >= 0 and field.pos_y + i * y < 8:  # While Fields in Board
        if foundFigure:
            board.fields[field.pos_y + i * y][field.pos_x + i * x].active = False  # every field after a found figure gets deactivated
        elif board.fields[field.pos_y + i * y][field.pos_x + i * x].figure_type != 0:  # check if there is a figure in the way
            foundFigure = True  # I don't know what this line does...
        i += 1






################################## CLASSES #######################################

class Field:
    def __init__(self, line, collum, figure_team, figure_type):
        self.active = False
        self.pos_x = collum
        self.pos_y = line

        self.figure_moved = False
        self.figure_team = figure_team                                  # 0-none 1-white 2-black
        self.figure_type = figure_type                                  # 0-none 1-pawn 2-rook 3-knight 4-bishop 5-queen 6-king
        self.move_pattern = pattern_generator(figure_type,figure_team)
        self.rochade_flag = 0

class Board:
    def __init__(self, start_pos):
        self.fields = fields_fill(start_pos)

"""
example_start_pos = [[[2,2],[2,3],[2,4],[2,5],[2,6],[2,4],[2,3],[2,2]], standard positioning of board
                     [[2,1],[2,1],[2,1],[2,1],[2,1],[2,1],[2,1],[2,1]],
                     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                     [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]],
                     [[1,2],[1,3],[1,4],[1,5],[1,6],[1,4],[1,3],[1,2]]]
"""

def fields_fill(start_pos):
    fields = [[] for _ in range(len(start_pos))]

    i = 0
    while i < len(start_pos):
        j = 0
        while j < len(start_pos[i]):
            fields[i].append(Field(i, j, start_pos[i][j][0], start_pos[i][j][1]))
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