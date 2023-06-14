import pygame
import sys

def title_page(window):
    # Initialize Pygame
    pygame.init()

    # Set window dimensions
    window_width = 800
    window_height = 600

    # Set colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Create the window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Recycle your garbage")

    # Load background image
    background_image = pygame.image.load("landfill.jpg")  # Replace "background.jpg" with your image file path if needed

    # Load font
    font = pygame.font.SysFont("Comic Sans", 30)
    big_font = pygame.font.SysFont("Comic Sans", 50)

    # Create buttons
    learn_button = pygame.Rect(300, 250, 200, 50)
    sorting_button = pygame.Rect(300, 350, 250, 50)
    exit_button = pygame.Rect(300, 450, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"  # Return "exit" game state if the user closes the window

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if sorting_button.collidepoint(mouse_pos):
                    return "sorting" 
                
                elif learn_button.collidepoint(mouse_pos):
                    return "learn"  # Return "sorting" game state if the sorting button is clicked

                elif exit_button.collidepoint(mouse_pos):
                    return "exit"  # Return "exit" game state if the exit button is clicked

        # Draw background
        window.blit(background_image, (0, 0))

        # Draw buttons
        pygame.draw.rect(window, white, learn_button)
        pygame.draw.rect(window, white, sorting_button)
        pygame.draw.rect(window, white, exit_button)

        # Draw button labels
        learn_text = font.render("Learn", True, black)
        start_text = font.render("Sorting Game", True, black)
        exit_text = font.render("Exit", True, black)

        window.blit(learn_text, (355, 260))
        window.blit(start_text, (325, 360))
        window.blit(exit_text, (355, 460))

        # Draw title
        title_text = big_font.render("Sort your garbage", True, black)
        window.blit(title_text, (250, 150))

        pygame.display.flip()
