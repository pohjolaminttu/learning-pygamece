# MINTTU POHJOLA, AUTUMN 2025
# LEARNING PYGAME(-CE) USING WITH YOUTUBE VIDEO 
# MATERIALS AND VIDEO IS MADE 19.5.2024 BY @ Clear Code

import pygame

# General setup
pygame.init() 
window_width, window_height = 1300, 750
display_surface = pygame.display.set_mode((window_width, window_height))
running = True

while running:
    # Event loop to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    pygame.display.update()

pygame.quit()