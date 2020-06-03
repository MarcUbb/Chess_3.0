from game_mechanics import *
from classes import *
import random
import copy


def ai_function(board, team, ai_messages):

    king_pos_x = 0
    king_pos_y = 0

    c = 0
    for i in board.fields:  # gets coordinates of king of the team which turn it is and saves them
        for f in i:
            if f.figure_team == team and f.figure_type == 6:
                king_pos_x = f.pos_x
                king_pos_y = f.pos_y
                c = 1
                break
        if c == 1:
            break

    king_moves = []                                                     #saves all possible moves for king

    mark_move_pattern(board.fields[king_pos_y][king_pos_x], board)      #fills array with fields that can be moved on
    for i in board.fields:
        for f in i:
            if f.active == True:
                king_moves.append(f)
    reset_specific_markers(board)

    for i in board.fields:                                              #activates all move_patterns for enemy team
        for f in i:
            if f.figure_team != team:
                mark_move_pattern(f, board)

    if board.fields[king_pos_y][king_pos_x].active == True:
        for i in board.fields:
            for f in i:
                for x in king_moves:
                    if x == f and f. active == False:
                        return board.fields[king_pos_y][king_pos_x], f, [5] #if theres a field where the king can go return the field
    reset_specific_markers(board)

#############################################################

    movable_figures = []                                                #creates array for movable figures

    for m in board.fields:                                              #fills array with fields where movable figures are
        for f in m:
            if f.figure_team == team: # and f.figure_type != 6:
                mark_move_pattern(f,board)
                counter = 0
                for n in board.fields:
                    for b in n:
                        if b.active == True:
                            counter += 1
                if counter > 1:
                    movable_figures.append(f)
                reset_specific_markers(board)

    moves = []                   # creates array for possible moves for movable figures

    i = 0
    while i < len(movable_figures):
        moves.append([])
        move_counter = 0
        mark_move_pattern(movable_figures[i], board)
        for m in board.fields:
            for f in m:
                if f.active == True and f.active != movable_figures[i]:
                    moves[i].append([f])
                    if f.figure_type == 0:
                        moves[i][move_counter].append(0)
                    elif f.figure_type == 1:
                        moves[i][move_counter].append(1)
                    elif f.figure_type == 2:
                        moves[i][move_counter].append(5)
                    elif f.figure_type == 3:
                        moves[i][move_counter].append(3)
                    elif f.figure_type == 4:
                        moves[i][move_counter].append(3)
                    elif f.figure_type == 5:
                        moves[i][move_counter].append(9)
                    elif f.figure_type == 6:
                        moves[i][move_counter].append(10)
                    move_counter += 1
        reset_specific_markers(board)
        i += 1


    reset_specific_markers(board)
    i = 0
    while i < len(moves):                                                   # gives every move that checks the ai the value -1
        j = 0
        while j < len(moves[i]):
            test_board = copy.deepcopy(board)
            test_board.fields[moves[i][j][0].pos_y][moves[i][j][0].pos_x].figure_moved = True
            test_board.fields[moves[i][j][0].pos_y][moves[i][j][0].pos_x].figure_team = team
            test_board.fields[moves[i][j][0].pos_y][moves[i][j][0].pos_x].figure_type = moves[i][j][0].figure_type
            test_board.fields[moves[i][j][0].pos_y][moves[i][j][0].pos_x].move_pattern = pattern_generator(moves[i][j][0].figure_type, moves[i][j][0].figure_team)  # also the pattern has to be raplaced since we dont reinitialize the field

            test_board.fields[movable_figures[i].pos_y][movable_figures[i].pos_x].figure_team = 0
            test_board.fields[movable_figures[i].pos_y][movable_figures[i].pos_x].figure_type = 0
            test_board.fields[movable_figures[i].pos_y][movable_figures[i].pos_x].move_pattern = 0

            for x in test_board.fields:
                for f in x:
                    if f.figure_team != team:
                        mark_move_pattern(f,test_board)

            if test_board.fields[king_pos_y][king_pos_x].active == True:
                moves[i][j][1] = -1
            reset_specific_markers(test_board)
            j += 1
        i += 1




    if len(movable_figures) == 0 or len(moves) == 0:
        return 0,0,[5]


    max_value = -1
    field_chosen = 0
    field_move = 0
    i = 0
    while i < len(moves):
        j = 0
        while j < len(moves[i]):
            if moves[i][j][1] >= max_value:
                max_value = moves[i][j][1]
                field_chosen = movable_figures[i]
                field_move = moves[i][j][0]
            j += 1
        i += 1

    if max_value == 0:
        x = random.randint(0, len(movable_figures)-1)
        field_chosen = movable_figures[x]
        y = random.randint(0, len(moves[x])-1)
        field_move = moves[x][y][0]

    return field_chosen, field_move, [5]