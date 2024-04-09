SELECT
    s.id,
    s.fullname,
    s.group_id,
    r.name as group_name,
    g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups_  r ON r.id = s.group_id
where g.discipline_id = 1 and s.group_id =1
ORDER BY s.fullname;

--OR

SELECT
    s.fullname,
    g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
where g.discipline_id = 1 and s.group_id =1
ORDER BY s.fullname;
