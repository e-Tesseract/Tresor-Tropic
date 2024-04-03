/*############################################################################################
# Développé par Brian
# Ce programme a pour seul but de faciliter la visualisation du code SQL pour un jeu vidéo.
############################################################################################
# Améliorations ou ajouts à faire :
#   - Ajouter des commentaires pour aider à la compréhension.
#
# Ajouts potentiels (non obligatoires) :
#   - (Aucun pour l'instant).
############################################################################################*/


/*################################################# Creation des Tables #################################################*/

DROP TABLE if EXISTS partie CASCADE;
DROP TABLE if EXISTS cases CASCADE;
DROP TABLE if EXISTS choisit CASCADE;
DROP TABLE if EXISTS resulta CASCADE;

-- permet de stocker id de la partie et le nombre de joueur
CREATE TABLE partie (
    id_partie INTEGER PRIMARY KEY,
    nb_joueur INTEGER
);

-- permet de la totalité es id des cases du plateau
CREATE TABLE cases (
    id_case INTEGER PRIMARY KEY
);

-- permet de stocker id du deplacement, si le deplacement est du à un deplacement normal, un combat, ou autres evenement
-- il utilise id de la partie en question id de la case et de id du joueur qui c'est deplacer mais aussi le resulta du des
CREATE TABLE choisit (
    id_nombre INTEGER,
    id_partie INTEGER,
    id_case INTEGER,
    id_joueur INTEGER,
    result_des INTEGER,
    spécial VARCHAR,
    PRIMARY KEY (id_nombre, id_partie, id_case, id_joueur),
    FOREIGN KEY (id_partie) REFERENCES partie(id_partie),
    FOREIGN KEY (id_case) REFERENCES cases(id_case)
);

-- permet de stocker les informations d'un combat avec un monstre si le joueur a gagner ou perdu
CREATE TABLE resulta (
    id_resulta INTEGER,
    id_joueur INTEGER,
    id_partie INTEGER,
    resulta BOOLEAN,
    PRIMARY KEY (id_resulta, id_joueur, id_partie, resulta),
    FOREIGN KEY (id_partie) REFERENCES partie(id_partie)
);

/*################################################# Creation des fonctions #################################################*/

-- permet d'automatisé insertion dans la table partie
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

/*################################################################################################*/

-- permet d'automatisé insertion de tuple dans la table cases
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

/*################################################################################################*/

-- permet d'automatisé insertion de tuple dans la table choisit
CREATE OR REPLACE PROCEDURE ajout_choisit(partie_actuel INTEGER, case_choix INTEGER, joueur_actul INTEGER, result_des INTEGER, spécial VARCHAR) AS $$
DECLARE
    nb_id_nombre INTEGER;
BEGIN
    SELECT MAX(id_nombre) INTO nb_id_nombre FROM choisit;

    IF nb_id_nombre IS NULL THEN
            nb_id_nombre := 0;
        ELSE
            nb_id_nombre := nb_id_nombre + 1;
        END IF;

    INSERT INTO choisit VALUES (nb_id_nombre, partie_actuel, case_choix, joueur_actul, result_des, spécial);
END;
$$
LANGUAGE plpgsql;
            

/*################################################################################################*/

-- permet d'automatisé insertion de tuple dans la table resulta
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

/*################################################# requete SQL #################################################*/

-- Nombre de case totales franchises
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



-- Nombre de parties joués
SELECT MAX(id_partie) FROM partie;

-- heatmap: cases les plus sélectionnées


-- Record du nombre de cases minimum et max que quelqu'un a fait pour gagner
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


-- Nombre de cases échelles empruntés
CREATE OR REPLACE FUNCTION total_echelles()
RETURNS INTEGER
AS $$
DECLARE
    result INTEGER;
BEGIN
    -- Calcul du nombre d'occurrences où la valeur de la colonne "spécial" est 'echelles'
    SELECT COUNT(*) INTO result FROM choisit WHERE spécial = 'echelles';

    -- Retourner le résultat
    RETURN result;
END;
$$
LANGUAGE plpgsql;


-- Nombre de défaite et victoire face aux monstres
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


-- Moyenne que les joueurs tirent quand ils lancent les dés
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
