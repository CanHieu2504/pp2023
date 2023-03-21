class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.student_id}\t\t{self.name}\t\t{self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"{self.name}\t\t{self.course_id}"

class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def __str__(self):
        return f"{self.student_id}\t\t{self.mark}"
class GPA:
    def __init__(self, student_id, gpa):
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self):
        return f"{self.student_id}\t\t{self.gpa}"

class Class:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
    # Input number of students in the class
    def input_num_students(self):
        self.num_students = int(input("Enter number of students: "))
    #Input student information 
    def input_student(self):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        student = Student(student_id, name, dob)
        self.students.append(student)
    #List all students
    def list_students(self):
        print("Student information")
        print("Student id\tStudent name\tStudent dob")
        for student in self.students:
            print(student)
    # Input number of courses in the class
    def input_num_courses(self):
        self.num_courses = int(input("Enter number of courses: "))
    def input_course(self):
        course_id = int(input("Enter course id: "))
        name = input("Enter course name: ")
        course = Course(course_id, name)
        self.courses.append(course)
    #List all courses
    def list_courses(self):
        print("Course information")
        print("Course name\tCourse id")
        for course in self.courses:
            print(course)
    #Input marks for a course
    def input_mark(self):
        course_id = int(input("Enter course id: "))
        for student in self.students:
            student_id = student.student_id
            mark = int(input(f"Enter {student.name}'s mark: "))
            mark = Mark(student_id, course_id, mark)
            self.marks.append(mark)
    #List marks for a course
    def list_marks(self):
        course_id = int(input("Enter course id: "))
        print("Student id\tStudent mark")
        for mark in self.marks:
            if mark.course_id == course_id:
                print(mark)
    #Add student to the class
    def add_student(self):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        student = Student(student_id, name, dob)
        self.students.append(student)
    #Add course to the class
    def add_course(self):
        course_id = int(input("Enter course id: "))
        name = input("Enter course name: ")
        course = Course(course_id, name)
        self.courses.append(course)
    #Remove student from the class
    def remove_student(self):
        student_id = input("Enter student id: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                # Remove all marks for this student
                self.marks = [mark for mark in self.marks if mark.student_id != student_id]
                print("Student removed")
                break
    #Remove course from the class
    def remove_course(self):
        course_id = int(input("Enter course id: "))
        for course in self.courses:
            if course.course_id == course_id:
                self.courses.remove(course)
                # Remove all marks for this course
                self.marks = [mark for mark in self.marks if mark.course_id != course_id]
                print("Course removed")
                break
    #Calculate GPA for a student
    def calculate_gpa(self, student_id):
        total = 0
        for mark in self.marks:
            if mark.student_id == student_id:
                total += mark.mark
        return total / len(self.marks)
    #Sort students by GPA
    def sort_students(self):
        self.students.sort(key=lambda student: self.calculate_gpa(student.student_id), reverse=True)
    #Print GPA for all students
    def print_gpa(self):
        print("Student id\tGPA")
        for student in self.students:
            print(f"{student.student_id}\t\t{self.calculate_gpa(student.student_id)}")
    def run(self):
        while True:
            print("1.List students")
            print("2.List courses")
            print("3.Input marks for a course")
            print("4.Show marks for a course")
            print("5.Add students")
            print("6.Add courses")
            print("7.Remove students")
            print("8.Remove courses")
            print("9.Calculate GPA for a student")
            print("10.Sort students by GPA")
            print("11.Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.list_students()
            elif choice == 2:
                self.list_courses()
            elif choice == 3:
                self.input_mark()
            elif choice == 4:
                self.list_marks()
            elif choice == 5:
                self.add_student()
            elif choice == 6:
                self.add_course()
            elif choice == 7:
                self.remove_student()
            elif choice == 8:
                self.remove_course()
            elif choice == 9:
                self.calculate_gpa( input("Enter student id: ") )
            elif choice == 10:
                self.sort_students()
                self.list_students()
                self.print_gpa()
            elif choice == 11:
                break
            else:
                print("Invalid choice")
if __name__ == "__main__":
    my_class = Class()
    my_class.input_num_students()
    for i in range(my_class.num_students):
        my_class.input_student()
    my_class.input_num_courses()
    for i in range(my_class.num_courses):
        my_class.input_course()
    my_class.run()
    
