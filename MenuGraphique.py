import pygame
from MainGraphique import main
# Initialiser Pygame
pygame.init()

# Récupérer les dimensions de l'écran
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h


taille_ajustee = 1

# Définir les dimensions de la fenêtre
window_width, window_height = int(screen_width * taille_ajustee), int(screen_height * taille_ajustee)

# Créer la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))

# Définir les couleurs
white = (255, 255, 255)
black = (0, 0, 0)

# Charger l'image de fond et la redimensionner
background_image = pygame.image.load('./images/background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Charger les images des boutons et les redimensionner
button_width, button_height = int(window_width * 0.20), int(window_height * 0.1)

play_button_image = pygame.image.load('./images/button_rect.png')
play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))

settings_button_image = pygame.image.load('./images/button_rect.png')
settings_button_image = pygame.transform.scale(settings_button_image, (button_width, button_height))

quit_button_image = pygame.image.load('./images/button_rect.png')
quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))

# Créer les objets Rect pour représenter la position et la taille des boutons
play_button_rect = play_button_image.get_rect()
play_button_rect.center = (screen_width // 2, screen_height // 2 - 200)

settings_button_rect = settings_button_image.get_rect()
settings_button_rect.center = (screen_width // 2, screen_height // 2)

quit_button_rect = quit_button_image.get_rect()
quit_button_rect.center = (screen_width // 2, screen_height // 2 + 200)


# Créer les surfaces de texte pour les boutons
font = pygame.font.SysFont("BlackBeard", screen_width // 30)
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