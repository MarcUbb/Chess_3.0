import constants                        # import functions fromother files
import game_mechanics
import basic_functions

import pygame                           # import necessary library
import copy


#from best_value_ai import *             # import AI files
#from best_value_ai_with_check import *


def ai_move():
    if constants.GAMEMODE == 1 and constants.TURN != constants.AI_TURN: # looks if its AIs turn (only for gamemode 1)
        return 0                                                        #TODO can't that just be a "continue"?
    pygame.time.wait(constants.AI_DELAY)                                # short delay so AI moves become visible
    AI_MESSAGES = [0]
    if constants.TURN == 1 or (constants.GAMEMODE == 1 and constants.TURN == constants.AI_TURN):                                # AI which is used in gamemode 1
        constants.FIELD_CHOSEN, constants.FIELD_MOVE, AI_MESSAGES = constants.AI_1.ai_function(constants.BOARD, constants.TURN)
    elif constants.TURN == 2:                                                                                                   # 2nd AI
        constants.FIELD_CHOSEN, constants.FIELD_MOVE, AI_MESSAGES = constants.AI_2.ai_function(constants.BOARD, constants.TURN)

    game_mechanics.check_for_draw()                                                 # checks if the game drawed
    game_mechanics.valid_ai_move(constants.FIELD_CHOSEN, constants.FIELD_MOVE)                          # checks if the AIs move was valid
    game_mechanics.move_dead_figures(constants.FIELD_MOVE)                                    # moves killed figure on the dead figures board
    game_mechanics.replace_figure(constants.FIELD_CHOSEN, constants.FIELD_MOVE)                         # executes the move
    game_mechanics.check_for_chess()                                                # checks if somebody is in check or lost
    constants.BOARD = game_mechanics.choose_figure(constants.BOARD, AI_MESSAGES[0]) # AI chooses figure if pawn reaches end of board
    constants.MOVES += 1
    constants.TURN = 1 if constants.TURN == 2 else 2                                                            # counts how many moves have been done



def human_move():
    basic_functions.draw_window()

    if pygame.mouse.get_pressed()[0]:
        game_mechanics.reset_markers()
        if not constants.MOVE:
            constants.FIELD_CHOSEN = constants.BOARD.fields[basic_functions.mouse_coordinates_to_field()[1]][basic_functions.mouse_coordinates_to_field()[0]]  # checks which coordinates were clicked and converts them in field coordinates
            constants.FIELD_CHOSEN.active = True  # activates field to be marked
            if constants.FIELD_CHOSEN.figure_team == constants.TURN:  # checks if figure on chosen field belongs to the team whichs turn it is
                constants.MOVE = True  # toggles MOVE-MODE so next click will be either a move or chosing another friendly figure
        if constants.MOVE:
            game_mechanics.mark_move_pattern(constants.FIELD_CHOSEN, constants.BOARD)
            constants.FIELD_CHOSEN.active = True
            constants.FIELD_MOVE = constants.BOARD.fields[basic_functions.mouse_coordinates_to_field()[1]][basic_functions.mouse_coordinates_to_field()[0]]  # checks which coordinates were clicked and converts them in field coordinates
            if constants.FIELD_CHOSEN == constants.FIELD_MOVE:
                return
            elif not constants.FIELD_MOVE.active:
                constants.FIELD_CHOSEN = constants.BOARD.fields[basic_functions.mouse_coordinates_to_field()[1]][basic_functions.mouse_coordinates_to_field()[0]]
                return
            elif constants.FIELD_MOVE.active:
                game_mechanics.check_for_draw()
                game_mechanics.valid_ai_move(constants.FIELD_CHOSEN, constants.FIELD_MOVE)
                game_mechanics.move_dead_figures(constants.FIELD_MOVE)
                game_mechanics.replace_figure(constants.FIELD_CHOSEN, constants.FIELD_MOVE)
                game_mechanics.check_for_chess()
                constants.BOARD = game_mechanics.choose_figure(constants.BOARD, 0)
                constants.TURN = 1 if constants.TURN == 2 else 2
                constants.MOVE = False
