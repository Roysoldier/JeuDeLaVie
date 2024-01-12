import pygame
from grille import Grille

def canon_a_planeur():
    # Création de l'objet Grille
    grille = Grille(probLife=0)

    # Ajout du canon à planeur au centre de la grille
    canon_pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

    start_row = (grille.cellNbr[0] - len(canon_pattern)) // 2
    start_col = (grille.cellNbr[1] - len(canon_pattern[0])) // 2

    for i in range(len(canon_pattern)):
        for j in range(len(canon_pattern[0])):
            grille.table[start_row + i][start_col + j] = canon_pattern[i][j]

    return grille


