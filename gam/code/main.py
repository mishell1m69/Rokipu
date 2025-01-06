import pygame
from player import Player
from particles import *
import random
from enemies import Enemy
import time
class App:

    def __init__(self):
        self.plist=[]
        self.draw_size=(320,180)
        self.screen_mult=6
        self.screen_size=(self.draw_size[0]*self.screen_mult,self.draw_size[1]*self.screen_mult)
        pygame.init()
        self.running = True
        self.buffer = pygame.Surface(self.draw_size, pygame.OPENGL)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.tiles=pygame.image.load("resources/floor_tiles.png").convert()
        self.gamestate="Paused"
        self.player=Player(self.buffer,[100,100],1)
        self.test_enemy=Enemy(self.buffer,[200,200],0.2)
        self.test_enemy2=Enemy(self.buffer,[300,100],0.3)
        self.loop()

    def loop(self):
        while self.running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_k]:
                time.sleep(1)

            self.update()
            self.draw()
            pygame.transform.scale_by(self.buffer,self.screen_mult,self.screen)
            pygame.display.update()
        pygame.quit()

    def draw(self):
        self.buffer.fill([0,0,0])
        for x in range(self.draw_size[0]+16):
            for y in range(self.draw_size[1]):
                """
                if (int(x/16)+int(y/12))%2==0:
                    pygame.Surface.set_at(self.buffer,(x,y),[25,25,25])
                """
                if x%16==0 and y%12==0 and (int(x/16)+int(y/12))%2==0:
                    self.buffer.blit(self.tiles, (x-16, y))
                    #pygame.Surface.set_at(self.buffer,(x,y),[100,0,0])
                
        
        self.player.draw()
        self.test_enemy.draw()
        self.test_enemy2.draw()
        update_particles_list(self.plist)
        

    def update(self):
        self.plist.append(Particle(self.buffer,list(self.player.pos),random.randint(100,150)))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False
        self.player.update()
        self.test_enemy.update(self.player.pos)
        self.test_enemy2.update(self.player.pos)
        



if __name__ == '__main__':
    App()