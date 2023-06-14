import pygame
import os
import random
import sys
from title_page import title_page

WIDTH = 800
HEIGHT = 600
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

large_font = pygame.font.SysFont("Comic Sans", 80)
button_font = pygame.font.SysFont("Comic Sans", 30)





GREEN_BIN = pygame.image.load(os.path.join('green_bin.png'))
GREEN_BIN = pygame.transform.scale(GREEN_BIN, (100, 100))
BLUE_BIN = pygame.image.load(os.path.join('blue_bin.png'))
BLUE_BIN = pygame.transform.scale(BLUE_BIN, (100, 100))
TRASH_BIN = pygame.image.load(os.path.join('trash_bin.png'))
TRASH_BIN = pygame.transform.scale(TRASH_BIN, (100, 100))
HEART_IMAGE = pygame.image.load(os.path.join('heart.png'))
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (50, 50))

GREEN_BIN_RECT = pygame.Rect(500, 500, 100, 100)
BLUE_BIN_RECT = pygame.Rect(300, 500, 100, 100)
TRASH_BIN_RECT = pygame.Rect(100, 500, 100, 100)

TRASH = ["bag", "banana", "can", "cartboard", "foil", "rose"]

trash_images = {
    "bag": pygame.image.load("bag.png"),
    "banana": pygame.image.load("banana.png"),
    "can": pygame.image.load("can.png"),
    "cartboard" : pygame.image.load("cartboard.png"),
    "foil" : pygame.image.load("foil.png"),
    "rose" : pygame.image.load("rose.png")
}

for trash in TRASH:
    trash_images[trash] = pygame.transform.scale(trash_images[trash], (150, 150))

trash_rect = trash_images[TRASH[0]].get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
initial_trash_pos = trash_rect.center


hearts = 3
game_over = False
dragging = False

pygame.display.set_caption("Garbage Sorting")

def draw_window():
    global hearts
    WINDOW.fill(WHITE)
    WINDOW.blit(GREEN_BIN, (600, 400))
    WINDOW.blit(BLUE_BIN, (350, 400))
    WINDOW.blit(TRASH_BIN, (100, 400))
    WINDOW.blit(trash, trash_rect)

    for i in range(hearts):
        heart_rect = HEART_IMAGE.get_rect()
        heart_rect.topleft = (50 + i * 50, 40)
        WINDOW.blit(HEART_IMAGE, heart_rect)
    
    pygame.display.update()

def sorting_game(window):
    global dragging, hearts, game_over, score
    clock = pygame.time.Clock()
    run = True
    score = 0

    def generate_new_trash():
        global trash, trash_rect, initial_trash_pos, trash_item
        trash_item = random.choice(TRASH)
        trash = trash_images[trash_item]
        WINDOW.blit(trash, trash_rect)
        WINDOW.blit(score, (100, 100))
        trash_rect = trash.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        initial_trash_pos = trash_rect.center
        pygame.display.update()
        print(trash_item)
    generate_new_trash()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if trash_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = trash_rect.x - mouse_x
                    offset_y = trash_rect.y - mouse_y
                    offset = (offset_x, offset_y)

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                trash_rect.center = pygame.mouse.get_pos()
                if trash_rect.colliderect(BLUE_BIN_RECT):
                    if trash_item in ["can", "cardboard"]:
                        score += 1
                    else:
                        hearts -= 1
                    generate_new_trash()
                elif trash_rect.colliderect(GREEN_BIN_RECT):
                    if trash_item in ["banana", "rose"]:
                        score += 1
                    else:
                        hearts -= 1
                    generate_new_trash()
                elif trash_rect.colliderect(TRASH_BIN_RECT):
                    if trash_item in ["bag", "foil"]:
                        score += 1
                    else:
                        hearts -= 1
                    generate_new_trash()

                if hearts == 0:
                    game_over = True
                    run = False         

            trash_rect.center = initial_trash_pos

        if dragging:
            mouse_pos = pygame.mouse.get_pos()
            trash_rect.center = mouse_pos

        draw_window()

    if game_over:
    # Clear the screen
        WINDOW.fill(WHITE)

        # Render "Game Over" text
        game_over_text = large_font.render("Game Over", True, BLACK)
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        WINDOW.blit(game_over_text, game_over_text_rect)

        # Render score text
        score_text = button_font.render("Score: " + str(score), True, BLACK)
        score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WINDOW.blit(score_text, score_text_rect)

        # Render reset button
        reset_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        pygame.draw.rect(WINDOW, RED, reset_button)
        reset_text = button_font.render("RESET", True, WHITE)
        reset_text_rect = reset_text.get_rect(center=reset_button.center)
        WINDOW.blit(reset_text, reset_text_rect)

        # Render quit button
        quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
        pygame.draw.rect(WINDOW, RED, quit_button)
        quit_text = button_font.render("QUIT", True, WHITE)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        WINDOW.blit(quit_text, quit_text_rect)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # pygame.quit()
                # sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if reset_button.collidepoint(mouse_pos):
                    hearts = 3
                    score = 0
                    game_over = False
                    run = True
                elif quit_button.collidepoint(mouse_pos):
                    run = False
                    title_page()
        

        pygame.display.update()
