SELECT round(avg(e.Rating), 1) avg_rating, sub.Name as sub_name, g.Name as group_name
FROM Evaluations e
JOIN Students s ON s.id = e.Student_id
JOIN Subjects sub ON sub.id = e.Subject_id
JOIN Groups g ON g.id = s.Group_id
WHERE sub.Name = 'art'
GROUP BY g.Name
ORDER BY avg_rating DESC