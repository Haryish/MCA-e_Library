create database exercise3_customer_management_system;

show databases;

use exercise3_customer_management_system;

-- DDL to implement the schema in MySQL:


CREATE TABLE CUSTOMER (
  CID INT PRIMARY KEY,
  CNAME VARCHAR(30)
);

CREATE TABLE ACCOUNT (
  ANO INT PRIMARY KEY,
  ATYPE ENUM('S', 'C'),
  BALANCE DECIMAL(10, 2),
  CID INT,
  FOREIGN KEY (CID) REFERENCES CUSTOMER(CID)
);

CREATE TABLE TRANSACTION (
  TID INT PRIMARY KEY,
  ANO INT,
  TTYPE ENUM('D', 'W'),
  TDATE DATE,
  TAMOUNT DECIMAL(10, 2),
  FOREIGN KEY (ANO) REFERENCES ACCOUNT(ANO)
);

-- Populating the database with a rich data set:


-- Inserting sample data into CUSTOMER table
INSERT INTO CUSTOMER (CID, CNAME) VALUES
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Mike Johnson');

-- Inserting sample data into ACCOUNT table
INSERT INTO ACCOUNT (ANO, ATYPE, BALANCE, CID) VALUES
(101, 'S', 5000.00, 1),
(102, 'C', 10000.00, 1),
(103, 'S', 3000.00, 2),
(104, 'C', 8000.00, 2),
(105, 'S', 2000.00, 3);

-- Inserting sample data into TRANSACTION table
INSERT INTO TRANSACTION (TID, ANO, TTYPE, TDATE, TAMOUNT) VALUES
(1, 101, 'D', '2023-01-01', 1000.00),
(2, 101, 'W', '2023-01-02', 500.00),
(3, 102, 'D', '2023-01-01', 2000.00),
(4, 103, 'D', '2023-01-01', 1500.00),
(5, 104, 'W', '2023-01-02', 1000.00),
(6, 105, 'D', '2023-01-02', 500.00);

-- SQL query to list the details of customers who have a savings account and a current account:


SELECT C.CID, C.CNAME
FROM CUSTOMER C
INNER JOIN ACCOUNT A1 ON C.CID = A1.CID
INNER JOIN ACCOUNT A2 ON C.CID = A2.CID
WHERE A1.ATYPE = 'S' AND A2.ATYPE = 'C';

-- SQL query to list the details of customers who have a balance less than the average balance of all customers:


SELECT C.CID, C.CNAME
FROM CUSTOMER C
INNER JOIN ACCOUNT A ON C.CID = A.CID
WHERE A.BALANCE < (SELECT AVG(BALANCE) FROM ACCOUNT);

-- SQL query to list the details of customers with the sum of balance in their account(s):


SELECT C.CID, C.CNAME, SUM(A.BALANCE) AS TOTAL_BALANCE
FROM CUSTOMER C
INNER JOIN ACCOUNT A ON C.CID = A.CID
GROUP BY C.CID, C.CNAME;

-- SQL query to list the details of customers who have performed three transactions on a day:


SELECT C.CID, C.CNAME
FROM CUSTOMER C
INNER JOIN ACCOUNT A ON C.CID = A.CID
INNER JOIN TRANSACTION T ON A.ANO = T.ANO
WHERE T.TDATE = '2023-01-01'
GROUP BY C.CID, C.CNAME
HAVING COUNT(T.TID) = 3;

-- Creating a view to keep track of customer details and the number of accounts each customer has:


CREATE VIEW CUSTOMER_ACCOUNT_COUNT AS
SELECT C.CID, C.CNAME, COUNT(A.ANO) AS ACCOUNT_COUNT
FROM CUSTOMER C
LEFT JOIN ACCOUNT A ON C.CID = A.CID
GROUP BY C.CID, C.CNAME;

Database trigger to not permit a customer to perform more than three transactions on a day:


DELIMITER //

CREATE TRIGGER limit_transaction
BEFORE INSERT ON TRANSACTION
FOR EACH ROW
BEGIN
  DECLARE transaction_count INT;

  SELECT COUNT(*)
  INTO transaction_count
  FROM TRANSACTION
  WHERE ANO = NEW.ANO AND TDATE = NEW.TDATE;

  IF transaction_count >= 3 THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Maximum transaction limit reached for the day.';
  END IF;
END //

DELIMITER ;

Database procedure to insert a record into the TRANSACTION table with specific conditions:


DELIMITER //

CREATE PROCEDURE INSERT_TRANSACTION(
  IN p_TID INT,
  IN p_ANO INT,
  IN p_TTYPE CHAR(1),
  IN p_TAMOUNT DECIMAL(10, 2)
)
BEGIN
  DECLARE v_BALANCE DECIMAL(10, 2);

  SELECT BALANCE
  INTO v_BALANCE
  FROM ACCOUNT
  WHERE ANO = p_ANO;

  IF p_TTYPE = 'D' THEN
    UPDATE ACCOUNT
    SET BALANCE = BALANCE + p_TAMOUNT
    WHERE ANO = p_ANO;
  ELSEIF p_TTYPE = 'W' THEN
    IF (v_BALANCE–p_TAMOUNT) >= 2000 AND (v_BALANCE–p_TAMOUNT) >= 5000 THEN
      UPDATE ACCOUNT
      SET BALANCE = BALANCE–p_TAMOUNT WHERE ANO = p_ANO;
    ELSE
      SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Minimum balance not maintained.';
    END IF;
  END IF;

  INSERT INTO TRANSACTION (TID, ANO, TTYPE, TDATE, TAMOUNT)
  VALUES (p_TID, p_ANO, p_TTYPE, CURDATE(), p_TAMOUNT);
END //

DELIMITER ;
