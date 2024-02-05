import pygame

from grille import Grille


class ImportMenu():

  def __init__(self, grille=Grille()):
    self.templates = ["Grille Vide","planneur", "grille", "Canon"]
    self.grille = grille
    self.grilleToChange = None
    self.logo = pygame.image.load("assets/logo.png")
    self.logo = pygame.transform.scale(self.logo, (200, 100))

  def switchGrille(self, grilleName):
    self.grille.showImportMenu = False
    self.grilleToChange = grilleName
    print("La grille a été changée pour :", grilleName)

  def drawMenu(self, events):
    width, height = self.grille.screen.get_size()

    pygame.draw.rect(
        self.grille.screen,
        (100, 100, 100),  # Dark gray
        (25 + 100, 25, width - 25 * 2 - 100 * 2,
         height - self.grille.buttonsOffset - 25 * 2),
        0,
        6)

    # draw logo
    self.grille.screen.blit(self.logo, (150, 20))

    # Draw buttons
    margin = 0
    for templateName in self.templates:
      self.grille.draw_button(events, 25 + (width - 25 * 2) // 2,
                              100 + 25 + margin, templateName, (244, 147, 144),
                              self.switchGrille, templateName)
      margin += 35 + 5
