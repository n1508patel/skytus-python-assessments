CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    room_no VARCHAR(10),
    contact VARCHAR(15),
    join_date DATE
);

CREATE TABLE menu (
    menu_id INT PRIMARY KEY AUTO_INCREMENT,
    day_name VARCHAR(20),
    meal_type VARCHAR(20),
    item_name VARCHAR(100),
    price DECIMAL(8,2)
);

CREATE TABLE meals (
    meal_id INT PRIMARY KEY AUTO_INCREMENT,
    menu_id INT,
    served_date DATE,
    FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    meal_id INT,
    status VARCHAR(10) DEFAULT 'Present',
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    payment_mode VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


CREATE TABLE complaints (
    complaint_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    complaint_text TEXT,
    complaint_date DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


INSERT INTO students (name, room_no, contact, join_date) VALUES
('Nistha Patel',  'A101', '9876543210', '2024-01-01'),
('Raj Shah',      'A102', '9876543211', '2024-01-01'),
('Priya Mehta',   'B201', '9876543212', '2024-01-15'),
('Meet Patel',    'B202', '9876543213', '2024-02-01'),
('Riya Desai',    'C301', '9876543214', '2024-02-01'),
('Arjun Kumar',   'C302', '9876543215', '2024-03-01'),
('Sneha Joshi',   'A103', '9876543216', '2024-03-15'),
('Dev Shah',      'D401', '9876543217', '2024-04-01');

INSERT INTO menu (day_name, meal_type, item_name, price) VALUES
('Monday',    'Breakfast', 'Poha + Chai',         30.00),
('Monday',    'Lunch',     'Dal Rice + Sabzi',     60.00),
('Monday',    'Dinner',    'Roti + Paneer',        70.00),
('Tuesday',   'Breakfast', 'Upma + Juice',         35.00),
('Tuesday',   'Lunch',     'Rajma Rice',           65.00),
('Tuesday',   'Dinner',    'Roti + Dal Makhani',   70.00),
('Wednesday', 'Breakfast', 'Idli Sambar',          40.00),
('Wednesday', 'Lunch',     'Chole Rice',           65.00),
('Wednesday', 'Dinner',    'Roti + Mix Veg',       60.00);

INSERT INTO meals (menu_id, served_date) VALUES
(1, '2024-06-03'),
(2, '2024-06-03'),
(3, '2024-06-03'),
(4, '2024-06-04'),
(5, '2024-06-04'),
(6, '2024-06-04');

INSERT INTO attendance (student_id, meal_id, status) VALUES
(1, 1, 'Present'), (2, 1, 'Present'), (3, 1, 'Absent'),
(1, 2, 'Present'), (2, 2, 'Present'), (4, 2, 'Present'),
(1, 3, 'Present'), (3, 3, 'Present'), (5, 3, 'Absent'),
(2, 4, 'Present'), (4, 4, 'Present'), (6, 4, 'Present'),
(1, 5, 'Present'), (2, 5, 'Absent'),  (3, 5, 'Present');

INSERT INTO payments (student_id, amount, payment_date, payment_mode) VALUES
(1, 3000.00, '2024-06-01', 'UPI'),
(2, 3000.00, '2024-06-01', 'Cash'),
(3, 2500.00, '2024-06-02', 'UPI'),
(4, 3000.00, '2024-06-03', 'Card'),
(5, 2000.00, '2024-06-05', 'Cash'),
(6, 3000.00, '2024-06-01', 'UPI'),
(1, 1500.00, '2024-06-15', 'UPI');

INSERT INTO complaints (student_id, complaint_text, complaint_date, status) VALUES
(1, 'Food was cold at dinner',      '2024-06-03', 'Resolved'),
(2, 'Not enough quantity in lunch', '2024-06-04', 'Pending'),
(3, 'Water not available',          '2024-06-04', 'Pending'),
(4, 'Food quality was poor',        '2024-06-05', 'Resolved');

SELECT * FROM students;
SELECT COUNT(*) AS total_students FROM students;
