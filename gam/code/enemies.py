"""
The enemy
"""

import pygame
from entity import Entity
import utlis.custom_math as cm
import constants as ct


class Enemy(Entity):

    def __init__(self, pos=[0, 0], speed = 1):
        Entity.__init__(self, pos, speed)

    
    def draw(self):
        pygame.draw.rect(ct.RENDER_BUFFER, [255, 0, 0], pygame.Rect(self.pos[0] - 8, self.pos[1] - 8, 16, 16))

    
    def movement(self, player_pos):
        self.gotoward(player_pos)

    
    def update(self, player_pos):
        self.entity_update()
        self.movement(player_pos)

