import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 60  # Size of each grid cell
GRID_MARGIN = 10  # Margin between grid cells
GRID_COLS = SCREEN_WIDTH // (GRID_SIZE + GRID_MARGIN)
GRID_ROWS = SCREEN_HEIGHT // (GRID_SIZE + GRID_MARGIN)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Square class
class Square:
    def __init__(self, x, y, size, color, name):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.name = name
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def show_name_popup(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and not self.dragging:
            font = pygame.font.Font(None, 24)
            text_surface = font.render(f"{self.name} ({self.rect.topleft})", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            pygame.draw.rect(screen, (200, 200, 200), text_rect)
            screen.blit(text_surface, text_rect.topleft)

    def snap_to_grid(self):
        # Calculate nearest grid position
        col = round(self.rect.left / (GRID_SIZE + GRID_MARGIN))
        row = round(self.rect.top / (GRID_SIZE + GRID_MARGIN))
        # Update square position
        self.rect.topleft = (col * (GRID_SIZE + GRID_MARGIN), row * (GRID_SIZE + GRID_MARGIN))

    def handle_drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                self.offset_x, self.offset_y = event.pos[0] - self.rect.left, event.pos[1] - self.rect.top
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.dragging:
                self.dragging = False
                self.snap_to_grid()
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.topleft = event.pos[0] - self.offset_x, event.pos[1] - self.offset_y

# Create some squares
squares = [
    Square(x, y, GRID_SIZE, color, f"Square {i+1}")
    for i, (x, y, color) in enumerate(
        [
            (100, 100, RED),
            (300, 200, GREEN),
            (500, 300, BLUE),
            (200, 400, YELLOW),
            (400, 100, PURPLE),
            # Add more squares as needed
        ]
    )
]

# Main loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Initialize screen
pygame.display.set_caption("Draggable Colored Squares")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for square in squares:
            square.handle_drag(event)

    # Draw grid (behind everything)
    screen.fill(WHITE)
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(
                col * (GRID_SIZE + GRID_MARGIN),
                row * (GRID_SIZE + GRID_MARGIN),
                GRID_SIZE,
                GRID_SIZE,
            )
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    # Draw everything (squares and popups)
    
    for square in squares:
        square.draw()
        square.show_name_popup(pygame.mouse.get_pos())

    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()