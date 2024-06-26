import sys
import pygame as pygame
import keyboard
from copy import deepcopy
from sudoku_generator import generate_sudoku


class Main:
    WIDTH = 1200
    HEIGHT = 800

    def draw_game_start(screen):
        WIDTH = 1200
        HEIGHT = 800

        BLACK = (0, 0, 0)
        CREAM = (255, 253, 208)

        title_font = pygame.font.Font(None, 150)
        button_font = pygame.font.Font(None, 90)

        screen.fill(CREAM)

        title_surface = title_font.render("Sudoku", 0, BLACK)
        title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 230))
        screen.blit(title_surface, title_rectangle)

        easy_surface = button_font.render("Easy", 0, BLACK)
        easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(easy_surface, easy_rectangle)

        medium_surface = button_font.render("Medium", 0, BLACK)
        medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
        screen.blit(medium_surface, medium_rectangle)

        hard_surface = button_font.render("Hard", 0, BLACK)
        hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 180))
        screen.blit(hard_surface, hard_rectangle)

        menu_running = True
        game_type = ''

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rectangle.collidepoint(event.pos):
                        menu_running = False
                        game_type = "easy"
                        print("Touching Easy Button")
                    elif medium_rectangle.collidepoint(event.pos):
                        menu_running = False
                        game_type = "medium"
                        print("Touching Medium Button")
                    elif hard_rectangle.collidepoint(event.pos):
                        menu_running = False
                        game_type = "hard"
                        print("Touching Hard Button")
            pygame.display.update()
            if not menu_running:
                return game_type

    def run_game(screen, game_type):
        won = False

        # Get the Sudoku Board from Sudoku Generator
        # Generate an Easy Board
        if game_type == 'easy':
            solution, original_board, board_list = generate_sudoku(9, 30)
        # Generate a Medium Board
        elif game_type == 'medium':
            solution, original_board, board_list = generate_sudoku(9, 40)
        # Generate a Hard Board
        elif game_type == 'hard':
            solution, original_board, board_list = generate_sudoku(9, 50)

        WIDTH = 1200
        HEIGHT = 800

        BLACK = (0, 0, 0)
        CREAM = (255, 253, 208)
        BROWN = (165, 42, 42)

        title_font = pygame.font.Font(None, 150)
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

        game_running = True

        # Put the Initial Sudoku Board onto the Pygame Board
        for i in range(0, len(board_list)):
            for j in range(0, len(board_list[0])):
                if board_list[i][j] != 0:
                    value = number_font.render(str(board_list[i][j]), True, (0, 0, 0))
                    screen.blit(value, ((j + 1) * 66 + 258, (i + 1) * 66 + 47))

        # Display Reset, Restart, and Exit Buttons
        button_font = pygame.font.Font(None, 70)
        # Display Reset Button
        reset_button_data = button_font.render("RESET", 0, BROWN)
        reset_button = reset_button_data.get_rect(center=(145, 200))
        screen.blit(reset_button_data, reset_button)
        # Display Restart Button
        restart_button_data = button_font.render("RESTART", 0, BROWN)
        restart_button = restart_button_data.get_rect(center=(145, 400))
        screen.blit(restart_button_data, restart_button)
        # Display Exit Button
        exit_button_data = button_font.render("EXIT", 0, BROWN)
        exit_button = exit_button_data.get_rect(center=(145, 600))
        screen.blit(exit_button_data, exit_button)

        # Loop while the Sudoku game is ongoing
        counter = 0
        x_pos = 0
        y_pos = 0

        drawn_nums = []

        while game_running:
            counter = counter + 1
            is_board_full = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if buttons were pressed
                    if reset_button.collidepoint(event.pos):
                        board_list = deepcopy(original_board)
                        drawn_nums = []
                    elif restart_button.collidepoint(event.pos):
                        return 0
                    elif exit_button.collidepoint(event.pos):
                        sys.exit()

                    # get mouse position when clicking and draw a square
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    x = x - 300
                    y = y - 100
                    if 0 <= x <= 600:
                        if y >= 0 and y <= 600:
                            x = int(x / 66)
                            y = int(y / 66)
                            x_pos = x
                            y_pos = y

                if event.type == pygame.KEYDOWN:
                    # sees if an arrow key is pressed
                    if keyboard.is_pressed('left arrow'):
                        if x_pos > 0:
                            x_pos = x_pos - 1
                    if keyboard.is_pressed('up arrow'):
                        if y_pos > 0:
                            y_pos = y_pos - 1
                    if keyboard.is_pressed('right arrow'):
                        if x_pos < 8:
                            x_pos = x_pos + 1
                    if keyboard.is_pressed('down arrow'):
                        if y_pos < 8:
                            y_pos = y_pos + 1

                    # display sketch if space is valid
                    if board_list[y_pos][x_pos] == 0:
                        # check for user keyboard input
                        count = 0
                        if event.key == pygame.K_1:
                            temp_num = 1
                            # check if number already present in drawn_nums
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_2:
                            temp_num = 2
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_3:
                            temp_num = 3
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_4:
                            temp_num = 4
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_5:
                            temp_num = 5
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_6:
                            temp_num = 6
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_7:
                            temp_num = 7
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_8:
                            temp_num = 8
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])
                        elif event.key == pygame.K_9:
                            temp_num = 9
                            for i in range(len(drawn_nums)):
                                if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                    drawn_nums[i][2] = temp_num
                                    count += 1
                            if count < 1:
                                drawn_nums.append([x_pos, y_pos, temp_num])

                    # Check if user clicks enter key
                    if keyboard.is_pressed('enter'):
                        # look for index in temp nums
                        for i in range(len(drawn_nums)):
                            if drawn_nums[i][0] == x_pos and drawn_nums[i][1] == y_pos:
                                board_list[y_pos][x_pos] = drawn_nums[i][2]
                        # check for a winner board
                        for i in range(len(board_list)):
                            if 0 in board_list[i]:
                                is_board_full = False
                        if is_board_full:
                            game_running = False
                            if board_list == solution:
                                return 1
                            else:
                                return 2

            screen.fill(CREAM)
            for mini_list in drawn_nums:
                value = number_font.render(str(mini_list[2]), True, (0, 0, 255))
                screen.blit(value, ((mini_list[0] + 1) * 66 + 258, (mini_list[1] + 1) * 66 + 47))
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

            # Print the Board
            for i in range(0, len(board_list)):
                for j in range(0, len(board_list[0])):
                    if board_list[i][j] != 0:
                        value = number_font.render(str(board_list[i][j]), True, (0, 0, 0))
                        screen.blit(value, ((j + 1) * 66 + 258, (i + 1) * 66 + 47))

            # Display Reset, Restart, and Exit Buttons
            button_font = pygame.font.Font(None, 70)
            # Display Reset Button
            reset_button_data = button_font.render("RESET", 0, BROWN)
            reset_button = reset_button_data.get_rect(center=(145, 200))
            screen.blit(reset_button_data, reset_button)
            # Display Restart Button
            restart_button_data = button_font.render("RESTART", 0, BROWN)
            restart_button = restart_button_data.get_rect(center=(145, 400))
            screen.blit(restart_button_data, restart_button)
            # Display Exit Button
            exit_button_data = button_font.render("EXIT", 0, BROWN)
            exit_button = exit_button_data.get_rect(center=(145, 600))
            screen.blit(exit_button_data, exit_button)
            button_font = pygame.font.Font(None, 90)

            x = x_pos
            y = y_pos
            if (x / 3) <= 1 and (y / 3) <= 1:  # 1
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 100),
                                 ((x * 66) + 368, (y * 66) + 100), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 166),
                                 ((x * 66) + 368, (y * 66) + 166), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 100),
                                 ((x * 66) + 302, (y * 66) + 166), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 368, (y * 66) + 100),
                                 ((x * 66) + 368, (y * 66) + 166), 4)
            elif 2 >= (x / 3) > 1 >= (y / 3):
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 100),
                                 ((x * 66) + 370, (y * 66) + 100), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 166),
                                 ((x * 66) + 370, (y * 66) + 166), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 100),
                                 ((x * 66) + 304, (y * 66) + 166), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 370, (y * 66) + 100),
                                 ((x * 66) + 370, (y * 66) + 166), 4)
            elif 2 < (x / 3) <= 3 and (y / 3) <= 1:
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 100),
                                 ((x * 66) + 372, (y * 66) + 100), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 166),
                                 ((x * 66) + 372, (y * 66) + 166), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 100),
                                 ((x * 66) + 306, (y * 66) + 166), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 372, (y * 66) + 100),
                                 ((x * 66) + 372, (y * 66) + 166), 4)
            elif (x / 3) <= 1 < (y / 3) <= 2:  # 2
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 103),
                                 ((x * 66) + 368, (y * 66) + 103), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 169),
                                 ((x * 66) + 368, (y * 66) + 169), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 103),
                                 ((x * 66) + 302, (y * 66) + 169), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 368, (y * 66) + 103),
                                 ((x * 66) + 368, (y * 66) + 169), 4)
            elif 1 < (x / 3) <= 2 and 1 < (y / 3) <= 2:
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 103),
                                 ((x * 66) + 370, (y * 66) + 103), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 169),
                                 ((x * 66) + 370, (y * 66) + 169), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 103),
                                 ((x * 66) + 304, (y * 66) + 169), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 370, (y * 66) + 103),
                                 ((x * 66) + 370, (y * 66) + 169), 4)
            elif 3 >= (x / 3) > 2 >= (y / 3) > 1:
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 103),
                                 ((x * 66) + 372, (y * 66) + 103), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 169),
                                 ((x * 66) + 372, (y * 66) + 169), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 103),
                                 ((x * 66) + 306, (y * 66) + 169), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 372, (y * 66) + 103),
                                 ((x * 66) + 372, (y * 66) + 169), 4)
            elif (x / 3) <= 1 and 2 < (y / 3) <= 3:  # 3
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 106),
                                 ((x * 66) + 368, (y * 66) + 106), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 172),
                                 ((x * 66) + 368, (y * 66) + 172), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 302, (y * 66) + 106),
                                 ((x * 66) + 302, (y * 66) + 172), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 368, (y * 66) + 106),
                                 ((x * 66) + 368, (y * 66) + 172), 4)
            elif 1 < (x / 3) <= 2 < (y / 3) <= 3:
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 106),
                                 ((x * 66) + 370, (y * 66) + 106), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 172),
                                 ((x * 66) + 370, (y * 66) + 172), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 304, (y * 66) + 106),
                                 ((x * 66) + 304, (y * 66) + 172), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 370, (y * 66) + 106),
                                 ((x * 66) + 370, (y * 66) + 172), 4)
            elif 2 < (x / 3) <= 3 and 2 < (y / 3) <= 3:
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 106),
                                 ((x * 66) + 372, (y * 66) + 106), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 172),
                                 ((x * 66) + 372, (y * 66) + 172), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 306, (y * 66) + 106),
                                 ((x * 66) + 306, (y * 66) + 172), 4)
                pygame.draw.line(screen, BROWN, ((x * 66) + 372, (y * 66) + 106),
                                 ((x * 66) + 372, (y * 66) + 172), 4)
            pygame.display.update()

            for i in range(0, len(drawn_nums)):
                temp_arr = drawn_nums[i]
                temp_x = temp_arr[0]
                temp_y = temp_arr[1]
                temp_num = temp_arr[2]
                num_font = pygame.font.Font(None, 40)
                num_surface = num_font.render(str(temp_num), 0, BLACK)
                number_rectangle = num_surface.get_rect(center=(300 + (temp_x * 66), 100 + (temp_y * 66)))
                screen.blit(num_surface, number_rectangle)

            if won:
                screen.fill(CREAM)

                won_surface = title_font.render("Game Won!", 0, BLACK)
                won_rectangle = won_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
                screen.blit(won_surface, won_rectangle)

                exit_surface = button_font.render("EXIT", 0, BLACK)
                exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
                screen.blit(exit_surface, exit_rectangle)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exit_rectangle.collidepoint(event.pos):
                            sys.exit()

    def hello(screen):
        WIDTH = 1200
        HEIGHT = 800

        BLACK = (0, 0, 0)
        CREAM = (255, 253, 208)

        title_font = pygame.font.Font(None, 150)
        button_font = pygame.font.Font(None, 90)

        screen.fill(CREAM)

        title_surface = title_font.render("Game Over", 0, BLACK)
        title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 230))
        screen.blit(title_surface, title_rectangle)

        medium_surface = button_font.render("Restart", 0, BLACK)
        medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
        screen.blit(medium_surface, medium_rectangle)

        menu_running = True

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if medium_rectangle.collidepoint(event.pos):
                        menu_running = False
            pygame.display.update()

    def win_screen_run(screen):
        WIDTH = 1200
        HEIGHT = 800

        BLACK = (0, 0, 0)
        CREAM = (255, 253, 208)

        title_font = pygame.font.Font(None, 150)
        button_font = pygame.font.Font(None, 90)

        screen.fill(CREAM)

        title_surface = title_font.render("Game Won!", 0, BLACK)
        title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 230))
        screen.blit(title_surface, title_rectangle)

        medium_surface = button_font.render("Play Again", 0, BLACK)
        medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.blit(medium_surface, medium_rectangle)

        hard_surface = button_font.render("Exit", 0, BLACK)
        hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(hard_surface, hard_rectangle)

        menu_running = True

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if medium_rectangle.collidepoint(event.pos):
                        return True
                    if hard_rectangle.collidepoint(event.pos):
                        return False
            pygame.display.update()

    if __name__ == '__main__':
        game_over = False
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")

        run_code = True

        while run_code:
            game_type = draw_game_start(screen)
            end_condition = run_game(screen, game_type)
            if end_condition == 1:
                keep_going = win_screen_run(screen)
                if not keep_going:
                    run_code = False
            elif end_condition == 2:
                hello(screen)
