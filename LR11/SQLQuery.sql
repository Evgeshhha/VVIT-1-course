CREATE TABLE gryp (
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES gryp(id)
);

CREATE TABLE student_marks (
    student_id INTEGER PRIMARY KEY,
    math_mark_average FLOAT,
    physics_mark_average FLOAT,
    python_mark_average FLOAT,
    FOREIGN KEY (student_id) REFERENCES student(id)
);

-- ������
INSERT INTO gryp(id, name, description) VALUES
(1, '������ A', '������ ������������ �����������'),
(2, '������ B', '������ ������������� �����������');

-- ��������
INSERT INTO student (id, name, group_id) VALUES
(1, '���� ������', 1),
(2, '���� ������', 1),
(3, '����� ��������', 2),
(4, '���� �������', 2);

-- ������ ���������
INSERT INTO student_marks (student_id, math_mark_average, physics_mark_average, python_mark_average) VALUES
(1, 4.5, 3.8, 4.2),
(2, 3.2, 4.0, 3.9),
(3, 4.8, 4.5, 4.6),
(4, 3.5, 3.7, 3.9);



--������� � �����������
--�������� �� '������ A'

SELECT s.id, s.name, g.name AS group_name 
FROM student s
JOIN gryp g ON s.group_id = g.id
WHERE g.name = '������ A';

--�������� � ������� ������� �� ���������� ���� 4.0:
SELECT s.name, sm.math_mark_average 
FROM student s
JOIN student_marks sm ON s.id = sm.student_id
WHERE sm.math_mark_average > 4.0;

--������, � ������� ���� �������� �� ������� ������ �� ������ ���� 4.0:
SELECT DISTINCT g.name 
FROM gryp g
JOIN student s ON g.id = s.group_id
JOIN student_marks sm ON s.id = sm.student_id
WHERE sm.physics_mark_average < 4.0;
