import pygame
import random
from Plateau import Plateau
from Joueur import Joueur

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

# Charger les images des faces du dé
images_des = [
    pygame.image.load("./images/Des/dice1.png"),
    pygame.image.load("./images/Des/dice2.png"),
    pygame.image.load("./images/Des/dice3.png"),
    pygame.image.load("./images/Des/dice4.png"),
    pygame.image.load("./images/Des/dice5.png"),
    pygame.image.load("./images/Des/dice6.png")
]

avatars = ["./images/pirate.png", "./images/pirate2.png", "./images/perroquet.png", "./images/aventurier.png"]

def main():

    # Demandez le nombre de joueurs entre 1 et 4 en graphique avec les boutons
    nombre_de_joueurs = None

    # Afficher 4 boutons pour choisir le nombre de joueurs (1, 2, 3 ou 4)
    while True:
        # Charger les images des boutons et les redimensionner
        button_width, button_height = int(largeur_fenetre * 0.20), int(hauteur_fenetre * 0.1)

        bouton1 = pygame.image.load('./images/button2.png')
        bouton1.set_alpha(0)
        bouton1 = pygame.transform.scale(bouton1, (button_width, button_height))

        bouton2 = pygame.image.load('./images/button2.png')
        bouton2.set_alpha(0)
        bouton2 = pygame.transform.scale(bouton2, (button_width, button_height))

        bouton3 = pygame.image.load('./images/button2.png')
        bouton3.set_alpha(0)
        bouton3 = pygame.transform.scale(bouton3, (button_width, button_height))

        bouton4 = pygame.image.load('./images/button2.png')
        bouton4.set_alpha(0)
        bouton4 = pygame.transform.scale(bouton4, (button_width, button_height))

        # Créer les objets Rect pour représenter la position et la taille des boutons
        bouton1_rect = bouton1.get_rect()
        bouton1_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 0.65)

        bouton2_rect = bouton2.get_rect()
        bouton2_rect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)

        bouton3_rect = bouton3.get_rect()
        bouton3_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 1.35)

        bouton4_rect = bouton4.get_rect()
        bouton4_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 1.65)

        # Afficher le texte des boutons
        font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 20)
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

        
        if nombre_de_joueurs is not None:
            break


    

    # Demandez le nombre de joueurs
    # nombre_de_joueurs = int(input("Entrez le nombre de joueurs : "))
    joueurs = []

    for i in range(nombre_de_joueurs):
        nom_joueur = f"Joueur {i}"

        # Afficher 4 boutons pour choisir le nombre de joueurs (1, 2, 3 ou 4)
    while True:
        # Charger les images des boutons et les redimensionner
        button_width, button_height = int(largeur_fenetre * 0.20), int(hauteur_fenetre * 0.1)

        bouton1 = pygame.image.load('./images/button2.png')
        bouton1.set_alpha(0)
        bouton1 = pygame.transform.scale(bouton1, (button_width, button_height))

        bouton2 = pygame.image.load('./images/button2.png')
        bouton2.set_alpha(0)
        bouton2 = pygame.transform.scale(bouton2, (button_width, button_height))

        bouton3 = pygame.image.load('./images/button2.png')
        bouton3.set_alpha(0)
        bouton3 = pygame.transform.scale(bouton3, (button_width, button_height))

        bouton4 = pygame.image.load('./images/button2.png')
        bouton4.set_alpha(0)
        bouton4 = pygame.transform.scale(bouton4, (button_width, button_height))

        # Créer les objets Rect pour représenter la position et la taille des boutons
        bouton1_rect = bouton1.get_rect()
        bouton1_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 0.65)

        bouton2_rect = bouton2.get_rect()
        bouton2_rect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)

        bouton3_rect = bouton3.get_rect()
        bouton3_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 1.35)

        bouton4_rect = bouton4.get_rect()
        bouton4_rect.center = (largeur_fenetre // 2, (hauteur_fenetre // 2) * 1.65)

        # Afficher le texte des boutons
        font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 20)
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

        
        if nombre_de_joueurs is not None:
            break


        



    # Créez les joueurs et ajoutez-les à la liste
    joueur1 = Joueur("Joueur 1", 1)
    joueur2 = Joueur("Joueur 2", 2)
    joueur3 = Joueur("Joueur 3", 3)
    joueur4 = Joueur("Joueur 4", 4)
    joueurs.append(joueur1)
    joueurs.append(joueur2)
    joueurs.append(joueur3)
    joueurs.append(joueur4)

    # Créez le plateau
    plateau = Plateau(joueurs=joueurs)

    pirate_image = pygame.image.load('./images/pirate.png')
    pirate2_image = pygame.image.load('./images/pirate2.png')
    perroquet_image = pygame.image.load('./images/perroquet.png')
    aventurier_image = pygame.image.load('./images/aventurier.png')

    joueur1.photo = pirate_image
    joueur2.photo = pirate2_image
    joueur3.photo = perroquet_image
    joueur4.photo = aventurier_image


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
        "Case 30": (largeur_ecran * taille_ajustee * 0.854, hauteur_ecran * taille_ajustee * 0.368)
    }

    # Ajuster la taille des images des personnages en fonction de la taille des cases
    taille_personnage = int(largeur_fenetre * 0.08)  # Vous pouvez ajuster la taille selon vos besoins

    # Ajuster la position initiale des personnages
    position_pirate = (positions_cercles["Case 1"][0] - taille_personnage, positions_cercles["Case 1"][1] - taille_personnage)
    position_pirate2 = (positions_cercles["Case 1"][0] - taille_personnage, positions_cercles["Case 1"][1] - taille_personnage)
    position_perroquet = (positions_cercles["Case 1"][0] - taille_personnage, positions_cercles["Case 1"][1] - taille_personnage)
    position_aventurier = (positions_cercles["Case 1"][0] - taille_personnage, positions_cercles["Case 1"][1] - taille_personnage)

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

                        # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer la case
                        if distance < largeur_ecran * taille_cercle * taille_ajustee:
                            print(f"Case cliquée : {case}")

            # Afficher l'image du plateau
            screen.blit(plateau_image, (0, 0))

            # Dessiner les cercles rouges pour chaque case
            for case, (cercle_x, cercle_y) in positions_cercles.items():
                surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
                pygame.draw.circle(surface_cercle, (255, 0, 0, opacité_cercles), (largeur_fenetre * taille_cercle, largeur_fenetre * taille_cercle), largeur_fenetre * taille_cercle)
                screen.blit(surface_cercle, (cercle_x - largeur_fenetre * taille_cercle, cercle_y - largeur_fenetre * taille_cercle))

            # Afficher les images des personnages
            screen.blit(pygame.transform.scale(pirate_image, (taille_personnage, taille_personnage)), position_pirate)
            screen.blit(pygame.transform.scale(pirate2_image, (taille_personnage, taille_personnage)), position_pirate2)
            screen.blit(pygame.transform.scale(perroquet_image, (taille_personnage, taille_personnage)), position_perroquet)
            screen.blit(pygame.transform.scale(aventurier_image, (taille_personnage, taille_personnage)), position_aventurier)

            finJeu = False
            gagnants= []

            print("---------------------- MAIN ----------------------\n")
            while not finJeu:

                # mettre à jour la fenêtre
                pygame.display.update()

                # Affichez les informations des joueurs
                for joueur in joueurs:
                    joueur.afficher_info()

                for joueur in joueurs:

                    print(f"\nTour de {joueur.nom}") 
                    # afficher le tour du joueur en graphique
                    font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 32)
                    text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                    # afficher le personnage du joueur en petit a coté de son nom
                    screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))
                    textRect = text.get_rect()
                    # centrer le texte en haut de la fenêtre (haut milieu)
                    textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                    screen.blit(text, textRect)
                    pygame.display.update()

                    # Animation de lancer de dés
                    # Boucle pour afficher les images des faces du dé de manière aléatoire
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

                    for i in range(1, reultat_lancer_des + 1):
                        if i + joueur.position <= 30:
                            cases_disponible.append(i + joueur.position)

                    # Redessiner les cercles des cases disponibles
                    for case, (cercle_x, cercle_y) in positions_cercles.items():
                        surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
                        
                        # Vérifier si la case est dans cases_disponible
                        if int(case.split()[1]) in cases_disponible:
                            pygame.draw.circle(surface_cercle, (255, 0, 0, opacité_cercles), (largeur_fenetre * taille_cercle, largeur_fenetre * taille_cercle), largeur_fenetre * taille_cercle)
                        
                        screen.blit(surface_cercle, (cercle_x - largeur_fenetre * taille_cercle, cercle_y - largeur_fenetre * taille_cercle))
                    
                    # Réafficher les images des personnages
                    screen.blit(pygame.transform.scale(pirate_image, (taille_personnage, taille_personnage)), position_pirate)
                    screen.blit(pygame.transform.scale(pirate2_image, (taille_personnage, taille_personnage)), position_pirate2)
                    screen.blit(pygame.transform.scale(perroquet_image, (taille_personnage, taille_personnage)), position_perroquet)
                    screen.blit(pygame.transform.scale(aventurier_image, (taille_personnage, taille_personnage)), position_aventurier)

                    # afficher le tour du joueur en graphique
                    font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 32)
                    text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                    # afficher le personnage du joueur en petit a coté de son nom
                    screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                    textRect = text.get_rect()
                    # centrer le texte en haut de la fenêtre (haut milieu)
                    textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                    screen.blit(text, textRect)

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

                                    if int(case.split()[1]) in cases_disponible and distance < largeur_ecran * taille_cercle * taille_ajustee:
                                        choix_case = int(case.split()[1])
                                        deplacement = choix_case
                                        print(f"Case cliquée : {case}")  
                                        break
                        
                        if deplacement is not None:
                            break

                    ancienne_position = joueur.position

                    print(f"ancienne position: {ancienne_position}")
                    print(f"deplacement: {deplacement}")

                    for i in range(ancienne_position, deplacement):
                        print(plateau.cases[i]["description"])

                        if plateau.cases[i]["description"] == "Monstre":
                            case_monstre = i + 1
                            print(case_monstre)

                            print(f"Combat entre {joueur.nom} et le monstre")
                            Egalite = True

                            while Egalite:

                                # Animation de lancer de dés 
                                font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 32)

                                # afficher le nom du joeuur au dessus des dés
                                text = font.render(f"{joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                                textRect = text.get_rect()
                                textRect = (largeur_fenetre * 0.12 , hauteur_fenetre * 0.3)
                                screen.blit(text, textRect)

                                # afficher le monstre au dessus des dés
                                text = font.render("Monstre", True, (255, 255, 255), (0, 0, 0)) 
                                textRect = text.get_rect()
                                textRect = (largeur_fenetre* 0.8 , hauteur_fenetre * 0.3)
                                screen.blit(text, textRect)
                                
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

                                # Afficher l'image des dés
                                screen.blit(image1_des_joueur, (largeur_fenetre / 6 - image1_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image1_des_joueur.get_height() / 2))
                                screen.blit(image2_des_joueur, (largeur_fenetre / 6 - image2_des_joueur.get_width() / 2, hauteur_fenetre / 2 + image2_des_joueur.get_height() / 2))

                                screen.blit(image1_des_monstre, (largeur_fenetre / 1.2 - image1_des_monstre.get_width() / 2, hauteur_fenetre / 2 - image1_des_monstre.get_height() / 2))
                                screen.blit(image2_des_monstre, (largeur_fenetre / 1.2 - image2_des_monstre.get_width() / 2, hauteur_fenetre / 2 + image2_des_monstre.get_height() / 2))

                                resultat_monstre = de1_monstre + de2_monstre
                                resultat_joueur = de1_joueur + de2_joueur

                                font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 20)

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

                                print(f"Résultat de {joueur.nom}: {resultat_joueur}")
                                print(f"Résultat du monstre: {resultat_monstre}")

                                if resultat_joueur > resultat_monstre:
                                    print(f"{joueur.nom} a gagné le combat !")
                                    Egalite = False
                                    break

                                elif resultat_joueur < resultat_monstre:
                                    print(f"{joueur.nom} a perdu le combat !")
                                    Egalite = False  
                                    deplacement = case_monstre -1
                                    break                    

                                else:
                                    print("Egalité !")
                                    print("Nouveau combat !")
                    
                    plateau.deplacer_joueur(joueur, ancienne_position, deplacement)

                    if joueur.position >= 30:
                        gagnants.append(joueur)
                        finJeu = True
                        break
                    
                    nouvelle_position_perdant = None

                    for i in range(len(joueurs)):
                        for j in range(i + 1, len(joueurs)):
                            if joueurs[i].position == joueurs[j].position:

                                if joueurs[i].position != 1 and joueurs[j].position != 1:    
                                    
                                    print(f"Combat entre {joueurs[i].nom} et {joueurs[j].nom}")

                                    Egalite = True

                                    while Egalite:

                                        # supprimer les rectangles noir en dessinant le plateau
                                        screen.blit(plateau_image, (0, 0))

                                        # Reafficher les personnages
                                        screen.blit(pygame.transform.scale(pirate_image, (taille_personnage, taille_personnage)), position_pirate)
                                        screen.blit(pygame.transform.scale(pirate2_image, (taille_personnage, taille_personnage)), position_pirate2)
                                        screen.blit(pygame.transform.scale(perroquet_image, (taille_personnage, taille_personnage)), position_perroquet)
                                        screen.blit(pygame.transform.scale(aventurier_image, (taille_personnage, taille_personnage)), position_aventurier)
                                    
                                        pygame.display.update()

                                        # Animation de lancer de dés 
                                        font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 32)

                                        # afficher le nom du joeuur au dessus des dés
                                        text = font.render(f"{joueurs[i].nom}", True, (255, 255, 255), (0, 0, 0)) 
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre * 0.12 , hauteur_fenetre * 0.3)
                                        screen.blit(text, textRect)

                                        # afficher le monstre au dessus des dés
                                        text = font.render(f"{joueurs[j].nom}", True, (255, 255, 255), (0, 0, 0)) 
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre* 0.8 , hauteur_fenetre * 0.3)
                                        screen.blit(text, textRect)

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

                                            pygame.display.update()

                                            # Attendre un court instant avant d'afficher la prochaine image
                                            pygame.time.wait(70)
                                       
                                        image1_des_joueur = images_des[de1 -1]
                                        image2_des_joueur = images_des[de2 -1]

                                        image1_des_joueur = pygame.transform.scale(image1_des_joueur, (int(image1_des_joueur.get_width() * 0.5 * taille_ajustee), int(image1_des_joueur.get_height() * 0.5 * taille_ajustee)))
                                        image2_des_joueur = pygame.transform.scale(image2_des_joueur, (int(image2_des_joueur.get_width() * 0.5 * taille_ajustee), int(image2_des_joueur.get_height() * 0.5 * taille_ajustee)))

                                        screen.blit(image1_des_joueur, (largeur_fenetre / 6 - image1_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image1_des_joueur.get_height() / 2))
                                        screen.blit(image2_des_joueur, (largeur_fenetre / 1.2 - image2_des_joueur.get_width() / 2, hauteur_fenetre / 2 - image2_des_joueur.get_height() / 2))

                                        font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 15)

                                        text = font.render(f"{de2}", True, (255, 255, 255), (0, 0, 0))
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre * 0.835 , hauteur_fenetre * 0.675)
                                        screen.blit(text, textRect)

                                        text = font.render(f"{de1}", True, (255, 255, 255), (0, 0, 0))
                                        textRect = text.get_rect()
                                        textRect = (largeur_fenetre * 0.15 , hauteur_fenetre * 0.675)
                                        screen.blit(text, textRect)

                                        pygame.display.update()
                                        pygame.time.wait(2000)

                                        print(f"Résultat de {joueurs[i].nom}: {de1}")
                                        print(f"Résultat de {joueurs[j].nom}: {de2}")

                                        if de1 > de2:
                                            gagnant = joueurs[i]
                                            perdant = joueurs[j]
                                            print(f"{joueurs[i].nom} a gagné le combat !")
                                            Egalite = False
                                        
                                        elif de1 < de2:
                                            gagnant = joueurs[j]
                                            perdant = joueurs[i]
                                            print(f"{joueurs[j].nom} a gagné le combat !")
                                            Egalite = False

                                        else:
                                            print("Égalité !")
                                            print("Nouveau combat !")
                                            
                                    # tant que le perdant tombe sur une case ou un autre joueur est déjà présent, le perdant est déplacé sur la case précédente
                                    nouvelle_position_perdant = perdant.position - 1  # Nouvelle position après avoir perdu
                                    while nouvelle_position_perdant >= 1 and plateau.cases[nouvelle_position_perdant - 1]["joueurs_sur_case"]:
                                        # dire quel joueur est déjà présent sur la case si le joeur ne dessent pas en dessous de 1
                                        print(f"Le joueur {plateau.cases[nouvelle_position_perdant - 1]['joueurs_sur_case'][0].nom} est déjà présent sur la case {nouvelle_position_perdant}. Le joueur {perdant.nom} est tombe sur la case {nouvelle_position_perdant - 1}.")
                                        nouvelle_position_perdant -= 1
                                    # Vérifie si la nouvelle position est inférieure à 1
                                    if nouvelle_position_perdant < 1:
                                        nouvelle_position_perdant = 1
                                    plateau.deplacer_joueur(perdant, perdant.position, nouvelle_position_perdant)
                                                        
                        for joueur in joueurs:
                            plateau.mettre_a_jour_joueurs_sur_case(joueur, joueur.position)   

                    # supprimer image de dés
                    screen.fill((0, 0, 0))
                    screen.blit(plateau_image, (0, 0))
                    
                    for joueur in joueurs:
                        plateau.mettre_a_jour_joueurs_sur_case(joueur, joueur.position)
                        # deplacer l'image du joueur sur la case
                        if joueur.nom == "Joueur 1":
                            position_pirate = (positions_cercles[f"Case {joueur.position}"][0] - taille_personnage // 2, positions_cercles[f"Case {joueur.position}"][1] - taille_personnage // 2)
                        elif joueur.nom == "Joueur 2":
                            position_pirate2 = (positions_cercles[f"Case {joueur.position}"][0] - taille_personnage // 2, positions_cercles[f"Case {joueur.position}"][1] - taille_personnage // 2)
                        elif joueur.nom == "Joueur 3":
                            position_perroquet = (positions_cercles[f"Case {joueur.position}"][0] - taille_personnage // 2, positions_cercles[f"Case {joueur.position}"][1] - taille_personnage // 2)
                        elif joueur.nom == "Joueur 4":
                            position_aventurier = (positions_cercles[f"Case {joueur.position}"][0] - taille_personnage // 2, positions_cercles[f"Case {joueur.position}"][1] - taille_personnage // 2)

                    # Réafficher les images des personnages
                    screen.blit(pygame.transform.scale(pirate_image, (taille_personnage, taille_personnage)), position_pirate)
                    screen.blit(pygame.transform.scale(pirate2_image, (taille_personnage, taille_personnage)), position_pirate2)
                    screen.blit(pygame.transform.scale(perroquet_image, (taille_personnage, taille_personnage)), position_perroquet)
                    screen.blit(pygame.transform.scale(aventurier_image, (taille_personnage, taille_personnage)), position_aventurier)
                    
                    # Mettre à jour l'affichage
                    pygame.display.update()
                    
                    # Pause de 1 secondes
                    pygame.time.wait(1000)

                    print("----------")
                    print("Position actuelle des joueurs: ", end="")
                    for joueur in joueurs:
                        print(f"{joueur.nom}: {joueur.position}", end=" ")
                    print("----------")


                    
            
            print("---------------------- FIN ----------------------")
            # Afficher le gagnant sur fond noir
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont("BlackBeard", largeur_fenetre // 20)
            text = font.render(f"{gagnants[0].nom} a TROUVÉ LE TRESOR !", True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)
            screen.blit(text, textRect)
            pygame.display.update()
            pygame.time.wait(6000)
            pygame.quit()
            
            print(f"{gagnants[0].nom} a TROUVÉ LE TRESOR !.")




if __name__ == '__main__':
    main()
