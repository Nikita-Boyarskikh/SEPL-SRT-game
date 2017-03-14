# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:36:33 2017

@author: aleks
"""
import sys
import pygame

from settings import Settings
from rocket import Rocket


def run_game():
    # Initialize pygame
    pygame.init()
    
    # Set title of screen
    pygame.display.set_caption("STO")
    
    #Set settings from settings.py
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    #create rocket
    rocket_1 = Rocket(screen)
    
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            """if event.type == pygame.KEYDOWN:
                if event.key == K_ESKAPE:
                    done = True"""
        # Set the screen background
        screen.fill(ai_settings.bg_color)
        rocket_1.blitme()
        
        # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

run_game()
pygame.quit()
    