CREATE TABLE players(
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50),
    nickname VARCHAR(50),
    register_date TIMESTAMP,
    PRIMARY KEY(email)
);

CREATE TABLE games(
    id_game INTEGER NOT NULL,
    seconds_played INTEGER NOT NULL,
    fk_player VARCHAR(50),
    PRIMARY KEY(id_game),
    CONSTRAINT cons_fk_player FOREIGN KEY(fk_player) REFERENCES players(email)
);

CREATE TABLE fruits(
    id_fruit INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(200),
    value INTEGER NOT NULL,
    PRIMARY KEY(id_fruit)
);

CREATE TABLE fruits_per_game(
    fk_idfruit INTEGER NOT NULL,
    fk_idgame INTEGER NOT NULL,
    total_fruits INTEGER NOT NULL,
    PRIMARY KEY(fk_idfruit, fk_idgame),
    CONSTRAINT cons_fkgame FOREIGN KEY(fk_idgame) REFERENCES games(id_game),
    CONSTRAINT cons_fkfruit FOREIGN KEY(fk_idfruit) REFERENCES fruits(id_fruit)
);