SELECT
    t.id,
    t.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers  t ON t.id = d.teacher_id
where t.id  = 2
GROUP BY t.id
ORDER BY average_grade;