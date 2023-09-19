from Plateau import Plateau  # Importez la classe Plateau
from Joueur import Joueur  # Importez la classe Joueur

# Créez les joueurs et associez le plateau
joueur1 = Joueur("Joueur 1", 1)
joueur2 = Joueur("Joueur 2", 2)

# Créez le plateau
plateau = Plateau(joueurs = [joueur1, joueur2])


print("---------------------- MAIN ----------------------\n")


while joueur1.position < 31 and joueur2.position < 31:
    # Tant que les joueurs ne sont pas sur la case 31, continuez le jeu

    print("---------------------- TOUR ----------------------")

    # Affichez les informations des joueurs
    joueur1.afficher_info()
    joueur2.afficher_info()

    # Demandez au joueur de lancer les dés et de choisir un déplacement
    print("")
    print("Tour du joueur 1")
    deplacement = joueur1.choix_deplacement() 
    ancienne_position = joueur1.position

    # Déplacez le joueur sur le plateau
    plateau.deplacer_joueur(joueur1, deplacement) 

    print("")
    print("Tour du joueur 2")
    deplacement2 = joueur2.choix_deplacement() 

    # Déplacez le joueur sur le plateau
    plateau.deplacer_joueur(joueur2, deplacement2)  

    # Mettre à jour la liste des joueurs sur la case
    plateau.mettre_a_jour_joueurs_sur_case(joueur1, joueur1.position)
    plateau.mettre_a_jour_joueurs_sur_case(joueur2, joueur2.position)

    # Si les joueurs sont sur la même case, combat
    if joueur1.position == joueur2.position:
        print("")
        gagnant = plateau.combat_joueurs(joueur1, joueur2)
        if gagnant == joueur1:
            plateau.deplacer_joueur(joueur2, -1)
            plateau.mettre_a_jour_joueurs_sur_case(joueur2, joueur2.position)
        elif gagnant == joueur2:
            plateau.deplacer_joueur(joueur1, -1)
            plateau.mettre_a_jour_joueurs_sur_case(joueur1, joueur1.position)

        

    # Affichez le plateau et les joueurs
    tour_suivant = input("Appuyez sur Entrée pour continuer...")
    print("")

    # Affichez le plateau et les joueurs
    plateau.afficher_plateau()

    print("")


if joueur1.position >= 30:
    print("Le joueur 1 a gagné !")
else:
    print("Le joueur 2 a gagné !")



