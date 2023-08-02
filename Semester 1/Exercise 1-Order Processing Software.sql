-- Creating new database for the given question
create database exercise1_order_processing;

show databases;

use exercise1_order_processing;
/* ---------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------*/

-- A.	DDL to implement the schema with primary key, check constraints, and foreign key constraints 
CREATE TABLE CUSTOMER (
  CUSTOMERNO BIGINT PRIMARY KEY,
  CNAME VARCHAR(30),
  CITY VARCHAR(30),
  CHECK (CUSTOMERNO LIKE '4%' AND LENGTH(CUSTOMERNO) = 5)
);

desc customer;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */

CREATE TABLE CUST_ORDER (
  ORDERNO BIGINT PRIMARY KEY,
  ODATE DATE,
  CUSTOMERNO BIGINT,
  ORD_AMT BIGINT,
  CHECK (ORDERNO LIKE '5%' AND LENGTH(ORDERNO) = 5),
  FOREIGN KEY (CUSTOMERNO) REFERENCES CUSTOMER (CUSTOMERNO)
);

desc cust_order;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */

CREATE TABLE ITEM (
  ITEMNO BIGINT PRIMARY KEY,
  ITEM_NAME VARCHAR(30),
  UNIT_PRICE DECIMAL(5),
  CHECK (ITEMNO LIKE '6%' AND LENGTH(ITEMNO) = 5)
);

desc item;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */

CREATE TABLE ORDER_ITEM (
  ORDERNO BIGINT,
  ITEMNO BIGINT,
  QTY INT(3),
  FOREIGN KEY (ORDERNO) REFERENCES CUST_ORDER (ORDERNO),
  FOREIGN KEY (ITEMNO) REFERENCES ITEM (ITEMNO)
);

desc order_item;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


-- B.	Populate the rich data set with atlease 5 records in each:

INSERT INTO customer (Customerno, cname, city) VALUES
	('40001', 'John Doe', 'New York'),
	('40002', 'Jane Smith', 'Los Angeles'),
	('40003', 'Michael', 'Chicago'),
	('40004', 'Robost', 'Hoston'),
	('40005', 'Emily', 'San Fransisco');
    
select * from customer;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */

    
INSERT INTO cust_order (orderno, odate, customerno, ord_amt) VALUES
	('50001', '2023-06-13', '40001', '1000'),
	('50002', '2023-06-14', '40002', '500'),
	('50003', '2023-06-15', '40003', '750'),
	('50004', '2023-06-13', '40001', '2000'),
	('50005', '2023-06-14', '40002', '300'),
	('50006', '2023-06-18', '40004', '1400'),
	('50007', '2023-06-13', '40001', '195'),
	('50008', '2023-06-20', '40005', '55'),
	('50009', '2023-06-14', '40003', '50'),
	('50010', '2023-06-20', '40003', '500'),
	('50011', '2023-06-23', '40005', '500');
    
select * from cust_order;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */

    
INSERT INTO item (itemno, item_name, unit_price) VALUES
	('60001', 'SF1', '10'),
	('60002', 'SF2', '20'),
	('60003', 'SF3', '40'),
	('60004', 'SF4', '160'),
	('60005', 'SF5', '30');
    
select * from item;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


INSERT INTO order_item (orderno, itemno, qty) VALUES
	('50001', '60001', '2'),
	('50002', '60002', '3'),
	('50002', '60003', '1'),
	('50003', '60002', '5'),
	('50003', '60005', '6'),
	('50003', '60002', '4'),
	('50004', '60001', '3'),
	('50005', '60005', '3');
    
    
select * from order_item;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


/*
-- Truncating if need any data need to clear
    truncate table order_item;
    truncate table item;
    truncate table cust_order;
    truncate table customer;
    
-- Killing the table need to clear
    drop table order_item;
    drop table item;
    drop table cust_order;
    drop table customer;
*/

-- c. SQL query to list the details of customers who have placed more than three orders:
SELECT
  c.CUSTOMERNO,
  c.CNAME,
  COUNT(*) AS NUM_ORDERS
FROM CUSTOMER c
INNER JOIN CUST_ORDER co ON c.CUSTOMERNO = co.CUSTOMERNO
GROUP BY c.CUSTOMERNO
having COUNT(*) > 3;


/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


-- d. SQL query to list the details of items whose price is less than the average price of all items:
SELECT ITEMNO, ITEM_NAME, UNIT_PRICE
FROM ITEM
WHERE UNIT_PRICE < (
  SELECT AVG(UNIT_PRICE)
  FROM ITEM
);

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


-- e. SQL query to list the orderno and number of items in each order:
SELECT ORDERNO, COUNT(*) AS NUM_ITEMS
FROM ORDER_ITEM
GROUP BY ORDERNO;

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


-- f. SQL query to list the details of items that are present in 25% of the orders:
SELECT
  i.ITEMNO,
  i.ITEM_NAME,
  COUNT(*) AS NUM_ORDERS
FROM ORDER_ITEM oi
INNER JOIN ITEM i ON oi.ITEMNO = i.ITEMNO
GROUP BY i.ITEMNO
HAVING COUNT(*) > (
    SELECT COUNT(*) * 0.25
    FROM CUST_ORDER
  );

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */

  
-- g. Update statement to update the value of ORD_AMT
UPDATE CUST_ORDER SET ORD_AMT = ORD_AMT * 1.10 WHERE CUSTOMERNO = 40001;
UPDATE cust_order SET customerno = '40003' WHERE orderno = 50011;

select * from cust_order where customerno in (40001,40003);

/* ---------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------- */


-- h. Create a view that keeps track of the details of each customer and the number of orders placed:
CREATE VIEW CUSTOMER_ORDERS_VIEW AS
SELECT C.CUSTOMERNO, C.CNAME, C.CITY, COUNT(O.ORDERNO) AS NUM_ORDERS
FROM CUSTOMER C
LEFT JOIN CUST_ORDER O ON C.CUSTOMERNO = O.CUSTOMERNO
GROUP BY C.CUSTOMERNO, C.CNAME, C.CITY;

select * from customer_orders_view;

/* ---------------------------------------------------------------------------------------------------
40001	John Doe	New York	3
40002	Jane Smith	Los Angeles	2
40003	Michael	Chicago	4
40004	Robost	Hoston	1
40005	Emily	San Fransisco	1
--------------------------------------------------------------------------------------------------- */


-- i. Database trigger to limit the insertion of more than six records in the CUST_ORDER table for a particular order

DROP TRIGGER IF EXISTS `exercise1_order_processing`.`order_item_BEFORE_INSERT`;

DELIMITER $$
USE `exercise1_order_processing`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `order_item_BEFORE_INSERT` 
BEFORE INSERT ON `order_item` 
FOR EACH ROW BEGIN
  IF (SELECT COUNT(*) FROM ORDER_ITEM WHERE ORDERNO = NEW.ORDERNO) > 6 THEN
    SIGNAL SQLSTATE '20001'
      SET MESSAGE_TEXT = 'Maximum number of items per order is 6.';
  END IF;
END$$
DELIMITER ;

INSERT INTO order_item (orderno, itemno, qty) VALUES
	('50003', '60001', '5'),
	('50003', '60002', '6'),
	('50003', '60003', '4'),
	('50003', '60004', '4'),
    ('50003', '60001', '5'),
	('50003', '60002', '6'),
	('50003', '60003', '4'),
	('50003', '60004', '4');

select count(orderno) from order_item where orderno=50003;

/* ---------------------------------------------------------------------------------------------------
13:52:17
Error Code: 1644. Maximum number of items per order is 6.	
0.062 sec
--------------------------------------------------------------------------------------------------- */

drop database exercise1_order_processing;