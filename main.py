import pygame
from grille import Grille
from planneur import grille_planneur
from canonplanneur import canon_a_planeur
# Boucle principale
grille = Grille()
#grille = grille_planneur()
#grille = canon_a_planeur()
while grille.running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      grille.running = False

  grille.screen.fill((255, 255, 255))
  grille.update_grille()
  pygame.display.flip()
  grille.set_fps(10)
