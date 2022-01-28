DROP TABLE countries;
DROP TABLE users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);