-- List all records with a name in second_table, ordered by score (desc)
-- Remember, "It's spelled F-R-A-N-C-I-S." Names matter, even in tables.

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
