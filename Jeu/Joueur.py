import random


class Joueur:
    def __init__(self, nom, identifiant) :
        self.nom = nom
        self.identifiant = identifiant
        self.position = 9
        self.photo = None 
        self.nomPhoto = None

    def lancer_de_des(self) -> int:
        """
        Simule un lancer de dés et renvoie le résultat (entre 1 et 6).

        Args:
            self (Joueur): L'objet joueur.

        Returns:
            int: Le résultat du lancer de dés.
        """
        resultat = random.randint(1, 6)
        return resultat

    def afficher_info(self):
        """
        Affiche des informations sur le joueur (nom, position, score, etc.).

        Args:
            self (Joueur): L'objet joueur.

        Returns:
            None
        """        
        print("Nom: ", self.nom, " Position: ", self.position)




if __name__ == "__main__":
    print("------Test de la classe Joueur------")
    joueur1 = Joueur("Joueur 1", 1)
    joueur2 = Joueur("Joueur 2", 2)

    # Affichage des informations des joueurs
    joueur1.afficher_info()
    joueur2.afficher_info()
