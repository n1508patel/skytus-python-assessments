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