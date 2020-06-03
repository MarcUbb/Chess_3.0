import classes

import pygame

########## WINDOW ##########
BACKGROUND = (255,255,255)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BOARD_IMAGE = "board.png"

ICON_PATH = "logo.png"
ICON = pygame.image.load(ICON_PATH)
pygame.display.set_icon(ICON)

TITLE = "Chess"
pygame.display.set_caption(TITLE)
############################


########## BOARDS ##########
START_POS = [[[2,2],[2,3],[2,4],[2,5],[2,6],[2,4],[2,3],[2,2]],
             [[2,1],[2,1],[2,1],[2,1],[2,1],[2,1],[2,1],[2,1]],
             [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
             [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
             [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
             [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
             [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]],
             [[1,2],[1,3],[1,4],[1,5],[1,6],[1,4],[1,3],[1,2],[0,0]]]
BOARD = classes.Board(START_POS, 0)

DEAD_POS = [[[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[0,0],[0,0],[0,0]]]
BOARD_DEAD = classes.Board(DEAD_POS, 8)

MARKER_COLOR = (255,0,0)
FIELD_SIZE = 100
############################


########## GAME ############
RUNNING = True
TURN = 2
MOVE = False

CHECK = 0

GAMEMODE = 2
AI_TURN = 1
AI_DELAY = 1
############################



########## STATS ###########
WINS_WHITE = 0
WINS_BLACK = 0
DRAWS = 0
MOVES = 0
############################



######### EVALUATION ########
ROUND_COUNT = 0
MOVES_AVERAGE = 0
X = []

WINS_WHITE_PLOT = []
WINS_BLACK_PLOT = []
DRAWS_PLOT = []
MOVES_PLOT = []
MOVES_AVERAGE_PLOT = []

UPDATE_FREQUENCY = 10
############################
