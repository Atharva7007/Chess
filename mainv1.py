from sys import exit
from piecesv1 import *
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

def menu():
    return

def main():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BROWN = (180,100,25)

    # Height of the board = 8 * height of a single cell 
    WIDTH = HEIGHT = 8 * 80

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    piece_drop = pygame.mixer.Sound("piece_drop.wav")
    turn_color = ["w", "b"]
    turn = 0

    board = [
    [Rook(0, 0, "b"), Knight(0, 1, "b"), Bishop(0, 2, "b"), Queen(0, 3, "b"), King(0, 4, "b"), Bishop(0, 5, "b"), Knight(0, 6, "b"), Rook(0, 7, "b")],
    [Pawn(1, 0, "b"), Pawn(1, 1, "b"), Pawn(1, 2, "b"), Pawn(1, 3, "b"), Pawn(1, 4, "b"), Pawn(1, 5, "b"), Pawn(1, 6, "b"), Pawn(1, 7, "b")],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    [Pawn(6, 0, "w"), Pawn(6, 1, "w"), Pawn(6, 2, "w"), Pawn(6, 3, "w"), Pawn(6, 4, "w"), Pawn(6, 5, "w"), Pawn(6, 6, "w"), Pawn(6, 7, "w")],
    [Rook(7, 0, "w"), Knight(7, 1, "w"), Bishop(7, 2, "w"), Queen(7, 3, "w"), King(7, 4, "w"), Bishop(7, 5, "w"), Knight(7, 6, "w"), Rook(7, 7, "w")]
    ]

    moving_piece = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if isinstance(board[mouse_y // 80][mouse_x // 80], Piece):
                    if board[mouse_y // 80][mouse_x // 80].color == turn_color[turn % 2]:
                        board[mouse_y // 80][mouse_x // 80].selected = True
                        prev_x, prev_y = mouse_x // 80, mouse_y // 80
            
            if event.type == pygame.MOUSEBUTTONUP:
                # Do the following ony if a valid piece is being moved
                if moving_piece:
                    
                    # If the position of the piece hasn't changed then don't count the move
                    if moving_piece.x == prev_x and moving_piece.y == prev_y:
                        board[mouse_y // 80][mouse_x // 80].selected = False
                    else:
                        # Replace the old cell of moving piece with a blank cell 
                        board[prev_y][prev_x] = "__"
                        
                        # Play the sound of the piece being dropped
                        piece_drop.play()
                        
                        # Drop the piece at the final location
                        board[moving_piece.y][moving_piece.x] = moving_piece
                        board[moving_piece.y][moving_piece.x].selected = False
                        board[moving_piece.y][moving_piece.x].has_moved = True
                        moving_piece = None
                        turn += 1
        
        # Drawing the board tiles first
        for i in range(0, WIDTH, 80):
            for j in range(0, HEIGHT, 80):
                if ((i + j) / 80) % 2 == 0:
                    pygame.draw.rect(screen, WHITE, (i, j, 80, 80))
                else:
                    pygame.draw.rect(screen, BROWN, (i, j, 80, 80))   
        # Drawing the pieces
        for row in board:
            for cell in row:
                if isinstance(cell, Piece):
                    cell.draw(screen)
                    if cell.selected:
                        cell.move(prev_x, prev_y, board)
                        moving_piece = cell

        pygame.display.update()

main()