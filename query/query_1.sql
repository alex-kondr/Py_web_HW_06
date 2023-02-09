SELECT  round(avg(e.Rating), 1) avg_rating, s.Name
FROM Evaluations e
JOIN Students s ON s.id = e.Student_id 
GROUP BY e.Student_id 
ORDER BY avg_rating DESC
LIMIT 5