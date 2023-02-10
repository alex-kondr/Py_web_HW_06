SELECT ROUND(AVG(e.Rating), 1) avg_Rating, t.Name Teacher, s.Name Subject
FROM Evaluations e
JOIN Subjects s ON s.id = e.Subject_id 
JOIN Teachers t ON t.id = s.Teacher_id 
GROUP BY s.Name 
ORDER BY t.Name 