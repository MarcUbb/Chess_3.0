from AI_s.ai_helper_functions import *
import random
import evaluation
import pygame



def translateValues(x):
    switch = {
        0: 0,
        1: 1,
        2: 5,
        3: 3,
        4: 3,
        5: 9,
        6: 12,
    }
    return switch.get(x)

def translateTypes1(x):
    switch = {
        0: " Weihnachtsbaum",
        1: " Bauer",
        2: " Turm",
        3: " Pferd",
        4: " Läufer",
        5: "e Dame",
        6: " König",
    }
    return switch.get(x)

def translateTypes2(x):
    switch = {
        0: "en Weihnachtsbaum",
        1: "en Bauern",
        2: "en Turm",
        3: " Pferd",
        4: "en Läufer",
        5: "e Dame",
        6: "en König",
    }
    return switch.get(x)

def ai_function(board, TEAM):

    if check_for_check(board, TEAM):
        print(" tim_ai: Ohh ich bin schach du alter Schlawiner!")
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
            return (king, board.fields[0][0] , [0, TEAM])
        figure_move = possible_moves[random.randint(0, len(possible_moves)-1)]
        return(figure_chosen, figure_move , [0, 0])

    friendly_fields = []

    for i in board.fields:
        for f in i:
            if f.figure_team == TEAM:
                friendly_fields.append(f)

    talk = random.randint(0,500)
    if talk == 0:
        print("Hmmm")
    elif talk == 1:
        print("puhh da muss ich aber länger nachdenken")
        pygame.time.wait(3000)
    elif talk == 2:
        print("Du hast irgendwas vor aber ich weiß noch nicht was!")
    elif talk == 3:
        print("Bist du sicher, dass du den Zug so stehen lassen willst? ;)")
    elif talk == 4:
        print("OHH...")
    elif talk == 5:
        print(">>Hust<< ... Entschuldigung")

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
                        kill_counter += translateValues(f.figure_type)
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
                possible_moves.append((f,translateValues(f.figure_type)))
    if len(possible_moves) <= 0:
        return(figure_chosen, board.fields[0][0], [5, TEAM])    
    figure_move = possible_moves[random.randint(0, len(possible_moves)-1)][0]
    max_value = 0
    for i in possible_moves:
        if i[1] > max_value:
            max_value = i[1]
            figure_move = i[0]


    #evaluation.print_board()
    if max_value > 0:
        if (random.randint(0,1)) == 0: 
            print("HAHA mein" + translateTypes1(board.fields[figure_chosen.pos_y][figure_chosen.pos_x].figure_type) + " F**** jetzt dein" + translateTypes2(board.fields[figure_move.pos_y][figure_move.pos_x].figure_type) + "!!")
        else:
            print("Musst wohl nächstes mal besser aufpassen auf dein" + translateTypes2(board.fields[figure_move.pos_y][figure_move.pos_x].figure_type) + "..." )
    return(figure_chosen, figure_move, [5, 0])

