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
import os
import json
from psycopg2 import sql

class init_bdd:
    def __init__(self):
        try:
            print("init_bdd")
            vide = False
            # Vérifier si le fichier existe déjà
            if not os.path.exists("connectionbdd.json"):
                # Créer le fichier s'il n'existe pas
                with open("connectionbdd.json", "w") as fichier:
                    fichier.write("[]")  # Écrire une liste vide pour initialiser le fichier JSON

            # Enregistrer les informations dans un fichier JSON
            with open("connectionbdd.json", "r+") as fichier:
                # Vérifier si le fichier est vide
                if os.path.getsize("connectionbdd.json") == 0:
                    vide = True
                else:
                    partie_data = json.load(fichier)

                    # Extraire les données de connexion
                    joueurs_data = partie_data["connection"][0]  # Accès au premier élément de la liste

                    # Créer les objets correspondant aux données de connection
                    nom_utilisateur = joueurs_data["nom"]
                    mot_de_passe = joueurs_data["mot_de_passe"]

            if vide==True:
                # on demande le nom et mot de passe de l'utilisateur
                nom_utilisateur = input("Nom d'utilisateur : ")
                mot_de_passe = input("Mot de passe de l'utilisateur : ")

            # Établir la connexion avec PostgreSQL pour créer la base de données
            conn_creation_db = psycopg2.connect(
                host="localhost",
                port="5432",
                user=nom_utilisateur,
                password=mot_de_passe
            )

            # Enregistrer les informations dans un fichier JSON
            with open("connectionbdd.json", "r+") as fichier:
                # Vérifier si le fichier est vide
                if os.path.getsize("connectionbdd.json") == 0:
                    # Créer une liste pour stocker les informations de connexion
                    connection = []

                    # nom du compte SQL
                    nom = nom_utilisateur

                    # mot de passe du compte SQL
                    mot_de_passe = mot_de_passe

                    # ajouter les informations de connection à la liste
                    connection.append({"nom": nom, "mot_de_passe": mot_de_passe})

                    # Créer un dictionnaire avec la clé "connection" contenant la liste des données
                    data = {"connection": connection}

                    # Enregistrer les données dans le fichier JSON
                    with open("connectionbdd.json", "w") as fichier:
                        # Retourner au début du fichier pour écrire les données
                        fichier.seek(0)
                        # enregistrer le dictionnaire dans le fichier
                        json.dump(data, fichier)

            # Désactiver la transaction automatique
            conn_creation_db.autocommit = True

            # Créer un curseur pour exécuter la commande CREATE DATABASE
            cur_creation_db = conn_creation_db.cursor()

            # Créer la base de données si elle n'existe pas déjà
            cur_creation_db.execute("SELECT 1 FROM pg_database WHERE datname = 'sql_jeux'")
            exists = cur_creation_db.fetchone()

            if not exists:
                cur_creation_db.execute("CREATE DATABASE sql_jeux;")
                print("Base de données créée avec succès.")
            else:
                print("La base de données existe déjà.")

            # Fermer le curseur et la connexion utilisés pour la création de la base de données
            cur_creation_db.close()
            conn_creation_db.close()

            # Établir la connexion avec la base de données nouvellement créée
            self.connexion = psycopg2.connect(
                host="localhost",
                database="sql_jeux",
                port="5432",
                user=nom_utilisateur,
                password=mot_de_passe
            )

            # Créer un curseur pour exécuter des requêtes SQL
            self.curseur = self.connexion.cursor()
            # Autres opérations d'initialisation...

            ################################# Partie création des Tables ################################################

            # supprime automatiquement les tables (à laisser en commentaire sauf si pour effectuer des tests)
            '#'"""
            self.curseur.execute("DROP TABLE IF EXISTS partie CASCADE;")
            self.curseur.execute("DROP TABLE IF EXISTS cases CASCADE;")
            self.curseur.execute("DROP TABLE IF EXISTS choisit CASCADE;")
            self.curseur.execute("DROP TABLE IF EXISTS resulta CASCADE;")

            self.curseur.execute("DROP PROCEDURE IF EXISTS ajout_partie CASCADE;")
            self.curseur.execute("DROP PROCEDURE IF EXISTS ajout_cases CASCADE;")
            self.curseur.execute("DROP PROCEDURE IF EXISTS ajout_choisit CASCADE;")
            self.curseur.execute("DROP PROCEDURE IF EXISTS ajout_resulta CASCADE;")
            '#'"""

            # Création des tables si elles existes pas (ne pas oublie de supprimer les tables si vous effectuer des modifications sur les tables)
            self.curseur.execute("CREATE TABLE IF NOT EXISTS partie (id_partie INTEGER PRIMARY KEY, nb_joueur INTEGER);")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS cases (id_case INTEGER PRIMARY KEY);")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS choisit (id_nombre INTEGER, id_partie INTEGER, id_case INTEGER, id_joueur INTEGER, result_des INTEGER, special VARCHAR, PRIMARY KEY (id_nombre, id_partie, id_case, id_joueur), FOREIGN KEY (id_partie) REFERENCES partie(id_partie), FOREIGN KEY (id_case) REFERENCES cases(id_case));")
            self.curseur.execute("CREATE TABLE IF NOT EXISTS resulta (id_joueur INTEGER, id_resulta INTEGER, id_partie INTEGER, resulta BOOLEAN, PRIMARY KEY (id_resulta, id_partie, id_joueur), FOREIGN KEY (id_partie) REFERENCES partie(id_partie));")

            ################################# Partie création des Fonction ################################################
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
            CREATE OR REPLACE PROCEDURE ajout_choisit(partie_actuel INTEGER, case_choix INTEGER, joueur_actul INTEGER, result_des INTEGER, special VARCHAR) AS $$
            DECLARE
                nb_id_nombre INTEGER;
            BEGIN
                SELECT MAX(id_nombre) INTO nb_id_nombre FROM choisit;

                IF nb_id_nombre IS NULL THEN
                        nb_id_nombre := 0;
                    ELSE
                        nb_id_nombre := nb_id_nombre + 1;
                    END IF;

                INSERT INTO choisit VALUES (nb_id_nombre, partie_actuel, case_choix, joueur_actul, result_des, special);
            END;
            $$
            LANGUAGE plpgsql;
            """

            # permet de faire des insert dans la table resulta de façon automatique
            sql_function_resulta = """
            CREATE OR REPLACE PROCEDURE ajout_resulta(resulta BOOLEAN, joueur_actul INTEGER, id_partie INTEGER) AS $$
            DECLARE
                nb_id_resulta INTEGER;
            BEGIN
                SELECT MAX(id_resulta) INTO nb_id_resulta FROM resulta;

                IF nb_id_resulta IS NULL THEN
                        nb_id_resulta := 0;
                    ELSE
                        nb_id_resulta := nb_id_resulta + 1;
                    END IF;

                INSERT INTO resulta VALUES (joueur_actul+1, nb_id_resulta, id_partie, resulta);
            END;
            $$
            LANGUAGE plpgsql;

            """

            total_cases_parcourues = """
            CREATE OR REPLACE FUNCTION total_cases_parcourues()
            RETURNS INTEGER
            AS $$
            DECLARE
                total_sum INTEGER := 0;
                prev_id_case INTEGER := NULL;
                current_id_case INTEGER := NULL;
            BEGIN
                -- Itérer à travers les enregistrements triés par ordre
                FOR current_id_case IN
                    SELECT id_case
                    FROM choisit
                    ORDER BY id_joueur, id_partie, id_nombre
                LOOP
                    -- Si ce n'est pas le premier enregistrement
                    IF prev_id_case IS NOT NULL THEN
                        -- Ajouter la différence entre les cases à la somme totale
                        total_sum := total_sum + LEAST(ABS(current_id_case - prev_id_case), 30 - ABS(current_id_case - prev_id_case));
                    END IF;

                    -- Mettre à jour la case précédente
                    prev_id_case := current_id_case;
                END LOOP;

                -- Retourner la somme totale des différences entre les cases parcourues par tous les joueurs
                RETURN total_sum;
            END;
            $$
            LANGUAGE plpgsql;
            """

            ##############################################################################################################

            total_deplacements_joueurs_gagnants = """
            CREATE OR REPLACE FUNCTION total_deplacements_joueurs_gagnants()
            RETURNS TABLE (minimum_total INTEGER, maximum_total INTEGER)
            AS $$
            DECLARE
                min_total INTEGER := 0;
                max_total INTEGER := 0;
            BEGIN
                -- Calcul du total des déplacements des joueurs ayant gagné
                SELECT MIN(total_deplacement), MAX(total_deplacement)
                INTO min_total, max_total
                FROM (
                    SELECT id_joueur, SUM(ABS(id_case - lag_id_case)) AS total_deplacement
                    FROM (
                        SELECT *,
                            LAG(id_case) OVER (PARTITION BY id_joueur, id_partie ORDER BY id_nombre) AS lag_id_case
                        FROM choisit
                    ) AS subquery
                    WHERE id_joueur IN (
                        SELECT id_joueur
                        FROM choisit
                        WHERE id_case = 30
                        GROUP BY id_joueur
                    )
                    GROUP BY id_joueur, id_partie -- Ajout de id_partie pour filtrer les déplacements par partie
                ) AS subquery;

                -- Retourner le minimum et le maximum des totaux de déplacements
                RETURN QUERY SELECT min_total, max_total;
            END;
            $$
            LANGUAGE plpgsql;
            """

            ##############################################################################################################

            total_echelles = """
            CREATE OR REPLACE FUNCTION total_echelles()
            RETURNS INTEGER
            AS $$
            DECLARE
                result INTEGER;
            BEGIN
                -- Calcul du nombre d'occurrences où la valeur de la colonne "special" est 'echelle'
                SELECT COUNT(*) INTO result FROM choisit WHERE special = 'echelle';

                -- Retourner le résultat
                RETURN result;
            END;
            $$
            LANGUAGE plpgsql;
            """
            
            ##############################################################################################################

            count_resultats = """
            CREATE OR REPLACE FUNCTION count_resultats()
            RETURNS TABLE (true_count INTEGER, false_count INTEGER)
            AS $$
            BEGIN
                -- Calcul du nombre de fois où le résultat est vrai (true) et faux (false)
                SELECT
                    COUNT(CASE WHEN resulta THEN 1 END) AS true_count,
                    COUNT(CASE WHEN NOT resulta THEN 1 END) AS false_count
                INTO
                    true_count,
                    false_count
                FROM resulta;

                -- Retourner le nombre de fois où le résultat est vrai (true) et faux (false)
                RETURN QUERY SELECT true_count, false_count;
            END;
            $$
            LANGUAGE plpgsql;
            """

            ##############################################################################################################

            moyenne_des = """
            CREATE OR REPLACE FUNCTION moyenne_des()
            RETURNS FLOAT
            AS $$
            DECLARE
                avg_result FLOAT;
            BEGIN
                -- Calcul de la moyenne des valeurs de la colonne result_des
                SELECT AVG(result_des) INTO avg_result FROM choisit;

                -- Retourner la moyenne
                RETURN avg_result;
            END;
            $$
            LANGUAGE plpgsql;
            """
            
            self.curseur.execute(total_cases_parcourues)
            self.curseur.execute(total_deplacements_joueurs_gagnants)
            self.curseur.execute(total_echelles)
            self.curseur.execute(count_resultats)
            self.curseur.execute(moyenne_des)

            # valide la la totalité des execute fait avant permetant leurs création
            self.connexion.commit()
                                    
            # on previens que la création à était réussie
            print("Initialisation des fonctions réussie!")

            self.curseur.execute(sql_function_partie)
            self.curseur.execute(sql_function_cases)
            self.curseur.execute(sql_function_choisit)
            self.curseur.execute(sql_function_resulta)

            # valide la la totalité des execute fait avant permetant leurs création
            self.connexion.commit()
                                 

            # on previens que la création à était réussie
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

