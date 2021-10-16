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
    
    # Returns if move is valid
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if abs(x - prev_x) <= 1 and abs(y - prev_y) <= 1:
            # If piece hasnt moved then dont register it
            if x == prev_x or y == prev_y:
                return False
            # If a piece exists at destination spot check
            # if it is an enemy piece
            elif isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
                    return True
            else:
                self.x, self.y = x, y
                return True
    
    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / 80, y / 80

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
    
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid 
        if abs(x - prev_x) == abs(y - prev_y):
            # Check if destination square has enemy piece
            if x == prev_x or y == prev_y:
                return False
            elif isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
                    return True
            # No movement
            else:
                self.x, self.y = x, y
                return True

    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / 80, y / 80

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
    
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if abs(x - prev_x) == 2 and abs(y - prev_y) == 1:
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
                    return True
            else:
                self.x, self.y = x, y
                return True
        elif abs(x - prev_x) == 1 and abs(y - prev_y) == 2:
            if isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
                    return True
            else:
                self.x, self.y = x, y
                return True
        # No movement
        elif x == prev_x and y == prev_y:
            self.x, self.y = x, y
            return False

    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / 80, y / 80

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
    
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if abs(x - prev_x) == abs(y - prev_y):
            self.x, self.y = x, y
            if x == prev_x or y == prev_y:
                return False
            elif isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
                    return True
            else:
                self.x, self.y = x, y
                return True
    
    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / 80, y / 80

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
    
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid        
        if x == prev_x or y == prev_y:
            if x == prev_x and y == prev_y:
                return False   
            elif isinstance(board[y][x], Piece):
                if board[y][x].color != self.color or board[y][x] == self:
                    self.x, self.y = x, y
                    return True         
            else:
                self.x, self.y = x, y
                return True

    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / 80, y / 80

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
    
    def move_is_valid(self, prev_x, prev_y, board):
        # Get current mouse position and convert to board indices
        x, y = pygame.mouse.get_pos()
        x, y = x // 80, y // 80

        # Check if the move is valid
        if self.color == "b": # Logic for black pieces
            if self.has_moved:
                if x == prev_x:
                    # Pawn can move only one square
                    if y - prev_y == 1:
                        self.x, self.y = x, y
                        return True 
                # Pawns can kill diagonally
                elif y - prev_y == 1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                    if board[y][x].color == "w":
                        self.x, self.y = x, y
                        return True
            else:
                # Pawn can move one or two squares for the first move
                if y - prev_y == 2 or y - prev_y == 1:
                    if x == prev_x:
                        self.x, self.y = x, y
                        return True
                    # Pawns can kill diagonally
                    elif y - prev_y == 1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                        if board[y][x].color == "w":
                            self.x, self.y = x, y
                            return True
        elif self.color == "w":
            if self.has_moved:
                if x == prev_x:
                    if y - prev_y == -1:
                        self.x, self.y = x, y 
                        return True   
                # Pawn can kill diagonally on either side
                elif y - prev_y == -1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                    if board[y][x].color == "b":
                        self.x, self.y = x, y
                        return True
            else:
                # Pawn can move one or two squares for the first move
                if y - prev_y == -1 or y - prev_y == -2:
                    if x == prev_x:
                        self.x, self.y = x, y
                        return True
                    # Pawn can kill diagonally
                    elif y - prev_y == -1 and abs(x - prev_x) == 1 and isinstance(board[y][x], Piece):
                        if board[y][x].color == "b":
                            self.x, self.y = x, y  
                            return True
            return False

    def move(self):
        x, y = pygame.mouse.get_pos()
        x, y = x - 40, y - 40
        self.x, self.y = x / 80, y / 80