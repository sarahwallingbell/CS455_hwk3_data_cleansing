## Sarah Walling-Bell
## October 7, 2019
## CS 455 Homework 3: Data Cleansing

import pandas as pd
import numpy as np

#load data and read file line by line
file_in = open('shmeeplesoft.raw.txt', 'r')

data = [] # list to hold lines of data from file

for line in file_in:
    parsed_line = line.split(',')
    if not '-' in parsed_line[0]: # skip line(s) that are: '--------'
        for elem in range(0, len(parsed_line)):
            parsed_line[elem] = parsed_line[elem].rstrip('\n') #remove trailing '\n'
            #clean data
            if parsed_line[elem] == '': parsed_line[elem] = 'NULL'
            elif parsed_line[elem] == 'FR': parsed_line[elem] = 'Freshman'
            elif parsed_line[elem] == 'SO': parsed_line[elem] = 'Sophomore'
            elif parsed_line[elem] == 'JR': parsed_line[elem] = 'Junior'
            elif parsed_line[elem] == 'SR': parsed_line[elem] = 'Senior'
            elif parsed_line[elem] == 'ENG': parsed_line[elem] = 'ENGL'

        data.append(parsed_line)

file_in.close()

column_names = data[0] # first elem is column names
data.pop(0) #delete column names from data

# create Pandas DataFrame with data
df = pd.DataFrame(data, columns = column_names)

#create column name variables for indexing into columns
studentID = 0
studentName = 1
class_ = 2
gpa = 3
major = 4
courseNum = 5
deptID = 6
courseName = 7
location = 8
meetDay = 9
meetTime = 10
deptName = 11
building = 12

#generate all print statements
student_inserts = []
dept_inserts = []
major_inserts = []
course_inserts = []
enroll_inserts = []

for index, row in df.iterrows():
     #insert into student
    if(row[studentID] != 'NULL' and row[studentName] != 'NULL' and row[class_] != 'NULL'):
        s_insert = 'INSERT INTO Student VALUES ({},"{}","{}","{}");'.format(row[studentID], row[studentName], row[class_], row[gpa])
        if not s_insert in student_inserts:
            student_inserts.append(s_insert)

    #insert into dept
    if(row[deptID] != 'NULL' and row[deptName] != 'NULL' and row[building] != 'NULL'):
        d_insert = 'INSERT INTO Dept VALUES ("{}","{}","{}");'.format(row[deptID], row[deptName], row[building])
        if not d_insert in dept_inserts:
            dept_inserts.append(d_insert)

    #insert into major
    if(row[studentID] != 'NULL' and row[major] != 'NULL'):
        majors = row[major].split(';')
        for major_ in majors:
            m_insert = 'INSERT INTO Major VALUES ({},"{}");'.format(row[studentID], major_)
            if not m_insert in major_inserts:
                major_inserts.append(m_insert)

    #insert into course
    if(row[courseNum] != 'NULL' and row[deptID] != 'NULL'):
        c_insert = 'INSERT INTO Course VALUES ({},"{}","{}","{}","{}","{}");'.format(row[courseNum], row[deptID], row[courseName], row[location], row[meetDay], row[meetTime])
        if not c_insert in course_inserts:
            course_inserts.append(c_insert)

    #insert into enroll
    if(row[courseNum] != 'NULL' and row[deptID] != 'NULL' and row[studentID] != 'NULL'):
        e_insert = 'INSERT INTO Enroll VALUES ({},"{}",{});'.format(row[courseNum], row[deptID], row[studentID])
        if not e_insert in enroll_inserts:
            enroll_inserts.append(e_insert)

#print!
for insert in student_inserts:
    print(insert)
for insert in dept_inserts:
    print(insert)
for insert in major_inserts:
    print(insert)
for insert in course_inserts:
    print(insert)
for insert in enroll_inserts:
    print(insert)
