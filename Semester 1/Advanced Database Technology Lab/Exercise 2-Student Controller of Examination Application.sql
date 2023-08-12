-- Creating new database for the given question
create database exercise2_student_controller_of_examination;

show databases;

use exercise2_student_controller_of_examination;
/* ---------------------------------------------------------------------------------------------------
------------------------------------*/

CREATE TABLE DEPARTMENT (
  DNO INT PRIMARY KEY,
  DNAME VARCHAR(30)
);

desc department;

CREATE TABLE BRANCH (
  BCODE INT PRIMARY KEY,
  BNAME VARCHAR(30),
  DNO INT,
  FOREIGN KEY (DNO) REFERENCES DEPARTMENT (DNO)
);

desc branch;

CREATE TABLE COURSE (
  CCODE INT PRIMARY KEY,
  CNAME VARCHAR(30),
  CREDITS INT,
  DNO INT,
  FOREIGN KEY (DNO) REFERENCES DEPARTMENT (DNO)
);

desc course;

CREATE TABLE BRANCH_COURSE (
  BCODE INT,
  CCODE INT,
  SEMESTER INT,
  PRIMARY KEY (BCODE, CCODE),
  FOREIGN KEY (BCODE) REFERENCES BRANCH (BCODE),
  FOREIGN KEY (CCODE) REFERENCES COURSE (CCODE)
);

desc branch_course;

CREATE TABLE PREREQUISITE_COURSE (
  CCODE INT,
  PCCODE varchar(4),
  PRIMARY KEY (CCODE, PCCODE),
  FOREIGN KEY (CCODE) REFERENCES COURSE (CCODE)
);

desc prerequisite_course;

create table student (
	rollno int not null primary key,
    name varchar(30),
    dob date,
    gender varchar(1),
    doa date,
    bcode int,
    check (gender in ('M','F')),
    foreign key (bcode) REFERENCES branch(bcode)
);

desc student;

CREATE TABLE ENROLLS (
  ROLLNO INT,
  CCODE INT,
  SESS VARCHAR(20),
  GRADE ENUM('S', 'A', 'B', 'C', 'D', 'E', 'U'),
  PRIMARY KEY (ROLLNO, CCODE, SESS),
  FOREIGN KEY (ROLLNO) REFERENCES STUDENT (ROLLNO),
  FOREIGN KEY (CCODE) REFERENCES COURSE (CCODE)
);

desc enrolls;

show tables;
-- B. B.	Data Population:
-- c. Insert into DEPARTMENT:
INSERT INTO DEPARTMENT (DNO, DNAME) VALUES
(201, 'Computer Science'),
(202, 'Electronics'),
(203, 'Mechanical'),
(204, 'Civil'),
(205, 'Electrical');

-- b. Insert into BRANCH:
INSERT INTO BRANCH (BCODE, BNAME, DNO) VALUES
(501, 'Computer Science', 201),
(502, 'Electronics', 202),
(503, 'Mechanical', 203),
(504, 'Civil', 204),
(505, 'Electrical', 205);

-- d. Insert into COURSE:


INSERT INTO COURSE (CCODE, CNAME, CREDITS, DNO) VALUES
('101', 'Database Management', 3, 201),
('102', 'Advanced Databases', 4, 201),
('103', 'Programming Fundamentals', 3, 202),
('104', 'Digital Electronics', 4, 202),
('105', 'Mechanics', 3, 203);

-- e. Insert into BRANCH COURSE:
INSERT INTO BRANCH_COURSE (BCODE, CCODE, SEMESTER) VALUES
(501, '101', 1),
(501, '102', 3),
(502, '103', 1),
(502, '104', 2),
(503, '105', 1);

-- f. Insert into PREREQUISITE_COURSE:

INSERT INTO PREREQUISITE_COURSE (CCODE, PCCODE) VALUES
('102', 'C101'),
('102', 'C103'),
('104', 'C103');

-- a. Insert into STUDENT:
INSERT INTO STUDENT (ROLLNO, NAME, DOB, GENDER, DOA, BCODE) VALUES
(1, 'John Smith', '1998-05-15', 'M', '2020-09-01', 501),
(2, 'Emily Johnson', '1999-08-23', 'F', '2020-09-01', 502),
(3, 'Michael Brown', '1997-03-10', 'M', '2021-01-15', 503),
(4, 'Emma Davis', '1998-11-30', 'F', '2021-01-15', 504),
(5, 'Ethan Wilson', '1999-07-02', 'M', '2022-03-10', 505);

-- g. Insert into ENROLLS:
INSERT INTO ENROLLS (ROLLNO, CCODE, SESS, GRADE) VALUES
(1, '101', 'APRIL20201', 'A'),
(1, '102', 'APRIL20201', 'B'),
(1, '103', 'NOVEMBER2020', 'S'),
(2, '101', 'APRIL20201', 'S'),
(2, '103', 'NOVEMBER2020', 'A'),
(2, '104', 'NOVEMBER2020', 'U'),
(3, '102', 'APRIL20201', 'C'),
(3, '104', 'APRIL20201', 'B'),
(4, '103', 'NOVEMBER2020', 'S'),
(5, '105', 'APRIL20201', 'E'),
(5, '102', 'APRIL20201', 'S');

-- C.	SQL query to list the details of departments that offer more than three branches:

SELECT D.DNO, D.DNAME
FROM DEPARTMENT D
JOIN BRANCH B ON D.DNO = B.DNO
GROUP BY D.DNO, D.DNAME
HAVING COUNT(B.BCODE) > 3;

-- D.	SQL query to list the details of courses that do not have prerequisite courses:

SELECT C.CCODE, C.CNAME
FROM COURSE C
LEFT JOIN PREREQUISITE_COURSE PC ON C.CCODE = PC.CCODE
WHERE PC.CCODE IS NULL;

-- E.	SQL query to list the details of courses that are common for more than three branches:

SELECT C.CCODE, C.CNAME
FROM COURSE C
JOIN BRANCH_COURSE BC ON C.CCODE = BC.CCODE
GROUP BY C.CCODE, C.CNAME
HAVING COUNT(BC.BCODE) > 3;

-- F.	SQL query to list the details of students who have got a 'U' grade in more than two courses during a single enrollment:


SELECT S.ROLLNO, S.NAME
FROM STUDENT S
JOIN ENROLLS E ON S.ROLLNO = E.ROLLNO
WHERE E.GRADE = 'U'
GROUP BY S.ROLLNO, S.NAME
HAVING COUNT(DISTINCT E.CCODE) > 2;

-- G.	View to keep track of the course code, name, and number of prerequisite courses:

CREATE VIEW COURSE_PREREQUISITES AS
SELECT C.CCODE, C.CNAME, COUNT(PC.PCCODE) AS NUM_PREREQUISITES
FROM COURSE C
LEFT JOIN PREREQUISITE_COURSE PC ON C.CCODE = PC.CCODE
GROUP BY C.CCODE, C.CNAME;

-- H.	Database trigger to not permit a student to enroll for a course if they have not completed the prerequisite courses:

DELIMITER //
CREATE TRIGGER CHECK_PREREQUISITES_BEFORE_ENROLLMENT
BEFORE INSERT ON ENROLLS
FOR EACH ROW
BEGIN
  DECLARE COUNT_PREREQUISITES INT;
  
  SELECT COUNT(*) INTO COUNT_PREREQUISITES
  FROM PREREQUISITE_COURSE
  WHERE CCODE = NEW.CCODE
    AND PCCODE NOT IN (
      SELECT CCODE
      FROM ENROLLS
      WHERE ROLLNO = NEW.ROLLNO
        AND GRADE IN ('S', 'A', 'B', 'C', 'D', 'E')
    );
  
  IF COUNT_PREREQUISITES > 0 THEN
    SIGNAL SQLSTATE '21000' SET MESSAGE_TEXT = 'Cannot enroll for the course without completing prerequisite courses.';
  END IF;
END//
DELIMITER ;

-- I.	Procedure DISP to accept a ROLLNO of a student as input and print the roll number, name, and the number of courses a student has successfully completed:
DELIMITER //
CREATE PROCEDURE DISP(IN STUDENT_ROLLNO INT)
BEGIN
  DECLARE STUDENT_NAME VARCHAR(30);
  DECLARE NUM_COMPLETED_COURSES INT;
  
  SELECT NAME INTO STUDENT_NAME
  FROM STUDENT
  WHERE ROLLNO = STUDENT_ROLLNO;
  
  SELECT COUNT(*) INTO NUM_COMPLETED_COURSES
  FROM ENROLLS
  WHERE ROLLNO = STUDENT_ROLLNO
    AND GRADE IN ('S', 'A', 'B', 'C', 'D', 'E');
  
  SELECT STUDENT_ROLLNO, STUDENT_NAME, NUM_COMPLETED_COURSES;
END//
DELIMITER ;

-- J. Procedure DISP_NOE to accept a CCODE of a COURSE as input and print the roll number and name of students who have enrolled for the course more than twice:
DELIMITER //
CREATE PROCEDURE DISP_NOE(IN COURSE_CCODE INT)
BEGIN
  SELECT S.ROLLNO, S.NAME
  FROM STUDENT S
  JOIN ENROLLS E ON S.ROLLNO = E.ROLLNO
  WHERE E.CCODE = COURSE_CCODE
  GROUP BY S.ROLLNO, S.NAME
  HAVING COUNT(E.CCODE) > 2;
END//
DELIMITER ;