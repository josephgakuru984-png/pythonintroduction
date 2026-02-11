
class Student:

    def __init__(self, fullname, course, age, feespaid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.feespaid = feespaid

student1 = Student("Moses wachira","fullstack",20,10000)
print(student1.fullname,student1.course,student1.age,student1.feespaid)

student2 = Student("wilson njuguna","cybersecurity",20,15000)
print(student2.fullname,student2.course,student2.age,student2.feespaid)

student3 = Student("christopher njuguna","DataScience",20,45000)
print(student3.fullname,student3.course,student3.age,student3.feespaid)