import pygame
from random import randint


class Grille():
  nombre = 0

  def __init__(self,
               cellWidth=10,
               cellNbr=(50, 50),
               color=(10, 10, 10),
               buttonsOffset=50,
               probLife=5):
    self.cellWidth = cellWidth
    self.cellNbr = cellNbr
    self.color = color

    # pygame setup
    pygame.init()
    self.screen = pygame.display.set_mode(
        (cellWidth * cellNbr[0], cellWidth * cellNbr[1] + buttonsOffset))
    self.clock = pygame.time.Clock()
    self.running = True
    self.nombre += 1
    self.table = self.set_grille_binaire(probLife)

  def set_fps(self, fps):
    self.clock.tick(fps)

  def set_grille_binaire(self, prob=5):
    self.table = [[
        1 if randint(0, prob) == 1 else 0 for v in range(self.cellNbr[1])
    ] for h in range(self.cellNbr[0])]
    return self.table

  def draw_grille(self):
    y = 0
    for line in self.table:
      x = 0
      for case in line:
        pygame.draw.rect(self.screen,
                         self.color, (x, y, self.cellWidth, self.cellWidth),
                         width=abs(case - 1))
        x += self.cellWidth
      y += self.cellWidth

  def check_life(self):
    copie = [[cell for cell in line] for line in self.table]

    for indexLigne, ligne in enumerate(self.table):
      for indexCellule, cellule in enumerate(ligne):
        voisinVivant = 0

        voisin = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                  (1, 1)]

        for x, y in voisin:
          new_row, new_col = (indexLigne + x) % self.cellNbr[0], (
              indexCellule + y) % self.cellNbr[1]
          voisinVivant += self.table[new_row][new_col]

        if cellule == 1:
          if voisinVivant < 2 or voisinVivant > 3:
            copie[indexLigne][indexCellule] = 0
        elif cellule == 0:
          if voisinVivant == 3:
            copie[indexLigne][indexCellule] = 1

    self.table = copie

  def update_grille(self):
    self.check_life()
    self.draw_grille()

    def __str__(self): 
        return f"Objet grille Permettant le focntionnement du jeu de la vie Grille initialiser en : {self.cellNbr} "
