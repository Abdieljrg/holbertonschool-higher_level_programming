-- list score and name for rows that are not null in name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;