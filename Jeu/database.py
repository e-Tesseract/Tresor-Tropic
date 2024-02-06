import psycopg2
from psycopg2 import sql

class init_bdd:
    def __init__(self):
        try:
            print("init_bdd")
            # Initialisation de la connexion
            self.connexion = psycopg2.connect(
                host="localhost",
                database="sql_jeux",
                port="5432",
                user="brian6",  #input("nom d'utilisateur : "),
                password="briandupuis220404" #input("mot de passe de l'utilisateur : ")
            )

            # Créer un curseur
            self.curseur = self.connexion.cursor()

            # Création des tables
            self.curseur.execute("CREATE TABLE IF NOT EXISTS partie (id_partie INTEGER PRIMARY KEY);")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS cases (id_case INTEGER PRIMARY KEY);")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS choisit (id_nombre INTEGER, id_partie INTEGER, id_case INTEGER, PRIMARY KEY (id_nombre, id_partie, id_case), FOREIGN KEY (id_partie) REFERENCES partie(id_partie), FOREIGN KEY (id_case) REFERENCES cases(id_case));")

            # Valider la transaction
            self.connexion.commit()

            print("Initialisation de la base de données réussie!")

        except Exception as e:
            # En cas d'erreur, annuler la transaction et fermer la connexion
            if hasattr(self, 'connexion') and self.connexion is not None:
                self.connexion.rollback()
                self.connexion.close()
            print(f"Erreur lors de l'initialisation de la base de données : {e}")

    def ajout_test(self):
        try:
            self.curseur.execute("INSERT INTO partie VALUES (1);")
            self.connexion.commit()
            print("Ajout de test réussi!")
        except Exception as e:
            # En cas d'erreur, annuler la transaction
            if hasattr(self, 'connexion') and self.connexion is not None:
                self.connexion.rollback()
            print(f"Erreur lors de l'ajout de test : {e}")
        finally:
            # Fermer le curseur
            if hasattr(self, 'curseur') and self.curseur is not None:
                self.curseur.close()

