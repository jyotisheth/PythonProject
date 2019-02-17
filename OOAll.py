class Student:

    '''
    this is a docstring
    '''

    #Class variable
    studentCount = 0

    def __init__(self,name):
        self.name = name
        self.grade = None
        self.__secretvar = 'secret'
        Student.studentCount += 1

    @classmethod
    def studentClassmethod(cls):
        print(cls.studentCount)

    def getName(self):
        print(self.name)

    def setGrade(self,grade):
        self.grade = grade

    def getStudentInfo(self):
        print("Name:{},Grade:{},lastname:{},Total:{}".format(self.name,self.grade,self.lastname, Student.studentCount))

    @staticmethod
    def studentSchool():
        schoolName = "SG"
        print(schoolName)

s1=Student("S1")
s1.lastname = "41"

s2 = Student("S2")
print(Student.studentCount)

s1.setGrade(3)
s2.setGrade(4)
s1.getStudentInfo()

print(hasattr(s2,"lastname"))

setattr(s2,"lastname","s3")
print(hasattr(s2,"lastname"))
s2.getStudentInfo()

delattr(s1,"lastname")
delattr(s2,"lastname")

print(s1.__dict__)

print(s1._Student__secretvar)

Student.studentSchool()
Student.studentClassmethod()
