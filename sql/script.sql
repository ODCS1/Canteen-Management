-- --> CREATING THE DATABASE TABLES AND INSERTING PRODUCT AND CASH REGISTER DATA <--
-- FOLLOW THE EXECUTION ORDER

-- 1 - CREATE DATA BASE
CREATE DATABASE Canteen;

-- 2 - TABLE ACCOUNT
CREATE TABLE Account (
    account_id INT IDENTITY,
    client_name VARCHAR(100) NULL,
    client_cpf BIGINT UNIQUE NULL,
    client_email VARCHAR(100) NULL,
    client_phone BIGINT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_Account PRIMARY KEY (account_id)
);

-- 3 - TABLE ORDER
CREATE TABLE [Order] (
    order_id INT IDENTITY,
    order_date DATETIME NOT NULL,
    order_value DECIMAL(10, 2) NOT NULL,
    paid_value DECIMAL(10, 2) NULL,
    change_value DECIMAL(10, 2) NULL,
    CONSTRAINT PK_Order PRIMARY KEY (order_id)
);

-- 4 - TABLE PRODUCT
CREATE TABLE Product (
    product_id INT IDENTITY,
    product_code VARCHAR(20) NULL,
    product_name VARCHAR(100) UNIQUE NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_Product PRIMARY KEY (product_id)
);

-- 5 - TABLE ITEM QUANTITY IN ORDER
CREATE TABLE [OrderItem] (
    order_id INT,
    product_id INT,
    quantity INT,
    CONSTRAINT PK_OrderItem PRIMARY KEY CLUSTERED (order_id, product_id),
    CONSTRAINT FK_OrderItem_Order FOREIGN KEY (order_id) REFERENCES [Order](order_id),
    CONSTRAINT FK_OrderItem_Product FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- 6 - TABLE CASH REGISTER
CREATE TABLE CashRegister (
    cash_register_id INT IDENTITY,
    cash_register_date DATETIME NOT NULL,
    opening_balance DECIMAL(10, 2) NOT NULL,
    closing_balance DECIMAL(10, 2) NULL,
    CONSTRAINT PK_CashRegister PRIMARY KEY (cash_register_id)
);

-- INSERTING DATA INTO THE PRODUCT TABLE
--
-- For the product codes, the following scheme was used:
-- First letter "C" for Code, the second letter corresponds to the respective category:
-- S --> Savory snack
-- B --> Beverage
-- L --> Sandwich
-- R --> Soft drink
-- E --> Special
--
-- And the number at the end differentiates products of the same category.

-- INSERTING DATA
-- 7 - INSERTING PRODUCT DATA
INSERT INTO Product (product_code, product_name, product_price)
VALUES 
    -- SNACKS
    ('CS01', 'Coxinha', 7.50),
    ('CS02', 'Sfiha /Chicken', 6),
    ('CS03', 'Burger', 8),
    ('CS04', 'Croissant', 6.50),
    ('CS05', 'Cheese Bread', 5),

    -- DRINKS
    ('CB01', 'Mineral Water', 3),
    ('CB02', 'DellVale Juice', 3.80),
    ('CB03', 'Lipton Tea', 3),
    ('CB04', 'Matte Tea', 2.50),

    -- SANDWICHES
    ('CL01', 'Hamburger', 12),
    ('CL02', 'Grilled Cheese', 5.80),

    -- SWEETS
    ('CD01', '7Belo Lollipop', 1),
    ('CD02', 'Candy Azedinho', 0.50),
    ('CD03', 'Mentos', 2.50),

    -- SODAS
    ('CR01', 'Coca-Cola', 5.50),
    ('CR02', 'Coca-Cola Zero', 5),
    ('CR03', 'Guarana', 5),
    ('CR04', 'Guarana Zero', 5),
    ('CR05', 'Orange Fanta', 4.60),

    -- SPECIALS
    ('CE01', 'Hot Dog', 5.50),
    ('CE02', 'Pastel', 6);

-- 8 - INSERTING DATA INTO THE CASH REGISTER
INSERT INTO CashRegister (cash_register_date, opening_balance, closing_balance)
VALUES 
    (GETDATE(), 0, 1000);

-- Testing if the inserted data was correctly added to the table
-- 9 - IN PRODUCTS
SELECT *
FROM Product;

-- EXPECTED RESULT
-- 1	CS01	Coxinha	7.50
-- 2	CS02	Chicken Esfiha	6.00
-- 3	CS03	Big Hamburger	8.00
-- 4	CS04	Croissant	6.50
-- 5	CS05	Cheese Bread	5.00
-- 6	CB01	Mineral Water	3.00
-- 7	CB02	DellVale Can	3.80
-- 8	CB03	Lipton Tea	3.00
-- 9	CB04	Matte Leão Tea	2.50
-- 10	CL01	Hamburger	12.00
-- 11	CL02	Hot Sandwich	5.80
-- 12	CD01	7belo Lollipop	1.00
-- 13	CD02	Azedinho Candy	0.50
-- 14	CD03	Mentos	2.50
-- 15	CR01	Coca-Cola	5.50
-- 16	CR02	Coca-Cola Zero	5.00
-- 17	CR03	Guaraná	5.00
-- 18	CR04	Guaraná Zero	5.00
-- 19	CR05	Fanta Orange	4.60
-- 20	CE01	Hot Dog	5.50
-- 21	CE02	Pastel	6.00

-- 10 - IN CASH REGISTER
SELECT * FROM CashRegister;

-- EXPECTED RESULT
-- 1	2023-06-23 15:46:09.977	0.00	1000.00