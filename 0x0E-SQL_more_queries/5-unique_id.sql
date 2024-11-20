-- Creates table 'unique_id' ensuring the 'id' is unique.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
