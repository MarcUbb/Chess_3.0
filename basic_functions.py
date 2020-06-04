import constants
import classes

import pygame
import math


def change_turn():
    if constants.TURN == 1:
        constants.TURN = 2
    else:
        constants.TURN = 1

def reset_game():
    constants.BOARD = classes.Board(constants.START_POS, 0)
    constants.BOARD_DEAD = classes.Board(constants.DEAD_POS, 8)
    constants.TURN = 1
    constants.CHECK = 0
    constants.RUNNING = True

    constants.MOVES = 0
    constants.ROUND_COUNT += 1


def mouse_coordinates_to_field():
    if pygame.mouse.get_pos()[0] > 700 or pygame.mouse.get_pos()[1] > 700:
        return 8,7
    else:
        return int(math.floor(float(pygame.mouse.get_pos()[0])/100.0)), int(math.floor(float(pygame.mouse.get_pos()[1])/100.0))


def draw_window():
    constants.SCREEN.fill(constants.BACKGROUND)
    constants.SCREEN.blit(pygame.image.load( "images\\board.png" ), (0, 0))

    for i in constants.BOARD.fields:
        for f in i:
            if f.active:
                pygame.draw.rect(constants.SCREEN, constants.MARKER_COLOR,(f.pos_x*constants.FIELD_SIZE, f.pos_y*constants.FIELD_SIZE, constants.FIELD_SIZE, constants.FIELD_SIZE))
            if f.figure_team == 1:
                if f.figure_type == 1:
                    constants.SCREEN.blit(pygame.image.load( "images\white_pawn.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 2:
                    constants.SCREEN.blit(pygame.image.load( "images\white_rook.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 3:
                    constants.SCREEN.blit(pygame.image.load( "images\white_knight.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 4:
                    constants.SCREEN.blit(pygame.image.load( "images\white_bishop.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 5:
                    constants.SCREEN.blit(pygame.image.load( "images\white_queen.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 6:
                    constants.SCREEN.blit(pygame.image.load( "images\white_king.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))

            elif f.figure_team == 2:
                if f.figure_type == 1:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_pawn.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 2:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_rook.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 3:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_knight.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 4:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_bishop.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 5:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_queen.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 6:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_king.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))

    for i in constants.BOARD_DEAD.fields:
        for f in i:
            if f.active:
                pygame.draw.rect(constants.SCREEN, constants.MARKER_COLOR, (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE, constants.FIELD_SIZE, constants.FIELD_SIZE))
            if f.figure_team == 1:
                if f.figure_type == 1:
                    constants.SCREEN.blit(pygame.image.load( "images\white_pawn.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 2:
                    constants.SCREEN.blit(pygame.image.load( "images\white_rook.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 3:
                    constants.SCREEN.blit(pygame.image.load( "images\white_knight.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 4:
                    constants.SCREEN.blit(pygame.image.load( "images\white_bishop.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 5:
                    constants.SCREEN.blit(pygame.image.load( "images\white_queen.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 6:
                    constants.SCREEN.blit(pygame.image.load( "images\white_king.png"),(f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))

            elif f.figure_team == 2:
                if f.figure_type == 1:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_pawn.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 2:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_rook.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 3:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_knight.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 4:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_bishop.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 5:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_queen.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))
                elif f.figure_type == 6:
                    constants.SCREEN.blit(pygame.image.load( "images\\black_king.png"), (f.pos_x * constants.FIELD_SIZE, f.pos_y * constants.FIELD_SIZE))

    if constants.CHECK == 0:
        text = ""
    elif constants.CHECK == 1:
        text = "Black King is under attack!"
    elif constants.CHECK == 2:
        text = "White King is under attack!"
    elif constants.CHECK == 3:
        text = "Black won!"
    elif constants.CHECK == 4:
        text = "White won!"

    myfont = pygame.font.SysFont("monospace", 50)
    label = myfont.render(text, 1, (0, 0, 0))
    constants.SCREEN.blit(label, (0, 800))

    pygame.display.update()

