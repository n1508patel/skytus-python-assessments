-- Database: company_db
-- Create tables and insert data

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

-- Insert departments
INSERT INTO departments VALUES (1, 'IT');
INSERT INTO departments VALUES (2, 'HR');
INSERT INTO departments VALUES (3, 'Finance');
INSERT INTO departments VALUES (4, 'Marketing');

-- Insert employees
INSERT INTO employees VALUES (1, 'Nistha Patel', 1, 60000);
INSERT INTO employees VALUES (2, 'Raj Shah', 2, 45000);
INSERT INTO employees VALUES (3, 'Priya Mehta', 1, 75000);
INSERT INTO employees VALUES (4, 'Meet Patel', 3, 55000);
INSERT INTO employees VALUES (5, 'Riya Desai', 2, 48000);
INSERT INTO employees VALUES (6, 'Arjun Kumar', 1, 80000);
INSERT INTO employees VALUES (7, 'Sneha Joshi', 4, 40000);
INSERT INTO employees VALUES (8, 'Dev Shah', NULL, 52000);