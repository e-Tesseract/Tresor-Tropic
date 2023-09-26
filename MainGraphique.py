import pygame

def main():
    pygame.init()

    # Récupérer les dimensions de l'écran
    infoObject = pygame.display.Info()
    screen_width, screen_height = infoObject.current_w, infoObject.current_h

    taille_ajustee = 0.9
    # Définir la taille de la fenêtre en pourcentage de la taille de l'écran
    window_width, window_height = int(screen_width * taille_ajustee), int(screen_height * taille_ajustee)

    # Créer une fenêtre de la taille définie
    screen = pygame.display.set_mode((window_width, window_height))

    # Charger l'image du plateau
    plateau_image = pygame.image.load('Map_AvecTraits.png')

    # Redimensionner l'image du plateau pour qu'elle remplisse la fenêtre
    plateau_image = pygame.transform.scale(plateau_image, (window_width, window_height))

    # Créer une surface pour le quadrillage
    grid_surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA)

    # Définir l'espacement entre les lignes du quadrillage en pourcentage de la taille de la fenêtre
    spacing = int(window_width * 0.03)

    # Dessiner des lignes horizontales
    for y in range(0, window_height, spacing):
        pygame.draw.line(grid_surface, (0, 0, 0, 50), (0, y), (window_width, y))

    # Dessiner des lignes verticales
    for x in range(0, window_width, spacing):
        pygame.draw.line(grid_surface, (0, 0, 0, 50), (x, 0), (x, window_height))

    # Créer un dictionnaire des positions des cercles en fonction des cases
    circle_positions = {
        "Case 1": (screen_width * taille_ajustee * 0.111, screen_height * taille_ajustee* 0.9),
        "Case 2": (screen_width * taille_ajustee * 0.2, screen_height * taille_ajustee * 0.9),
        "Case 3": (screen_width * taille_ajustee * 0.29, screen_height * taille_ajustee * 0.89),
        "Case 4": (screen_width * taille_ajustee * 0.355, screen_height * taille_ajustee * 0.82),
        "Case 5": (screen_width * taille_ajustee * 0.26, screen_height * taille_ajustee * 0.76),
        "Case 6": (screen_width * taille_ajustee * 0.235, screen_height * taille_ajustee * 0.515),
        "Case 7": (screen_width * taille_ajustee * 0.088, screen_height * taille_ajustee * 0.44),

    }

    # Définir l'opacité (transparence) des cercles
    circle_opacity = 128  # 128 sur 255 correspond à 50 % d'opacité

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Vérifier si le clic est le clic gauche de la souris
                    # Obtenir les coordonnées du clic de souris
                    x, y = event.pos

                    # Parcourir les positions des cercles
                    for case, (circle_x, circle_y) in circle_positions.items():
                        # Calculer la distance entre le clic et la position du cercle
                        distance = ((circle_x - x) ** 2 + (circle_y - y) ** 2) ** 0.5

                        # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer l'identifiant de la case
                        if distance < screen_width * 0.03:
                            print(f"Case cliquée : {case}")

        # Afficher l'image du plateau
        screen.blit(plateau_image, (0, 0))

        # Afficher le quadrillage
        screen.blit(grid_surface, (0, 0))

        # Dessiner les cercles rouges pour chaque case
        for case, (circle_x, circle_y) in circle_positions.items():
            circle_surface = pygame.Surface((window_width * 0.03 * 2, window_width * 0.03 * 2), pygame.SRCALPHA)
            pygame.draw.circle(circle_surface, (255, 0, 0, circle_opacity), (window_width * 0.03, window_width * 0.03), window_width * 0.03)
            screen.blit(circle_surface, (circle_x - window_width * 0.03, circle_y - window_width * 0.03))

        pygame.display.flip()

if __name__ == '__main__':
    main()
