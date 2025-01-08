"""
A file containing all constants needed
"""

import pygame


RENDER_BUFFER = None  #This is the original buffer where everything is rendered. Will be set to actual buffer on startup
GAME_DRAW_SIZE_X = 320  #The original width at which the game is rendered
GAME_DRAW_SIZE_Y = 180  #The original height at which the game is rendered
CLOCK = pygame.time.Clock()
TIME_SINCE_LAST_TICK=CLOCK.tick(30)

DEFAULT_FRICTION=0.9
