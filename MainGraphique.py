import pygame

def main():
    pygame.init()

    # Récupérer les dimensions de l'écran
    infoObject = pygame.display.Info()
    largeur_ecran, hauteur_ecran = infoObject.current_w, infoObject.current_h

    taille_ajustee = 0.9
    # Définir la taille de la fenêtre en pourcentage de la taille de l'écran
    largeur_fenetre, hauteur_fenetre = int(largeur_ecran * taille_ajustee), int(hauteur_ecran * taille_ajustee)

    # Créer une fenêtre de la taille définie
    screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

    # Charger l'image du plateau
    plateau_image = pygame.image.load('Map_AvecTraits2.png')

    # Redimensionner l'image du plateau pour qu'elle remplisse la fenêtre
    plateau_image = pygame.transform.scale(plateau_image, (largeur_fenetre, hauteur_fenetre))



    # Créer un dictionnaire des positions des cercles en fonction des cases
    positions_cercles = {
        "Case 1": (largeur_ecran * taille_ajustee * 0.111, hauteur_ecran * taille_ajustee* 0.9),
        "Case 2": (largeur_ecran * taille_ajustee * 0.2, hauteur_ecran * taille_ajustee * 0.9),
        "Case 3": (largeur_ecran * taille_ajustee * 0.29, hauteur_ecran * taille_ajustee * 0.89),
        "Case 4": (largeur_ecran * taille_ajustee * 0.355, hauteur_ecran * taille_ajustee * 0.815),
        "Case 5": (largeur_ecran * taille_ajustee * 0.26, hauteur_ecran * taille_ajustee * 0.76),
        "Case 6": (largeur_ecran * taille_ajustee * 0.235, hauteur_ecran * taille_ajustee * 0.515),
        "Case 7": (largeur_ecran * taille_ajustee * 0.088, hauteur_ecran * taille_ajustee * 0.44),
        "Case 8": (largeur_ecran * taille_ajustee * 0.147, hauteur_ecran * taille_ajustee * 0.34),
        "Case 9": (largeur_ecran * taille_ajustee * 0.075, hauteur_ecran * taille_ajustee * 0.25),
        "Case 10": (largeur_ecran * taille_ajustee * 0.145, hauteur_ecran * taille_ajustee * 0.18),
        "Case 11": (largeur_ecran * taille_ajustee * 0.238, hauteur_ecran * taille_ajustee * 0.16),
        "Case 12": (largeur_ecran * taille_ajustee * 0.328, hauteur_ecran * taille_ajustee * 0.19),
        "Case 13": (largeur_ecran * taille_ajustee * 0.402, hauteur_ecran * taille_ajustee * 0.245),
        "Case 14": (largeur_ecran * taille_ajustee * 0.525, hauteur_ecran * taille_ajustee * 0.186),
        "Case 15": (largeur_ecran * taille_ajustee * 0.6, hauteur_ecran * taille_ajustee * 0.11),
        "Case 16": (largeur_ecran * taille_ajustee * 0.695, hauteur_ecran * taille_ajustee * 0.13),
        "Case 17": (largeur_ecran * taille_ajustee * 0.682, hauteur_ecran * taille_ajustee * 0.238),
        "Case 18": (largeur_ecran * taille_ajustee * 0.6, hauteur_ecran * taille_ajustee * 0.255),
        "Case 19": (largeur_ecran * taille_ajustee * 0.5, hauteur_ecran * taille_ajustee * 0.395),
        "Case 20": (largeur_ecran * taille_ajustee * 0.446, hauteur_ecran * taille_ajustee * 0.485),
        "Case 21": (largeur_ecran * taille_ajustee * 0.535, hauteur_ecran * taille_ajustee * 0.53),
        "Case 22": (largeur_ecran * taille_ajustee * 0.494, hauteur_ecran * taille_ajustee * 0.645),
        "Case 23": (largeur_ecran * taille_ajustee * 0.585, hauteur_ecran * taille_ajustee * 0.685),
        "Case 24": (largeur_ecran * taille_ajustee * 0.538, hauteur_ecran * taille_ajustee * 0.8),
        "Case 25": (largeur_ecran * taille_ajustee * 0.662, hauteur_ecran * taille_ajustee * 0.835),
        "Case 26": (largeur_ecran * taille_ajustee * 0.809, hauteur_ecran * taille_ajustee * 0.805),
        "Case 27": (largeur_ecran * taille_ajustee * 0.84, hauteur_ecran * taille_ajustee * 0.69),
        "Case 28": (largeur_ecran * taille_ajustee * 0.818, hauteur_ecran * taille_ajustee * 0.55),
        "Case 29": (largeur_ecran * taille_ajustee * 0.773, hauteur_ecran * taille_ajustee * 0.43),
        "Case 30": (largeur_ecran * taille_ajustee * 0.854, hauteur_ecran * taille_ajustee * 0.368),

    }

    # Définir l'opacité (transparence) des cercles
    opacité_cercles = 100  # 128 sur 255 correspond à 50 % d'opacité    
    taille_cercle = 0.025

 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Vérifier si le clic est le clic gauche de la souris
                    # Obtenir les coordonnées du clic de souris
                    x, y = event.pos

                    # Parcourir les positions des cercles
                    for case, (cercle_x, cercle_y) in positions_cercles.items():
                        # Calculer la distance entre le clic et la position du cercle
                        distance = ((cercle_x - x) ** 2 + (cercle_y - y) ** 2) ** 0.5

                        # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer l'identifiant de la case
                        if distance < largeur_ecran * taille_cercle * taille_ajustee:
                            print(f"Case cliquée : {case}")

        # Afficher l'image du plateau
        screen.blit(plateau_image, (0, 0))

        # Dessiner les cercles rouges pour chaque case
        for case, (cercle_x, cercle_y) in positions_cercles.items():
            surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
            pygame.draw.circle(surface_cercle, (255, 0, 0, opacité_cercles), (largeur_fenetre * taille_cercle, largeur_fenetre * taille_cercle), largeur_fenetre * taille_cercle)
            screen.blit(surface_cercle, (cercle_x - largeur_fenetre * taille_cercle, cercle_y - largeur_fenetre * taille_cercle))

        pygame.display.flip()

if __name__ == '__main__':
    main()
