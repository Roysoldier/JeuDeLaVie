import pygame
from grille import Grille
from planneur import grille_planneur
from importMenu import ImportMenu
from canonplanneur import gun_glider

pygame.display.set_caption("Jeu de La Mort")
pygame.display.set_icon(pygame.image.load("assets/favicon.png"))


def get_grille(grille='grille'):
  if grille == 'planneur':
    return grille_planneur()
  elif grille == 'Canon':
    return gun_glider()
  elif grille == "Grille Vide":
    return Grille(probLife=0,typeGrille="Grille Vide")
  else:
    return Grille()


grille = get_grille()
importMenu = ImportMenu(grille)
# Boucle principale
while grille.running:

  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      grille.running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      # Vérifier si un rectangle a été cliqué
      x, y = event.pos
      for rect in grille.allCase:
          if rect[0].collidepoint(x, y):
              if grille.table[rect[1]][rect[2]] == 1: 
                grille.table[rect[1]][rect[2]] = 0
              else: 
                grille.table[rect[1]][rect[2]] = 1
              
  grille.screen.fill((255, 255, 255))
  grille.update_grille()

  # Buttons
  width, height = grille.screen.get_size()
  magicValue = 70  # According to aproxima
  widthOffset = width // 3

  grille.draw_button(
      events, width // 2, height - 50 - (50 // 2),
      "BORDURES ACTIVÉES" if grille.border else "BORDURES DÉSACTIVÉES",
      (21, 113, 69) if grille.border else (119, 32, 20),
      grille.switchBordersState)

  grille.draw_button(events, widthOffset * 0 + magicValue, height - (50 // 2),
                     "ARRÊTER" if grille.inGame else "LANCER",
                     (119, 32, 20) if grille.inGame else (21, 113, 69),
                     grille.switchState)

  if not grille.inGame:
    grille.draw_button(events, widthOffset * 1 + magicValue,
                       height - (50 // 2), "RÉINITIALISER", (79, 53, 165),
                       grille.reset_grille)

    grille.draw_button(events, widthOffset * 2 + magicValue,
                       height - (50 // 2), "IMPORTER", (244, 147, 144),
                       grille.switchShowImportMenu)

  if grille.showImportMenu:
    importMenu.drawMenu(events)
  if importMenu.grilleToChange is not None:
    grille = get_grille(importMenu.grilleToChange)
    importMenu.grilleToChange = None

  pygame.display.flip()
  grille.set_fps(10)
