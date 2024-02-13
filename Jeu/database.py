############################################################################################
# développer par brian
# le programme sert à crée une base de donnée postgreSQL pour un jeux vidéo
############################################################################################
# amélioration ou ajouter à faire:
#   - amélioré la qualité du code
#   - ajout des derniers commentaires
#
# ajout potenciel(non obligatoire):
#   - (aucune pour l'instant)
############################################################################################

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

            self.curseur.execute("DROP TABLE IF EXISTS partie CASCADE;")
            self.curseur.execute("DROP TABLE IF EXISTS cases CASCADE;")
            self.curseur.execute("DROP TABLE IF EXISTS choisit CASCADE;")
            self.curseur.execute("DROP TABLE IF EXISTS resulta CASCADE;")

            # Création des tables
            self.curseur.execute("CREATE TABLE IF NOT EXISTS partie (id_partie INTEGER PRIMARY KEY, nb_joueur INTEGER);")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS cases (id_case INTEGER PRIMARY KEY);")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS choisit (id_nombre INTEGER, id_partie INTEGER, id_case INTEGER, id_joueur INTEGER, dés INTEGER, PRIMARY KEY (id_nombre, id_partie, id_case, id_joueur), FOREIGN KEY (id_partie) REFERENCES partie(id_partie), FOREIGN KEY (id_case) REFERENCES cases(id_case));")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS resulta (id_joueur INTEGER, id_resulta INTEGER, id_partie INTEGER, resulta BOOLEAN, PRIMARY KEY (id_resulta, id_partie, id_joueur), FOREIGN KEY (id_partie) REFERENCES partie(id_partie));")

            ################################# partie création fonction ################################################
            # permet de faire des insert dans la table partie de façon automatique
            sql_function_partie = """
            CREATE OR REPLACE PROCEDURE ajout_partie(joueur_nb INTEGER) AS $$
            DECLARE
                nb_id_partie INTEGER;
            BEGIN
                SELECT MAX(id_partie) INTO nb_id_partie FROM partie;

                IF nb_id_partie IS NULL THEN
                    nb_id_partie := 1;
                ELSE
                    nb_id_partie := nb_id_partie + 1;
                END IF;

                INSERT INTO partie VALUES (nb_id_partie, joueur_nb);
            END;
            $$
            LANGUAGE plpgsql;

            """

            # permet de faire des insert dans la table cases de façon automatique
            sql_function_cases = """
            CREATE OR REPLACE PROCEDURE ajout_cases() AS $$
            DECLARE
                nb_id_cases INTEGER;
            BEGIN
                SELECT MAX(id_case) INTO nb_id_cases FROM cases;

                IF nb_id_cases IS NULL THEN
                        nb_id_cases := 0;
                    ELSE
                        nb_id_cases := nb_id_cases + 1;
                    END IF;

                INSERT INTO cases VALUES (nb_id_cases);
            END;
            $$
            LANGUAGE plpgsql;
            """

            # permet de faire des insert dans la table choisit de façon automatique
            sql_function_choisit = """
            CREATE OR REPLACE PROCEDURE ajout_choisit(partie_actuel INTEGER, case_choix INTEGER, joueur_actul INTEGER) AS $$
            DECLARE
                nb_id_nombre INTEGER;
            BEGIN
                SELECT MAX(id_nombre) INTO nb_id_nombre FROM choisit;

                IF nb_id_nombre IS NULL THEN
                        nb_id_nombre := 0;
                    ELSE
                        nb_id_nombre := nb_id_nombre + 1;
                    END IF;

                INSERT INTO choisit VALUES (nb_id_nombre, partie_actuel, case_choix, joueur_actul);
            END;
            $$
            LANGUAGE plpgsql;
            """

            # permet de faire des insert dans la table resulta de façon automatique
            sql_function_resulta = """
            CREATE OR REPLACE PROCEDURE ajout_resulta(resulta BOOLEAN, id_resulta INTEGER, joueur_actul INTEGER, id_partie INTEGER) AS $$
            DECLARE
                nb_id_resulta INTEGER;
            BEGIN
                SELECT MAX(id_resulta) INTO nb_id_resulta FROM resulta;

                IF nb_id_resulta IS NULL THEN
                        nb_id_resulta := 0;
                    ELSE
                        nb_id_resulta := nb_id_resulta + 1;
                    END IF;

                INSERT INTO resulta VALUES (joueur_actul, nb_id_resulta, id_partie, resulta);
            END;
            $$
            LANGUAGE plpgsql;
            """

            # ajout a la base de donné les fonctions sql et les tables
            self.curseur.execute(sql_function_partie)
            self.curseur.execute(sql_function_cases)
            self.curseur.execute(sql_function_choisit)
            self.curseur.execute(sql_function_resulta)
            self.connexion.commit()
                                 

            # Exécutez la requête pour créer 

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

