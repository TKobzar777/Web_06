SELECT
    d.id,
    d.name,
    t.fullname
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id
where t.id = 1
ORDER BY d.name;