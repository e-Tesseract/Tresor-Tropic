############################################################################################
# développer par Brian
# le programme sert à crée un page noir avec du texte et de montré les données contenue sur la base de donné
############################################################################################
# amélioration ou ajouter à faire:
#   - 
#
# ajout potenciel(non obligatoire):
#   - optimisation
#   - commentaire à faire
############################################################################################

import pygame
import psycopg2
from database import init_bdd

# Initialiser Pygame
pygame.init()

# Récupérer les dimensions de l'écran
infoObject = pygame.display.Info()
largeur_ecran, hauteur_ecran = infoObject.current_w, infoObject.current_h

# Permettre de redimensionner la fenêtre 
taille_ajustee = 0.7

# Définir la taille de la fenêtre en pourcentage de la taille de l'écran
largeur_fenetre, hauteur_fenetre = int(largeur_ecran * taille_ajustee), int(hauteur_ecran * taille_ajustee)

# Créer une fenêtre
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Définir la couleur noire
black = (0, 0, 0)

# Définir la couleur du texte
white = (255, 255, 255)

# Créer une police de texte
font = pygame.font.Font(None, 36)

# Créer une instance de la classe init_bdd pour accéder à la base de données
bdd = init_bdd()
curseur = bdd.connexion.cursor()

total= 0
partie= 0
total_gagnants = 0
echelles= 0
resulta= 0
moyenne= 0

curseur.execute("SELECT total_cases_parcourues()")
total = curseur.fetchone()[0]

curseur.execute("SELECT MAX(id_partie) FROM partie;")
partie = curseur.fetchone()[0]

curseur.execute("SELECT total_deplacements_joueurs_gagnants()")
total_gagnants = curseur.fetchone()[0]

curseur.execute("SELECT count(*) FROM choisit where special='echelle'")
echelles = curseur.fetchone()[0]

curseur.execute("SELECT count_resultats()")
resulta = curseur.fetchone()[0]

curseur.execute("SELECT moyenne_des()")
moyenne = curseur.fetchone()[0]

# Liste des lignes de texte à afficher
lines = [
    ("Nombre de case totales franchises", total),
    ("Nombre de parties joués", partie),
    ("Record du nombre de cases minimum et max que quelqu'un a fait pour gagner", total_gagnants),
    ("Nombre de cases échelles empruntés", echelles),
    ("Nombre de victoire et défaite face aux monstres", resulta),
    ("Moyenne que les joueurs tirent quand ils lancent les dés", moyenne),
]

# Calculer la position verticale de chaque ligne de texte
vertical_spacing = 50
y = (hauteur_fenetre - (len(lines) * vertical_spacing)) / 2

# Remplir l'écran avec la couleur noire
screen.fill(black)

# Dessiner chaque ligne de texte
for line in lines:
    if isinstance(line, tuple):
        # Si la ligne est un tuple, elle contient le texte et le total des cases parcourues
        text = f"{line[0]} : {line[1]}" if line[1] is not None else line[0]
    else:
        # Sinon, la ligne contient uniquement du texte
        text = line
    
    # Convertir le texte en unicode
    text = str(text)

    # Créer une surface de texte
    text_surface = font.render(text, True, white)
    # Obtenir le rectangle englobant de la surface de texte
    text_rect = text_surface.get_rect()
    # Centrer le rectangle de texte horizontalement
    text_rect.centerx = largeur_fenetre // 2
    # Définir la position verticale du rectangle de texte
    text_rect.centery = y
    # Dessiner la surface de texte sur l'écran
    screen.blit(text_surface, text_rect)
    # Augmenter la position verticale pour la prochaine ligne de texte
    y += vertical_spacing

# Actualiser l'écran
pygame.display.flip()

# Boucle principale du programme
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quitter Pygame
pygame.quit()