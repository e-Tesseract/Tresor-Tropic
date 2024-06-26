############################################################################################
# Développé par Hugo et Brian
# le programme sert à joue au jeux, choisir le nombre de joueur, chosir a quoi vont ressembler les personnage
############################################################################################
# amélioration ou ajouter à faire:
#   - ajouter automatique a la table resulta
#
#
# ajout potenciel(non obligatoire):
#   - (aucune pour l'instant)
############################################################################################

#-------------------------------------- IMPORTATIONS --------------------------------------#
import pygame
import random
import json
import sys
from Plateau import Plateau
from Joueur import Joueur
from database import  init_bdd
"from MenuPopUp import menu_popup"
#------------------------------------------------------------------------------------------#


pygame.init()

# Récupérer les dimensions de l'écran
infoObject = pygame.display.Info()
largeur_ecran, hauteur_ecran = infoObject.current_w, infoObject.current_h

# Permettre de redimensionner la fenêtre 
taille_ajustee =0.8

# Définir la taille de la fenêtre en pourcentage de la taille de l'écran
largeur_fenetre, hauteur_fenetre = int(largeur_ecran * taille_ajustee), int(hauteur_ecran * taille_ajustee)

# Créer une fenêtre de la taille définie
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Charger l'image du plateau
plateau_image = pygame.image.load('./images/Map2.png')

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

images_cartes =  [
    pygame.image.load("./images/Cartes/Rejouer.png"),
    pygame.image.load("./images/Cartes/Echanger.png"),
    pygame.image.load("./images/Cartes/Reculer.png")
]


# Charger les images des personnages
pirate_image = pygame.image.load('./images/Avatars/pirate.png')
pirate2_image = pygame.image.load('./images/Avatars/pirate2.png')
perroquet_image = pygame.image.load('./images/Avatars/perroquet.png')
aventurier_image = pygame.image.load('./images/Avatars/aventurier.png')
squelette_pirate_image = pygame.image.load('./images/Avatars/squelette_pirate.png')
crocodile_image = pygame.image.load('./images/Avatars/crocodile.png')

avatar_to_variable = {
    pirate_image: "pirate_image",
    pirate2_image: "pirate2_image",
    perroquet_image: "perroquet_image",
    aventurier_image: "aventurier_image",
    squelette_pirate_image: "squelette_pirate_image",
    crocodile_image: "crocodile_image"
}

avatar_to_image = {
    "pirate_image": pirate_image,
    "pirate2_image": pirate2_image,
    "perroquet_image": perroquet_image,
    "aventurier_image": aventurier_image,
    "squelette_pirate_image": squelette_pirate_image,
    "crocodile_image": crocodile_image
}

# Liste des images des personnages
avatars_noms = [pirate_image, pirate2_image, perroquet_image, aventurier_image, squelette_pirate_image, crocodile_image]

# def pause_menu(screen):
#     menu_popup(screen)
#     pygame.event.clear(pygame.KEYDOWN)  


#--------------------------------------------------------- MAIN ---------------------------------------------------------#
def main(reprendre=False):

    spécial = "rien"
    id_partie = -1
    bdd = init_bdd()
    curseur = bdd.connexion.cursor()

    tour_actuel = 1
    for i in range(30):
        curseur.execute('CALL ajout_cases()')
        bdd.connexion.commit()

    """curseur.execute('SELECT * FROM cases')
    
    
    # Récupération de toutes les lignes de résultats
    resultats = curseur.fetchall()
    
    # Affichage des résultats
    for row in resultats:
        print(row)"""


    if not reprendre:
            
        #--- Demander le nombre de joueurs entre 1 et 4 avec les boutons ---#
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


                    curseur.execute('CALL ajout_partie(%s)', [nombre_de_joueurs])

                    curseur.execute('SELECT MAX(id_partie) FROM partie')
    
                    # Récupération de toutes les lignes de résultats
                    resultats = curseur.fetchall()
                    
                    id_partie = resultats[0][0]
                    print(id_partie)
                    bdd.connexion.commit()


            # Si un nombre de joueurs a été choisi, sortir de la boucle (et effacer les boutons)
            if nombre_de_joueurs is not None:
                screen.fill((0, 0, 0))
                break

        # Créer les joueurs
        joueurs = []
        if nombre_de_joueurs is not None:
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

            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 20)

            # Redimensionner les avatars
            avatar_width = int(button_width * 0.8) 
            avatar_height = int(button_height * 2) 


            # Créer une liste des avatars redimensionnés
            avatars = [
                pygame.transform.scale(pirate_image, (avatar_width, avatar_height)),
                pygame.transform.scale(pirate2_image, (avatar_width, avatar_height)),
                pygame.transform.scale(perroquet_image, (avatar_width, avatar_height)),
                pygame.transform.scale(aventurier_image, (avatar_width, avatar_height)),
                pygame.transform.scale(squelette_pirate_image, (avatar_width, avatar_height)),
                pygame.transform.scale(crocodile_image, (avatar_width, avatar_height))        
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

            # Créer les boutons pour les flèches
            fleche_droite = pygame.Rect(50, hauteur_fenetre // 2, 50, 50)
            fleche_gauche = pygame.Rect(largeur_fenetre - 100, hauteur_fenetre // 2, 50, 50)

            # Initialiser l'index de l'avatar
            index_avatar = 0

            # Tant que l'avatar n'a pas été choisi
            while choix_avatar is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Vérifier si le clic est sur une flèche
                        if fleche_gauche.collidepoint(event.pos):
                            # Aller à l'avatar précédent
                            index_avatar = (index_avatar - 1) % len(avatars)
                        elif fleche_droite.collidepoint(event.pos):
                            # Aller à l'avatar suivant
                            index_avatar = (index_avatar + 1) % len(avatars)
                        else:
                            # Si le clic n'est pas sur une flèche, choisir l'avatar
                            avatar = avatars[index_avatar]
                            avatar_nom = avatar = avatars_noms[index_avatar]
                            joueur.photo = avatar
                            joueur.nomPhoto = avatar_to_variable.get(avatar_nom, "Inconnu")
                            choix_avatar = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            # Aller à l'avatar précédent
                            index_avatar = (index_avatar - 1) % len(avatars)
                        elif event.key == pygame.K_RIGHT:
                            # Aller à l'avatar suivant
                            index_avatar = (index_avatar + 1) % len(avatars)
                        elif event.key == pygame.K_RETURN:
                            # Si la touche Entrée est pressée, choisir l'avatar
                            avatar = avatars[index_avatar]
                            avatar_nom = avatar = avatars_noms[index_avatar]
                            joueur.photo = avatar
                            joueur.nomPhoto = avatar_to_variable.get(avatar_nom, "Inconnu")
                            choix_avatar = True

                # Effacer l'écran
                screen.fill((0, 0, 0))

                # Afficher le nom du joueur
                font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 15)
                text = font.render(f"{joueur.nom}, choisissez votre avatar", True, (255, 255, 255), (0, 0, 0)) 
                textRect = text.get_rect()
                textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 10)
                screen.blit(text, textRect)

                # Afficher l'avatar
                avatar_rect = avatars[index_avatar].get_rect()
                avatar_rect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)
                screen.blit(avatars[index_avatar], avatar_rect)

                # Afficher les flèches
                pygame.draw.polygon(screen, (255, 255, 255), [(fleche_gauche.right, fleche_gauche.centery), (fleche_gauche.left, fleche_gauche.top), (fleche_gauche.left, fleche_gauche.bottom)])
                pygame.draw.polygon(screen, (255, 255, 255), [(fleche_droite.left, fleche_droite.centery), (fleche_droite.right, fleche_droite.top), (fleche_droite.right, fleche_droite.bottom)])

                # Mettre à jour l'affichage
                pygame.display.update()
        # Créez le plateau
        plateau = Plateau(joueurs=joueurs)

    else:

        # Charger les données JSON depuis le fichier
        with open("partie.json", "r") as f:
            partie_data = json.load(f)

        # Extraire les données des joueurs
        joueurs_data = partie_data["joueurs"]

        nombre_de_joueurs = len(joueurs_data)

        # Créer les objets Joueur correspondant aux données des joueurs
        joueurs = []
        for joueur_data in joueurs_data:
            joueur_obj = Joueur(joueur_data["nom"], joueur_data["identifiant"])
            joueur_obj.position = joueur_data["position"]
            joueur_obj.photo = avatar_to_image[joueur_data["nomPhoto"]]
            joueur_obj.nomPhoto = joueur_data["nomPhoto"]
            joueurs.append(joueur_obj)
        
        id_partie=joueur_data["id_partie"]

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
                
                # Compter combien de joueurs sont sur la même case
                joueurs_sur_meme_case = [j for j in joueurs if j.position == joueur.position]

                if len(joueurs_sur_meme_case) > 1:
                    # Reduire l'image du personnage
                    image_joueur = pygame.transform.scale(image_joueur, (taille_personnage // 1.1, taille_personnage // 1.1))

                    # Si plusieurs joueurs sont sur la même case, décaler les images
                    index = joueurs_sur_meme_case.index(joueur)
                    offset = taille_personnage // 3
                    x_image = x_case - (taille_personnage // 1.5) + (index % 2) * offset
                    y_image = y_case - (taille_personnage // 1.5) + (index // 2) * offset
                else:
                    # Sinon, centrer l'image sur la case
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

                    menu_visible = False

                    # Attendre que le joueur clique sur une case disponible
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            
                            # # Vérifier si le joueur a appuyé sur echap
                            # elif event.type == pygame.KEYDOWN:
                            #     if event.key == pygame.K_ESCAPE:
                            #         print("Echap")
                            #         menu_visible = True
                            #         if menu_visible:
                            #             option_selection = menu_popup(screen)
                            #             if option_selection == "Reprendre":
                            #                 print("Reprendre MainGraphique")
                            #                 menu_visible = False  
                            #             elif option_selection == "Sauvegarder":
                            #                 print("Sauvegarder MainGraphique")
                            #             elif option_selection == "Quitter":
                            #                 print("Quitter MainGraphique")
                            #                 pygame.quit()
                            #                 quit()

                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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

                            ######################################### MAJ Affichage #########################################

                            screen.blit(plateau_image, (0, 0))

                            # Afficher le tour du joueur
                            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                            text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                            
                            # Afficher le personnage du joueur en petit a coté de son nom
                            screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                            # Centrer le texte en haut de la fenêtre (haut milieu)
                            textRect = text.get_rect()
                            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                            screen.blit(text, textRect)

                            
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
                            x_case, y_case = positions_cercles[f"Case {case_monstre}"]
                            x_image = x_case - (taille_personnage // 2)
                            y_image = y_case - (taille_personnage // 2)
                            screen.blit(image_joueur, (x_image, y_image))

                            pygame.display.update()

                            ################################################################################################

                            # Attendre un court instant avant d'afficher la suite
                            pygame.time.wait(1000)

                            Egalite = True

                            # Tant que le joueur n'a pas gagné ou perdu
                            while Egalite:

                                ######################################### MAJ Affichage #########################################

                                # Supprimer les dés
                                screen.blit(plateau_image, (0, 0))

                                # Afficher le tour du joueur
                                font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                                text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                                
                                # Afficher le personnage du joueur en petit a coté de son nom
                                screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                                # Centrer le texte en haut de la fenêtre (haut milieu)
                                textRect = text.get_rect()
                                textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                                screen.blit(text, textRect)

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
                                x_case, y_case = positions_cercles[f"Case {case_monstre}"]
                                x_image = x_case - (taille_personnage // 2)
                                y_image = y_case - (taille_personnage // 2)
                                screen.blit(image_joueur, (x_image, y_image))
                            
                                # Mettre à jour l'affichage
                                pygame.display.update()

                                ################################################################################################

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

                                resulta=False
                                if resultat_joueur > resultat_monstre:
                                    Egalite = False
                                    resulta=True
                                    curseur.execute('CALL ajout_choisit(%s, %s, %s, %s, %s)', [id_partie, deplacement, joueur.identifiant, reultat_lancer_des, spécial])
                                    curseur.execute('CALL ajout_resulta(%s, %s, %s)', [resulta, joueur.identifiant, id_partie]) 
                                    bdd.connexion.commit()
                                    break

                                elif resultat_joueur < resultat_monstre:
                                    Egalite = False  
                                    resulta = False
                                    deplacement = case_monstre -1
                                    curseur.execute('CALL ajout_choisit(%s, %s, %s, %s, %s)', [id_partie, deplacement, joueur.identifiant, reultat_lancer_des, spécial])    
                                    curseur.execute('CALL ajout_resulta(%s, %s, %s)', [resulta, joueur.identifiant, id_partie])
                                    bdd.connexion.commit()
                            
                                    break                    

                    
                    # Déplacer le joueur
                    spécial = plateau.deplacer_joueur(joueur, ancienne_position, deplacement)

                    curseur.execute('CALL ajout_choisit(%s, %s, %s, %s, %s)', [id_partie, deplacement, joueur.identifiant, reultat_lancer_des, spécial])    
                    bdd.connexion.commit()

                    #################################   #################################

                    # On enregistre la position du joueur
                    case_spéciale_deja_passée = []

                    # Tant que le joueur tombe une case spéciale; on applique les effets de la case
                    while plateau.cases[joueur.position - 1]["description"] == "Speciale":

                        # Si la position du joueur est dans la liste des cases spéciales déjà passées
                        if joueur.position in case_spéciale_deja_passée:
                            break

                        ######################################### MAJ Affichage #########################################

                        screen.blit(plateau_image, (0, 0))

                        # Afficher le tour du joueur
                        font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                        text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                        
                        # Afficher le personnage du joueur en petit a coté de son nom
                        screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                        # Centrer le texte en haut de la fenêtre (haut milieu)
                        textRect = text.get_rect()
                        textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                        screen.blit(text, textRect)

                        
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

                        pygame.display.update()

                        ################################################################################################
                    
                        # Choisir une carte spéciale
                        carte_speciale = None

                        for i in range(15):
                            # Afficher les cartes une par une (sachant qu'il y a 3 cartes spéciales)
                            image_carte = images_cartes[i%3]
                            image_carte = pygame.transform.scale(image_carte, (int(image_carte.get_width() * 0.3 * taille_ajustee), int(image_carte.get_height() * 0.3 * taille_ajustee)))
                            carte_position = (largeur_fenetre / 2 - image_carte.get_width() / 2, hauteur_fenetre / 2 - image_carte.get_height() / 2)
                            
                            # Créer une surface noire de la même taille que la carte
                            ombre = pygame.Surface(image_carte.get_size())
                            ombre.fill((0, 0, 0))

                            # Rendre la surface semi-transparente
                            ombre.set_alpha(50)

                            # Calculer la position de l'ombre (légèrement décalée par rapport à la carte)
                            ombre_position = (carte_position[0] + 5, carte_position[1] + 5)

                            # Dessiner l'ombre puis la carte
                            screen.blit(ombre, ombre_position)
                            screen.blit(image_carte, carte_position)
                            pygame.display.update()

                            # Attendre un court instant avant d'afficher la prochaine image
                            pygame.time.wait(100)

                        # On choisi une carte au hasard parmi les cartes spéciales
                        if nombre_de_joueurs == 1:
                            carte_speciale = random.choice(["Relancer"])
                        else:
                            carte_speciale = random.choice(["Relancer"] * 45 + ["Echanger_Joueur"] * 25 + ["Reculer_Joueur"] * 30)

                        # Afficher la carte correspondante
                        if carte_speciale == "Relancer":
                            image_carte = images_cartes[0]
                        elif carte_speciale == "Echanger_Joueur":
                            image_carte = images_cartes[1]
                        elif carte_speciale == "Reculer_Joueur":
                            image_carte = images_cartes[2]

                        image_carte = pygame.transform.scale(image_carte, (int(image_carte.get_width() * 0.3 * taille_ajustee), int(image_carte.get_height() * 0.3 * taille_ajustee)))

                        screen.blit(image_carte, (largeur_fenetre / 2 - image_carte.get_width() / 2, hauteur_fenetre / 2 - image_carte.get_height() / 2))
                        pygame.display.update()
                        pygame.time.wait(1000)
                                

                        # Si la carte est une carte Relancer
                        if carte_speciale == "Relancer":

                            ######################################### MAJ Affichage #########################################

                            screen.blit(plateau_image, (0, 0))

                            # Afficher le tour du joueur
                            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                            text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                            
                            # Afficher le personnage du joueur en petit a coté de son nom
                            screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                            # Centrer le texte en haut de la fenêtre (haut milieu)
                            textRect = text.get_rect()
                            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                            screen.blit(text, textRect)

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

                            pygame.display.update()

                            ################################################################################################

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

                            plateau.deplacer_joueur(joueur, joueur.position, joueur.position + reultat_lancer_des)

                        elif carte_speciale == "Echanger_Joueur":
                            
                            case_joueurs = []

                            # Ajouter les cases des joueurs dans la liste case_joueurs
                            for joueur_echanger in joueurs:
                                if joueur_echanger != joueur:
                                    case_joueurs.append(joueur_echanger.position)


                            ######################################### MAJ Affichage #########################################

                            screen.blit(plateau_image, (0, 0))

                            # Afficher le tour du joueur
                            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                            text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                            
                            # Afficher le personnage du joueur en petit a coté de son nom
                            screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                            # Centrer le texte en haut de la fenêtre (haut milieu)
                            textRect = text.get_rect()
                            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                            screen.blit(text, textRect)

                            # Redessiner les cercles des cases disponibles
                            for case, (cercle_x, cercle_y) in positions_cercles.items():
                                surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
                                
                                # Vérifier si la case est dans cases_joueurs
                                if int(case.split()[1]) in case_joueurs:

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

                            pygame.display.update()

                            ################################################################################################

                            # Attendre que le joueur clique sur une case disponible
                            case_selection = False
                            while not case_selection:
                                for event in pygame.event.get():                            
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()

                                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                        x, y = event.pos

                                        # On vérifie si le clic est sur une case disponible
                                        for case, (cercle_x, cercle_y) in positions_cercles.items():
                                            distance = ((cercle_x - x) ** 2 + (cercle_y - y) ** 2) ** 0.5

                                            # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer la case
                                            if distance < largeur_ecran * taille_cercle * taille_ajustee:
                                                deplacement = int(case.split()[1])

                                                # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer la case
                                                if deplacement in case_joueurs:
                                                    # On choisi le joueur à échanger
                                                    for joueur_echanger in joueurs:
                                                        if joueur_echanger.position == deplacement:
                                                            case_selection = True
                                                            break

                            # Echanger les positions des deux joueurs
                            position_joueur1 = joueur.position
                            position_joueur2 = joueur_echanger.position 
                            plateau.deplacer_joueur(joueur, position_joueur1, joueur_echanger.position )
                            plateau.deplacer_joueur(joueur_echanger, position_joueur2, position_joueur1)

                        elif carte_speciale == "Reculer_Joueur":

                            case_spéciale_deja_passée.append(joueur.position)

                            case_joueurs = []

                            # Ajouter les cases des joueurs dans la liste case_joueurs
                            for joueur_echanger in joueurs:
                                if joueur_echanger != joueur:
                                    case_joueurs.append(joueur_echanger.position)


                            ######################################### MAJ Affichage #########################################

                            screen.blit(plateau_image, (0, 0))

                            # Afficher le tour du joueur
                            font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                            text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                            
                            # Afficher le personnage du joueur en petit a coté de son nom
                            screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                            # Centrer le texte en haut de la fenêtre (haut milieu)
                            textRect = text.get_rect()
                            textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                            screen.blit(text, textRect)

                            # Redessiner les cercles des cases disponibles
                            for case, (cercle_x, cercle_y) in positions_cercles.items():
                                surface_cercle = pygame.Surface((largeur_fenetre * taille_cercle * 2, largeur_fenetre * taille_cercle * 2), pygame.SRCALPHA)
                            
                                # Vérifier si la case est dans cases_joueurs
                                if int(case.split()[1]) in case_joueurs:

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

                            pygame.display.update()

                            ################################################################################################

                            
                            # Attendre que le joueur clique sur une case disponible
                            case_selection = False
                            while not case_selection:
                                for event in pygame.event.get():                            
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()

                                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                        x, y = event.pos

                                        # On vérifie si le clic est sur une case disponible
                                        for case, (cercle_x, cercle_y) in positions_cercles.items():
                                            distance = ((cercle_x - x) ** 2 + (cercle_y - y) ** 2) ** 0.5

                                            # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer la case
                                            if distance < largeur_ecran * taille_cercle * taille_ajustee:
                                                deplacement = int(case.split()[1])

                                                # Si la distance est inférieure à un seuil (la moitié de la taille du cercle), renvoyer la case
                                                if deplacement in case_joueurs:
                                                    # On choisi le joueur à échanger
                                                    for joueur_reculer in joueurs:
                                                        if joueur_reculer.position == deplacement:
                                                            case_selection = True
                                                            break

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

                            # Verifier que le joueur ne recule pas plus que la case 1
                            if joueur_reculer.position - reultat_lancer_des < 1:
                                if joueur_reculer.position == 1:
                                    pass
                                else:
                                    nb_a_reculer = joueur_reculer.position - 1
                                    plateau.deplacer_joueur(joueur_reculer, joueur_reculer.position, joueur_reculer.position - nb_a_reculer)
                            else:
                                # Déplacer le joueur
                                plateau.deplacer_joueur(joueur_reculer, joueur_reculer.position, joueur_reculer.position - reultat_lancer_des)


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

                                        # Afficher le tour du joueur
                                        font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)
                                        text = font.render(f"Tour de {joueur.nom}", True, (255, 255, 255), (0, 0, 0)) 
                                        
                                        # Afficher le personnage du joueur en petit a coté de son nom
                                        screen.blit(pygame.transform.scale(joueur.photo, (taille_personnage // 2, taille_personnage // 2)), (text.get_width() * 3.6, 0))

                                        # Centrer le texte en haut de la fenêtre (haut milieu)
                                        textRect = text.get_rect()
                                        textRect.center = (largeur_fenetre // 2, hauteur_fenetre // 30)
                                        screen.blit(text, textRect)

                                        # Reafficher les personnages 
                                        for joueur in joueurs:
                                            # Redimensionner l'image du personnage
                                            image_joueur = pygame.transform.scale(joueur.photo, (taille_personnage, taille_personnage))

                                            # Calculer les coordonnées pour centrer l'image sur la case
                                            x_case, y_case = positions_cercles[f"Case {joueur.position}"]
                                            
                                            # Compter combien de joueurs sont sur la même case
                                            joueurs_sur_meme_case = [j for j in joueurs if j.position == joueur.position]

                                            if len(joueurs_sur_meme_case) > 1:
                                                # Reduire l'image du personnage
                                                image_joueur = pygame.transform.scale(image_joueur, (taille_personnage // 1.05, taille_personnage // 1.05))

                                                # Si plusieurs joueurs sont sur la même case, décaler les images
                                                index = joueurs_sur_meme_case.index(joueur)
                                                offset = taille_personnage // 3
                                                x_image = x_case - (taille_personnage // 1.5) + (index % 2) * offset
                                                y_image = y_case - (taille_personnage // 1.5) + (index // 2) * offset
                                            else:
                                                # Sinon, centrer l'image sur la case
                                                x_image = x_case - (taille_personnage // 2)
                                                y_image = y_case - (taille_personnage // 2)


                                            # Afficher l'image centrée sur la case
                                            screen.blit(image_joueur, (x_image, y_image))
                                        
                                        # Mettre à jour l'affichage
                                        pygame.display.update()

                                        font = pygame.font.Font("./images/BlackBeard/BlackBeard.otf", largeur_fenetre // 32)

                                        # Afficher le nom du joueur au dessus des dés
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

                                            # Attendre un court instant avant d'afficher la prochaine image 
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
                                    spécial = plateau.deplacer_joueur(perdant, perdant.position, nouvelle_position_perdant)
                                    curseur.execute('CALL ajout_choisit(%s, %s, %s, %s, %s)', [id_partie, deplacement, joueur.identifiant, reultat_lancer_des, "combat"])    
                                    bdd.connexion.commit()
                                    



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
                                joueurs_data.append({"nom": nom, "identifiant": identifiant, "position": position, "photo": avatar, "nomPhoto": avatar, "id_partie": id_partie})

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
            text = font.render(f"{gagnants[0].nom} a TROUVÉ LE TRESOR !", True, (255, 255, 255), (0, 0, 0))
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