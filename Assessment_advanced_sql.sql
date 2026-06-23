
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE
);

INSERT INTO employees (emp_name, salary, hire_date) VALUES
('Nistha',  80000, '2024-01-15'),
('Raj',     45000, '2023-06-10'),
('Priya',   75000, '2024-03-20'),
('Meet',    55000, '2023-12-05'),
('Riya',    45000, '2024-05-18'),
('Arjun',   90000, '2024-02-28'),
('Sneha',   60000, '2023-08-14'),
('Dev',     75000, '2024-06-01'),
('Amit',    45000, '2023-11-22'),
('Pooja',   90000, '2024-04-10');

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

SET @N = 2;
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET (@N - 1);


CREATE TABLE duplicate_test (
    id INT,
    name VARCHAR(50),
    salary INT
);

INSERT INTO duplicate_test VALUES
(1, 'Nistha', 50000),
(2, 'Raj',    45000),
(3, 'Nistha', 50000),
(4, 'Priya',  60000),
(5, 'Raj',    45000);

-- View duplicates
SELECT name, salary, COUNT(*) AS count
FROM duplicate_test
GROUP BY name, salary
HAVING COUNT(*) > 1;


DELETE FROM duplicate_test
WHERE id NOT IN (
    SELECT min_id FROM (
        SELECT MIN(id) AS min_id
        FROM duplicate_test
        GROUP BY name, salary
    ) AS temp
);


SELECT * FROM duplicate_test;

CREATE TABLE table_a (
    emp_id INT,
    emp_name VARCHAR(50)
);

CREATE TABLE table_b (
    emp_id INT,
    emp_name VARCHAR(50)
);

INSERT INTO table_a VALUES (1,'Nistha'),(2,'Raj'),(3,'Priya'),(4,'Meet');
INSERT INTO table_b VALUES (2,'Raj'),(3,'Priya'),(5,'Riya'),(6,'Arjun');

SELECT a.emp_id, a.emp_name
FROM table_a a
INNER JOIN table_b b
ON a.emp_id = b.emp_id AND a.emp_name = b.emp_name;



SELECT emp_name, hire_date
FROM employees
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
ORDER BY hire_date DESC;


CREATE TABLE numbers_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    value INT
);

INSERT INTO numbers_table (value) VALUES
(1),(1),(2),(3),(3),(3),(4),(5),(5);

SELECT DISTINCT a.value
FROM numbers_table a
JOIN numbers_table b ON a.id = b.id - 1
WHERE a.value = b.value;

SELECT a.id, a.value
FROM numbers_table a
JOIN numbers_table b ON a.id = b.id - 1
WHERE a.value = b.value;