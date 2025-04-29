'''
    Program: To store student code and marks in the dictionary object and print them
    Author : Milan Lamichhane
    Date   : May 3, 2023
'''

i = 0
subject = ("Math", "English", "Computer")
marks = []
students = {}

stud_count = int(input("How many students records? "))

# Read the marks for each student and store them in the dictionary object
while i < stud_count:
    stud_code = input("Enter student code: ")
    marks.clear()
    for j in range(len(subject)):
        subject_mark = float(input("Enter marks for {}: ".format(subject[j])))
        marks.append(subject_mark)
    students[stud_code] = tuple(marks)
    i += 1

#print(students)
# Print marks obtained in each subject for each of the students.
print("")
for key in students:
    print("Student ID: ", key)
    i = 0
    for sub in subject:
        print("{0}:{1}".format(sub,students[key][i]))
        i += 1
    print("")
