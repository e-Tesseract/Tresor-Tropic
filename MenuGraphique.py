import pygame
from MainGraphique import main

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

# Charger l'image de fond et la redimensionner
background_image = pygame.image.load('./images/background.png')
background_image = pygame.transform.scale(background_image, (largeur_ecran , hauteur_ecran ))


# Charger les images des boutons et les redimensionner
button_width, button_height = int(largeur_fenetre * 0.20), int(hauteur_fenetre * 0.1)

play_button_image = pygame.image.load('./images/button_rect.png')
play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))

settings_button_image = pygame.image.load('./images/button_rect.png')
settings_button_image = pygame.transform.scale(settings_button_image, (button_width, button_height))

quit_button_image = pygame.image.load('./images/button_rect.png')
quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))

# Créer les objets Rect pour représenter la position et la taille des boutons
play_button_rect = play_button_image.get_rect()
play_button_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 0.65)

settings_button_rect = settings_button_image.get_rect()
settings_button_rect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)

quit_button_rect = quit_button_image.get_rect()
quit_button_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 1.35)


# Créer les surfaces de texte pour les boutons
font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 30)
play_button_text = font.render('Jouer', True, black)
settings_button_text = font.render('Paramètres', True, black)
quit_button_text = font.render('Quitter', True, black)

# Obtenez les rectangles des surfaces de texte
play_button_text_rect = play_button_text.get_rect()
settings_button_text_rect = settings_button_text.get_rect()
quit_button_text_rect = quit_button_text.get_rect()

# Centrez le texte sur les boutons
play_button_text_rect.center = play_button_rect.center
settings_button_text_rect.center = settings_button_rect.center
quit_button_text_rect.center = quit_button_rect.center

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
                print('Jouer !')
                main()
            elif settings_button_rect.collidepoint(event.pos):
                print('Paramètres')
            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                quit()

    screen.blit(background_image, (0, 0))


    # Dessiner les images des boutons
    screen.blit(play_button_image, play_button_rect)
    screen.blit(settings_button_image, settings_button_rect)
    screen.blit(quit_button_image, quit_button_rect)

    # Dessiner les surfaces de texte centrées sur les boutons
    screen.blit(play_button_text, play_button_text_rect)
    screen.blit(settings_button_text, settings_button_text_rect)
    screen.blit(quit_button_text, quit_button_text_rect)

    # Rafraîchir l'écran
    pygame.display.flip()