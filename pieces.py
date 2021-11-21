import pygame
pygame.init()
CELL_DIM = 70
class Piece:
    """
    Parent class Piece contains the attributes that are common for all pieces
    """
    def __init__(self, y, x, color):
        self.selected = False
        self.x, self.y = x, y
        self.color = color
        self.WIDTH, self.HEIGHT = CELL_DIM, CELL_DIM
        self.has_moved = False
        self.possible_moves = []
    
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // CELL_DIM, y // CELL_DIM

        # Check if the move is valid
        if (x, y) in self.possible_moves:
            self.x, self.y = x, y
            return True
    
    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / CELL_DIM, y / CELL_DIM

class King(Piece):
    """
    King inherits from Piece since it is one (duh).
    Contains attributes of a King piece and valid moves, etc
    """
    def __init__(self, y, x, color):
        Piece.__init__(self, y, x, color)
        self.img = pygame.image.load("images/"+color+"K.png")
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))
    
    def draw(self, board):
        board.blit(self.img, (self.x * CELL_DIM, self.y * CELL_DIM))
    
    def generate_possible_moves(self, prev_x, prev_y, board):
        self.possible_moves = []
        
        # Add possible moves King can move to
        for x_pos in range(prev_x-1, prev_x+2):
            for y_pos in range(prev_y-1, prev_y+2):
                if x_pos >= 0 and x_pos <= 7: # Check if move is within board limits
                    if y_pos >= 0 and y_pos <= 7: # Check if move is within board limits
                        if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                            if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                                self.possible_moves.append((x_pos, y_pos))
                        else: # Free cell
                            self.possible_moves.append((x_pos, y_pos))
        print(self.possible_moves)

class Queen(Piece):
    """
    Queen inherits from Piece since it is one (duh).
    Contains attributes of a Queen and valid moves, etc
    """
    def __init__(self, y, x, color):
        Piece.__init__(self, y, x, color)
        self.img = pygame.image.load("images/"+color+"Q.png")
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))
    
    def draw(self, board):
        board.blit(self.img, (self.x * CELL_DIM, self.y * CELL_DIM))
    
    def generate_possible_moves(self, prev_x, prev_y, board):
        self.possible_moves = []
        
        # Add possible moves to the right of queen
        for x_pos in range(prev_x+1, 8):
            if isinstance(board[prev_y][x_pos], Piece):
                if board[prev_y][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, prev_y))
                break # Piece obstructs the path
            self.possible_moves.append((x_pos, prev_y))

        # Add possible moves to the left of queen
        for x_pos in range(prev_x-1, -1, -1):
            if isinstance(board[prev_y][x_pos], Piece):
                if board[prev_y][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, prev_y))
                break # Piece obstructs the path
            self.possible_moves.append((x_pos, prev_y))

        # Add possible moves below the queen
        for y_pos in range(prev_y+1, 8):
            if isinstance(board[y_pos][prev_x], Piece):
                if board[y_pos][prev_x].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x, y_pos))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x, y_pos))
        
        # Add possible moves above the queen
        for y_pos in range(prev_y-1, -1, -1):
            if isinstance(board[y_pos][prev_x], Piece):
                if board[y_pos][prev_x].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x, y_pos))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x, y_pos))    
        
        # Scan all diagonal cells top right
        #print(prev_x, prev_y)
        for i in range(1, min(8-prev_x, prev_y+1)):
            if isinstance(board[prev_y-i][prev_x+i], Piece):
                if board[prev_y-i][prev_x+i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x+i, prev_y-i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x+i, prev_y-i))
        
        # Scan all diagonal cells top left
        for i in range(1, min(prev_x, prev_y)+1):
            if isinstance(board[prev_y-i][prev_x-i], Piece):
                if board[prev_y-i][prev_x-i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x-i, prev_y-i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x-i, prev_y-i))

        # Scan all diagonal cells bottom left
        for i in range(1, min(prev_x+1, 8-prev_y)):
            if isinstance(board[prev_y+i][prev_x-i], Piece):
                if board[prev_y+i][prev_x-i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x-i, prev_y+i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x-i, prev_y+i))

        # Scan all diagonal cells bottom left
        for i in range(1, min(8-prev_x, 8-prev_y)):
            if isinstance(board[prev_y+i][prev_x+i], Piece):
                if board[prev_y+i][prev_x+i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x+i, prev_y+i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x+i, prev_y+i))

        #print(self.possible_moves)

class Knight(Piece):
    """
    Knight inherits from Piece since it is one (duh).
    Contains attributes of a Knight and valid moves, etc
    """
    def __init__(self, y, x, color):
        Piece.__init__(self, y, x, color)
        self.img = pygame.image.load("images/"+color+"N.png")
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))
    
    def draw(self, board):
        board.blit(self.img, (self.x * CELL_DIM, self.y * CELL_DIM))

    def generate_possible_moves(self, prev_x, prev_y, board):
        self.possible_moves = []
        
        # Add possible moves Knight can move to
        x_pos = prev_x + 2
        y_pos = prev_y + 1
        if x_pos < 8 and y_pos < 8:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))
        
        # Add possible moves Knight can move to
        x_pos = prev_x + 1
        y_pos = prev_y + 2
        if x_pos < 8 and y_pos < 8:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))
        
        # Add possible moves Knight can move to
        x_pos = prev_x - 1
        y_pos = prev_y + 2
        if x_pos >= 0 and y_pos < 8:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))
        
        # Add possible moves Knight can move to
        x_pos = prev_x + 2
        y_pos = prev_y - 1
        if x_pos < 8 and y_pos >= 0:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))

        # Add possible moves Knight can move to
        x_pos = prev_x + 1
        y_pos = prev_y - 2
        if x_pos < 8 and y_pos >= 0:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))

        # Add possible moves Knight can move to
        x_pos = prev_x - 2
        y_pos = prev_y + 1
        if x_pos >= 0 and y_pos < 8:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))

        # Add possible moves Knight can move to
        x_pos = prev_x - 2
        y_pos = prev_y - 1
        if x_pos >= 0 and y_pos >= 0:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))

        # Add possible moves Knight can move to
        x_pos = prev_x - 1
        y_pos = prev_y - 2
        if x_pos >= 0 and y_pos >= 0:
            if isinstance(board[y_pos][x_pos], Piece): # Check if a piece exists in that square
                if board[y_pos][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, y_pos))
            else:
                self.possible_moves.append((x_pos, y_pos))

        print(self.possible_moves)

class Bishop(Piece):
    """
    Bishop inherits from Piece since it is one (duh).
    Contains attributes of a Bishop and valid moves, etc
    """
    def __init__(self, y, x, color):
        Piece.__init__(self, y, x, color)
        self.img = pygame.image.load("images/"+color+"B.png")
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))

    def draw(self, board):
        board.blit(self.img, (self.x * CELL_DIM, self.y * CELL_DIM))
    
    def generate_possible_moves(self, prev_x, prev_y, board):
        self.possible_moves = []
        
        # Scan all diagonal cells top right
        #print(prev_x, prev_y)
        for i in range(1, min(8-prev_x, prev_y+1)):
            if isinstance(board[prev_y-i][prev_x+i], Piece):
                if board[prev_y-i][prev_x+i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x+i, prev_y-i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x+i, prev_y-i))
        
        # Scan all diagonal cells top left
        for i in range(1, min(prev_x, prev_y)+1):
            if isinstance(board[prev_y-i][prev_x-i], Piece):
                if board[prev_y-i][prev_x-i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x-i, prev_y-i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x-i, prev_y-i))

        # Scan all diagonal cells bottom left
        for i in range(1, min(prev_x+1, 8-prev_y)):
            if isinstance(board[prev_y+i][prev_x-i], Piece):
                if board[prev_y+i][prev_x-i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x-i, prev_y+i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x-i, prev_y+i))

        # Scan all diagonal cells bottom left
        for i in range(1, min(8-prev_x, 8-prev_y)):
            if isinstance(board[prev_y+i][prev_x+i], Piece):
                if board[prev_y+i][prev_x+i].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x+i, prev_y+i))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x+i, prev_y+i))

class Rook(Piece):
    """
    Rook inherits from Piece since it is one (duh).
    Contains attributes of a Rook and valid moves, etc
    """
    def __init__(self, y, x, color):
        Piece.__init__(self, y, x, color)
        self.img = pygame.image.load("images/"+color+"R.png")
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))

    def draw(self, board):
        board.blit(self.img, (self.x * CELL_DIM, self.y * CELL_DIM))

    def generate_possible_moves(self, prev_x, prev_y, board):
        self.possible_moves = []
        
        # Add possible moves to the right of rook
        for x_pos in range(prev_x+1, 8):
            if isinstance(board[prev_y][x_pos], Piece):
                if board[prev_y][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, prev_y))
                break # Piece obstructs the path
            self.possible_moves.append((x_pos, prev_y))

        # Add possible moves to the left of rook
        for x_pos in range(prev_x-1, -1, -1):
            if isinstance(board[prev_y][x_pos], Piece):
                if board[prev_y][x_pos].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((x_pos, prev_y))
                break # Piece obstructs the path
            self.possible_moves.append((x_pos, prev_y))

        # Add possible moves below the rook
        for y_pos in range(prev_y+1, 8):
            if isinstance(board[y_pos][prev_x], Piece):
                if board[y_pos][prev_x].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x, y_pos))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x, y_pos))
        
        # Add possible moves above the rook
        for y_pos in range(prev_y-1, -1, -1):
            if isinstance(board[y_pos][prev_x], Piece):
                if board[y_pos][prev_x].color != self.color: # Possible move if piece is enemy piece
                    self.possible_moves.append((prev_x, y_pos))
                break # Piece obstructs the path
            self.possible_moves.append((prev_x, y_pos))

class Pawn(Piece):
    """
    Pawn inherits from Piece since it is one (duh).
    Contains attributes of a Pawn and valid moves, etc
    """
    def __init__(self, y, x, color):
        Piece.__init__(self, y, x, color)
        self.img = pygame.image.load("images/"+color+"P.png")
        self.img = pygame.transform.scale(self.img, (self.WIDTH, self.HEIGHT))
        

    def draw(self, board):
        board.blit(self.img, (self.x * CELL_DIM, self.y * CELL_DIM))
    
    def generate_possible_moves(self, prev_x, prev_y, board):
        self.possible_moves = []
        
        # Check if the move is valid
        if self.color == "b": # Logic for black pieces
            # If pawn has moved then it can only move 1 square else it can also move 2 squares
            if self.has_moved:
                # If there is a piece in front of the pawn, it cannot go forward
                if not isinstance(board[prev_y + 1][prev_x], Piece):
                    self.possible_moves.append((prev_x, prev_y + 1))

            else:
                # Pawn hasnt moved so it can move 1 or 2 squares
                if not isinstance(board[prev_y + 1][prev_x], Piece): # 1 square ahead
                    self.possible_moves.append((prev_x, prev_y + 1))
                if not isinstance(board[prev_y + 2][prev_x], Piece): # 2 squares ahead
                    self.possible_moves.append((prev_x, prev_y + 2))
                
            # Pawns can kill diagonally
            if isinstance(board[prev_y + 1][prev_x + 1], Piece):
                if board[prev_y + 1][prev_x + 1].color == "w":
                    self.possible_moves.append((prev_x + 1, prev_y + 1))
            if isinstance(board[prev_y + 1][prev_x - 1], Piece):
                if board[prev_y + 1][prev_x - 1].color == "w":
                    self.possible_moves.append((prev_x - 1, prev_y + 1))

        elif self.color == "w":
            # If pawn has moved then it can only move 1 square else it can also move 2 squares
            if self.has_moved:
                # If there is a piece in front of the pawn, it cannot go forward
                if not isinstance(board[prev_y - 1][prev_x], Piece):
                    self.possible_moves.append((prev_x, prev_y - 1))

            else:
                # Pawn hasnt moved so it can move 1 or 2 squares
                if not isinstance(board[prev_y - 1][prev_x], Piece): # 1 square ahead
                    self.possible_moves.append((prev_x, prev_y - 1))
                if not isinstance(board[prev_y - 2][prev_x], Piece): # 2 squares ahead
                    self.possible_moves.append((prev_x, prev_y - 2))
                
            # Pawns can kill diagonally
            if isinstance(board[prev_y - 1][prev_x + 1], Piece):
                if board[prev_y - 1][prev_x + 1].color == "b":
                    self.possible_moves.append((prev_x + 1, prev_y - 1))
            if isinstance(board[prev_y - 1][prev_x - 1], Piece):
                if board[prev_y - 1][prev_x - 1].color == "b":
                    self.possible_moves.append((prev_x - 1, prev_y - 1))      
