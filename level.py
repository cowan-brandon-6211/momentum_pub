import pygame
import constants
import sys
import os


class Platform(pygame.sprite.Sprite):
    ''' define platform class '''
    def __init__(self, width, height):
        ''' platform constructor '''
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.WHITE)
        ''' dictates requirements for platform creatio '''
        self.rect = self.image.get_rect()
        ''' creates the rectangle '''
class Level():

    def __init__(self, player):
        self.platform_list = None
        self.enemy_list = None
        ''' lists for platform and enemies '''
        self.background = None
        ''' sets level background '''
        self.world_shift = 0
        self.level_limit = -1000
        ''' world shift and world range '''
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player 
        ''' sprite group and player indication '''
    def update(self):
        ''' updates level '''
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        ''' program for drawing the level '''
        screen.fill(constants.GREEN)
        #screen.blit(self.background, (self.world_shift // 3,0))
        screen.set_colorkey(constants.GREEN)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        ''' program to define the shift of the world '''
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

class Level_1(Level):
    ''' defines the first level '''
    def __init__(self, player):
        ''' constructor '''
        Level.__init__(self, player)

        self.background = None

        self.level_limit = -2500
        ''' level length '''
        level = [[210, 70, 500, 500],
                [210, 70, 800, 400],
                [210, 70, 1000, 500],
                [210, 70, 1120, 280],
                ]
        ''' platofrms in the level by x,y location and width/height'''
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        ''' loop that constructs and places the platforms '''
