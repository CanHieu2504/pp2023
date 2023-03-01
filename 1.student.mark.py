#List of students
students = []

#List of courses
courses = []

#List of marks for each course
marks =  []

#Input number of students in the class
num_students = int(input("Enter number of students: "))
#input student information : id,name,dob
for i in range(num_students):
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student dob: ")
    #append student information to students list
    students.append([student_id,student_name,student_dob])

num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
        course_name = input("Enter course name: ")
        course_id = int(input("Enter course id: "))
        courses.append([course_name,course_id])
def input_marks():
    course_id = int(input("Enter course id: "))
    #Case course id not in the course id in the list
    if course_id not in [courses[i][1] for i in range (num_courses)]:
        print("Course id not found")
    else:
        for i in range(num_students):
            student_id = input("Enter student id: ")
            student_mark = int(input("Enter student mark: "))
            marks.append([student_id,student_mark])
    
#Define to list students
def list_students():
    print("Student information")
    print("Student id\tStudent name\tStudent dob")
    for i in range(len(students)):
        print(students[i][0],"\t\t",students[i][1],"\t\t",students[i][2])

#Define to list all courses
def list_courses():
    print("Course information")
    print("Course name\tCourse id")
    for i in range(len(courses)):
        print(courses[i][0],"\t\t",courses[i][1])

#Define to show marks
def show_marks():
    course_id = int(input("Enter course id: "))
    #Case course id not in the course id in the list
    if course_id not in [courses[i][1] for i in range (num_courses)]:
        print("Course id not found")
    else:
        print("Student id\tStudent mark")
        for i in range(num_students):
            print(marks[i][0],"\t\t",marks[i][1])
#Remove student in the list
def remove_student():
    student_id = input("Enter student id: ")
    #Case student id not in the student id in the list
    if student_id not in [students[i][0] for i in range (num_students)]:
        print("Student id not found")
    #Case when you remove all student in the list
    elif num_students == 0:
        print("Student list is empty")
    else:
        for i in range(num_students -1):
            if student_id == students[i][0]:
                students.remove(students[i])
                print("Student id removed")
#Remove course in the list
def remove_course():
    course_id = int(input("Enter course id: "))
    #Case course id not in the course id in the list
    if course_id not in [courses[i][1] for i in range (num_courses)]:
        print("Course id not found")
    else:
        for i in range(num_courses - 1):
            if course_id == courses[i][1]:
                courses.remove(courses[i])
                print("Course id removed")
choice = 0
while choice != 7:
    print("1.List students")
    print("2.List courses")
    print("3.Input marks for each student in a course")
    print("4.Show marks of each student in a course")
    print("5.Remove student in the list")
    print("6.Remove course in the list")
    print("7.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_students()
    elif choice == 2:
        list_courses()
    elif choice == 3:
        input_marks()
    elif choice == 4:
        show_marks()
    elif choice == 5:
        remove_student()
    elif choice == 6:
        remove_course()
    elif choice == 7:
        print("Exit")
    else:
        print("Invalid choice")




