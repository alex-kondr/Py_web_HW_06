SELECT e.Rating Rating, e.Date, stud.Name Student, g.Name Group_, sub.Name Subject
FROM Evaluations e
JOIN Subjects sub ON sub.id = e.Subject_id
JOIN Students stud ON stud.id = e.Student_id
JOIN Groups g ON g.id = stud.Group_id
WHERE sub.Name = 'art' AND g.Name = 'Adams-Jones'
WHERE e.Date = (SELECT e2.Date FROM Evaluations e2 ORDER BY DESC LIMIT 1)