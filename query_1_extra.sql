WITH StudentGradesOfTeacher AS (
    SELECT
        s.id,
        s.fullname,
        g.grade,
        t.id as t_id
    FROM students s
    JOIN grades g ON s.id = g.student_id
    join disciplines d on d.id = g.discipline_id
    join teachers t on t.id = d.teacher_id
    WHERE s.id = 1
)
select
	id,
	ROUND(AVG(grade), 2) as average_grade
	from StudentGradesOfTeacher
	where t_id = 2
	group by id;