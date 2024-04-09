SELECT
    d.name as discipline_name
FROM grades g
JOIN students s ON s.id = g.student_id
join disciplines d on d.id = g.discipline_id
where g.student_id = 30;