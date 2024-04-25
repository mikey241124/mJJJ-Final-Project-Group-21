import pygame

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        #Constructor for the cell class

    def set_cell_value(self, value):
        self.value = value
        return self.value
        #setter for this cell's value

    def set_sketched_value(self, value):
        self.value = value
        return self.value
        #setter for this sells sketched value

    def draw(self):
        pygame.draw.rect(self.screen, (200, 0, 0), (60, 60, 60, 60,), width=8,)
        #Draws this cell, along with the value inside it.
        #If this cell has a nonzero value, that value is displayed.
        #Otherwise, no value is displayed in the cell.
        #The cell is outlined red if it is currently selected.