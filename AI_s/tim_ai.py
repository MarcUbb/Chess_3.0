from AI_s.ai_helper_functions import *
import random
import evaluation

def ai_function(board, TEAM):

    if check_for_check(board, TEAM):
        print("Ohh ich bin schach du alter Schlawiner!")
        king = 0
        for i in board.fields:
            for j in i:    
                if j.figure_type == 6 and j.figure_team == TEAM:
                    king = j
        mark_move_pattern(king, board)
        possible_moves = []
        for i in board.fields:
            for f in i:
                if f.active == True:
                    possible_moves.append(king)
        figure_chosen = king
        if len(possible_moves) <= 0:
            return (0, 0, [0, TEAM])
        figure_move = possible_moves[random.randint(0, len(possible_moves)-1)]
        return(figure_chosen, figure_move, [0, 0])

    friendly_fields = []

    for i in board.fields:
        for f in i:
            if f.figure_team == TEAM:
                friendly_fields.append(f)


    movable_figures = []
    i = 0
    while i < len(friendly_fields):
        kill_counter = 0
        move_counter = 0                                    #counts how many moves each figure can do (1 = no moves)
        mark_move_pattern(friendly_fields[i], board)
        for c in board.fields:
            for f in c:
                if f.active == True:
                    move_counter += 1
                    if f.figure_team == TEAM - pow(-1, TEAM):
                        kill_counter += f.figure_type
        if move_counter >= 1:
            movable_figures.append((friendly_fields[i], kill_counter))
        reset_markers(board)
        i += 1

    figure_chosen = movable_figures[random.randint(0, len(movable_figures)-1)][0]

    for f in movable_figures:
        max_kill = 0
        if f[1] > max_kill:
            max_kill = f[1]
            figure_chosen = f[0]

    possible_moves = []

    mark_move_pattern(figure_chosen, board)
    for i in board.fields:
        for f in i:
            if f.active == True:
                possible_moves.append((f,f.figure_type))
    if len(possible_moves) <= 0:
        return(0, 0, [5, TEAM])    
    figure_move = possible_moves[random.randint(0, len(possible_moves)-1)][0]

    for i in possible_moves:
        max_value = 0
        if i[1] > max_value:
            max_value = i[1]
            figure_move = i[0]


    #evaluation.print_board()
    return(figure_chosen, figure_move, [5, 0])