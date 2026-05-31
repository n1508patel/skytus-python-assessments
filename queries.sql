-- Task 1: Display all student records
SELECT * FROM students;

-- Task 2: Display only name and department
SELECT name, department FROM students;

-- Task 3: Find students with marks greater than 75
SELECT * FROM students
WHERE marks > 75;

-- Task 4: Display students from CSE department
SELECT * FROM students
WHERE department = 'CSE';

-- Task 5: Sort students by marks descending
SELECT * FROM students
ORDER BY marks DESC;

-- Task 6: Display top 3 scorers
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3;

-- Task 7: Count total number of students
SELECT COUNT(*) AS total_students FROM students;

-- Task 8: Find average marks of students
SELECT AVG(marks) AS average_marks FROM students;

-- Task 9: Find highest and lowest marks
SELECT MAX(marks) AS highest_marks, 
       MIN(marks) AS lowest_marks 
FROM students;

-- Task 10: Find department-wise average marks
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

-- Task 11: Display departments where average marks > 70
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;