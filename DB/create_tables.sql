CREATE TABLE players(
    email VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50),
    nickname VARCHAR(50),
    register_date TIMESTAMP
);

CREATE TABLE games(
    id INT PRIMARY KEY,
    seconds_played INT NOT NULL,
    fk_player VARCHAR(50),
    CONSTRAINT cons_fk_player FOREIGN KEY(fk_player) REFERENCES players(email)
);

CREATE TABLE fruits(
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(200),
    value INT NOT NULL
);

CREATE TABLE fruits_per_game(
    fk_idfruit INT NOT NULL,
    fk_idgame INT NOT NULL,
    PRIMARY KEY(fk_idfruit, fk_idgame),
    CONSTRAINT cons_fkgame FOREIGN KEY(fk_idgame) REFERENCES games(id),
    CONSTRAINT cons_fkfruit FOREIGN KEY(fk_idfruit) REFERENCES fruits(id)
);