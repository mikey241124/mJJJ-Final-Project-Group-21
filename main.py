import sys
import pygame as pygame
#import self as self
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku

import sudoku_generator
from board import Board


class Main:
    WIDTH = 1200
    HEIGHT = 800

    def draw_game_start(screen):
        WIDTH = 1200
        HEIGHT = 800

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (50, 50, 50)
        CREAM = (255, 253, 208)

        title_font = pygame.font.Font(None, 150)
        button_font = pygame.font.Font(None, 90)

        screen.fill(CREAM)

        title_surface = title_font.render("Sudoku", 0, BLACK)
        title_rectangle = title_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 230))
        screen.blit(title_surface, title_rectangle)

        easy_surface = button_font.render("Easy", 0, BLACK)
        easy_rectangle = easy_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 40))
        screen.blit(easy_surface, easy_rectangle)

        medium_surface = button_font.render("Medium", 0, BLACK)
        medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
        screen.blit(medium_surface, medium_rectangle)

        hard_surface = button_font.render("Hard", 0, BLACK)
        hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 180))
        screen.blit(hard_surface, hard_rectangle)


        menu_runnning = True
        game_type = ''
        while menu_runnning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rectangle.collidepoint(event.pos):
                        menu_runnning = False
                        game_type = "easy"
                        print("Touching Easy Button")
                    elif medium_rectangle.collidepoint(event.pos):
                        menu_runnning = False
                        game_type = "medium"
                        print("Touching Medium Button")
                    elif hard_rectangle.collidepoint(event.pos):
                        menu_runnning = False
                        game_type = "hard"
                        print("Touching Hard Button")
            pygame.display.update()
            if menu_runnning == False:
                return game_type

    def run_game(screen, game_type):
        print(game_type)

        lost = False
        won = False

        #Get the Sudoku Board from Sudoku Generator
        # Generate an Easy Board
        if game_type == 'easy':
            board_list = generate_sudoku(9, 30)
        # Generate a Medium Board
        elif game_type == 'medium':
            board_list = generate_sudoku(9, 40)
        # Generate a Hard Board
        elif game_type == 'hard':
            board_list = generate_sudoku(9, 50)

        print(board_list)


        WIDTH = 1200
        HEIGHT = 800

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (50, 50, 50)
        CREAM = (255, 253, 208)

        title_font = pygame.font.Font(None, 150)
        button_font = pygame.font.Font(None, 90)
        number_font = pygame.font.SysFont('Comic Sans MS', 35)

        screen.fill(CREAM)

        pygame.draw.line(screen, BLACK, (300, 100), (300, 700), 4)
        pygame.draw.line(screen, BLACK, (900, 100), (900, 700), 4)
        pygame.draw.line(screen, BLACK, (300, 100), (900, 100), 4)
        pygame.draw.line(screen, BLACK, (300, 700), (900, 700), 4)

        # Thick columns
        pygame.draw.line(screen, BLACK, (500, 100), (500, 700), 4)
        pygame.draw.line(screen, BLACK, (700, 100), (700, 700), 4)
        # Thick rows
        pygame.draw.line(screen, BLACK, (300, 300), (900, 300), 4)
        pygame.draw.line(screen, BLACK, (300, 500), (900, 500), 4)

        # Thin columns
        pygame.draw.line(screen, BLACK, (366, 100), (366, 700), 2)
        pygame.draw.line(screen, BLACK, (433, 100), (433, 700), 2)
        pygame.draw.line(screen, BLACK, (566, 100), (566, 700), 2)
        pygame.draw.line(screen, BLACK, (633, 100), (633, 700), 2)
        pygame.draw.line(screen, BLACK, (766, 100), (766, 700), 2)
        pygame.draw.line(screen, BLACK, (833, 100), (833, 700), 2)

        # Thin rows
        pygame.draw.line(screen, BLACK, (300, 166), (900, 166), 2)
        pygame.draw.line(screen, BLACK, (300, 233), (900, 233), 2)
        pygame.draw.line(screen, BLACK, (300, 366), (900, 366), 2)
        pygame.draw.line(screen, BLACK, (300, 433), (900, 433), 2)
        pygame.draw.line(screen, BLACK, (300, 566), (900, 566), 2)
        pygame.draw.line(screen, BLACK, (300, 633), (900, 633), 2)

        game_runnning = True

        #Put the Sudoku Board onto the Pygame Board
        silly = number_font.render("2", True, (0, 0, 0))
        #screen.blit(silly, (456, 110))
        for i in range(0, len(board_list)):
            for j in range(0, len(board_list[0])):
                if board_list[i][j] != 0:
                    value = number_font.render(str(board_list[i][j]), True, (0, 0, 0))
                    screen.blit(value, ((j+1) *66 +258, (i+1)*66 + 47))

        while game_runnning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Mouse clicked.")
            pygame.display.update()
            if game_runnning == False:
                pass

            if lost:
                screen.fill(CREAM)

                lost_surface = title_font.render("Game Over :(", 0, BLACK)
                lost_rectangle = lost_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
                screen.blit(lost_surface, lost_rectangle)

                restart_surface = button_font.render("RESTART", 0, BLACK)
                restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
                screen.blit(restart_surface, restart_rectangle)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rectangle.collidepoint(event.pos):
                            #restarting the game goes here

            if won:
                screen.fill(CREAM)

                won_surface = title_font.render("Game Won!", 0, BLACK)
                won_rectangle = won_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
                screen.blit(won_surface, won_rectangle)

                exit_surface = button_font.render("EXIT", 0, BLACK)
                exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
                screen.blit(exit_surface, exit_rectangle)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exit_rectangle.collidepoint(event.pos):
                            sys.exit()


    if __name__ == '__main__':
        game_over = False
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")

        game_type = draw_game_start(screen)

        run_game(screen, game_type)
        board = Board(WIDTH, HEIGHT, screen, game_type)
        board.draw()

