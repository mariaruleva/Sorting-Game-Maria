import pygame
import sys
from title_page import title_page
from sorting_game import sorting_game
from learn import learn

def main():
    # Initialize Pygame
    pygame.init()

    # Set window dimensions
    window_width = 800
    window_height = 600

    # Create the window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Recycle your garbage")

    # Game state
    game_state = "title"  # Initial game state

    while True:
        if game_state == "title":
            game_state = title_page(window)  # Call title_page function and update game state accordingly
        elif game_state == "sorting":
            game_state = sorting_game(window)
        elif game_state == "learn":
            game_state = learn()  # Call sorting_game function and update game state accordingly
        elif game_state == "exit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
