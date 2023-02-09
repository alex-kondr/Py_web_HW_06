SELECT  round(avg(e.Rating), 1) avg_rating, s.Name, sub.Name, g.Name 
FROM Evaluations e
JOIN Students s ON s.id = e.Student_id
JOIN Subjects sub ON sub.id = e.Subject_id
JOIN Groups g ON g.id = s.Group_id
WHERE sub.Name = 'music'
GROUP BY g.Name
ORDER BY avg_rating DESC
LIMIT 1