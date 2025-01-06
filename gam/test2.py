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
    def __init__(self, buffer, pos, lifespan, start_color, end_color, speed, direction, size):
        self.buffer = buffer
        self.pos = pos
        self.fulllife = lifespan
        self.lifespan = lifespan
        self.start_color = start_color
        self.end_color = end_color
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

        # Interpolate color based on remaining lifespan
        t = 1 - (self.lifespan / self.fulllife)
        interp_color = [
            int((1 - t) * self.start_color[i] + t * self.end_color[i])
            for i in range(3)
        ]

        pygame.draw.circle(self.buffer, interp_color, (int(self.pos[0]), int(self.pos[1])), self.size)

# Parameters
gauge_min, gauge_max = 10, 100
gauge_value = gauge_min
mouse_dragging = False

# Initial parameter values
start_color = [255, 0, 200]
end_color = [255, 255, 0]
speed = 20
direction = 50
size = 3

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    start_color = [255, 200, 100]
    end_color = [255, random.randint(0,255), 0]
    speed = random.randint(1,5)
    direction = random.randint(70,110)
    size = random.randint(1,5)

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
        particles.append(Particle(screen, [x, y], lifespan, start_color, end_color, speed, direction, size))

    # Update and display particles
    screen.fill((0, 0, 0))
    for p in particles:
        if p.update():
            particles.remove(p)  # Remove particles that have reached the end of their lifespan

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
