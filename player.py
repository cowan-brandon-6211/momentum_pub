"""
This module defines the Player class and dictates how the player sprite will
interact with other sprites, the world as well as platforms. The class also 
dictates gravity, movement speed, and creates the sprite animation loops.
"""

import pygame
import sys
import os
from sprite_sheet import Sprite_sheet
import constants
import level 


class Player(pygame.sprite.Sprite):
    ''' Define player class '''
    pygame.display.set_mode()

    change_x = 0
    ''' movement along x coordinate '''
    change_y = 0
    ''' movement along y coordinate '''
    walking_frames_l = []
    ''' list for walking animations left '''
    walking_frames_r = []
    ''' list for walking animation right '''
    direction = "R"
    ''' create standard movement direction '''

    level = None
    ''' sprites relation to game '''
    
    def __init__(self):
        super().__init__()
        ''' player constructor '''

        pygame.sprite.Sprite.__init__(self)

        s_sheet = Sprite_sheet()
        image = s_sheet.get_image(0, 0, 19, 23)
        self.walking_frames_r.append(image)
        image = s_sheet.get_image(20, 0, 19, 23)
        self.walking_frames_r.append(image)
        image = s_sheet.get_image(40, 0, 19, 23)
        self.walking_frames_r.append(image)
        image = s_sheet.get_image(60, 0, 19, 23)
        self.walking_frames_r.append(image)
        ''' grabs images for right movement and appends to list '''

        image = s_sheet.get_image(0, 0, 19, 23)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = s_sheet.get_image(20, 0, 19, 23)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = s_sheet.get_image(40, 0, 19, 23)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = s_sheet.get_image(60, 0, 19, 23)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        ''' grabs image then flips for left list '''

        self.image = self.walking_frames_r[0]
        ''' attaches images to player '''

        self.rect = self.image.get_rect()
        
        
        #print(self.walking_frames_r)
        #print(self.walking_frames_l)
        #breakpoint
    def update(self):
        ''' updates player class '''
        self.gravity()
        ''' pins gravity '''
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        ''' links the movement lists to movement input '''
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = self.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        ''' if player runs into a platform or "block" they stop moving '''
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            
            self.change_y = 0
        ''' repeated her for top and bottom of platform '''
    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.y >= constants.SCREEN_H - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_W - self.rect.height
        ''' set gravity and sets the bottom of the screen as a floor '''
    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        ''' defines jump motion '''
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_H:
            self.chang = -10
        ''' limits just to one, no double jump '''
    def go_left(self):
        self.change_x = -6
        self.direction = "L"
        ''' left movement speed'''
    def go_right(self):
        self.change_x = 6
        self.direction = "R"
        ''' right movement speed '''
    def stop(self):
        ''' define stop '''
        self.change_x = 0