DROP TABLE holidays;
DROP TABLE cities;
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

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id)
);

CREATE TABLE holidays (
    id SERIAL PRIMARY KEY,
    holiday_type VARCHAR(255),
    country_id INT REFERENCES countries(id),
    city_id INT REFERENCES cities(id),
    review TEXT,
    user_id INT REFERENCES users(id)
);