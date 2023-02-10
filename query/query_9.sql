SELECT stud.Name Student, sub.Name Sunject
FROM Students stud
JOIN Evaluations e ON e.Student_id = stud.id 
JOIN Subjects sub ON sub.id = e.Subject_id
WHERE stud.Name = 'Eugene Huff'
GROUP BY sub.Name