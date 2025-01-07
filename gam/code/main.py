"""The game's main file"""
#Library import
import pygame
import random
import time
from particles import *

#Other files imports
from enemies import Enemy
from player import Player
import constants as ct

class App:

    def __init__(self):
        """Called on game startup, all basic stuff
        """
        self.plist=[] #Particle list. Ugly AF, please fix

        #Creating basics of the game 
        self.screen_mult=7
        self.screen_size=(ct.GAME_DRAW_SIZE_X*self.screen_mult,ct.GAME_DRAW_SIZE_Y*self.screen_mult)
        pygame.init()
        self.running = True
        ct.RENDER_BUFFER = pygame.Surface((ct.GAME_DRAW_SIZE_X,ct.GAME_DRAW_SIZE_Y), pygame.OPENGL)
        self.screen = pygame.display.set_mode(self.screen_size)

        #Initiating game
        self.tiles=pygame.image.load("resources/floor_tiles.png").convert()
        self.gamestate="Playing"
        self.player=Player([100,100],1)
        self.test_enemy=Enemy([200,200],0.2)
        self.test_enemy2=Enemy([300,100],0.3)

        #Starting game loop
        self.loop()

    def loop(self):
        """Global game loop
        """
        while self.running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.gamestate=="Playing":
                        self.gamestate="Paused"
                    elif event.key == pygame.K_ESCAPE:
                        self.gamestate="Playing"
                elif event.type == pygame.QUIT:
                    self.running = False
            if keys[pygame.K_k]:
                time.sleep(1)
                
            if self.gamestate=="Paused":
                continue
            self.update()
            self.draw()
            pygame.transform.scale_by(ct.RENDER_BUFFER,self.screen_mult,self.screen)
            pygame.display.update()
        pygame.quit()

    def draw(self):
        ct.RENDER_BUFFER.fill([0,0,0])
        for x in range(ct.GAME_DRAW_SIZE_X+16):
            for y in range(ct.GAME_DRAW_SIZE_Y):
                """
                if (int(x/16)+int(y/12))%2==0:
                    pygame.Surface.set_at(ct.RENDER_BUFFER,(x,y),[25,25,25])
                """
                if x%16==0 and y%12==0 and (int(x/16)+int(y/12))%2==0:
                    ct.RENDER_BUFFER.blit(self.tiles, (x-16, y))
                    #pygame.Surface.set_at(ct.RENDER_BUFFER,(x,y),[100,0,0])
                
        
        self.player.draw()
        self.test_enemy.draw()
        self.test_enemy2.draw()
        update_particles_list(self.plist) #will be replaced by particle system
        

    def update(self):
        self.plist.append(Particle(list(self.player.pos),random.randint(100,150))) #Will be replaced by particle generator
        self.player.update()
        self.test_enemy.update(self.player.pos)
        self.test_enemy2.update(self.player.pos)
        



if __name__ == '__main__':
    App()