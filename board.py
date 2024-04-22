class Board:

    def __init__(self, width, height, screen, difficulty):
        pass
        #constructor for the board class
        #screen is a window from pygame
        #difficulty is to select easy medium or hard motherfucker
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        pass
        #draws outline of sudoku grid, bold lines to seperate 3x3 blocks
        #draws every cell on board

    def select(self, row, col):
        pass
        #marks the cell (at row,col) as the current selected cell
        #once a cell has been selected, the user can edit its value or sketched value

    def click(self, x, y):
        pass
        #IF A TUPLE OF (X,Y) COORDINATES IS WITHIN THE DISPLAYED BOARD THIS FUNCTION RETURNS A TUPLE OF THE (ROW, COL)
        #OF THE CELL WHICH WAS CLICKED. OTHERWISE THIS FUNCTION RETURNS NONE.

    def clear(self):
        pass
        #clear the value cell, note that the user can only return the cell values and sketched value that are filled]
        #by themselves

    def sketch(self, value):
        pass
        #Sets the sketched value of the current selected cell equal to user entered value
        #it will be displayed at the top left corner of the cell using the draw() function

    def place_number(self, value):
        pass
        #Updates the underlying 2D board with the values in all cells

    def find_empty(self):
        pass
        #Finds an empty cell and returns its row and col as a tuple (x, y).

    def check_board(self):
        pass
        #Check whether the sudoku board is solved correctly
