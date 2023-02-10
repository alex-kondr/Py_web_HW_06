SELECT e.Rating Rating, e.Date, stud.Name Student, stud.id, g.Name Group_, sub.Name Subject
FROM Evaluations e
JOIN Subjects sub ON sub.id = e.Subject_id
JOIN Students stud ON stud.id = e.Student_id
JOIN Groups g ON g.id = stud.Group_id
WHERE sub.Name = 'art' 
	AND g.Name = 'Adams-Jones'
	AND e.Date = (	
		SELECT e2.Date 
		FROM Evaluations e2
		JOIN Subjects sub ON sub.id = e2.Subject_id
		JOIN Students stud ON stud.id = e2.Student_id
		JOIN Groups g ON g.id = stud.Group_id 
		WHERE sub.Name = 'art'
			AND g.Name = 'Adams-Jones'
		ORDER BY e2.Date DESC 
		LIMIT 1
	)