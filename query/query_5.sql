SELECT s.Name Subject, t.Name Teacher_Name 
FROM Subjects s
JOIN Teachers t ON t.id = s.Teacher_id
ORDER BY t.Name