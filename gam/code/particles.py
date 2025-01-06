import pygame
import random
def update_particles_list(l):
    for i, particle in reversed(list(enumerate(l))):
        if particle.update():
            l.pop(i)

class Particle:
    def __init__(self,buffer,pos,lifespan):
        self.buffer=buffer
        self.col=[255,255,200]
        self.pos=pos
        self.fulllife=lifespan
        self.lifespan=lifespan
        
    def update(self):
        self.lifespan-=1
        if self.lifespan<=0:
            return True
        self.pos[1]-=random.random()*0.5*(self.fulllife/100)
        self.pos[0]+=(random.random()-0.5)*(self.fulllife/100)
        self.col[0]-=(255/self.fulllife)*0.4
        self.col[1]-=(255/self.fulllife)*1.1
        self.col[2]-=(255/self.fulllife)*2
        self.col=[min(max(self.col[0],0),255),min(max(self.col[1],0),255),min(max(self.col[2],0),255)] #makes sure the values never go over limits [0,255]
        pygame.draw.circle(self.buffer, self.col, self.pos, self.lifespan/20+0.5)

    

        