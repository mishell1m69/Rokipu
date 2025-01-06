import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

particles = []

class Particle:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(5, 10)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def apply_gravity(self):
        self.speed_y += 0.1  # Increase the downward speed

for _ in range(100):
    particles.append(Particle())

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for particle in particles:
        dx = mouse_x - particle.x
        dy = mouse_y - particle.y
        dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
        particle.speed_x += 0.5 * dx / dist
        particle.speed_y += 0.5 * dy / dist
        particle.move()
        particle.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()