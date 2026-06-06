-- Task 1: Display employee name with department name
SELECT e.emp_name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- Task 2: Display employees earning more than 50,000
SELECT emp_name, salary
FROM employees
WHERE salary > 50000;

-- Task 3: Display department-wise total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- Task 4: Display departments with more than 2 employees
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;

-- Task 5: Display employees without a department
SELECT emp_name
FROM employees
WHERE dept_id IS NULL;