import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colliding Spheres")

clock = pygame.time.Clock()

class Sphere:
    def __init__(self):
        self.radius = random.randint(10, 20)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.gravity = 0.1

    def update(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= self.radius or self.x >= width - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius or self.y >= height - self.radius:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

spheres = [Sphere() for _ in range(30)]

def check_collision(s1, s2):
    dx = s1.x - s2.x
    dy = s1.y - s2.y
    distance = (dx ** 2 + dy ** 2) ** 0.5
    if distance <= s1.radius + s2.radius:
        s1.speed_x, s2.speed_x = s2.speed_x, s1.speed_x
        s1.speed_y, s2.speed_y = s2.speed_y, s1.speed_y

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for sphere in spheres:
        sphere.update()
        sphere.draw()

    for i, s1 in enumerate(spheres):
        for s2 in spheres[i+1:]:
            check_collision(s1, s2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()