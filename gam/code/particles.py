import pygame
import random

import constants as ct
def update_particles_list(l):
    for i, particle in reversed(list(enumerate(l))):
        if particle.update():
            l.pop(i)

class Particle:
    """A single particle. quite useless on its own.
    Should rather be used in a particle system
    """
    def __init__(self,pos,lifespan):
        self.col=[255,255,200]
        self.pos=pos
        self.fulllife=lifespan
        self.lifespan=lifespan
        
    def update(self):
        self.lifespan-=1
        if self.lifespan<=0:
            return True
        #Random aaaaah shit for a fire particle
        self.pos[1]-=random.random()*0.5*(self.fulllife/100)
        self.pos[0]+=(random.random()-0.5)*(self.fulllife/100)
        self.col[0]-=(255/self.fulllife)*0.4
        self.col[1]-=(255/self.fulllife)*1.1
        self.col[2]-=(255/self.fulllife)*2
        self.col=[min(max(self.col[0],0),255),min(max(self.col[1],0),255),min(max(self.col[2],0),255)] #makes sure the values never go over limits [0,255]
        pygame.draw.circle(ct.RENDER_BUFFER, self.col, self.pos, self.lifespan/20+0.5)
        
        
        
class ParticleGenerator:
    """_summary_
    """
    
    def __init__(self):
        pass
        
class ParticleSystem:
    """A system that manages a group of particles
    Better if all particles have the same settings
    """
    def __init__(self,particleGenerator=None,particleList=[]):
        """Create a new ParticleSystem. In most cases it should have a generator but no list

        Args:
            particleGenerator (ParticleGenerator, optional): A tool that generates particles constantly based on some parameters. Defaults to None.
            particleList (list, optional): The list containing all particles. Giving it a value in the parameters should be used when only having a burst of particles at once. Defaults to [].
        """

    

        