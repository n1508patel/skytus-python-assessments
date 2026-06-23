
SELECT * FROM orders WHERE customer_id = 1;

CREATE INDEX idx_customer_id ON orders(customer_id);


SELECT * FROM orders WHERE customer_id = 1;


EXPLAIN SELECT * FROM orders WHERE customer_id = 1;


EXPLAIN
SELECT c.name, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.city = 'Surat';

SELECT *
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;


CREATE INDEX idx_order_customer ON orders(customer_id);
CREATE INDEX idx_orderitem_order ON order_items(order_id);
CREATE INDEX idx_orderitem_product ON order_items(product_id);

SELECT
    c.name,
    c.city,
    p.product_name,
    oi.quantity,
    o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.city = 'Surat';

SELECT
    c.name,
    c.city,
    p.product_name,
    oi.quantity,
    o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.city = 'Surat';

SHOW INDEX FROM orders;
SHOW INDEX FROM customers;