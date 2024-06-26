############################################################################################
# Développé par Hugo et Brian et Léo
# Le programme sert à lancer le menu pour démarrer ou reprendre une partie, regarder les statistiques, jouer en multijoueurs.
############################################################################################
# Améliorations ou ajouts à faire :
#   - Ouvrir une nouvelle page quand le bouton statistique est appuyé pour pouvoir afficher les statistiques.
#   - Afficher les statistiques (regarder discord dans générale pour voir les statistiques à mettre).
#   
#
# Ajouts potentiels (non obligatoires) :
#   - création d'un document dans le programme qui explique les statistiques choisit et pourquoi.
############################################################################################


#-------------------------------------- IMPORTATIONS --------------------------------------#
import pygame
from MainGraphique import main
import subprocess
from database import init_bdd
#------------------------------------------------------------------------------------------#

# Initialiser Pygame
pygame.init()

# Récupérer les dimensions de l'écran
infoObject = pygame.display.Info()
largeur_ecran, hauteur_ecran = infoObject.current_w, infoObject.current_h

# Définir les dimensions de la fenêtre
largeur_fenetre, hauteur_fenetre = int(largeur_ecran ), int(hauteur_ecran )

# Créer la fenêtre
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

# Définir les couleurs
white = (255, 255, 255)
black = (0, 0, 0)

bdd = init_bdd()

def main_menu():
    
    # Charger l'image de fond et la redimensionner
    background_image = pygame.image.load('./images/background.png')
    background_image = pygame.transform.scale(background_image, (largeur_ecran , hauteur_ecran ))

    # Charger les images des boutons et les redimensionner
    button_width, button_height = int(largeur_fenetre * 0.20), int(hauteur_fenetre * 0.1)

    play_button_image = pygame.image.load('./images/Boutons/button_rect.png')
    play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))

    save_button_image = pygame.image.load('./images/Boutons/button_rect.png')
    save_button_image = pygame.transform.scale(save_button_image, (button_width, button_height))

    quit_button_image = pygame.image.load('./images/Boutons/button_rect.png')
    quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))

    stats_button_image = pygame.image.load('./images/Boutons/button_rect.png')
    stats_button_image = pygame.transform.scale(stats_button_image, (button_width, button_height))

    Multijoueur_button_image = pygame.image.load('./images/Boutons/button_rect.png')
    Multijoueur_button_image = pygame.transform.scale(Multijoueur_button_image, (button_width, button_height))

    # Créer les objets Rect pour représenter la position et la taille des boutons
    play_button_rect = play_button_image.get_rect()
    play_button_rect.center = (int(largeur_fenetre // 2), int((hauteur_fenetre // 2) * 0.30),)

    Multijoueur_button_rect = Multijoueur_button_image.get_rect()
    Multijoueur_button_rect.center = (int(largeur_fenetre // 2), int((hauteur_fenetre // 2) * 0.65),)

    save_button_rect = save_button_image.get_rect()
    save_button_rect.center = (int(largeur_fenetre // 2), int(hauteur_fenetre // 2))

    quit_button_rect = quit_button_image.get_rect()
    quit_button_rect.center = (int(largeur_fenetre // 2),int((hauteur_fenetre // 2 * 1.35)),)

    stats_button_rect = stats_button_image.get_rect()
    stats_button_rect.center = (int(largeur_fenetre // 2), int((hauteur_fenetre // 2) * 1.70),)

    # Créer les surfaces de texte pour les boutons
    font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", int(largeur_fenetre // 30))
    play_button_text = font.render('Jouer', True, black)
    save_button_text = font.render('Reprendre partie', True, black)
    quit_button_text = font.render('Quitter', True, black)
    stats_button_text = font.render('Statistique', True, black)
    Multijoueur_button_text = font.render('Multijoueur', True, black)

    play_button_text_rect = play_button_text.get_rect()
    save_button_text_rect = save_button_text.get_rect()
    quit_button_text_rect = quit_button_text.get_rect()
    stats_button_text_rect = stats_button_text.get_rect()
    Multijoueur_button_text_rect = Multijoueur_button_text.get_rect()

    # Centrez le texte sur les boutons
    play_button_text_rect.center = play_button_rect.center
    save_button_text_rect.center = save_button_rect.center
    quit_button_text_rect.center = quit_button_rect.center
    stats_button_text_rect.center = stats_button_rect.center
    Multijoueur_button_text_rect.center = Multijoueur_button_rect.center

    # Boucle principale
    while True:
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Vérifier si un bouton a été cliqué
                if play_button_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "MainGraphique.py"])
                elif Multijoueur_button_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "MainGraphiqueReseau.py"])
                elif save_button_rect.collidepoint(event.pos):
                    main(True)
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
                elif stats_button_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "StatsGraphique.py"])
                    
        screen.blit(background_image, (0, 0))

        # Dessiner les images des boutons
        screen.blit(play_button_image, play_button_rect)
        screen.blit(save_button_image, save_button_rect)
        screen.blit(quit_button_image, quit_button_rect)
        screen.blit(stats_button_image, stats_button_rect)
        screen.blit(Multijoueur_button_image, Multijoueur_button_rect)

        # Dessiner les surfaces de texte centrées sur les boutons
        screen.blit(play_button_text, play_button_text_rect)
        screen.blit(save_button_text, save_button_text_rect)
        screen.blit(quit_button_text, quit_button_text_rect)
        screen.blit(stats_button_text, stats_button_text_rect)
        screen.blit(Multijoueur_button_text, Multijoueur_button_text_rect)

        # Rafraîchir l'écran
        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
