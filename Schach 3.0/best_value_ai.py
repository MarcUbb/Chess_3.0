from game_mechanics import *
import random


def ai_function(board, team, ai_messages):

    movable_figures = []                                                #creates array for movable figures

    for m in board.fields:                                              #fills array with fields where movable figures are
        for f in m:
            if f.figure_team == team:
                mark_move_pattern(f,board)
                counter = 0
                for n in board.fields:
                    for b in n:
                        if b.active == True:
                            counter += 1
                if counter > 1:
                    movable_figures.append(f)
                reset_specific_markers(board)

    values = []                   # creates array for possible moves for movable figures

    i = 0
    while i < len(movable_figures):
        values.append([])
        move_counter = 0
        mark_move_pattern(movable_figures[i], board)
        for m in board.fields:
            for f in m:
                if f.active == True and f.active != movable_figures[i]:
                    values[i].append([f])
                    if f.figure_type == 0:
                        values[i][move_counter].append(0)
                    elif f.figure_type == 1:
                        values[i][move_counter].append(1)
                    elif f.figure_type == 2:
                        values[i][move_counter].append(5)
                    elif f.figure_type == 3:
                        values[i][move_counter].append(3)
                    elif f.figure_type == 4:
                        values[i][move_counter].append(3)
                    elif f.figure_type == 5:
                        values[i][move_counter].append(9)
                    elif f.figure_type == 6:
                        values[i][move_counter].append(10)
                    move_counter += 1
        reset_specific_markers(board)
        i += 1




    if len(movable_figures) == 0 or len(values) == 0:
        return 0,0,[5]


    max_value = 0
    field_chosen = 0
    field_move = 0
    i = 0
    while i < len(values):
        j = 0
        while j < len(values[i]):
            if values[i][j][1] > max_value:
                max_value = values[i][j][1]
                field_chosen = movable_figures[i]
                field_move = values[i][j][0]
            j += 1
        i += 1

    if max_value == 0:
        x = random.randint(0, len(movable_figures)-1)
        field_chosen = movable_figures[x]
        y = random.randint(0, len(values[x])-1)
        field_move = values[x][y][0]

    return field_chosen, field_move, [5]