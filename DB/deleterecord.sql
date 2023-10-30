DELETE FROM players 
WHERE players.email LIKE "";

DELETE FROM fruits
WHERE fruit.id_fruit = NULL;

DELETE FROM games
WHERE id_games = 1;

DELETE FROM fruits_per_game 
WHERE fk_idgame = 1;