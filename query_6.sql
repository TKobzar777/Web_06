SELECT
    s.id as student_id,
    s.fullname as student_name,
    g.name as group_name
FROM students s
JOIN groups_ g ON g.id = s.group_id
where g.id  = 2
ORDER BY s.fullname;