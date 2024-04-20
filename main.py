import random
from tkinter import Label, Tk, Canvas, ALL


class Main:
    if __name__ == '__main__':
        # gamestate 0, 1, 2 are main menu, game menu, end screen
        gameState = 0

        gameWidth = 1000
        gameHeight = 800
        window = Tk()
        window.title('Sudoku Game')
        window.resizable(False, False)
        canvas = Canvas(window, bg='#000000', height=gameHeight, width=gameWidth)
        canvas.pack

        window.update()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#        window.bind('<Left>', lambda event: change_direction('left'))
#        window.bind('<Up>', lambda event: change_direction('up'))
#        window.bind('<Right>', lambda event: change_direction('right'))
#        window.bind('<Down>', lambda event: change_direction('down'))

        while True:
            if gameState == 0:
                pass
            elif gameState == 1:
                pass
            elif gameState == 2:
                pass
