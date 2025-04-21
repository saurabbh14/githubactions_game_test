import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Dino - Web Test")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill((255, 255, 255))
    msg = font.render("Ready for game start", True, (0, 0, 0))
    screen.blit(msg, (200, 140))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
