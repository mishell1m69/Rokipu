import pygame
import random
import math

# Initialization
pygame.init()

# Screen parameters
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particles")

# Particle list
particles = []

class Particle:
    def __init__(self, buffer, pos, lifespan, color, speed, direction, size):
        self.buffer = buffer
        self.pos = pos
        self.fulllife = lifespan
        self.lifespan = lifespan
        self.color = color
        self.speed = speed
        self.direction = direction
        self.size = size

    def update(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            return True
        dx = self.speed * math.cos(math.radians(self.direction))
        dy = -self.speed * math.sin(math.radians(self.direction))
        self.pos[0] += dx
        self.pos[1] += dy
        self.color = [
            max(min(self.color[0], 255), 0),
            max(min(self.color[1], 255), 0),
            max(min(self.color[2], 255), 0),
        ]
        pygame.draw.circle(self.buffer, self.color, (int(self.pos[0]), int(self.pos[1])), self.size)

# Gauge parameters
gauge_min, gauge_max = 10, 100
gauge_value = gauge_min

# Mouse interaction variables
mouse_dragging = False

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_dragging = False

    # Update gauge value based on mouse position
    if mouse_dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        normalized_y = max(0, min(mouse_y, height))  # Ensure it's within screen bounds
        gauge_value = int((normalized_y / height) * (gauge_max - gauge_min) + gauge_min)

    # Create new particles based on gauge value
    for _ in range(gauge_value):
        x, y = random.randint(0, width), random.randint(0, height)
        lifespan = random.randint(50, 200)
        color = [random.randint(0, 255) for _ in range(3)]
        speed = random.uniform(1, 3)
        direction = random.uniform(0, 360)
        size = random.randint(2, 5)
        particles.append(Particle(screen, [x, y], lifespan, color, speed, direction, size))

    # Update and display particles
    screen.fill((0, 0, 0))
    for p in particles:
        if p.update():
            particles.remove(p)  # Remove particles that have reached the end of their lifespan

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
