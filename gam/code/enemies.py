#The enemy
#One instancez only, with all the properties of the current player.
import pygame
from entity import Entity
import custom_math as cm

class Enemy(Entity):

    def __init__(self,buffer,pos=[0,0],speed=1):
        Entity.__init__(self,buffer,pos,speed)

    def draw(self):
        pygame.draw.rect(self.buffer, [255,0,0], pygame.Rect(self.pos[0]-8, self.pos[1]-8, 16, 16))

    def update(self,player_pos):
        self.entity_update()
        self.movement(player_pos)


    def movement(self,player_pos):
        self.gotoward(player_pos)