CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);



INSERT INTO customers (name, city) VALUES
('Nistha Patel', 'Surat'),
('Raj Shah', 'Ahmedabad'),
('Priya Mehta', 'Surat'),
('Meet Patel', 'Mumbai'),
('Riya Desai', 'Ahmedabad'),
('Arjun Kumar', 'Delhi'),
('Sneha Joshi', 'Surat');

INSERT INTO products (product_name, price) VALUES
('Python Book', 499.00),
('Laptop Stand', 749.00),
('Wireless Mouse', 649.00),
('USB-C Hub', 899.00),
('Mechanical Keyboard', 2499.00),
('Webcam', 1299.00);

INSERT INTO orders (customer_id, order_date, amount) VALUES
(1, '2024-01-15', 25000.00),
(1, '2024-02-20', 30000.00),
(2, '2024-01-10', 15000.00),
(3, '2024-03-05', 55000.00),
(4, '2024-02-14', 12000.00),
(5, '2024-03-20', 48000.00),
(1, '2024-03-25', 10000.00),
(2, '2024-04-01', 20000.00);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 5, 3),
(3, 2, 1),
(4, 4, 5),
(5, 6, 2),
(6, 3, 4),
(7, 1, 1),
(8, 5, 2);


SELECT c.name, COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_orders DESC;


SELECT name, city
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id FROM orders
);

SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_sold DESC
LIMIT 1;

SELECT
    MONTHNAME(order_date) AS month,
    YEAR(order_date) AS year,
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY YEAR(order_date), MONTH(order_date);

SELECT c.name, SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000;

SELECT c.city, SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC
LIMIT 3;