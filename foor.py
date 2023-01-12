import pygame
pygame.init()
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Floor Georg-Johann Seeder")
screen.fill
([0, 0, 0])
pygame.draw.circle(screen, [255, 255, 0],  [150, 150], 40, 0)
pygame.draw.circle(screen, [255, 0, 0], [150, 60], 40, 0)
pygame.draw.circle(screen, [0, 255, 0], [150, 240], 40, 0)
pygame.draw.rect(screen, [128, 128, 128], [100, 10, 100, 280], 2)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

