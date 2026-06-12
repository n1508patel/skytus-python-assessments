-- Constraints, Foreign Key, Index, View Assessment

-- Task 1: Create users table with Primary Key, Unique Email, Not Null Password
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_name VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    -- Task 2: Add foreign key between orders and users
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert sample data
INSERT INTO users (username, email, password) VALUES
('Nistha', 'nistha@gmail.com', 'pass123'),
('Raj', 'raj@gmail.com', 'pass456'),
('Priya', 'priya@gmail.com', 'pass789');

INSERT INTO orders (user_id, product_name, amount) VALUES
(1, 'Python Book', 499.00),
(1, 'Laptop Stand', 749.00),
(2, 'Wireless Mouse', 649.00),
(3, 'USB-C Hub', 899.00),
(2, 'Keyboard', 2499.00);

-- Task 3: Create index on email column
CREATE INDEX idx_email ON users(email);

-- Task 4: Create view to display user order summary
CREATE VIEW user_order_summary AS
SELECT
    u.user_id,
    u.username,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.username, u.email;

-- Display the view
SELECT * FROM user_order_summary;