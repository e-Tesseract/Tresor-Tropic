import random 
import math

from Joueur import Joueur

# class Plateau qui contient les cases du jeu ainsi que des méthodes pour gérer les joueurs, des fonctions pour simuler les combats, etc.
class Plateau:
    def __init__(self, joueurs: list[Joueur]):
        self.cases = []

        # Ajout des cases au plateau (par exemple, 30 cases)
        for numero_case in range(1, 31):
            case = {
                "numero": numero_case,    # Numéro de la case
                "description": "Normale",  # Description de la case (peut être modifiée)
                "joueurs_sur_case" : []  # Liste des joueurs sur cette case (initialement vide)
            }
            self.cases.append(case)

        # Ajout des cases spéciales
        # Case 6
        self.cases[5]["description"] = "Monstre" 
        # Case 25
        self.cases[24]["description"] = "Monstre"
        # Case 30
        self.cases[29]["description"] = "Monstre"

        # Case 5
        self.cases[4]["description"] = "\033[92mEchelle\033[0m"
        # Case 8
        self.cases[7]["description"] = "\033[92mEchelle\033[0m"
        # Case 29
        self.cases[28]["description"] = "\033[92mEchelle\033[0m"

        for joueur in joueurs:
            self.cases[joueur.position - 1]["joueurs_sur_case"].append(joueur)

    def afficher_plateau(self) -> None:
        # Affiche le plateau avec les descriptions des cases
        for case in self.cases:
            joueurs_sur_case = ", ".join([joueur.nom for joueur in case["joueurs_sur_case"]])
            print(f'Case {case["numero"]}: {case["description"]}, Joueurs sur case: {joueurs_sur_case}')

    def joueur_sur_case(self, joueur, numero_case) -> bool:
        # Vérifie si le joueur se trouve sur la case avec le numéro spécifié
        return joueur.position == numero_case
    
    
    def deplacer_joueur(self, joueur, ancienne_position,  distance) -> None:
        """Déplace le joueur sur le plateau.
        param joueur: le joueur à déplacer
        param distance: la distance à parcourir"""

        # Déplace le joueur sur le plateau
        self.cases[joueur.position - 1]["joueurs_sur_case"].remove(joueur)

        # Vérifie si le déplacement est valide
        if distance is not None:

            joueur.position += distance
            # Echelles pour monter ou descendre de plusieurs cases à la fois sur le plateau
            if joueur.position == 5:
                print("Le joueur est sur la case 5, il recule case 2.")
                joueur.position = 2
            elif joueur.position == 8:
                print("Le joueur est sur la case 8, il avance case 12.")
                joueur.position = 12
            elif joueur.position == 29:
                print("Le joueur est sur la case 29, il recule case 21.")
                joueur.position = 21


            



        else:
            print("Déplacement invalide. Le joueur ne bouge pas.")

        # On ajoute le joueur à la case
        self.cases[joueur.position - 1]["joueurs_sur_case"].append(joueur)

        

    def mettre_a_jour_joueurs_sur_case(self, joueur, numero_case) -> None: 
        # Met à jour la liste des joueurs sur la case spécifiée
        case = self.cases[numero_case - 1] 

        if joueur in case["joueurs_sur_case"]:
            # Si le joueur est déjà dans la liste, le retirer
            case["joueurs_sur_case"].remove(joueur)

        # Ajouter le joueur à la case
        case["joueurs_sur_case"].append(joueur)

    
    def combat_joueurs(self, joueur1, joueur2) -> Joueur:
        # Fonction pour simuler un combat entre deux joueurs
        gagnant = None

        while gagnant is None:
            # Méthode pour simuler un combat entre deux joueurs
            de1_joueur1 = joueur1.lancer_de_des()
            de2_joueur1 = joueur1.lancer_de_des()
            de1_joueur2 = joueur2.lancer_de_des()
            de2_joueur2 = joueur2.lancer_de_des()

            resultat_joueur1 = de1_joueur1 + de2_joueur1
            resultat_joueur2 = de1_joueur2 + de2_joueur2

            print(f"Combat entre {joueur1.nom} et {joueur2.nom}")
            print(f"Résultat de {joueur1.nom}: {resultat_joueur1}")
            print(f"Résultat de {joueur2.nom}: {resultat_joueur2}")

            if resultat_joueur1 > resultat_joueur2:
                print(f"{joueur1.nom} a gagné le combat !")
                gagnant = joueur1
                
            elif resultat_joueur1 < resultat_joueur2:
                print(f"{joueur2.nom} a gagné le combat !")
                gagnant = joueur2
            else:
                print("Égalité !")
                print("Nouveau combat !")
        
        return gagnant
    
    def combat_monstre(self, joueur) -> bool:
        '''Fonction pour simuler un combat entre un joueur et un monstre.\n 
        Retourne True si le joueur gagne le combat, False sinon.'''

        # Simuler le combat avec le monstre

        Egalite = True

        while Egalite:

            de1_monstre = random.randint(1, 6)
            de2_monstre = random.randint(1, 6)
            de1_joueur = joueur.lancer_de_des()
            de2_joueur = joueur.lancer_de_des()

            resultat_monstre = de1_monstre + de2_monstre
            resultat_joueur = de1_joueur + de2_joueur

            print(f"Combat entre {joueur.nom} et le monstre")
            print(f"Résultat de {joueur.nom}: {resultat_joueur}")
            print(f"Résultat du monstre: {resultat_monstre}")

            if resultat_joueur > resultat_monstre:
                print(f"{joueur.nom} a gagné le combat !")
                Egalite = False
                return True
            elif resultat_joueur < resultat_monstre:
                print(f"{joueur.nom} a perdu le combat !")
                Egalite = False
                return False
            else:
                print("Égalité !")
                print("Nouveau combat !")


    
if __name__ == "__main__":
    print("------Test de la classe Plateau------")
    joueur1 = Joueur("Joueur 1", 1)
    joueur2 = Joueur("Joueur 2", 2)

    # Créez une liste de joueurs
    joueurs = [joueur1, joueur2]

    plateau = Plateau(joueurs)

    # Affichage du plateau
    plateau.afficher_plateau()

    # Informations sur les joueurs
    print("\n------------------ Informations sur les joueurs ------------------")
    joueur1.afficher_info()
    joueur2.afficher_info()








    