CREATE TABLE worker (
worker_id INTEGER PRIMARY KEY,
gryp_id INTEGER REFERENCES gryp(id),
name VARCHAR(255),
salary INTEGER NOT NULL,
position VARCHAR(255));


INSERT INTO worker (worker_id, gryp_id, name, salary, position) 
VALUES
(1, 1, 'Иван Петров', 75000, 'Senior Developer'),
(2, 1, 'Мария Смирнова', 65000, 'QA Engineer'),
(3, 2, 'Алексей Иванов', 85000, 'Project Manager'),
(4, 2, 'Ольга Сидорова', 60000, 'DevOps Engineer'),
(5, 1, 'Сергей Козлов', 55000, 'Junior Developer'),
(6, 2, 'Анна Кузнецова', 95000, 'CTO'),
(7, 1, 'Дмитрий Новиков', 58000, 'Backend Developer'),
(8, 2, 'Екатерина Воробьева', 72000, 'Product Manager');

-- Количество студентов в каждой группе
SELECT 
    g.name AS group_name, 
    COUNT(s.id) AS student_count 
FROM gryp g
LEFT JOIN student s ON g.id = s.group_id
GROUP BY g.name
ORDER BY student_count DESC;

--Средние оценки по предметам в каждой группе
SELECT 
    g.name AS group_name,
    ROUND(AVG(sm.math_mark_average), 2) AS avg_math,
    ROUND(AVG(sm.physics_mark_average), 2) AS avg_physics,
    ROUND(AVG(sm.python_mark_average), 2) AS avg_python
FROM gryp g
JOIN student s ON g.id = s.group_id
JOIN student_marks sm ON s.id = sm.student_id
GROUP BY g.name
ORDER BY g.name;

--Сортировка студентов по средней оценке по Python:
SELECT 
    s.name AS student_name,
    sm.python_mark_average AS python_avg
FROM student s
JOIN student_marks sm ON s.id = sm.student_id
ORDER BY python_avg DESC;

--Общая сумма зарплат по группам:
SELECT 
    gryp_id AS группа,
    SUM(salary) AS общая_сумма_зарплат
FROM worker
GROUP BY gryp_id
ORDER BY общая_сумма_зарплат DESC;