from studentRegistry import Student, Course

s1 = Student("Ham", 10, ["English"], 2.1, "skool")
s2 = Student("Hum", 4, [], 1.1, "skool")

c1 = Course("Math", [], "Bob", 10)
c2 = Course("Science", [], "Bub", 10)

c1.add_student(s1)
c1.add_student(s2)
c1.list_students()
