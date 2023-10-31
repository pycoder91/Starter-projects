import pygame
import sys

# Set up the screen
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Battle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tank properties
tank_blue = pygame.image.load("blue_tank.png")  # Replace with your tank image
tank_red = pygame.image.load("red_tank.png")  # Replace with your tank image
tank_blue = pygame.transform.scale(tank_blue, (50, 50))  # Adjust size as per your tank image
tank_red = pygame.transform.scale(tank_red, (50, 50))  # Adjust size as per your tank image

tank_blue_x, tank_blue_y = 100, HEIGHT - 100
tank_red_x, tank_red_y = WIDTH - 150, HEIGHT - 100

# Bullets
bullet_radius = 5
bullet_speed = 5
blue_bullet = None
red_bullet = None

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Red tank fires
                red_bullet = (tank_red_x, tank_red_y)
            if event.key == pygame.K_RETURN:  # Blue tank fires
                blue_bullet = (tank_blue_x, tank_blue_y)

    keys = pygame.key.get_pressed()

    # Movement controls for blue tank
    if keys[pygame.K_LEFT]:
        tank_blue_x -= 5
    if keys[pygame.K_RIGHT]:
        tank_blue_x += 5

    # Movement controls for red tank
    if keys[pygame.K_a]:
        tank_red_x -= 5
    if keys[pygame.K_d]:
        tank_red_x += 5

    # Display tanks and bullets
    screen.blit(tank_blue, (tank_blue_x, tank_blue_y))
    screen.blit(tank_red, (tank_red_x, tank_red_y))

    if blue_bullet:
        pygame.draw.circle(screen, BLUE, blue_bullet, bullet_radius)
        blue_bullet = (blue_bullet[0], blue_bullet[1] - bullet_speed)
        if blue_bullet[1] < 0:
            blue_bullet = None

    if red_bullet:
        pygame.draw.circle(screen, RED, red_bullet, bullet_radius)
        red_bullet = (red_bullet[0], red_bullet[1] - bullet_speed)
        if red_bullet[1] < 0:
            red_bullet = None

    pygame.display.flip()

pygame.quit()
sys.exit()
