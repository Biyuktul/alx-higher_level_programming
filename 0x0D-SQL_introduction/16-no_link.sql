-- selecting rows that are not NULL
SELECT name, score FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
