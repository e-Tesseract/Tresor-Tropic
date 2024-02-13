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



CREATE TABLE partie (
    id_partie INTEGER PRIMARY KEY,
    nb_joueur INTEGER
);

CREATE TABLE cases (
    id_case INTEGER PRIMARY KEY
);

CREATE TABLE choisit (
    id_nombre INTEGER,
    id_partie INTEGER,
    id_case INTEGER,
    id_joueur INTEGER,
    PRIMARY KEY (id_nombre, id_partie, id_case, id_joueur),
    FOREIGN KEY (id_partie) REFERENCES partie(id_partie),
    FOREIGN KEY (id_case) REFERENCES cases(id_case)
);

CREATE TABLE resulta (
    id_joueur INTEGER,
    id_resulta INTEGER,
    id_partie INTEGER,
    resulta BOOLEAN,
    PRIMARY KEY (id_nombre, id_partie, id_case, id_joueur, resulta),
    FOREIGN KEY (id_partie) REFERENCES partie(id_partie),
);

################################################################################################

CREATE PROCEDURE ajout_partie(joueur_nb INTEGER) AS $$
DECLARE
    nb_id_joueur INTEGER;
BEGIN
    SELECT MAX(id_joueur) INTO nb_id_joueur FROM partie;

    IF nb_id_joueur IS NULL THEN
            nb_id_joueur := 1;
        ELSE
            nb_id_joueur := nb_id_joueur + 1;
        END IF;

    INSERT INTO partie VALUES (nb_id_joueur, joueur_nb);
END;
$$
LANGUAGE plpgsql;

################################################################################################

CREATE PROCEDURE ajout_cases() AS $$
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

################################################################################################


CREATE PROCEDURE ajout_choisit(partie_actuel INTEGER, case_choix INTEGER, joueur_actul INTEGER) AS $$
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

################################################################################################

CREATE PROCEDURE ajout_resulta(resulta BOOLEAN, id_resulta INTEGER, joueur_actul INTEGER, id_partie INTEGER) AS $$
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