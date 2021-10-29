from sys import exit
from pieces import *
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

# Colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (210, 100, 25)

# Height of the board = 8 * height of a single cell 
WIDTH = HEIGHT = 8 * 80

font = "Eight-Bit Madness.ttf"
menu_font = pygame.font.Font(font, 70)

def menu(screen):
    X, Y = 190, 230 # Coordinates of the chess logo
    button_x, buttton_y = X + 60, Y + 150 # Co-ordinates of the play button
    rect_big = pygame.Rect(X+50, Y+140, 150, 60) # Rect for outline rectangle of button in normal conditions
    rect_small = pygame.Rect(X+55, Y+145, 140, 50) # Rect for outline rectangle of button when mouse hovers over it
    border_width = 3
    
    title = pygame.image.load("Chess.png")
    play_button = menu_font.render("Play", True, BLACK)
    
    while True:

        # Event loop
        for event in pygame.event.get():
            # Close the window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(rect_big, event.pos):
                    return
        
        screen.fill(WHITE)
        screen.blit(title, (X, Y))
        if pygame.Rect.collidepoint(rect_big, pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BLACK, rect_small, border_width)
        else:
            pygame.draw.rect(screen, BLACK, rect_big, border_width)
        screen.blit(play_button, (button_x, buttton_y))

        pygame.display.update()
    return

def draw_board(screen):
    for i in range(0, WIDTH, 80):
        for j in range(0, HEIGHT, 80):
            if ((i + j) / 80) % 2 == 0:
                pygame.draw.rect(screen, WHITE, (i, j, 80, 80))
            else:
                pygame.draw.rect(screen, BROWN, (i, j, 80, 80))  

def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    icon = pygame.image.load("chess_icon.ico")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    FPS = 120

    menu(screen)

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
        clock.tick(FPS)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if a piece  exists at that location
                if isinstance(board[mouse_y // 80][mouse_x // 80], Piece):
                    if board[mouse_y // 80][mouse_x // 80].color == turn_color[turn % 2]:
                        board[mouse_y // 80][mouse_x // 80].selected = True
                        prev_x, prev_y = mouse_x // 80, mouse_y // 80
                        try:
                            board[mouse_y // 80][mouse_x // 80].generate_possible_moves(prev_x, prev_y, board)
                        except Exception as e:
                            # For debugging
                            print(e) 
            
            if event.type == pygame.MOUSEBUTTONUP:
                # Do the following ony if a valid piece is being moved
                if moving_piece:
                    
                    # If the position of the piece hasn't changed then don't count the move
                    if moving_piece.x == prev_x and moving_piece.y == prev_y:
                        board[mouse_y // 80][mouse_x // 80].selected = False
                    else:
                        # Check if piece has moved to a valid cell
                        if moving_piece.move_is_valid(prev_x, prev_y, board):
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
                        else:
                            moving_piece.x, moving_piece.y = prev_x, prev_y
                            board[moving_piece.y][moving_piece.x].selected = False
                            moving_piece = None
        
        # Drawing the board tiles first
        draw_board(screen)
        
        # Drawing the pieces
        for row in board:
            for cell in row:
                if isinstance(cell, Piece):
                    # Draw the moving piece after all the other pieces
                    if cell.selected:
                        cell.move()
                        moving_piece = cell
                        continue
                    cell.draw(screen)
        
        # Draw the moving piece last so that it appears in front of other pieces
        if moving_piece:
            moving_piece.draw(screen)

        pygame.display.update()

main()