import sys
import pygame as pygame

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
        title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 230))
        screen.blit(title_surface, title_rectangle)

        game_runnning = True
        game_type = ''
        while game_runnning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            pygame.display.update()
            if game_runnning == False:
                pass


    if __name__ == '__main__':
        game_over = False

        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")

        game_type = draw_game_start(screen)

        #run_game(screen, game_type)
        board = Board(WIDTH, HEIGHT, screen, game_type)
        board.draw
