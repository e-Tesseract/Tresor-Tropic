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
            # on demande le nom et mot de passe de utilisateur
            nom_utilisateur = "brian6" #input("Nom d'utilisateur : ")
            mot_de_passe = "briandupuis220404" #input("Mot de passe de l'utilisateur : ")

            # Établir la connexion avec la base de données
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                user=nom_utilisateur,
                password=mot_de_passe
            )

            # Création du curseur pour exécuter des requêtes SQL
            cur = conn.cursor()

            # Vérifier si la base de données existe déjà
            cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), ['sql_jeux'])
            exists = cur.fetchone()

            # Si la base de données n'existe pas, la créer
            if not exists:
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('sql_jeux')))
                print("Base de données créée avec succès.")
            else:
                print("La base de données existe déjà.")

            # Fermeture du curseur et validation de la transaction
            cur.close()
            conn.commit()

            print("connection réussit")
            # Connexion à la base de données "sql_jeux"
            self.connexion = psycopg2.connect(
                host="localhost",
                database="sql_jeux",
                port="5432",
                user=nom_utilisateur,
                password=mot_de_passe
            )
            # Créer un curseur
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
                -- Calcul du nombre d'occurrences où la valeur de la colonne "special" est 'echelles'
                SELECT COUNT(*) INTO result FROM choisit WHERE special = 'echelles';

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
