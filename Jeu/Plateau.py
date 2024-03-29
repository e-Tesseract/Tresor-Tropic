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
            
        ### Monstres ###
            
        # Case 6
        self.cases[5]["description"] = "Monstre" 
        # Case 25
        self.cases[24]["description"] = "Monstre"
        # Case 30
        self.cases[29]["description"] = "Monstre"

        ### Trésors ###

        # Case 5
        self.cases[4]["description"] = "\033[92mEchelle\033[0m"
        # Case 8
        self.cases[7]["description"] = "\033[92mEchelle\033[0m"
        # Case 14
        self.cases[13]["description"] = "\033[92mEchelle\033[0m"
        # Case 24
        self.cases[23]["description"] = "\033[92mEchelle\033[0m"
        # Case 26
        self.cases[25]["description"] = "\033[92mEchelle\033[0m"
        # Case 29
        self.cases[28]["description"] = "\033[92mEchelle\033[0m"

        ### Rejouer ###

        # Case 10
        self.cases[9]["description"] = "Speciale"

        # Case 16
        self.cases[15]["description"] = "Speciale"

        for joueur in joueurs:
            self.cases[joueur.position - 1]["joueurs_sur_case"].append(joueur)

    def afficher_plateau(self) -> None:
        """
        Affiche le plateau avec les descriptions des cases et les joueurs sur chaque case.

        Returns:
            None
        """
        for case in self.cases:
            joueurs_sur_case = ", ".join([joueur.nom for joueur in case["joueurs_sur_case"]])
            print(f'Case {case["numero"]}: {case["description"]}, Joueurs sur case: {joueurs_sur_case}')

    def joueur_sur_case(self, joueur: Joueur, numero_case: int) -> bool:
        """
        Vérifie si le joueur se trouve sur la case avec le numéro spécifié.

        Args:
            joueur (Joueur): Le joueur à vérifier.
            numero_case (int): Le numéro de la case à vérifier.

        Returns:
            bool: True si le joueur se trouve sur la case, False sinon.
        """
        return joueur.position == numero_case
    
    
    def deplacer_joueur(self, joueur: Joueur, ancienne_position, distance: int) -> str:
        """
        Déplace le joueur sur le plateau.

        Args:
            joueur (Joueur): Le joueur à déplacer.
            distance (int): La distance à parcourir.

        Returns:
            None
        """
        echelle = "Rien"
        # Déplace le joueur sur le plateau
        self.cases[joueur.position - 1]["joueurs_sur_case"].remove(joueur)

        # Vérifie si le déplacement est valide
        if distance is not None:

            joueur.position = distance
            # Echelles pour monter ou descendre de plusieurs cases à la fois sur le plateau
            if joueur.position == 5:
                print("Le joueur est sur la case 5, il recule case 2.")
                joueur.position = 2
                echelle = "echelle"
            elif joueur.position == 8:
                print("Le joueur est sur la case 8, il avance case 12.")
                joueur.position = 12
                echelle = "echelle"
            elif joueur.position == 14:
                print("Le joueur est sur la case 14, il avance case 18.")
                joueur.position = 18
                echelle = "echelle"
            elif joueur.position == 24:
                print("Le joueur est sur la case 24, il recule case 20.")
                joueur.position = 20
                echelle = "echelle"
            elif joueur.position == 26:
                print("Le joueur est sur la case 26, il avance case 28.")
                joueur.position = 28
                echelle = "echelle"
            elif joueur.position == 29:
                print("Le joueur est sur la case 29, il recule case 21.")
                joueur.position = 21
                echelle = "echelle"

        else:
            print("Déplacement invalide. Le joueur ne bouge pas.")

        # On ajoute le joueur à la case
        self.cases[joueur.position - 1]["joueurs_sur_case"].append(joueur)
        return echelle


    def echanger_joueurs(self, joueur1: Joueur, joueur2: Joueur) -> None:
        """
        Echange les positions de deux joueurs.

        Args:
            joueur1 (Joueur): Le premier joueur.
            joueur2 (Joueur): Le deuxième joueur.

        Returns:
            None
        """
        echange="vide"

        # Echange les positions des joueurs
        joueur1.position, joueur2.position = joueur2.position, joueur1.position

        # Met à jour les joueurs sur les cases
        self.mettre_a_jour_joueurs_sur_case(joueur1, joueur1.position)
        self.mettre_a_jour_joueurs_sur_case(joueur2, joueur2.position)
        echange = "echange"
        return echange

        

    def mettre_a_jour_joueurs_sur_case(self, joueur: Joueur, numero_case: int) -> None: 
        """
        Met à jour la liste des joueurs sur la case spécifiée.

        Args:
            joueur (Joueur): Le joueur à ajouter à la case.
            numero_case (int): Le numéro de la case à mettre à jour.

        Returns:
            None
        """

        case = self.cases[numero_case - 1] 

        if joueur in case["joueurs_sur_case"]:
            # Si le joueur est déjà dans la liste, le retirer
            case["joueurs_sur_case"].remove(joueur)

        # Ajouter le joueur à la case
        case["joueurs_sur_case"].append(joueur)

    
    def combat_joueurs(self, joueur1: Joueur, joueur2: Joueur) -> Joueur:
        """
        Simule un combat entre deux joueurs.

        Args:
            joueur1 (Joueur): Le premier joueur.
            joueur2 (Joueur): Le deuxième joueur.

        Returns:
            Joueur: Le joueur gagnant le combat.
        """

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
    
    def relancer(self, joueur, lancer):
        # Deplacer le joueur sur le plateau
        joueur.position += lancer

    
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