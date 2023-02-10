SELECT stud.Name Student, e.Rating Rating, e.Date, sub.Name Subject, g.Name Group_
FROM Students stud
JOIN Groups g ON g.id = stud.Group_id
JOIN Evaluations e ON e.Student_id = stud.id
JOIN Subjects sub ON sub.id = e.Subject_id
WHERE g.Name = 'Adams-Jones' AND sub.Name = 'art'
ORDER BY stud.Name