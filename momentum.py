#!/usr/bin/env python 3
"""
This program is supposed to be a simple platformer, I originally had hopes of being
able to program in some enemies a little more platforms to the level. I started the
project by writing out the overall goal and the broke that down into individual 
sections and focused on how they worked. I did a lot of research and found quite a 
lot of information on each section as well as a tutorial guide for building more in
depth games. 
This program should allow a player to control a ninja sprite, the sprite should have
the ability to move left and right with the respective arrow keys as well as the "A" 
and "D" keys. The player can jump with "W" as well as the up arrow keys. 
The program is split into 5 different files to both simplify the look of the program 
but to also create more ease in solving traceback errors. Each program handles a 
seperate aspect of the game. The Constants are simply the constants of the game. The
Player file handles the actions and results of the player and sprite interaction. 
Level file will dictate the basic construction of the level with a class dedicated to
each level. The Sprite_sheet file breaks down sprite sheets so that the Player and Level
files can apply them where needed. 
I really wanted to take this program further in incorporating enemies, attacking and a 
variable modifier. Yet with issues and errors revolving around invisible sprites and how
to resolve the issue I was left with little ability to. I feel that I have learned a lot
by building this program and enjoyed every moment of it. 

"""


import pygame
import sys
import os
import constants
import level
from player import Player
''' importing the files that are created to run the game '''
def main():
    ''' defines the game '''
    pygame.init()

    size = [constants.SCREEN_W, constants.SCREEN_H]
    screen = pygame.display.set_mode(size)
    ''' size of screen '''
    pygame.display.set_caption("Momentum")
    ''' puts game name in the window '''
    player = Player()
    ''' import player '''
    level_list = []
    level_list.append(level.Level_1(player))
    ''' import level(s) and creates room list '''
    current_level_number = 0
    current_level = level_list[current_level_number]
    ''' indicated level number '''
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    ''' creates sprite group for easy drawing '''
    player.rect.x = 32
    player.rect.y = constants.SCREEN_H - player.rect.height
    active_sprite_list.add(player)

    game = True

    clock = pygame.time.Clock()

    while game:
        ''' defines the game state '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            ''' exit the game '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                player.go_left()
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                player.go_right()
            if event.key == pygame.K_UP or event.key == ord("w"):
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                player.stop()
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                player.stop()
        ''' defines movement '''
        active_sprite_list.update()
        ''' update sprite list for movement '''
        current_level.update()
        ''' update level '''
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_number < len(level_list) -1:
                current_level_number += 1
                current_level = level_list[current_level_number]
                player.level = current_level
        ''' creates an area of "slack" so the player can move a small amount before
        the screen will move with them, to keep the screen a little more static '''

        current_level.draw(screen)
        ''' draws level into the screen '''
        active_sprite_list.draw(screen)
        ''' draws sprites into the screen '''
        player.update()
        ''' updates player specs ''' 
        clock.tick(60)
        ''' starts frame count '''
        pygame.display.flip()
        ''' updates display '''
    pygame.quit()

if __name__ == "__main__":
    main()