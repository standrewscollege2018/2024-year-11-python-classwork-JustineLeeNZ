''' run queries on student database with user input - Justine Lee '''

# import sqlite3 library
import sqlite3

# define database to use
DATABASE = 'student_info_v2.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# select all names from student database
cursor.execute("SELECT student_id, first_name, last_name FROM student ORDER BY student_id")
results = cursor.fetchall()

# display student names as numbered list using primary key
for result in results:
    name = f" {result[1]} {result[2]}"
    print(f"{result[0]:3} {name:}")

# get name of student to display
first_name = input("Enter the first name of selected student: ")
last_name = input("Enter the last name of selected student: ")

# get details of selected student
cursor.execute("SELECT * FROM student WHERE first_name=? AND last_name=?",(first_name,last_name))
details = cursor.fetchall()

# check for no results
if len(details) == 0:
    print("No results")

else:

    # display info about selected student
    for detail in details:
        # name
        print(f"Name: {detail[1]} {detail[2]}")
        # age
        print(f"Age: {detail[3]}")
        # year group
        print(f"Year group: {detail[4]}")
        # tutor
        print(f"Tutor: {detail[5]}")
        # phone
        print(f"Phone: {detail[6]}")











