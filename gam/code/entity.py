#The global entity class
#represents players, projectiles, enemies, allies...
import pygame

import utlis.custom_math as cm
import constants as ct
class Entity:
    def __init__(self,pos=[0,0],speed=1):
        self.pos=pos
        self.momentum=[0,0]
        self.speed=speed
        self.rotation=0
    
    def gotoward(self,pos):
        vect=cm.calcvect(self.pos,pos)
        self.pos[0]+=cm.normalize(vect,self.speed)[0]
        self.pos[1]+=cm.normalize(vect,self.speed)[1]
    
    def entity_update(self):
        if cm.getnorm(self.momentum)>self.speed:
            self.momentum=cm.normalize(self.momentum,self.speed)
        self.pos[0],self.pos[1]=self.pos[0]+self.momentum[0],self.pos[1]+self.momentum[1]
        self.momentum=[self.momentum[0]*0.9,self.momentum[1]*0.9] if cm.getnorm(self.momentum)>0.001 else [0,0]

    def draw(self):
        pygame.draw.rect(ct.RENDER_BUFFER, [255,255,255], pygame.Rect(self.pos[0]-8, self.pos[1]-8, 16, 16)) #Default entity renderer, should always be overriden