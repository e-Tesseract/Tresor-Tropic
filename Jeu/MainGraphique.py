#-------------------------------------- IMPORTATIONS --------------------------------------#
import pygame
import random
import json
from Plateau import Plateau
from Joueur import Joueur
#------------------------------------------------------------------------------------------#

pygame.init()

# Récupérer les dimensions de l'écran
infoObject = pygame.display.Info()
largeur_ecran, hauteur_ecran = infoObject.current_w, infoObject.current_h

# Permettre de redimensionner la fenêtre 
taille_ajustee =1

# Définir la taille de la fenêtre en pourcentage de la taille de l'écran
largeur_fenetre, hauteur_fenetre = int(largeur_ecran * taille_ajustee), int(hauteur_ecran * taille_ajustee)

# Créer une fenêtre de la taille définie
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Charger l'image du plateau
plateau_image = pygame.image.load('./images/Map.png')

# Redimensionner l'image du plateau pour qu'elle remplisse la fenêtre
plateau_image = pygame.transform.scale(plateau_image, (largeur_fenetre, hauteur_fenetre))

# Charger les images des faces du dé
images_des = [
    pygame.image.load("./images/Des/dice1.png"),
    pygame.image.load("./images/Des/dice2.png"),
    pygame.image.load("./images/Des/dice3.png"),
    pygame.image.load("./images/Des/dice4.png"),
    pygame.image.load("./images/Des/dice5.png"),
    pygame.image.load("./images/Des/dice6.png")
]


# Charger les images des personnages
pirate_image = pygame.image.load('./images/Avatars/pirate.png')
pirate2_image = pygame.image.load('./images/Avatars/pirate2.png')
perroquet_image = pygame.image.load('./images/Avatars/perroquet.png')
aventurier_image = pygame.image.load('./images/Avatars/aventurier.png')

avatar_to_variable = {
    pirate_image: "pirate_image",
    pirate2_image: "pirate2_image",
    perroquet_image: "perroquet_image",
    aventurier_image: "aventurier_image"
}

avatar_to_image = {
    "pirate_image": pirate_image,
    "pirate2_image": pirate2_image,
    "perroquet_image": perroquet_image,
    "aventurier_image": aventurier_image
}

# Liste des images des personnages
avatars = [pirate_image, pirate2_image, perroquet_image, aventurier_image]


#--------------------------------------------------------- MAIN ---------------------------------------------------------#
def main(reprendre=False):

    tour_actuel = 1

    if not reprendre:
            
        #--- Demandez le nombre de joueurs entre 1 et 4 avec les boutons ---#
        choix_nombre_joueurs = None
        nombre_de_joueurs = None

        # Afficher 4 boutons pour choisir le nombre de joueurs (1, 2, 3 ou 4)
        while choix_nombre_joueurs is None:

            # Afficher le nom du joueur
            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 15)
            text = font.render(f"Nombre de joueurs", True, (255, 255, 255), (0, 0, 0)) 
            textRect = text.get_rect()
            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 15)
            screen.blit(text, textRect)
            pygame.display.update()

            # Charger les images des boutons et les redimensionner
            button_width, button_height = int(largeur_fenetre * 0.20), int(hauteur_fenetre * 0.1)

            bouton1 = pygame.image.load('./images/Boutons/button2.png')
            bouton1.set_alpha(0)
            bouton1 = pygame.transform.scale(bouton1, (button_width, button_height))

            bouton2 = pygame.image.load('./images/Boutons/button2.png')
            bouton2.set_alpha(0)
            bouton2 = pygame.transform.scale(bouton2, (button_width, button_height))

            bouton3 = pygame.image.load('./images/Boutons/button2.png')
            bouton3.set_alpha(0)
            bouton3 = pygame.transform.scale(bouton3, (button_width, button_height))

            bouton4 = pygame.image.load('./images/Boutons/button2.png')
            bouton4.set_alpha(0)
            bouton4 = pygame.transform.scale(bouton4, (button_width, button_height))

            # Créer les objets Rect pour représenter la position et la taille des boutons
            bouton1_rect = bouton1.get_rect()
            bouton1_rect.center = (largeur_fenetre // 2, int((hauteur_fenetre // 2) * 0.65))

            bouton2_rect = bouton2.get_rect()
            bouton2_rect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)

            bouton3_rect = bouton3.get_rect()
            bouton3_rect.center = (largeur_fenetre // 2, int((hauteur_fenetre // 2) * 1.35))

            bouton4_rect = bouton4.get_rect()
            bouton4_rect.center = (largeur_fenetre // 2, int((hauteur_fenetre // 2) * 1.65))

            # Afficher le texte des boutons
            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 20)
            text = font.render("1 joueur", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = bouton1_rect.center
            screen.blit(text, textRect)

            text = font.render("2 joueur", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = bouton2_rect.center
            screen.blit(text, textRect)

            text = font.render("3 joueur" , True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = bouton3_rect.center
            screen.blit(text, textRect)

            text = font.render("4 joueur", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = bouton4_rect.center
            screen.blit(text, textRect) 

            # Mettre à jour l'affichage
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    # Vérifier si le clic est sur un bouton
                    if bouton1_rect.collidepoint(event.pos):
                        nombre_de_joueurs = 1
                    elif bouton2_rect.collidepoint(event.pos):
                        nombre_de_joueurs = 2
                    elif bouton3_rect.collidepoint(event.pos):
                        nombre_de_joueurs = 3
                    elif bouton4_rect.collidepoint(event.pos):
                        nombre_de_joueurs = 4

            # Si un nombre de joueurs a été choisi, sortir de la boucle (et effacer les boutons)
            if nombre_de_joueurs is not None:
                screen.fill((0, 0, 0))
                break

        # Créer les joueurs
        joueurs = []
        for i in range(nombre_de_joueurs):
            joueur = Joueur(f"Joueur {i + 1}", i + 1)
            joueurs.append(joueur)

        for joueur in joueurs:

            # Afficher le nom du joueur
            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 15)
            text = font.render(f"{joueur.nom}, choisissez votre avatar", True, (255, 255, 255), (0, 0, 0)) 
            textRect = text.get_rect()
            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 10)
            screen.blit(text, textRect)
            pygame.display.update()

            # Charger les images des boutons et les redimensionner
            button_width, button_height = int(largeur_fenetre * 0.20), int(hauteur_fenetre * 0.1)

            bouton1 = pygame.image.load('./images/Boutons/button2.png')
            bouton1.set_alpha(0)
            bouton1 = pygame.transform.scale(bouton1, (button_width, button_height))

            bouton2 = pygame.image.load('./images/Boutons/button2.png')
            bouton2.set_alpha(0)
            bouton2 = pygame.transform.scale(bouton2, (button_width, button_height))

            bouton3 = pygame.image.load('./images/Boutons/button2.png')
            bouton3.set_alpha(0)
            bouton3 = pygame.transform.scale(bouton3, (button_width, button_height))

            bouton4 = pygame.image.load('./images/Boutons/button2.png')
            bouton4.set_alpha(0)
            bouton4 = pygame.transform.scale(bouton4, (button_width, button_height))

            # Créer les objets Rect pour représenter la position et la taille des boutons
            bouton1_rect = bouton1.get_rect()
            bouton1_rect.center = (int((largeur_fenetre // 2) * 0.4), hauteur_fenetre // 2)

            bouton2_rect = bouton2.get_rect()
            bouton2_rect.center = (int((largeur_fenetre // 2) * 0.8), hauteur_fenetre // 2)

            bouton3_rect = bouton3.get_rect()
            bouton3_rect.center = (int((largeur_fenetre // 2) * 1.2), hauteur_fenetre // 2)

            bouton4_rect = bouton4.get_rect()
            bouton4_rect.center = (int((largeur_fenetre // 2) * 1.6), hauteur_fenetre // 2)

            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 20)

            # Redimensionner les avatars
            avatar_width = int(button_width * 0.8) 
            avatar_height = int(button_height * 2) 

            # Créer une liste des avatars redimensionnés
            avatars = [
                pygame.transform.scale(pirate_image, (avatar_width, avatar_height)),
                pygame.transform.scale(pirate2_image, (avatar_width, avatar_height)),
                pygame.transform.scale(perroquet_image, (avatar_width, avatar_height)),
                pygame.transform.scale(aventurier_image, (avatar_width, avatar_height))
            ]

            # Pour chaque bouton
            for i, bouton_rect in enumerate([bouton1_rect, bouton2_rect, bouton3_rect, bouton4_rect]):
                text = font.render(str(i + 1), True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = bouton_rect.center
                screen.blit(text, textRect)

                # Afficher l'avatar sur le bouton
                avatar_rect = avatars[i].get_rect()
                avatar_rect.center = bouton_rect.center
                screen.blit(avatars[i], avatar_rect)

            # Mettre à jour l'affichage
            pygame.display.update()

            choix_avatar = None
            avatar: pygame.Surface = pygame.Surface((0, 0))

            # Tant que les avatar n'on pas été choisis
            while choix_avatar is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos

                        # Vérifier si le clic est sur un bouton
                        if bouton1_rect.collidepoint(event.pos):
                            avatar = pirate_image
                        elif bouton2_rect.collidepoint(event.pos):
                            avatar = pirate2_image
                        elif bouton3_rect.collidepoint(event.pos):
                            avatar = perroquet_image
                        elif bouton4_rect.collidepoint(event.pos):
                            avatar = aventurier_image
                        
                        # Attribution de l'avatar au joueur
                        joueur.photo = avatar
                        joueur.nomPhoto = avatar_to_variable.get(avatar, "Inconnu")

                        choix_avatar = True

                        # Effacer les boutons
                        screen.fill((0, 0, 0))

        # Créez le plateau
        plateau = Plateau(joueurs=joueurs)

    else:

        # Charger les données JSON depuis le fichier
        with open("partie.json", "r") as f:
            partie_data = json.load(f)

        # Extraire les données des joueurs
        joueurs_data = partie_data["joueurs"]

        # Créer les objets Joueur correspondant aux données des joueurs
        joueurs = []
        for joueur_data in joueurs_data:
            joueur_obj = Joueur(joueur_data["nom"], joueur_data["identifiant"])
            joueur_obj.position = joueur_data["position"]
            joueur_obj.photo = avatar_to_image[joueur_data["nomPhoto"]]
            joueur_obj.nomPhoto = joueur_data["nomPhoto"]
            joueurs.append(joueur_obj)

        # Créer l'objet Plateau correspondant aux données de la partie
        plateau = Plateau(joueurs=joueurs)

        # Récupérer le tour actuel depuis les données de la partie
        tour_actuel = partie_data["tour_actuel"]

        # Récupérer le joueur actuel en fonction du tour actuel
        joueur_actuel = joueurs[(tour_actuel - 1) % len(joueurs)]


    # Créer un dictionnaire des positions des cercles en fonction des cases
    positions_cercles = {
        "Case 1": (largeur_ecran * taille_ajustee * 0.111, hauteur_ecran * taille_ajustee* 0.9),
        "Case 2": (largeur_ecran * taille_ajustee * 0.2, hauteur_ecran * taille_ajustee * 0.9),
        "Case 3": (largeur_ecran * taille_ajustee * 0.29, hauteur_ecran * taille_ajustee * 0.89),
        "Case 4": (largeur_ecran * taille_ajustee * 0.355, hauteur_ecran * taille_ajustee * 0.815),
        "Case 5": (largeur_ecran * taille_ajustee * 0.262, hauteur_ecran * taille_ajustee * 0.76),
        "Case 6": (largeur_ecran * taille_ajustee * 0.235, hauteur_ecran * taille_ajustee * 0.515),
        "Case 7": (largeur_ecran * taille_ajustee * 0.088, hauteur_ecran * taille_ajustee * 0.44),
        "Case 8": (largeur_ecran * taille_ajustee * 0.147, hauteur_ecran * taille_ajustee * 0.34),
        "Case 9": (largeur_ecran * taille_ajustee * 0.075, hauteur_ecran * taille_ajustee * 0.25),
        "Case 10": (largeur_ecran * taille_ajustee * 0.1455, hauteur_ecran * taille_ajustee * 0.18),
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
        "Case 30": (largeur_ecran * taille_ajustee * 0.854, hauteur_ecran * taille_ajustee * 0.368)
    }

    # Ajuster la taille des images des personnages en fonction de la taille des cases
    taille_personnage = int(largeur_fenetre * 0.08) 

    # Définir l'opacitédes cercles
    opacité_cercles = 100  # (0 = transparent, 255 = opaque)
    taille_cercle = 0.025

    # Boucle principale du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Vérifier si le clic est le clic gauche de la souris
                if event.button == 1:  

                    # Obtenir les coordonnées du clic de souris
                    x, y = event.pos

                    # Parcourir les positions des cercles
                    for case, (cercle_x, cercle_y) in positions_cercles.items():

                        # Calculer la distance entre le clic et la position du cercle
                        distance = ((cercle_x - x) ** 2 + (cercle_y - y) ** 2) ** 0.5

            # Afficher l'image du plateau
            screen.blit(plateau_image, (0, 0))

            # Dessiner les cercles rouges pour chaque case
            for case, (cercle_x, cercle_y) in positions_cercles.items():
                surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
                pygame.draw.circle(surface_cercle, (255, 0, 0, opacité_cercles), (largeur_fenetre * taille_cercle, largeur_fenetre * taille_cercle), largeur_fenetre * taille_cercle)
                screen.blit(surface_cercle, (cercle_x - largeur_fenetre * taille_cercle, cercle_y - largeur_fenetre * taille_cercle))

            # Afficher les images des personnages
            for joueur in joueurs:

                # Redimensionner l'image du personnage
                image_joueur = pygame.transform.scale(joueur.photo, (taille_personnage, taille_personnage))

                # Calculer les coordonnées pour centrer l'image sur la case
                x_case, y_case = positions_cercles[f"Case {joueur.position}"]
                x_image = x_case - (taille_personnage // 2)
                y_image = y_case - (taille_personnage // 2)

                # Afficher l'image centrée sur la case
                screen.blit(image_joueur, (x_image, y_image))

            finJeu = False
            gagnants= []

            # ------------------------------------ MAIN  ------------------------------------ #
            # Tant que le jeu n'est pas fini
            while not finJeu:

                # Mettre à jour la fenêtre
                pygame.display.update()

                # Commencer au tour actuel
                # reorganiser la liste des joueurs pour que le joueur actuel soit le premier puis permutter les autres joueurs
                joueurs = joueurs[(tour_actuel - 1):] + joueurs[:(tour_actuel - 1)]
                
                for joueur in joueurs:
                    # Afficher le tour du joueur en haut de la fenêtre
                    font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                    text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 

                    # Afficher le personnage du joueur en petit a coté de son nom
                    screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))
                    textRect = text.get_rect()

                    # Centrer le texte en haut de la fenêtre (haut milieu)
                    textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                    screen.blit(text, textRect)
                    pygame.display.update()

                    # ------------------------ Animation de lancer de dés ------------------------ #

                    # Boucle pour afficher les images des faces du dé de manière aléatoire
                    reultat_lancer_des = 0
                    for i in range(25):
                        # Afficher une image aléatoire du dé
                        reultat_lancer_des = random.randint(1, 6)
                        image_des = images_des[reultat_lancer_des -1]
                        image_des = pygame.transform.scale(image_des, (int(image_des.get_width() * 0.8 * taille_ajustee), int(image_des.get_height() * 0.8 * taille_ajustee)))
                        screen.blit(image_des, (largeur_fenetre / 2 - image_des.get_width() / 2, hauteur_fenetre / 2 - image_des.get_height() / 2))
                        pygame.display.update()

                        # Attendre un court instant avant d'afficher la prochaine image
                        pygame.time.wait(70)

                    # Afficher une image aléatoire du dé 
                    image_des = images_des[reultat_lancer_des -1]
                    image_des = pygame.transform.scale(image_des, (int(image_des.get_width() * 0.8 * taille_ajustee), int(image_des.get_height() * 0.8 * taille_ajustee)))

                    # Afficher l'image du dé
                    screen.blit(image_des, (largeur_fenetre / 2 - image_des.get_width() / 2, hauteur_fenetre / 2 - image_des.get_height() / 2))
                    pygame.display.update()
                    pygame.time.wait(1000)

                    # Supprimer l'image du dé	
                    screen.fill((0, 0, 0))

                    # Redimensionner l'image du dé
                    image_des = pygame.transform.scale(image_des, (int(image_des.get_width() * 0.5), int(image_des.get_height() * 0.5)))

                    # Supprimer l'image du dé	
                    screen.blit(plateau_image, (0, 0))

                    # Redimensionner l'image du dé
                    image_des = pygame.transform.scale(image_des, (int(image_des.get_width() * 0.5), int(image_des.get_height() * 0.5)))
                    screen.blit(image_des, (0, 0))

                    cases_disponible = []

                    # Ajouter les cases disponibles dans la liste cases_disponible
                    for i in range(1, reultat_lancer_des + 1):
                        if i + joueur.position <= 30:
                            cases_disponible.append(i + joueur.position)

                    # Redessiner les cercles des cases disponibles
                    for case, (cercle_x, cercle_y) in positions_cercles.items():
                        surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
                        
                        # Vérifier si la case est dans cases_disponible
                        if int(case.split()[1]) in cases_disponible:

                            # Dessiner un cercle rouge
                            pygame.draw.circle(surface_cercle, (255, 0, 0, opacité_cercles), (largeur_fenetre * taille_cercle, largeur_fenetre * taille_cercle), largeur_fenetre * taille_cercle)
                        
                        screen.blit(surface_cercle, (cercle_x - largeur_fenetre * taille_cercle, cercle_y - largeur_fenetre * taille_cercle))
                    
                    # Réafficher les images des personnages autre que le joueur actuel (sinon ils ne sont pas affichés)
                    for joueur_autre in joueurs:
                        if joueur_autre != joueur:
                            image_joueur = pygame.transform.scale(joueur_autre.photo, (taille_personnage, taille_personnage))

                            # Calculer les coordonnées pour centrer l'image sur la case
                            x_case, y_case = positions_cercles[f"Case {joueur_autre.position}"]
                            x_image = x_case - (taille_personnage // 2)
                            y_image = y_case - (taille_personnage // 2)

                            # Afficher l'image centrée sur la case
                            screen.blit(image_joueur, (x_image, y_image))

                    # Afficher l'image du personnage du joueur actuel
                    image_joueur = pygame.transform.scale(joueur.photo, (taille_personnage, taille_personnage))
                    x_case, y_case = positions_cercles[f"Case {joueur.position}"]
                    x_image = x_case - (taille_personnage // 2)
                    y_image = y_case - (taille_personnage // 2)
                    screen.blit(image_joueur, (x_image, y_image))

                    # Afficher le tour du joueur
                    font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                    text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                    
                    # Afficher le personnage du joueur en petit a coté de son nom
                    screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                    # Centrer le texte en haut de la fenêtre (haut milieu)
                    textRect = text.get_rect()
                    textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                    screen.blit(text, textRect)

                    # Mettre à jour l'affichage
                    pygame.display.update()
                    
                    deplacement = None

                    # Attendre que le joueur clique sur une case disponible
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                x, y = event.pos

                                # On vérifie si le clic est sur une case disponible
                                for case, (cercle_x, cercle_y) in positions_cercles.items():
                                    distance = ((cercle_x - x) ** 2 + (cercle_y - y) ** 2) ** 0.5

                                    # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer la case
                                    if int(case.split()[1]) in cases_disponible and distance < largeur_ecran * taille_cercle * taille_ajustee:
                                        choix_case = int(case.split()[1])
                                        deplacement = choix_case
                                        break

                        # Si le joueur a cliqué sur une case disponible, sortir de la boucle
                        if deplacement is not None:
                            break

                    ancienne_position = joueur.position

                    for i in range(ancienne_position, deplacement):

                        # Si la case est une case monstre
                        if plateau.cases[i]["description"] == "Monstre":

                            # On récupère la case
                            case_monstre = i + 1

                            Egalite = True

                            # Tant que le joueur n'a pas gagné ou perdu
                            while Egalite:

                                # Animation de lancer de dés 
                                font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)

                                # Afficher le nom du joeuur au dessus des dés
                                text = font.render(f"{joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                                textRect = text.get_rect()
                                textRect = (largeur_fenetre * 0.12 , hauteur_fenetre * 0.3)
                                screen.blit(text, textRect)

                                # Afficher le monstre au dessus des dés
                                text = font.render("Monstre", True, (255, 255, 255), (0, 0, 0)) 
                                textRect = text.get_rect()
                                textRect = (largeur_fenetre* 0.8 , hauteur_fenetre * 0.3)
                                screen.blit(text, textRect)

                                # Initialisation des dés
                                de1_monstre = 0
                                de2_monstre = 0
                                de1_joueur = 0
                                de2_joueur = 0
                                
                                # Boucle pour afficher les images des faces du dé de manière aléatoire
                                for i in range(25):

                                    # Afficher une image aléatoire du dé
                                    de1_monstre = random.randint(1, 6)
                                    de2_monstre = random.randint(1, 6)
                                    de1_joueur = joueur.lancer_de_des()
                                    de2_joueur = joueur.lancer_de_des()

                                    image1_des_joueur = images_des[de1_joueur -1]
                                    image2_des_joueur = images_des[de2_joueur -1]

                                    image1_des_monstre = images_des[de1_monstre -1]
                                    image2_des_monstre = images_des[de2_monstre -1]

                                    image1_des_joueur = pygame.transform.scale(image1_des_joueur, (int(image1_des_joueur.get_width() * 0.5 * taille_ajustee), int(image1_des_joueur.get_height() * 0.5 * taille_ajustee)))
                                    image2_des_joueur = pygame.transform.scale(image2_des_joueur, (int(image2_des_joueur.get_width() * 0.5 * taille_ajustee), int(image2_des_joueur.get_height() * 0.5 * taille_ajustee)))

                                    image1_des_monstre = pygame.transform.scale(image1_des_monstre, (int(image1_des_monstre.get_width() * 0.5 * taille_ajustee), int(image1_des_monstre.get_height() * 0.5 * taille_ajustee)))
                                    image2_des_monstre = pygame.transform.scale(image2_des_monstre, (int(image2_des_monstre.get_width() * 0.5 * taille_ajustee), int(image2_des_monstre.get_height() * 0.5 * taille_ajustee)))

                                    screen.blit(image1_des_joueur, (largeur_fenetre / 6 - image1_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image1_des_joueur.get_height() / 2))
                                    screen.blit(image2_des_joueur, (largeur_fenetre / 6 - image2_des_joueur.get_width() / 2, hauteur_fenetre / 2 + image2_des_joueur.get_height() / 2))

                                    screen.blit(image1_des_monstre, (largeur_fenetre / 1.2 - image1_des_monstre.get_width() / 2, hauteur_fenetre / 2 - image1_des_monstre.get_height() / 2))
                                    screen.blit(image2_des_monstre, (largeur_fenetre / 1.2 - image2_des_monstre.get_width() / 2, hauteur_fenetre / 2 + image2_des_monstre.get_height() / 2))

                                    pygame.display.update()

                                    # Attendre un court instant avant d'afficher la prochaine image
                                    pygame.time.wait(70)

                                # Afficher une image aléatoire du dé 
                                image1_des_joueur = images_des[de1_joueur -1]
                                image2_des_joueur = images_des[de2_joueur -1]

                                image1_des_monstre = images_des[de1_monstre -1]
                                image2_des_monstre = images_des[de2_monstre -1]

                                image1_des_joueur = pygame.transform.scale(image1_des_joueur, (int(image1_des_joueur.get_width() * 0.5 * taille_ajustee), int(image1_des_joueur.get_height() * 0.5 * taille_ajustee)))
                                image2_des_joueur = pygame.transform.scale(image2_des_joueur, (int(image2_des_joueur.get_width() * 0.5 * taille_ajustee), int(image2_des_joueur.get_height() * 0.5 * taille_ajustee)))
                                image1_des_monstre = pygame.transform.scale(image1_des_monstre, (int(image1_des_monstre.get_width() * 0.5 * taille_ajustee), int(image1_des_monstre.get_height() * 0.5 * taille_ajustee)))
                                image2_des_monstre = pygame.transform.scale(image2_des_monstre, (int(image2_des_monstre.get_width() * 0.5 * taille_ajustee), int(image2_des_monstre.get_height() * 0.5 * taille_ajustee)))

                                # Afficher les images des dés
                                screen.blit(image1_des_joueur, (largeur_fenetre / 6 - image1_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image1_des_joueur.get_height() / 2))
                                screen.blit(image2_des_joueur, (largeur_fenetre / 6 - image2_des_joueur.get_width() / 2, hauteur_fenetre / 2 + image2_des_joueur.get_height() / 2))

                                screen.blit(image1_des_monstre, (largeur_fenetre / 1.2 - image1_des_monstre.get_width() / 2, hauteur_fenetre / 2 - image1_des_monstre.get_height() / 2))
                                screen.blit(image2_des_monstre, (largeur_fenetre / 1.2 - image2_des_monstre.get_width() / 2, hauteur_fenetre / 2 + image2_des_monstre.get_height() / 2))

                                # Récupérer les résultat du combat
                                resultat_monstre = de1_monstre + de2_monstre
                                resultat_joueur = de1_joueur + de2_joueur

                                font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 20)

                                text = font.render(f"{resultat_joueur}", True, (255, 255, 255), (0, 0, 0)) 
                                textRect = text.get_rect()
                                textRect = (largeur_fenetre * 0.15 , hauteur_fenetre * 0.875)
                                screen.blit(text, textRect)

                                text = font.render(f"{resultat_monstre}", True, (255, 255, 255), (0, 0, 0)) 
                                textRect = text.get_rect()
                                textRect = (largeur_fenetre * 0.835 , hauteur_fenetre * 0.875)
                                screen.blit(text, textRect)

                                pygame.display.update()
                                pygame.time.wait(2000)

                                if resultat_joueur > resultat_monstre:
                                    Egalite = False
                                    break

                                elif resultat_joueur < resultat_monstre:
                                    Egalite = False  
                                    deplacement = case_monstre -1
                                    break                    

                    
                    # Déplacer le joueur
                    plateau.deplacer_joueur(joueur, ancienne_position, deplacement)

                    # Si le joueur est sur la case 30, il a gagné
                    if joueur.position >= 30:
                        gagnants.append(joueur)
                        finJeu = True
                        break
                    
                    nouvelle_position_perdant = None

                    # On parcourt tous les joueurs
                    for i in range(len(joueurs)):
                        for j in range(i + 1, len(joueurs)):

                            # Si deux joueurs sont sur la même case
                            if joueurs[i].position == joueurs[j].position:

                                # Si les deux joueurs sont sur la case 1, on ne fait rien
                                if joueurs[i].position != 1 and joueurs[j].position != 1:    
                                    
                                    Egalite = True
                                    
                                    # Tant que les deux joueurs font égalité
                                    while Egalite:

                                        # Supprimer les dés
                                        screen.blit(plateau_image, (0, 0))

                                        # Reafficher les personnages
                                        for joueur in joueurs:
                                            image_joueur = pygame.transform.scale(joueur.photo, (taille_personnage, taille_personnage))
                                            x_case, y_case = positions_cercles[f"Case {joueur.position}"]
                                            x_image = x_case - (taille_personnage // 2)
                                            y_image = y_case - (taille_personnage // 2)
                                            screen.blit(image_joueur, (x_image, y_image))
                                    
                                        # Mettre à jour l'affichage
                                        pygame.display.update()

                                        font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)

                                        # Afficher le nom du joeuur au dessus des dés
                                        text = font.render(f"{joueurs[i].nom}", True, (255, 255, 255), (0, 0, 0)) 
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre * 0.12 , hauteur_fenetre * 0.3)
                                        screen.blit(text, textRect)

                                        # Afficher "Monstre" au dessus des dés
                                        text = font.render(f"{joueurs[j].nom}", True, (255, 255, 255), (0, 0, 0)) 
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre* 0.8 , hauteur_fenetre * 0.3)
                                        screen.blit(text, textRect)

                                        # Initialisation des dés
                                        de1: int = 0
                                        de2: int = 0

                                        # Boucle pour afficher les images des faces du dé de manière aléatoire
                                        for a in range(25):

                                            # Afficher une image aléatoire du dé
                                            de1 = joueurs[i].lancer_de_des()
                                            de2 = joueurs[j].lancer_de_des()
                                            image1_des_joueur = images_des[de1 -1]
                                            image2_des_joueur = images_des[de2 -1]

                                            image1_des_joueur = pygame.transform.scale(image1_des_joueur, (int(image1_des_joueur.get_width() * 0.5 * taille_ajustee), int(image1_des_joueur.get_height() * 0.5 * taille_ajustee)))
                                            image2_des_joueur = pygame.transform.scale(image2_des_joueur, (int(image2_des_joueur.get_width() * 0.5 * taille_ajustee), int(image2_des_joueur.get_height() * 0.5 * taille_ajustee)))

                                            screen.blit(image1_des_joueur, (largeur_fenetre / 1.2 - image1_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image1_des_joueur.get_height() / 2))
                                            screen.blit(image2_des_joueur, (largeur_fenetre / 6 - image2_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image2_des_joueur.get_height() / 2))

                                            # Mettre à jour l'affichage
                                            pygame.display.update()

                                            # Attendre un court instant (70 millisecondes) avant d'afficher la prochaine image 
                                            pygame.time.wait(70)
                                       
                                        # Afficher une image aléatoire du dé
                                        image1_des_joueur = images_des[de1 -1]
                                        image2_des_joueur = images_des[de2 -1]

                                        image1_des_joueur = pygame.transform.scale(image1_des_joueur, (int(image1_des_joueur.get_width() * 0.5 * taille_ajustee), int(image1_des_joueur.get_height() * 0.5 * taille_ajustee)))
                                        image2_des_joueur = pygame.transform.scale(image2_des_joueur, (int(image2_des_joueur.get_width() * 0.5 * taille_ajustee), int(image2_des_joueur.get_height() * 0.5 * taille_ajustee)))

                                        screen.blit(image1_des_joueur, (largeur_fenetre / 6 - image1_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image1_des_joueur.get_height() / 2))
                                        screen.blit(image2_des_joueur, (largeur_fenetre / 1.2 - image2_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image2_des_joueur.get_height() / 2))

                                        font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 15)

                                        # Afficher les résultats des dés en dessous de ses derniers
                                        text = font.render(f"{de2}", True, (255, 255, 255), (0, 0, 0))
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre * 0.835 , hauteur_fenetre * 0.675)
                                        screen.blit(text, textRect)

                                        text = font.render(f"{de1}", True, (255, 255, 255), (0, 0, 0))
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre * 0.15 , hauteur_fenetre * 0.675)
                                        screen.blit(text, textRect)

                                        # Mettre à jour l'affichage et attendre 2 secondes
                                        pygame.display.update()
                                        pygame.time.wait(2000)

                                        # Si le joueur 1 a un plus grand nombre que le joueur 2, le joueur 1 gagne
                                        if de1 > de2:
                                            perdant = joueurs[j]
                                            Egalite = False
                                        
                                        # Si le joueur 2 a un plus grand nombre que le joueur 1, le joueur 2 gagne
                                        elif de1 < de2:
                                            perdant = joueurs[i]
                                            Egalite = False

                                    #--- Tant que le perdant tombe sur une case ou un autre joueur est déjà présent, le perdant est déplacé sur la case précédente ---#

                                    # Nouvelle position après avoir perdu
                                    nouvelle_position_perdant = perdant.position - 1  

                                    while nouvelle_position_perdant >= 1 and plateau.cases[nouvelle_position_perdant - 1]["joueurs_sur_case"]:
                                        # dire quel joueur est déjà présent sur la case si le joeur ne dessent pas en dessous de 1
                                        nouvelle_position_perdant -= 1

                                    # Vérifie si la nouvelle position est inférieure à 1
                                    if nouvelle_position_perdant < 1:
                                        nouvelle_position_perdant = 1

                                    # Déplacer le perdant sur la nouvelle position
                                    plateau.deplacer_joueur(perdant, perdant.position, nouvelle_position_perdant)

                        # Mettre à jour la position des joueurs sur le plateau      
                        for joueur in joueurs:
                            plateau.mettre_a_jour_joueurs_sur_case(joueur, joueur.position)   

                    # supprimer image de dés
                    screen.fill((0, 0, 0))
                    screen.blit(plateau_image, (0, 0))

                    tour_actuel= tour_actuel + 1
                    
                    # Pour chaque joueur, afficher son image sur la case
                    for joueur in joueurs:
                        plateau.mettre_a_jour_joueurs_sur_case(joueur, joueur.position)

                        # Charger l'image du joueur
                        image_joueur = pygame.transform.scale(joueur.photo, (taille_personnage, taille_personnage))

                        # Calculer les coordonnées pour centrer l'image sur la case
                        x_case, y_case = positions_cercles[f"Case {joueur.position}"]
                        x_image = x_case - (taille_personnage // 2)
                        y_image = y_case - (taille_personnage // 2)

                        # Afficher l'image centrée sur la case
                        screen.blit(image_joueur, (x_image, y_image))

                        # Enregistrer les informations dans un fichier JSON
                        with open("partie.json", "w") as fichier:
                            # Créer une liste pour stocker les informations des joueurs
                            joueurs_data = []

                            for joueur in joueurs:
                                # enregistrer les informations du joueur dans la liste

                                # nom du joueur
                                nom = joueur.nom

                                # position du joueur
                                position = joueur.position

                                # identifiant du joueur
                                identifiant = joueur.identifiant

                                # avatar du joueur
                                avatar = joueur.nomPhoto

                                # ajouter les informations du joueur à la liste
                                joueurs_data.append({"nom": nom, "identifiant": identifiant, "position": position, "photo": avatar, "nomPhoto": avatar})

                            # enregistrer la liste des joueurs dans le fichier
                            json.dump(joueurs_data, fichier)

                        # Enregistrer le tour actuel avec les informations des joueurs
                        with open("partie.json", "w") as fichier:
                            # Enregistrez le tour actuel ainsi que les informations des joueurs
                            partie_data = {
                                "tour_actuel": tour_actuel,
                                "joueurs": joueurs_data
                            }
                            json.dump(partie_data, fichier)



                    # Mettre à jour l'affichage
                    pygame.display.update()
                    
                    # Pause de 1 secondes
                    pygame.time.wait(1000)

            
            #---------------------------------------------------------- FIN DU JEU ----------------------------------------------------------#
            # Afficher le gagnant sur fond noir
            screen.fill((0, 0, 0))
            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 20)
            text = font.render(f"{gagnants[0].nom} à TROUVÉ LE TRESOR !", True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)
            screen.blit(text, textRect)
            pygame.display.update()
            pygame.time.wait(4000)

            # Afficher un bouton pour quitter le jeu et revenir au menu
            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 20)
            text = font.render("Retour au menu", True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (largeur_fenetre // 2, int((hauteur_fenetre // 2) * 1.5))
            screen.blit(text, textRect)
            pygame.display.update()

            retour_menu = False
            # Attendre que le joueur clique sur le bouton
            while not retour_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos

                        # Vérifier si le clic est sur le bouton
                        if textRect.collidepoint(x, y):

                            # Quitter le jeu et revenir au menu
                            pygame.quit()
                            quit()
        


if __name__ == '__main__':
    main()