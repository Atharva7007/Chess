import pygame
pygame.init()

class Piece:
    """
    Parent class Piece contains the common attricbutes of all different pieces
    """
    def __init__(self, y, x, color):
        self.selected = False
        self.x, self.y = x, y
        self.color = color
        self.WIDTH, self.HEIGHT = 80, 80
        self.has_moved = False
    
    def check_diagonal(self, board):
        pass

    def check_col(self, board):
        pass

    def check_row(self, board):
        pass

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
        board.blit(self.img, (self.x * 80, self.y * 80))
    
    def move(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if abs(x - prev_x) <= 1 and abs(y - prev_y) <= 1:
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
            else:
                self.x, self.y = x, y
            self.x, self.y = x, y

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
        board.blit(self.img, (self.x * 80, self.y * 80))
    
    def move(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid 
        if x == prev_x or y == prev_y or abs(x - prev_x) == abs(y - prev_y):
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
            else:
                self.x, self.y = x, y

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
        board.blit(self.img, (self.x * 80, self.y * 80))
    
    def move(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if abs(x - prev_x) == 2 and abs(y - prev_y) == 1:
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
            else:
                self.x, self.y = x, y
        elif abs(x - prev_x) == 1 and abs(y - prev_y) == 2:
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
            else:
                self.x, self.y = x, y
        # No movement
        elif x == prev_x and y == prev_y:
            self.x, self.y = x, y

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
        board.blit(self.img, (self.x * 80, self.y * 80))
    
    def move(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if abs(x - prev_x) == abs(y - prev_y):
            self.x, self.y = x, y
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
            else:
                self.x, self.y = x, y

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
        board.blit(self.img, (self.x * 80, self.y * 80))
    
    def move(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if x == prev_x or y == prev_y:
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
            else:
                self.x, self.y = x, y

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
        board.blit(self.img, (self.x * 80, self.y * 80))
    
    def move(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if self.color == "b": # Logic for black pieces
            if self.has_moved:
                if x == prev_x:
                    if y - prev_y <= 1 and y - prev_y >=0:
                        self.x, self.y = x, y   
                # Pawns can kill diagonally
                elif y - prev_y == 1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                    if board[y][x].color == "w":
                        self.x, self.y = x, y
            else:
                # Pawn can move two squares for the first move
                if y - prev_y <= 2 and y - prev_y >= 0:
                    if x == prev_x:
                        self.x, self.y = x, y
                    # Pawns can kill diagonally
                    elif y - prev_y == 1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                        if board[y][x].color == "w":
                            self.x, self.y = x, y
        elif self.color == "w":
            if self.has_moved:
                if x == prev_x:
                    if y - prev_y == -1 or y - prev_y ==0:
                        self.x, self.y = x, y    
                # Pawn can kill diagonally
                elif y - prev_y == -1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                    if board[y][x].color == "b":
                        self.x, self.y = x, y
            else:
                # Pawn can move two squares for the first move
                if y - prev_y <= 0 and y - prev_y >= -2:
                    if x == prev_x:
                        self.x, self.y = x, y
                    # Pawn can kill diagonally
                    elif y - prev_y == -1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                        if board[y][x].color == "b":
                            self.x, self.y = x, y        
                              