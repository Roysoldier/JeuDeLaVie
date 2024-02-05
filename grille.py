import pygame

pygame.init()

import pygame
from random import randint

class Case():
  def __init__(self,x,y,ibLigne,idCase):
    self.x = x
    self.y = y 
    self.idLigne = ibLigne
    self.idCase = idCase

class Grille():
  """
      Classe Grille pour le jeu de la vie.
      """

  nombre = 0

  def __init__(self,
               cellWidth=10,
               cellNbr=(50, 50),
               color=(10, 10, 10),
               buttonsOffset=100,
               probLife=5,
               typeGrille="grille",
               border=True):
    """
            Initialise une instance de la classe Grille.

            Args:
                cellWidth (int): Largeur d'une cellule en pixels.
                cellNbr (tuple): Nombre de cellules en largeur et en hauteur (colonnes, lignes).
                color (tuple): Couleur de la grille au format RGB.
                buttonsOffset (int): Décalage vertical pour les boutons.
                probLife (int): Probabilité initiale pour qu'une cellule soit en vie.
                typeGrille (str): Type de grille ("grille" ou "base").
                border (bool): Si True, applique des bordures au bord de la grille.

            Attributes:
                cellWidth (int): Largeur d'une cellule en pixels.
                cellNbr (tuple): Nombre de cellules en largeur et en hauteur (colonnes, lignes).
                color (tuple): Couleur de la grille au format RGB.
                buttons_font: Police d'écriture pour les boutons.
                buttonsOffset (int): Décalage vertical pour les boutons.
                inGame (bool): Indique si le jeu est en cours.
                typeGrille (str): Type de grille ("grille" ou "base").
                showImportMenu (bool): Indique si le menu d'importation est affiché.
                border (bool): Si True, applique des bordures au bord de la grille.
                baseGrille: Grille de base pour la réinitialisation.
                screen: Surface d'affichage pygame.
                clock: Objet Clock de pygame pour contrôler les FPS.
                running (bool): Indique si la boucle principale est en cours.
                nombre (int): Nombre d'instances de la classe Grille.
                table: Grille principale du jeu de la vie.
            """
    # Initialisation des attributs
    self.cellWidth = cellWidth
    self.cellNbr = cellNbr
    self.color = color
    self.buttons_font = pygame.font.SysFont('arial', 15)
    self.buttonsOffset = buttonsOffset
    self.inGame = False
    self.typeGrille = typeGrille
    self.showImportMenu = False
    self.border = border
    self.baseGrille = []
    self.allCase = []
    # Initialisation de pygame
    pygame.init()
    self.screen = pygame.display.set_mode(
        (cellWidth * cellNbr[0], cellWidth * cellNbr[1] + buttonsOffset))
    self.clock = pygame.time.Clock()
    self.running = True
    self.nombre += 1
    self.prob = probLife
    self.table = self.set_grille_binaire()

  def set_fps(self, fps):
    """
            Définit le nombre d'images par seconde.

            Args:
                fps (int): Nombre d'images par seconde.
            """
    self.clock.tick(fps)

  def set_grille_binaire(self):
    """
            Initialise une grille binaire avec une probabilité donnée.

            Args:
                prob (int): Probabilité qu'une cellule soit en vie.

            Returns:
                list: Grille binaire générée aléatoirement.
            """
    self.table = [[
        1 if randint(0, self.prob) == 1 else 0 for v in range(self.cellNbr[1])
    ] for h in range(self.cellNbr[0])]
    return self.table

  def switchState(self):
    """
            Inverse l'état du jeu (en cours ou en pause).
            """
    self.inGame = not self.inGame

  def switchBordersState(self):
    """
            Inverse l'état des bordures.
            """
    self.border = not self.border

  def switchShowImportMenu(self):
    """
            Inverse l'état d'affichage du menu d'importation.
            """
    self.showImportMenu = not self.showImportMenu

  def draw_button(self, events, x, y, text, color, action, parameter=None):
    """
            Dessine un bouton et gère les événements de clic.

            Args:
                events (list): Liste des événements pygame.
                x (int): Coordonnée x du bouton.
                y (int): Coordonnée y du bouton.
                text (str): Texte du bouton.
                color (tuple): Couleur du bouton au format RGB.
                action (function): Fonction à exécuter lors du clic.
                parameter: Paramètre optionnel à passer à la fonction d'action.
            """
    text_image = self.buttons_font.render(text, True, (255, 255, 255))  # Blanc
    text_size = self.buttons_font.size(text)

    rect = pygame.Rect(x - text_size[0], y - text_size[1], text_size[0] * 2,
                       text_size[1] * 2)

    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Clic gauche
          if rect.collidepoint(event.pos):
            if not parameter:
              action()
            else:
              action(parameter)

    pygame.draw.rect(self.screen, color, rect, 0, 4)
    self.screen.blit(text_image,
                     (x - text_size[0] // 2, y - text_size[1] // 2))

  def draw_grille(self):
    """
            Dessine la grille sur la surface d'affichage.
            """
    y = 0
    self.allCase = []
    for indexLigne , line in enumerate(self.table):
      x = 0
      for indexCase, case in enumerate(line):
        rect = pygame.Rect(x, y, self.cellWidth, self.cellWidth)
        pygame.draw.rect(self.screen,
                         self.color,rect,
                         width=abs(case - 1))
        self.allCase.append((rect,indexLigne,indexCase))
        x += self.cellWidth
      y += self.cellWidth

  def check_life(self):
    """
            Applique les règles du jeu de la vie pour déterminer l'état suivant de chaque cellule.
            """
    copie = [[cellule for cellule in ligne] for ligne in self.table]

    for indexLigne, ligne in enumerate(self.table):
      for indexCellule, cellule in enumerate(ligne):
        voisinVivant = 0

        voisin = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                  (1, 1)]
        if self.border:
          for x, y in voisin:
            new_row, new_col = indexLigne + x, indexCellule + y

            # Ajouter des bordures
            if 0 <= new_row < self.cellNbr[0] and 0 <= new_col < self.cellNbr[
                1]:
              voisinVivant += self.table[new_row][new_col]
        else:
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
    """
            Met à jour la grille en fonction de l'état du jeu et la dessine.
            """
    if self.inGame:
      self.check_life()
    self.draw_grille()

  def reset_grille(self):
    """
            Réinitialise la grille en fonction du type choisi.
            """
    if self.typeGrille == "grille" or self.typeGrille == "Grille Vide":
      self.set_grille_binaire()
    else:
      print(self.baseGrille)
      self.table = self.baseGrille

  def __str__(self):
    """
            Retourne une représentation textuelle de l'objet Grille.
            """
    return f"Objet grille permettant le fonctionnement du jeu de la vie. Grille initialisée en : {self.cellNbr}"
