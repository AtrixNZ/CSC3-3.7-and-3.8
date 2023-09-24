import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spelling Game")

# Fonts
title_font = pygame.font.Font(None, 100)
menu_font = pygame.font.Font(None, 50)
instruction_font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 36)

# Words for different levels
easy_words = ["cat", "dog", "bird", "fish", "lion"]
medium_words = ["apple", "banana", "grape", "pear", "orange"]
hard_words = ["measure", "although", "thought", "again", "alright"]

# Difficulty settings
difficulty_levels = ["Easy", "Medium", "Hard"]
current_difficulty = 0  # Default to Easy

# Age Verification Screen
def age_verification_screen():
    age = ""
    age_valid = False
    age_message = ""

    screen.fill(BLACK)
    
    age_text = menu_font.render("How old are you? (Must be 5-12 years old to play)", True, WHITE)
    age_text_rect = age_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(age_text, age_text_rect)

    age_input_surface = pygame.Surface((400, 50))
    age_input_surface.fill(WHITE)
    age_input_rect = pygame.Rect(200, SCREEN_HEIGHT // 2 + 20, 400, 50)
    pygame.draw.rect(age_input_surface, BLACK, age_input_rect, 2)
    
    age_input_render = input_font.render(age, True, BLACK)
    screen.blit(age_input_surface, age_input_rect)
    screen.blit(age_input_render, (age_input_rect.x + 10, age_input_rect.y + 10))

    if age_message:
        message_text = menu_font.render(age_message, True, RED)
        message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(message_text, message_rect)

    # Add small text below the text box
    proceed_text = input_font.render("Press Enter to Proceed", True, WHITE)
    proceed_rect = proceed_text.get_rect(center=(SCREEN_WIDTH // 2, age_input_rect.bottom + 20))
    screen.blit(proceed_text, proceed_rect)

    # Style the "Return to Main Menu" button to look like the "Continue" button
    return_to_menu_button_text = menu_font.render("Return to Main Menu", True, WHITE)
    return_to_menu_button_rect = return_to_menu_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
    pygame.draw.rect(screen, WHITE, return_to_menu_button_rect, 2)  # Add a box around the button
    screen.blit(return_to_menu_button_text, return_to_menu_button_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check if the age is valid
                    try:
                        age_value = int(age)
                        if 5 <= age_value <= 12:
                            age_valid = True
                            waiting_for_input = False
                        else:
                            age_message = "You are too young or too old to play this game."
                    except ValueError:
                        age_message = "Please enter a valid age (5-12)."
                elif event.key == pygame.K_BACKSPACE:
                    age = age[:-1]
                else:
                    age += event.unicode

                # Update age input rendering
                age_input_render = input_font.render(age, True, BLACK)
                screen.fill(BLACK, age_input_rect)
                screen.blit(age_input_surface, age_input_rect)
                screen.blit(age_input_render, (age_input_rect.x + 10, age_input_rect.y + 10))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if return_to_menu_button_rect.collidepoint(mouse_pos):
                    return_to_main_menu()  # Return to the main menu
        
        pygame.display.flip()

    if age_valid:
        instruction_screen()  # Take the user to the instructions screen




# Return to Main Menu
def return_to_main_menu():
    main_menu()

# Display a message in the center of the screen
def display_message(message):
    message_text = menu_font.render(message, True, WHITE)
    message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
    screen.fill(BLACK)
    screen.blit(message_text, message_rect)
    pygame.display.flip()
    pygame.time.delay(2000)  # Display the message for 2 seconds

# Main Menu
def draw_main_menu():
    screen.fill(BLACK)
    title_text = title_font.render("Spelling Game", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(title_text, title_rect)

    start_text = menu_font.render("Start", True, WHITE)
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(start_text, start_rect)

    settings_text = menu_font.render("Settings", True, WHITE)
    settings_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    screen.blit(settings_text, settings_rect)

    quit_text = menu_font.render("Quit", True, WHITE)
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()
    return start_rect, settings_rect, quit_rect

def main_menu():
    running = True
    start_rect, settings_rect, quit_rect = draw_main_menu()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    age_verification_screen()  # Show age verification screen
                elif settings_rect.collidepoint(mouse_pos):
                    change_settings()
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        draw_main_menu()

    pygame.quit()
    sys.exit()

# Instruction Screen
def instruction_screen():
    screen.fill(BLACK)

    instruction_title = title_font.render("HOW TO PLAY:", True, WHITE)
    instruction_title_rect = instruction_title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(instruction_title, instruction_title_rect)

    instruction_text = instruction_font.render("Write the word that is being displayed on the screen.", True, WHITE)
    instruction_text_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
    screen.blit(instruction_text, instruction_text_rect)

    instruction_text2 = instruction_font.render("If you get the word right, you move on to the next word.", True, WHITE)
    instruction_text_rect2 = instruction_text2.get_rect(center=(SCREEN_WIDTH // 2, 300))
    screen.blit(instruction_text2, instruction_text_rect2)

    instruction_text3 = instruction_font.render("If you get the word wrong, you lose a life.", True, WHITE)
    instruction_text_rect3 = instruction_text3.get_rect(center=(SCREEN_WIDTH // 2, 350))
    screen.blit(instruction_text3, instruction_text_rect3)

    instruction_text4 = instruction_font.render("You only have 3 lives!", True, WHITE)
    instruction_text_rect4 = instruction_text4.get_rect(center=(SCREEN_WIDTH // 2, 400))
    screen.blit(instruction_text4, instruction_text_rect4)

    # Continue button
    continue_text = menu_font.render("Continue", True, WHITE)
    continue_rect = continue_text.get_rect(bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20))
    pygame.draw.rect(screen, GREEN, continue_rect)
    screen.blit(continue_text, continue_rect)

    pygame.display.flip()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(pygame.mouse.get_pos()):
                    waiting_for_key = False

    # Start the game
    play_game()


# Game
def play_game():
    current_level = 0
    words = get_words_by_difficulty(current_difficulty)
    correct_word = random.choice(words)
    input_text = ""
    correct_words = 0
    lives = 3  # Initialize lives
    wrong_words = 0  # Initialize wrong words
    background_color = BLACK
    change_time = 0
    
    while lives > 0:  # Continue while the player has lives
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_RETURN:
                    if input_text == correct_word:
                        correct_words += 1
                        words.remove(correct_word)
                        if not words:
                            show_results(correct_words, len(get_words_by_difficulty(current_difficulty)), wrong_words)
                            return
                        correct_word = random.choice(words)
                        input_text = ""
                        background_color = GREEN
                        change_time = pygame.time.get_ticks()
                    else:
                        lives -= 1  # Decrement lives on a wrong word
                        wrong_words += 1  # Increment wrong words
                        background_color = RED
                        change_time = pygame.time.get_ticks()
                        if lives == 0:
                            show_results(correct_words, len(get_words_by_difficulty(current_difficulty)), wrong_words)
                            return
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        
        # Check if it's time to change the background color back to black
        if background_color != BLACK and pygame.time.get_ticks() - change_time > 500:  # Changed to 0.5 seconds (500 milliseconds)
            background_color = BLACK
        
        screen.fill(background_color)
        
        word_text = title_font.render(correct_word, True, WHITE)
        word_rect = word_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(word_text, word_rect)
        
        lives_text = menu_font.render(f"Lives: {lives}", True, WHITE)
        lives_rect = lives_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        screen.blit(lives_text, lives_rect)
        
        input_surface = pygame.Surface((400, 50))
        input_surface.fill(WHITE)
        input_rect = pygame.Rect(200, SCREEN_HEIGHT // 2 + 50, 400, 50)
        pygame.draw.rect(input_surface, BLACK, input_rect, 2)
        input_text_render = input_font.render(input_text, True, BLACK)
        screen.blit(input_surface, input_rect)
        screen.blit(input_text_render, (input_rect.x + 10, input_rect.y + 10))
        
        pygame.display.flip()

# Results Screen
def show_results(correct_words, total_levels, wrong_words):
    result_text = title_font.render(f"Results: {correct_words}/{total_levels} Correct", True, WHITE)
    result_rect = result_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    wrong_text = menu_font.render(f"Wrong Words: {wrong_words}/5", True, WHITE)
    wrong_rect = wrong_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    
    screen.fill(BLACK)
    screen.blit(result_text, result_rect)
    screen.blit(wrong_text, wrong_rect)

    back_text = menu_font.render("Back to Main Menu", True, WHITE)
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
    pygame.draw.rect(screen, BLACK, back_rect, 2)
    screen.blit(back_text, back_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_rect.collidepoint(mouse_pos):
                    main_menu()  # Go back to the main menu

# Settings Screen
def draw_settings_menu():
    screen.fill(BLACK)
    settings_text = title_font.render("Settings", True, WHITE)
    settings_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
    screen.blit(settings_text, settings_rect)

    difficulty_text = menu_font.render(f"Difficulty: {difficulty_levels[current_difficulty]}", True, WHITE)
    difficulty_rect = difficulty_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(difficulty_text, difficulty_rect)

    select_text = menu_font.render("Select", True, WHITE)
    select_rect = select_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
    pygame.draw.rect(screen, BLACK, select_rect, 2)
    screen.blit(select_text, select_rect)

    esc_text = menu_font.render("Press Esc to go back to main menu", True, WHITE)
    esc_rect = esc_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))
    screen.blit(esc_text, esc_rect)

    pygame.display.flip()
    return difficulty_rect

def change_settings():
    global current_difficulty
    settings_running = True
    difficulty_rect = draw_settings_menu()
    
    while settings_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_running = False
                elif event.key == pygame.K_DOWN:
                    current_difficulty = (current_difficulty + 1) % len(difficulty_levels)
                    difficulty_rect = draw_settings_menu()  # Redraw settings menu
                elif event.key == pygame.K_UP:
                    current_difficulty = (current_difficulty - 1) % len(difficulty_levels)
                    difficulty_rect = draw_settings_menu()  # Redraw settings menu
                elif event.key == pygame.K_RETURN:
                    words = get_words_by_difficulty(current_difficulty)
                    random.shuffle(words)  # Shuffle the words based on selected difficulty
                    main_menu()  # Go back to the main menu

        # Update displayed difficulty
        difficulty_text = menu_font.render(f"Difficulty: {difficulty_levels[current_difficulty]}", True, WHITE)
        screen.blit(difficulty_text, difficulty_rect)
        pygame.display.flip()

    draw_main_menu()

# Utility function to get words by difficulty
def get_words_by_difficulty(difficulty):
    if difficulty == 0:
        return easy_words
    elif difficulty == 1:
        return medium_words
    elif difficulty == 2:
        return hard_words

# Run the main menu
main_menu()
