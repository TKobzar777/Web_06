SELECT --10
    d.name as discipline_name
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE g.student_id = 30 AND d.teacher_id = 1;

--OR

SELECT --10
    d.name AS discipline_name,
    s.fullname AS student_name,
    t.fullname AS teacher_name
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE g.student_id = 30 AND d.teacher_id = 1;
