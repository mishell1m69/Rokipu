#The player class
#One instance only, with all the properties of the current player.
import pygame
from entity import Entity
import settings
import custom_math as cm

class Player(Entity):

    def __init__(self,buffer,pos=[0,0],speed=1):
        Entity.__init__(self,buffer,pos,speed)

    def draw(self):
        pygame.draw.rect(self.buffer, [0,255,0], pygame.Rect(self.pos[0]-8, self.pos[1]-8, 16, 16))

    def update(self):
        self.entity_update()
        self.movement()


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[settings.KEYS["UP"]]:
            self.momentum[1]-=self.speed/9
        if keys[settings.KEYS["RIGHT"]]:
            self.momentum[0]+=self.speed/9
        if keys[settings.KEYS["LEFT"]]:
            self.momentum[0]-=self.speed/9
        if keys[settings.KEYS["DOWN"]]:
            self.momentum[1]+=self.speed/9