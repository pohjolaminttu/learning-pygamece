# MINTTU POHJOLA, AUTUMN 2025
# LEARNING PYGAME(-CE) USING WITH YOUTUBE VIDEO 
# MATERIALS AND VIDEO IS MADE 19.5.2024 BY @ Clear Code
# The first game; a spaceship which shoots a laser towards meteors and distroyes them

import pygame, random

# General setup
pygame.init() 
window_width, window_height = 1300, 750
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('StarDistroyer')
running = True

# Surface by importing an image of the ship
player_surf = pygame.image.load('materials/space shooter/images/player.png').convert_alpha()
x = 0

# Surface for the stars (image)
star_surf = pygame.image.load('materials/space shooter/images/star.png').convert_alpha()
star_positions = [(random.randint(0, window_width), random.randint(0, window_height)) for _ in range(20)]

while running:
    # Event loop to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    display_surface.fill('darkslategray')
    for star in star_positions:
        display_surface.blit(star_surf, star)
    x += 0.1
    display_surface.blit(player_surf, (x,150))
    pygame.display.update()

pygame.quit()
