-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  location text,
  price float,
  description text,
  user_id int
);

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  name text,
  password text
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  space_id int,
  date_booked date,
  userid_booker int,
  userid_approver int,
  approved bool DEFAULT False
);

-- Finally, we add any records that are needed for the tests to run

INSERT INTO spaces (name, location, price, description, user_id) VALUES ('Wizarding Cupboard', 'London', 50.00, 'A cosy room under the stairs. Comes with complementary spiders.', 1);
INSERT INTO spaces (name, location, price, description, user_id) VALUES ('Amore Penthouse', 'Paris', 87.00, 'Within view of the Eiffel Tower, this penthouse is your parisian dream.', 2);
INSERT INTO spaces (name, location, price, description, user_id) VALUES ('Paella Place', 'Madrid', 31.59, 'Eat paella and sleep.', 3);
INSERT INTO spaces (name, location, price, description, user_id) VALUES ('Mi Casa', 'Madrid', 45.50, 'Es tu Casa.', 3);

INSERT INTO users (username, name, password) VALUES ('mrs_dursley', 'Petunia Dursley', 'hatemynephew123');
INSERT INTO users (username, name, password) VALUES ('ratatouille', 'Remy Rat', 'kissthecook');
INSERT INTO users (username, name, password) VALUES ('montoya', 'Inigo Montoya', 'prepare2die');

INSERT INTO bookings (space_id, date_booked, userid_booker, userid_approver, approved) VALUES (4, '2024-07-12', 1, 3, False);
INSERT INTO bookings (space_id, date_booked, userid_booker, userid_approver, approved) VALUES (3, '2024-07-12', 2, 3, False);
INSERT INTO bookings (space_id, date_booked, userid_booker, userid_approver, approved) VALUES (2, '2024-07-12', 1, 2, True);
INSERT INTO bookings (space_id, date_booked, userid_booker, userid_approver, approved) VALUES (2, '2024-07-09', 1, 2, True);

