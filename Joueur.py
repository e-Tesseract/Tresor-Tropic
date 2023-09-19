
import random
import math

class Joueur:
    def __init__(self, nom, identifiant) :
        self.nom = nom
        self.identifiant = identifiant
        self.position = 0


    def lancer_de_des(self) -> int:
        # Simuler un lancer de dés et renvoyer le résultat (par exemple, un nombre entre 1 et 6)
        resultat = random.randint(1, 6)
        return resultat

    def choix_deplacement(self) -> int:
        # Demander au joueur de choisir un déplacement (par exemple, 1 ou 2)
        resultat = random.randint(1, 6)
        print("Résultat du lancer de dés du Joueur: ", resultat)

        cases_disponible = []
        # Toutes les cases disponibles pour le joueur
        for i in range(1, resultat + 1):
            cases_disponible.append(i)

        # Afficher les cases disponibles
        print("Cases disponible: ", cases_disponible)

        while True:
            # Demander au joueur de choisir un déplacement (par exemple, 1 ou 2)
            distance = int(input("Choisissez un déplacement: "))

            # Le choix doit être inférieur ou égal au nombre du dé tiré de la fonction lancer_de_des
            if distance <= resultat and distance > 0:
                return distance
            else:
                print("Choix invalide. Veuillez choisir un déplacement valide.")




    def afficher_info(self):
        # Méthode pour afficher des informations sur le joueur (nom, position, score, etc.)
        print("Nom: ", self.nom, " Position: ", self.position)




if __name__ == "__main__":
    print("------Test de la classe Joueur------")
    joueur1 = Joueur("Joueur 1", 1)
    joueur2 = Joueur("Joueur 2", 2)

    # Affichage des informations des joueurs
    joueur1.afficher_info()
    joueur2.afficher_info()
