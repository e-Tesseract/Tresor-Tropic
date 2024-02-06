--il ne sert a rien seulement a donner une representation de la base de donner

CREATE TABLE partie (
    id_partie INTEGER PRIMARY KEY
);

CREATE TABLE cases (
    id_case INTEGER PRIMARY KEY
);

CREATE TABLE choisit (
    id_nombre INTEGER,
    id_partie INTEGER,
    id_case INTEGER,
    PRIMARY KEY (id_nombre, id_partie, id_case),
    FOREIGN KEY (id_partie) REFERENCES partie(id_partie),
    FOREIGN KEY (id_case) REFERENCES cases(id_case)
);