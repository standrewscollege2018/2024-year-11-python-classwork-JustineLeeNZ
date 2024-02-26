''' Gets student mark and displays the grade - Justine Lee '''

# store student mark
student_mark = input("Grade? Enter a number between 0 and 100")

student_mark = int(student_mark)


# calculate grade

if student_mark >= 80:
    print("A")
elif student_mark >= 60:
    print("B")
elif student_mark >= 50:
    print("C")
else:
    print("Fail")





