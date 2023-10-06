from Plateau import Plateau
from Joueur import Joueur

# Demandez le nombre de joueurs
nombre_de_joueurs = int(input("Entrez le nombre de joueurs : "))
joueurs = []

# Créez les joueurs et ajoutez-les à la liste
for i in range(1, nombre_de_joueurs + 1):
    nom = input(f"Nom du joueur {i}: ")
    joueur = Joueur(nom, i)
    joueurs.append(joueur)

# Créez le plateau
plateau = Plateau(joueurs=joueurs)

print("---------------------- MAIN ----------------------\n")
while all(joueur.position < 30 for joueur in joueurs):
    # Tant que les joueurs ne sont pas sur la case 31, continuez le jeu
    print("---------------------- TOUR ----------------------")

    # afficher le plateau
    plateau.afficher_plateau()

    # Affichez les informations des joueurs
    for joueur in joueurs:
        joueur.afficher_info()

    for joueur in joueurs:
        print(f"\nTour de {joueur.nom}")

        # ------------------------------------------------------------------- #
        reultat_lancer_des = joueur.lancer_de_des()                                                         
        print("Résultat du lancer de dés du Joueur: ", reultat_lancer_des)
        cases_disponible = []

        for i in range(1, reultat_lancer_des + 1):
            cases_disponible.append(i + joueur.position)
        
        print("Cases disponible: ", cases_disponible)

        while True:
            choix_case = int(input("Choisissez un déplacement: "))
            if int(choix_case) in cases_disponible and int(choix_case) != 0:
                break
            else:
                print("Choix invalide. Veuillez choisir un déplacement valide.")

        deplacement = choix_case

        # ------------------------------------------------------------------- #

        ancienne_position = joueur.position

        for i in range(ancienne_position, deplacement):
            print(plateau.cases[i]["description"])
            if plateau.cases[i]["description"] == "Monstre":
                if plateau.combat_monstre(joueur) is False:
                    print("Case du monstre: ", plateau.cases[i]["numero"])
                    print("Case à reculer: ", plateau.cases[i]["numero"] - 1)
                    deplacement = plateau.cases[i]["numero"] - 1
                    break


        plateau.deplacer_joueur(joueur, ancienne_position, deplacement)

        for i in range(len(joueurs)):
            for j in range(i + 1, len(joueurs)):
                if joueurs[i].position == joueurs[j].position:
                    if joueur.position != 1:       
                        gagnant = plateau.combat_joueurs(joueurs[i], joueurs[j])
                        perdant = joueurs[j] if gagnant == joueurs[i] else joueurs[i] 
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



    tour_suivant = input("\nAppuyez sur Entrée pour continuer...\n")
    plateau.afficher_plateau()

gagnants = [joueur for joueur in joueurs if joueur.position >= 30]
if gagnants:
    print("Les joueurs gagnants sont :")
    for gagnant in gagnants:
        print(f"- {gagnant.nom}")
else:
    print("Aucun joueur n'a atteint la case 31. C'est un match nul.")
