import pygame
from sense_hat import SenseHat
from pygame.locals import *
from random import randint

# creer une variable 'sense' interagir avec le sense hat
sense = SenseHat()

# initialize pygame
pygame.init()
pygame.display.set_mode((640, 480))

# incarner, representer qu'est-ce qu'un joueur ?
# pseudo, attaque, vie, x, y, z...
# deplacer(), attaquer(), recuperer pseudo, son attaque, ...
class Player():
    
    # definir le code lorsqu'un nouveau joueur apparait
    def __init__(self, pseudo):
        # code
        self.pseudo = pseudo
        self.x = 0
        self.y = 7
        
    # methodes permettant au joueur d'interagir avec l'environnement
    def get_pseudo(self):
        return self.pseudo
    
    def move_left(self):
        self.x -= 1
        
    def move_right(self):
        self.x += 1
        
    def move_up(self):
        self.y -= 1
        
    def move_down(self):
        self.y += 1
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
# incarner, representer qu'est-ce qu'un objectif/point
# coordonnées en x, y
# recuperer ces coordonnées, get_x, get_y, verifier la capture
class Objective():
    
    # fonction qui s'initialize lorsqu'on creer un objectif
    def __init__(self):
        self.x = randint(0, 7)
        self.y = randint(0, 7)
    
    # methodes pour recuperer des informations sur l'objectif
    def random_place(self):
        self.x = randint(0, 7)
        self.y = randint(0, 7)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def check_capture(self, player):
        return player.get_x() == self.x and player.get_y() == self.y
    
# creer une nouvelle instance du jeu
running = True
player = Player("Vinetos")
objective = Objective()
points = 0
print("Bienvenue au joueur ", player.get_pseudo())

# placer un pixel de couleur orange sur cette matrice aux coordonnées
# du joueur

sense.clear()

# la couleur de l'objectif
obj_color = (140, 140, 140)
sense.set_pixel(objective.get_x(), objective.get_y(), obj_color)

# la couleur du joueur
color = (229, 141, 41)
player_x = player.get_x()
player_y = player.get_y()
sense.set_pixel(player_x, player_y, color)

# boucle du jeu
# tache qui va se repeter tant que le jeu est cours d'execution
# - actualiser le jeu sur la matrice
# - verifier les evenements du joystick
# - faire la detection de victoire
while running is True:
    
    # boucle qui va verifier les evenements du joystick
    for event in pygame.event.get():
        
        # verifications
        if event.type == QUIT:
            # le joueur essaye de quitter le jeu
            running = False
            print("Bye bye !")
        elif event.type == KEYDOWN:
            # le joueur essaye d'interagir avec le joystick
            if event.key == K_LEFT and player.get_x() > 0:
                print("gauche")
                player.move_left()
            elif event.key == K_RIGHT and player.get_x() < 7:
                print("droite")
                player.move_right()
            elif event.key == K_UP and player.get_y() > 0:
                print("haut")
                player.move_up()
            elif event.key == K_DOWN and player.get_y() < 7:
                print("bas")
                player.move_down()
            # verifier la capture
            if objective.check_capture(player):
                print("capture !")
                # choisir un autre point pour notre objectif
                objective.random_place()
                points += 1
                # detection de victoire
                if points >= 3:
                    print("Victoire")
                    sense.clear()
                    sense.show_message("Bravo !")
                    points = 0
            # actualiser
            sense.clear()
            sense.set_pixel(player.get_x(), player.get_y(), color)
            sense.set_pixel(objective.get_x(), objective.get_y(), obj_color)
