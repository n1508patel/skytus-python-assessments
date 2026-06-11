CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
);

-- Insert data
INSERT INTO departments VALUES (1, 'IT');
INSERT INTO departments VALUES (2, 'HR');
INSERT INTO departments VALUES (3, 'Finance');
INSERT INTO departments VALUES (4, 'Marketing');

INSERT INTO employees VALUES (1, 'Nistha', 1, 60000);
INSERT INTO employees VALUES (2, 'Amit', 2, 45000);
INSERT INTO employees VALUES (3, 'Priya', 1, 75000);
INSERT INTO employees VALUES (4, 'Meet', 3, 55000);
INSERT INTO employees VALUES (5, 'Riya', 2, 48000);
INSERT INTO employees VALUES (6, 'Arjun', 1, 80000);
INSERT INTO employees VALUES (7, 'Sneha', 4, 40000);
INSERT INTO employees VALUES (8, 'Dev', NULL, 52000);

-- Task 1: Find employees earning more than average salary
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Task 2: Find department with highest total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC
LIMIT 1;

-- Task 3: Display employee with second highest salary
SELECT emp_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Task 4: Display employees working in same department as "Amit"
SELECT emp_name, dept_id
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);

-- Task 5: Find employees whose salary is more than all HR employees
SELECT emp_name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary FROM employees
    WHERE dept_id = (
        SELECT dept_id FROM departments
        WHERE dept_name = 'HR'
    )
);

-- Task 6: Find departments that have at least one employee
SELECT dept_name
FROM departments
WHERE dept_id IN (
    SELECT DISTINCT dept_id FROM employees
    WHERE dept_id IS NOT NULL
);

-- Task 7: Display employees who earn the maximum salary in their department
SELECT emp_name, salary, dept_id
FROM employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE dept_id = e.dept_id
);