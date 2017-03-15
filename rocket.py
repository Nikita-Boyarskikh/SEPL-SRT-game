# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 18:18:03 2017

@author: aleks
"""
import pygame


class Rocket():
    
    def __init__(self, screen):
        self.screen = screen
        #download image of rocket and create rectangle
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 
    def blitme(self):
        #draw rocket in her position
        self.screen.blit(self.image, self.rect)