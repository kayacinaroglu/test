class Student:
    def __init__(self, name, age, courses, gpa, school):
        self.name = name
        self.age = age
        self.age = age
        self.courses = courses
        self.gpa = gpa
        self.school = school

    def drop_course(self, course_name):
        self.courses.remove(course_name)
    
    def add_course(self, course_name):
        self.courses.append(course_name)

    def list_courses(self):
        print([i.name for i in self.courses])

class Course:
    def __init__(self, name, students, teacher, credits):
        self.name = name
        self.students = students
        self.teacher = teacher
        self.credits = credits

    def change_teacher(self, teacher_name):
        self.teacher = teacher_name
    
    def list_students(self):
        print([i.name for i in self.students])

    def add_student(self, student):
        self.students.append(student)

math = Course("Math", [], "Bob", 10)
physics = Course("Science", [], "Mary", 10)

s1 = Student("Kaya", 17, [], 4.0, "Robert College")
s2 = Student("Omer", 17, [], 3.9, "Robert College")
s3 = Student("Jack", 16, [], 3.5, "Robert College")


math.add_student(s1)
math.add_student(s2)
math.add_student(s3)
math.list_students()

s1.add_course(math)
s1.add_course(physics)
s1.list_courses()
    




    