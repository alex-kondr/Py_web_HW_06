SELECT  round(avg(e.Rating), 1) avg_rating, s.Name, sub.Name
FROM Evaluations e
JOIN Students s ON s.id = e.Student_id
JOIN Subjects sub ON sub.id = e.Subject_id
WHERE sub.Name = 'music'
ORDER BY avg_rating DESC
LIMIT 1