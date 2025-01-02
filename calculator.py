import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52
PIPE_HEIGHT = 320
PIPE_GAP = 150
GRAVITY = 0.5
FLAP_STRENGTH = -10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
bird_image = pygame.image.load('file:///C:/Users/User/OneDrive/Pictures/png-transparent-flappy-bird-video-games-android-app-store-score-logo-yellow-smile.png')  # Replace with your bird image path
pipe_image = pygame.image.load('file:///C:/Users/User/OneDrive/Pictures/FLAPPYCHOMS.JPG.webp')  # Replace with your pipe image path

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        screen.blit(bird_image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.passed = False

    def update(self):
        self.x -= 5

    def draw(self, screen):
        screen.blit(pipe_image, (self.x, self.height - PIPE_HEIGHT))
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

# Main game function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        screen.fill(WHITE)
        bird.update()
        bird.draw(screen)

        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)

            # Check for collision
            if (bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH):
                if (bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.height + PIPE_GAP):
                    running = False

            # Check if bird passed the pipe
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                score += 1

        # Add new pipes
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())

        # Remove off-screen pipes
        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

    pygame.quit()

if __name__ == "__main__":
    main()