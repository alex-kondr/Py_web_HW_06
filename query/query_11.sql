SELECT ROUND(AVG(e.Rating), 1) avg_Rating, stud.Name Student, t.Name Teacher
FROM Evaluations e
JOIN Subjects sub ON sub.id = e.Subject_id
JOIN Teachers t ON t.id = sub.Teacher_id
JOIN Students stud ON stud.id = e.Student_id
WHERE stud.Name = 'Eugene Huff' AND t.Name = 'Kevin Washington'