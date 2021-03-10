class Student:

    def __init__(self, name, mark, branch):
        self.name = name
        self.mark = mark
        self.branch = branch

    def displayCount(self):
        print("Total Student %d" % Student.stuCount)

    def displayStudent(self):
        print("Name : ", self.name, "Mark: ", self.mark, "Branch: ", self.branch)


stu1 = Student("abcd", 2000, "MCA")
stu2 = Student("efgh", 2001, "MBA")
stu3 = Student("ijkl", 2002, "BTECH")
stu1.displayStudent()
stu2.displayStudent()
stu3.displayStudent()
del stu3.branch
print("stu3 branch deleted")