CREATE TABLE accounts (
    account_id INT PRIMARY KEY ATO_INCREMENT,
    account_name VARCHAR(50) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL
);
INSERT INTO accounts (account_name, balance) VALUES
('Nistha', 50000.00),
('Raj', 30000.00),
('Priya', 20000.00);

START TRANSACTION;
=
INSERT INTO accounts (account_name, balance)
VALUES ('Meet', 15000.00);

SELECT * FROM accounts;

ROLLBACK;

SELECT * FROM accounts;
START TRANSACTION;

INSERT INTO accounts (account_name, balance)
VALUES ('Riya', 25000.00);

UPDATE accounts
SET balance = balance + 5000
WHERE account_name = 'Nistha';
COMMIT;

SELECT * FROM accounts;

START TRANSACTION;


UPDATE accounts
SET balance = balance - 10000
WHERE account_name = 'Nistha';

UPDATE accounts
SET balance = balance + 10000
WHERE account_name = 'Raj';


SELECT * FROM accounts;


COMMIT;
SELECT * FROM accounts;