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
while all(joueur.position < 31 for joueur in joueurs):
    # Tant que les joueurs ne sont pas sur la case 31, continuez le jeu
    print("---------------------- TOUR ----------------------")

    # Affichez les informations des joueurs
    for joueur in joueurs:
        joueur.afficher_info()

    for joueur in joueurs:
        print(f"\nTour de {joueur.nom}")
        deplacement = joueur.choix_deplacement()
        ancienne_position = joueur.position

        for i in range(ancienne_position, ancienne_position + deplacement):
            print(plateau.cases[i]["description"])
            if plateau.cases[i]["description"] == "Monstre":
                if plateau.combat_monstre(joueur) is False:
                    print("Case du monstre: ", plateau.cases[i]["numero"])
                    print("Case à reculer: ", plateau.cases[i]["numero"] - 1)
                    deplacement = i - ancienne_position
                    break


        plateau.deplacer_joueur(joueur, ancienne_position, deplacement)

        for i in range(len(joueurs)):
            for j in range(i + 1, len(joueurs)):
                if joueurs[i].position == joueurs[j].position:
                    print(f"\nCombat entre {joueurs[i].nom} et {joueurs[j].nom}")
                    gagnant = plateau.combat_joueurs(joueurs[i], joueurs[j])
                    perdant = joueurs[j] if gagnant == joueurs[i] else joueurs[i] 
                    plateau.deplacer_joueur(perdant, perdant.position, -1)
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
