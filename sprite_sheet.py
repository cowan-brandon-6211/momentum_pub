"""
Sprite sheet is designed to take the given image file and cut an image from said
file. It then creates a blank rectangle and pastes the image over that rectangle
and returns that image.
"""

import pygame
import constants

class Sprite_sheet(object):
    ''' This class will grab images from the spritesheet.'''

    def __init__(self):
        ''' Constructor, passes in file name of spritesheet'''
        self.sprite_sheet = pygame.image.load("ninja_move.png").convert()

    def get_image(self, x, y, width, height):
        '''
        This will grab each image out of the larger sheet by
        passing in the x, y coordinates as well as width and 
        height
        '''

        ''' Creates blank image'''
        image = pygame.Surface([width, height]).convert()

        ''' Copies sprite onto blank image'''
        image.set_colorkey(constants.BLACK)

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        

        return image