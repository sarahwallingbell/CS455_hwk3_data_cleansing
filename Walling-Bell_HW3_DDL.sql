-- Sarah Wallin-Bell
-- October 7, 2019
-- Homework 3: Data Cleansing

-- Turn on foreign keys
PRAGMA foreign_keys = ON;

-- Delete the tables if they already exist
drop table if exists Student;
drop table if exists Course;
drop table if exists Enroll;
drop table if exists Dept;
drop table if exists Major;

-- Create the schema for your tables below
create table Student (
  studentID integer primary key,
  studentName text not null,
  class text check(class = "Freshman" or class = "Sophomore" or class = "Junior" or class = "Senior"),
  gpa real check(gpa >= 0.0 and gpa <= 4.0)
);

create table Dept (
  deptID text primary key check(length(deptID) <= 4),
  name text,
  building text
);

create table Course (
  courseNum integer,
  deptID text,
  courseName text,
  location text,
  meetDay text,
  meetTime text check(meetTime >= '07:00' and meetTime <= '17:00'),
  primary key(courseNum, deptID),
  foreign key(deptID) references Dept(deptID)
    on update cascade
    on delete cascade
);

create table Enroll (
  courseNum integer,
  deptID text,
  studentID integer,
  primary key(courseNum, deptID, studentID),
  foreign key(deptID) references Dept(deptID)
    on update cascade
    on delete cascade
);

create table Major (
  studentID integer,
  major text check(length(major) <= 4),
  primary key(studentID, major),
  foreign key(major) references Dept(deptID)
    on update cascade
    on delete cascade,
  foreign key(studentID) references Student(studentID)
    on update cascade
    on delete cascade
);
