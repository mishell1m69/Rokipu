import pygame
import random
import constants as ct


def update_particles_list(l):
    for i, particle in reversed(list(enumerate(l))):
        if particle.update():
            l.pop(i)

def draw_particles_list(l):
    for particle in l:
        particle.draw()

def circle(col,pos,size):
    pygame.draw.circle(ct.RENDER_BUFFER, col, pos, size)

class Particle:
    
    """
    A single particle. quite useless on its own.
    Should rather be used in a particle system
    """

    
    def __init__(self,pos,momentum,momentumVar,momentumLifeEffect,lifespan,force,color,colvar=[0,0,0],shapefunc=circle):
        """initialise a new particle based on input args

        Args:
            pos (list(float,float)): the pos at which the particle spawns
            momentum (list(float,float)): default particle momentum
            momentumVar (list(float,float)): amount of random variation to momentum
            momentumLifeEffect (list(float,float)): effect of fullLife on momentum
            lifespan (int): number of frames the particle will be alive
            shapefunc (function, optional): the function that will be called when drawing the particle. Can either be geometric shapes or a sprite. Defaults to circle.
            force (list(float,float)): the force that is applied to the particle each frame
            color (list(float,float,float)): default particle color.
            colvar (list(float,float,float), optional): color variation each frame. Defaults to [0,0,0]
        """
        self.col = color
        self.pos = pos
        self.shapefunc = shapefunc
        self.momentum = momentum
        self.momentumVar = momentumVar
        self.momentumLifeEffect = momentumLifeEffect
        self.fullLife = lifespan
        self.lifespan = lifespan
        self.colvar = colvar

    
    def update(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            return True
        #Random aaaaah shit for a fire particle
        self.pos[0] += (random.random()-0.5)*(self.fullLife*self.momentumLifeEffect[1])
        self.pos[1] += self.momentum[1]*random.random()*0.5*(self.fullLife*self.momentumLifeEffect[1])

        self.col[0] += (255/self.fullLife)*self.colvar[0]
        self.col[1] += (255/self.fullLife)*self.colvar[1]
        self.col[2] += (255/self.fullLife)*self.colvar[2]
        
        self.col=[min(max(self.col[0],0),255),min(max(self.col[1],0),255),min(max(self.col[2],0),255)] #makes sure the values never go over limits [0,255]

    def draw(self):
        self.shapefunc(self.col, self.pos, self.lifespan/20+0.5)
        
        
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

    

        
