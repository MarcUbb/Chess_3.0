import classes
import constants

import pygame

def check_for_draw():
    movable_figures = []

    for m in constants.BOARD.fields:
        for f in m:
            if f.figure_team == constants.TURN:
                mark_move_pattern(f, constants.BOARD)
                counter = 0
                for n in constants.BOARD.fields:
                    for b in n:
                        if b.active == True:
                            counter += 1
                if counter > 1:
                    movable_figures.append(f)
                reset_markers()

    if len(movable_figures) == 0:
        constants.DRAWS += 1
        constants.RUNNING = False



def valid_ai_move(FIELD_CHOSEN, FIELD_MOVE):
    mark_move_pattern(FIELD_CHOSEN, constants.BOARD)
    if constants.BOARD.fields[FIELD_MOVE.pos_y][FIELD_MOVE.pos_x].active == False:
        reset_markers()
        print("INVALID MOVE BY TEAM", constants.TURN, "!!!")
        if constants.TURN == 1:
            constants.WINS_BLACK += 1
        else:
            constants.WINS_WHITE += 1
        constants.RUNNING = False


def move_dead_figures(figure):
    c = 0
    for i in constants.BOARD_DEAD.fields:
        for f in i:
            if f.figure_team == 0 and f.figure_type == 0:
                f.figure_team = figure.figure_team
                f.figure_type = figure.figure_type
                c = 1
                break
        if c == 1:
            break

def replace_figure(FIELD_CHOSEN, FIELD_MOVE):
    FIELD_MOVE.figure_moved = True
    FIELD_MOVE.figure_team = FIELD_CHOSEN.figure_team
    FIELD_MOVE.figure_type = FIELD_CHOSEN.figure_type
    FIELD_MOVE.move_pattern = classes.pattern_generator(FIELD_CHOSEN.figure_type,FIELD_CHOSEN.figure_team)
    FIELD_CHOSEN.figure_team = 0
    FIELD_CHOSEN.figure_type = 0
    FIELD_CHOSEN.move_pattern = 0
    if FIELD_MOVE.rochade_flag != 0:
        rochade(FIELD_MOVE, constants.BOARD, FIELD_MOVE.rochade_flag)




def reset_markers():
    for i in constants.BOARD.fields:
        for f in i:
            f.active = False
            f.rochade_flag = 0











def check_for_chess():
    reset_markers()                                                #TODO not so reliable
    white_king = False
    black_king = False
    for i in constants.BOARD.fields:
        for f in i:
            if f.figure_team == 1 and f.figure_type == 6:
                white_king = True
            if f.figure_team == 2 and f.figure_type == 6:
                black_king = True

    if white_king == False:
        constants.CHECK = 3
        constants.WINS_BLACK += 1
        constants.RUNNING = False
    if black_king == False:
        constants.CHECK = 4
        constants.WINS_WHITE += 1
        constants.RUNNING = False


    king_pos_x = 0
    king_pos_y = 0

    c = 0
    for i in constants.BOARD.fields:
        for f in i:
            if f.figure_team == constants.TURN and f.figure_type == 6:
                king_pos_x = f.pos_x
                king_pos_y = f.pos_y
                c = 1
                break
        if c == 1:
            break

    for i in constants.BOARD.fields:
        for f in i:
            if f.figure_team != constants.TURN and f.figure_team != 0:
                mark_move_pattern(f, constants.BOARD)

    if constants.BOARD.fields[king_pos_y][king_pos_x].active == True:
        reset_markers()
        constants.CHECK = constants.TURN + 2
        if constants.TURN == 1:
            constants.WINS_BLACK += 1
        else:
            constants.WINS_WHITE += 1
        constants.RUNNING = False

    else:
        reset_markers()
        king_pos_x = 0
        king_pos_y = 0

        c = 0
        for i in constants.BOARD.fields:
            for f in i:
                if f.figure_team != constants.TURN and f.figure_type == 6:
                    king_pos_x = f.pos_x
                    king_pos_y = f.pos_y
                    c = 1
                    break
            if c == 1:
                break

        for i in constants.BOARD.fields:
            for f in i:
                if f.figure_team == constants.TURN:
                    mark_move_pattern(f,constants.BOARD)

        if constants.BOARD.fields[king_pos_y][king_pos_x].active == True:
            reset_markers()
            constants.CHECK = constants.TURN

        else:
            reset_markers()
            constants.CHECK = 0















def choose_figure(board, AI_SELECTION):
    pawn = 0

    for f in board.fields[0]:
        if f.figure_type == 1:
            pawn = f
            break

    for f in board.fields[7]:
        if f.figure_type == 1:
            pawn = f
            break

    if pawn == 0:
        return board
    
    if AI_SELECTION == 1 or AI_SELECTION > 5:
        print("INVALID FIGURE CHOSEN BY TEAM", constants.TURN, "!!!")
        if constants.TURN == 1:
            constants.WINS_BLACK += 1
        else:
            constants.WINS_WHITE += 1
        constants.RUNNING = False

    if AI_SELECTION > 1 and AI_SELECTION < 6:
        board.fields[pawn.pos_y][pawn.pos_x].figure_type = AI_SELECTION
        return board

    CHOOSE_SCREEN_WIDTH = 400
    CHOOSE_SCREEN_HEIGHT = 100
    CHOOSE_TITLE = "Choose a figure"
    CHOOSE_ICON_PATH = "logo.png"

    pygame.init()  # initializing Pygame
    choose_screen = pygame.display.set_mode((CHOOSE_SCREEN_WIDTH, CHOOSE_SCREEN_HEIGHT))  # initializing window
    CHOOSE_ICON = pygame.image.load(CHOOSE_ICON_PATH)  # set icon image

    pygame.display.set_caption(CHOOSE_TITLE)  # imports title to window
    pygame.display.set_icon(CHOOSE_ICON)  # imports icon to window

    while True:
        choose_screen.fill((255,255,255))

        if pawn.figure_team == 1:
            choose_screen.blit(pygame.image.load("white_choose.png"), (0, 0))
        elif pawn.figure_team == 2:
            choose_screen.blit(pygame.image.load("black_choose.png"), (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                x_coord = pygame.mouse.get_pos()[0]
                if x_coord < 100:
                    board.fields[pawn.pos_y][pawn.pos_x].figure_type = 2

                elif x_coord < 200:
                    board.fields[pawn.pos_y][pawn.pos_x].figure_type = 3

                elif x_coord < 300:
                    board.fields[pawn.pos_y][pawn.pos_x].figure_type = 4

                elif x_coord < 400:
                    board.fields[pawn.pos_y][pawn.pos_x].figure_type = 5

                pygame.init()  # initializing Pygame
                screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))  # initializing window
                ICON = pygame.image.load(constants.ICON_PATH)  # set icon image

                pygame.display.set_caption(constants.TITLE)  # imports title to window
                pygame.display.set_icon(constants.ICON)  # imports icon to window
                return board

















def mark_move_pattern(field,board):  # mark_move_pattern marks all the possible moves when a field is selected
    field.move_pattern = classes.pattern_generator(field.figure_type, field.figure_team)  #allways reload Moveset so we can later delete unavailable Moves
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
