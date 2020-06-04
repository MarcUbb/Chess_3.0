import constants                        # import functions fromother files
import game_mechanics
import basic_functions

import pygame                           # import necessary library
import copy


from best_value_ai import *             # import AI files
from best_value_ai_with_check import *


def ai_move():
    if constants.GAMEMODE == 1 and constants.TURN != constants.AI_TURN: # looks if its AIs turn (only for gamemode 1)
        return 0
    pygame.time.wait(constants.AI_DELAY)                                # short delay so AI moves become visible
    AI_MESSAGES = [0]
    if constants.TURN == 1 or (constants.GAMEMODE == 1 and constants.TURN == constants.AI_TURN):                                # AI which is used in gamemode 1
        FIELD_CHOSEN, FIELD_MOVE, AI_MESSAGES = constants.AI_1.ai_function(constants.BOARD, constants.TURN)
    elif constants.TURN == 2:                                                                                                   # 2nd AI
        FIELD_CHOSEN, FIELD_MOVE, AI_MESSAGES = constants.AI_2.ai_function(constants.BOARD, constants.TURN)

    game_mechanics.check_for_draw()                                                 # checks if the game drawed
    game_mechanics.valid_ai_move(FIELD_CHOSEN, FIELD_MOVE)                          # checks if the AIs move was valid
    game_mechanics.move_dead_figures(FIELD_MOVE)                                    # moves killed figure on the dead figures board
    game_mechanics.replace_figure(FIELD_CHOSEN, FIELD_MOVE)                         # executes the move
    game_mechanics.check_for_chess()                                                # checks if somebody is in check or lost
    constants.BOARD = game_mechanics.choose_figure(constants.BOARD, AI_MESSAGES[0]) # AI chooses figure if pawn reaches end of board
    constants.MOVES += 1                                                            # counts how many moves have been done




def human_move():                           #TODO make it work

    basic_functions.draw_window()

    if pygame.mouse.get_pressed()[0]:  # if mousebutton is being pressed
        game_mechanics.reset_markers()  # delete all marks on board

        if constants.MOVE == False:  # case if no friendly figure was pressed before
            FIELD_CHOSEN = constants.BOARD.fields[basic_functions.mouse_coordinates_to_field()[1]][basic_functions.mouse_coordinates_to_field()[0]]  # checks which coordinates were clicked and converts them in field coordinates
            FIELD_CHOSEN.active = True  # activates field to be marked
            if FIELD_CHOSEN.figure_team == constants.TURN:  # checks if figure on chosen field belongs to the team whichs turn it is
                game_mechanics.mark_move_pattern(FIELD_CHOSEN, constants.BOARD)  # shows possible moves for the chosen figure
                constants.MOVE = True  # toggles MOVE-MODE so next click will be either a move or chosing another friendly figure

    if pygame.mouse.get_pressed()[0] and constants.MOVE == True:
        game_mechanics.mark_move_pattern(FIELD_CHOSEN,constants.BOARD)  # remarks pattern because it is being reseted every click and the markers are needed to allow only possible moves
        FIELD_MOVE = constants.BOARD.fields[basic_functions.mouse_coordinates_to_field()[1]][basic_functions.mouse_coordinates_to_field()[0]]  # saves coordinates of for move chosen field

        if FIELD_MOVE.figure_team != constants.TURN and FIELD_MOVE.active:  # moves figure if field is empthy or occupied by enemy, only moves on marked fields are possible
            game_mechanics.check_for_draw()
            game_mechanics.valid_ai_move(FIELD_CHOSEN, FIELD_MOVE)
            game_mechanics.move_dead_figures(FIELD_MOVE)
            game_mechanics.replace_figure(FIELD_CHOSEN, FIELD_MOVE)
            game_mechanics.check_for_chess()
            constants.BOARD = game_mechanics.choose_figure(constants.BOARD, 0)
            in_turn = False



        else:  # if a friendly figure is selected
            game_mechanics.reset_markers()  # resets move pattern of previously picked figure
            FIELD_CHOSEN = constants.BOARD.fields[basic_functions.mouse_coordinates_to_field()[1]][basic_functions.mouse_coordinates_to_field()[0]]  # checks which coordinates were clicked and converts them in field coordinates
            FIELD_CHOSEN.active = True  # activates field to be marked
            if FIELD_CHOSEN.figure_team == constants.TURN:  # checks if figure on chosen field belongs to the team whichs turn it is
                game_mechanics.mark_move_pattern(FIELD_CHOSEN, constants.BOARD)  # shows possible moves for the chosen figure
                constants.MOVE = True  # toggles MOVE-MODE so next click will be either a move or chosing another friendly figure
            else:
                constants.MOVE = False
