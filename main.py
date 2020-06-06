import constants                        # import functions from other files
import basic_functions
import moves
import evaluation

import sys                              # import necessary libraries
import pygame


pygame.init()                           # initialize pygame

while True:                             # starts game loop
    for event in pygame.event.get():    # interrupt request
        if event.type == pygame.QUIT:
            sys.exit()

    if constants.RUNNING == False:      # game is finished
        basic_functions.draw_window()   # updates window fo final position
        evaluation.evaluate()           # evaluate match
        basic_functions.reset_game()    # restart game

    if constants.RUNNING == True:       # game is running
        basic_functions.draw_window()   # update pygame window
        
        if constants.GAMEMODE == 0:     # human vs human
            moves.human_move()          # execute human move

        elif constants.GAMEMODE == 1:   # AI vs human
            moves.ai_move()             # if AIs turn execute AI move
            moves.human_move()          # if not execute human move

        elif constants.GAMEMODE == 2:   # AI vs AI
            moves.ai_move()             # execute AI move

        constants.BOARD.fields[7][8].active = False
