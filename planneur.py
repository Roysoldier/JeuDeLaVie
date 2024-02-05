import pygame
from grille import Grille


def grille_planneur():
  grille = Grille(probLife=0, typeGrille='planneur')
  planeur_pattern = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]

  start_row = (grille.cellNbr[0] - len(planeur_pattern)) // 2
  start_col = (grille.cellNbr[1] - len(planeur_pattern[0])) // 2

  for i in range(len(planeur_pattern)):
    for j in range(len(planeur_pattern[0])):
      grille.table[start_row + i][start_col + j] = planeur_pattern[i][j]

  grille.baseGrille = grille.table
  return grille
