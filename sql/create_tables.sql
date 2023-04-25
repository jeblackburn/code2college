CREATE TABLE student (
  id integer primary key AUTO_INCREMENT,
  studentid varchar(45) NOT NULL unique,
  lastname varchar(45) NOT NULL,
  firstname varchar(45) NOT NULL,
  dob date NOT NULL,
  grade int NOT NULL,
  gpa float DEFAULT NULL
);

CREATE TABLE course (
  id integer primary key AUTO_INCREMENT,
  courseid int NOT NULL unique,
  title varchar(45) NOT NULL,
  studentyear int DEFAULT NULL,
  syllabus blob
);