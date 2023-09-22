import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 30
FONT = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spelling Game")

# Game states
MENU = 0
GAME = 1
SETTINGS = 2
RESULT = 3
current_state = MENU

# Word lists for different levels
easy_words = ["apple", "banana", "cat", "dog", "elephant"]
medium_words = ["computer", "keyboard", "elephant", "restaurant", "guitar"]
hard_words = ["ambitious", "juxtapose", "perpendicular", "quizzical", "zephyr"]

# Initialize game variables
current_level = easy_words
current_word_index = 0
current_word = current_level[current_word_index]
typed_text = ""

# Settings variables
current_difficulty = "Easy"

# Timer variables
time_limit = 60
start_time = 0

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    if current_state == MENU:
        # Display menu options and handle input
        menu_text = FONT.render("Press ENTER to Start, S for Settings", True, BLACK)
        screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2))
    elif current_state == GAME:
        # Start the timer
        if start_time == 0:
            start_time = pygame.time.get_ticks()
        
        # Display the time remaining
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(0, time_limit - elapsed_time)
        timer_text = FONT.render("Time: {}s".format(remaining_time), True, BLACK)
        screen.blit(timer_text, (10, 10))
        
        # Display the word to spell and the typed text
        word_display = FONT.render(current_word, True, BLACK)
        typed_display = FONT.render(typed_text, True, BLACK)
        screen.blit(word_display, (WIDTH // 2 - word_display.get_width() // 2, HEIGHT // 3))
        screen.blit(typed_display, (WIDTH // 2 - typed_display.get_width() // 2, HEIGHT // 2))
        
        # Check if the typed text matches the current word
        if typed_text == current_word:
            current_word_index += 1
            if current_word_index < len(current_level):
                current_word = current_level[current_word_index]
                typed_text = ""
            else:
                current_state = RESULT
                elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    elif current_state == SETTINGS:
        # Display settings options and handle input
        settings_text = FONT.render("Difficulty: " + current_difficulty, True, BLACK)
        back_text = FONT.render("Press ESC or B to Go Back to Menu", True, BLACK)
        screen.blit(settings_text, (WIDTH // 2 - settings_text.get_width() // 2, HEIGHT // 3))
        screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT // 2))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if current_difficulty == "Easy":
                        current_difficulty = "Medium"
                    elif current_difficulty == "Medium":
                        current_difficulty = "Hard"
                    else:
                        current_difficulty = "Easy"
                    settings_text = FONT.render("Difficulty: " + current_difficulty, True, BLACK)
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                    current_state = MENU
    elif current_state == RESULT:
        # Display result screen
        result_text = FONT.render("Game Over!", True, BLACK)
        score_text = FONT.render("Time: {}s".format(elapsed_time), True, BLACK)
        restart_text = FONT.render("Press R to Restart", True, BLACK)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_state = MENU
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if current_state == MENU:
                if event.key == pygame.K_RETURN:
                    current_state = GAME
                    start_time = pygame.time.get_ticks()  # Reset the timer
                elif event.key == pygame.K_s:
                    current_state = SETTINGS
            elif current_state == GAME:
                if event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                elif event.key == pygame.K_SPACE:
                    typed_text += " "
                elif event.key == pygame.K_ESCAPE:
                    current_state = MENU
                else:
                    typed_text += event.unicode
            elif current_state == SETTINGS:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                    current_state = MENU
            elif current_state == RESULT:
                if event.key == pygame.K_r:
                    current_state = MENU
    
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
