SELECT s.Name, g.Name
FROM Students s
JOIN Groups g ON g.id = s.Group_id
WHERE g.Name = 'Adams-Jones'