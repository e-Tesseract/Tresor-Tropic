from Plateau import Plateau
from Joueur import Joueur
import random


# Demandez le nombre de joueurs
nombre_de_joueurs = None

while nombre_de_joueurs is None:
    try:
        nombre_de_joueurs = int(input("Entrez le nombre de joueurs : "))
    except ValueError:
        print("Veuillez entrer un nombre entier.")

joueurs = []

# Créez les joueurs et ajoutez-les à la liste
for i in range(1, nombre_de_joueurs + 1):
    nom = input(f"Nom du joueur {i}: ")
    while nom == "":
        print("Choisissez un nom valide... Parce que un nom vide c'est pas ouf pour l'affichage :)")
        nom = input(f"Nom du joueur {i}: ")

    joueur = Joueur(nom, i)
    joueurs.append(joueur)

# Créez le plateau
plateau = Plateau(joueurs=joueurs)

finJeu = False
gagnants= []

print("---------------------- MAIN ----------------------\n")

# Tant que le jeu n'est pas terminé
while not finJeu:

    tour_suivant = input("\nAppuyez sur Entrée pour continuer...\n")
    plateau.afficher_plateau()

    print("---------------------- TOUR ----------------------")

    # Affichez les informations des joueurs
    for joueur in joueurs:
        joueur.afficher_info()

    # Pour chaque joueur
    for joueur in joueurs:

        # Affichez le tour du joueur
        print(f"\nTour de {joueur.nom}")

        # Lancez les dés
        reultat_lancer_des = joueur.lancer_de_des()                                                         
        print("Résultat du lancer de dés du Joueur: ", reultat_lancer_des)
        cases_disponible = []

        # Vérifiez les cases disponibles
        for i in range(1, reultat_lancer_des + 1):
            if i + joueur.position <= 30:
                cases_disponible.append(i + joueur.position)
            
        # Affichez les cases disponibles
        print("Cases disponible: ", cases_disponible)

        # Demandez au joueur de choisir une case
        while True:
            choix_case = int(input("Choisissez un déplacement: "))
            if int(choix_case) in cases_disponible and int(choix_case) != 0:
                break
            else:
                print("Choix invalide. Veuillez choisir un déplacement valide.")

        deplacement = choix_case
        ancienne_position = joueur.position

        # Si la case est un relancer
        if plateau.cases[deplacement - 1]["description"] == "Relancer":
            print("Relancer !")
            deplacement += joueur.lancer_de_des()
            print("Résultat du lancer de dés du Joueur: ", deplacement)

        
       
        for i in range(ancienne_position, deplacement):
            print(plateau.cases[i]["description"])

             # Si le joueur tombe sur une case monstre
            if plateau.cases[i]["description"] == "Monstre":

                print(f"Combat entre {joueur.nom} et le monstre")
                Egalite = True

                #  Tant que le combat n'est pas terminé
                while Egalite:

                    # Lancez les dés
                    de1_monstre = random.randint(1, 6)
                    de2_monstre = random.randint(1, 6)
                    de1_joueur = joueur.lancer_de_des()
                    de2_joueur = joueur.lancer_de_des()

                    # Calculez le résultat
                    resultat_monstre = de1_monstre + de2_monstre
                    resultat_joueur = de1_joueur + de2_joueur

                    # Affichez le résultats
                    print(f"Résultat de {joueur.nom}: {resultat_joueur}")
                    print(f"Résultat du monstre: {resultat_monstre}")

                    # Si le joueur gagne
                    if resultat_joueur > resultat_monstre:
                        print(f"{joueur.nom} a gagné le combat !")
                        Egalite = False
                        break

                    # Si le monstre gagne
                    elif resultat_joueur < resultat_monstre:
                        Egalite = False
                        print(f"{joueur.nom} a perdu le combat !")
                        deplacement = plateau.cases[i]["numero"] - 1
                        break

                    # Si égalité
                    else:
                        print("Égalité !")
                        print("Nouveau combat !")

        # Déplacez le joueur
        plateau.deplacer_joueur(joueur, ancienne_position, deplacement)

        # Vérifiez si le joueur a gagné
        if joueur.position >= 30:
            gagnants.append(joueur)
            finJeu = True
            break

        for i in range(len(joueurs)):
            for j in range(i + 1, len(joueurs)):

                # Si deux joueurs sont sur la même case
                if joueurs[i].position == joueurs[j].position:

                    # Si le joueur est sur la case 1, il ne peut pas combattre
                    if joueur.position != 1:       

                        # Affichez le combat
                        print(f"Combat entre {joueurs[i].nom} et {joueurs[j].nom}")

                        Egalite = True

                        # Tant que le combat n'est pas terminé
                        while Egalite:

                            # Lancez les dés
                            de1 = joueurs[i].lancer_de_des()
                            de2 = joueurs[j].lancer_de_des()
                            print(f"Résultat de {joueurs[i].nom}: {de1}")
                            print(f"Résultat de {joueurs[j].nom}: {de2}")

                            # Calculez le résultat
                            if de1 > de2:
                                gagnant = joueurs[i]
                                perdant = joueurs[j]
                                print(f"{joueurs[i].nom} a gagné le combat !")
                                Egalite = False
                            
                            elif de1 < de2:
                                gagnant = joueurs[j]
                                perdant = joueurs[i]
                                print(f"{joueurs[j].nom} a gagné le combat !")

                            else:
                                print("Égalité !")
                                print("Nouveau combat !")
                                Egalite = False
                                continue
                            
                        # Tant que le perdant tombe sur une case ou un autre joueur est déjà présent, le perdant est déplacé sur la case précédente
                        nouvelle_position_perdant = perdant.position - 1  # Nouvelle position après avoir perdu

                        while nouvelle_position_perdant >= 1 and plateau.cases[nouvelle_position_perdant - 1]["joueurs_sur_case"]:

                            # Dire quel joueur est déjà présent sur la case si le joeur ne dessent pas en dessous de 1
                            print(f"Le joueur {plateau.cases[nouvelle_position_perdant - 1]['joueurs_sur_case'][0].nom} est déjà présent sur la case {nouvelle_position_perdant}. Le joueur {perdant.nom} est tombe sur la case {nouvelle_position_perdant - 1}.")
                            nouvelle_position_perdant -= 1

                        # Vérifie si la nouvelle position est inférieure à 1
                        if nouvelle_position_perdant < 1:
                            nouvelle_position_perdant = 1
                        plateau.deplacer_joueur(perdant, perdant.position, nouvelle_position_perdant)
            
            # Mettre à jour les joueurs sur les cases
            for joueur in joueurs:
                plateau.mettre_a_jour_joueurs_sur_case(joueur, joueur.position)

        
                
print("---------------------- FIN ----------------------")
# Affichez le gagnant
print(f"{gagnants[0].nom} a TROUVÉ LE TRESOR !.")

