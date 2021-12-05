CREATE TABLE temperature_data (
    id int NOT NULL AUTO_INCREMENT,
    timestamp varchar(50) NOT NULL,
    temperature float NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE action_log (
    id int NOT NULL AUTO_INCREMENT,
    timestamp varchar(50) NOT NULL,
    action varchar(50) NOT NULL,
    PRIMARY KEY(id)
);
