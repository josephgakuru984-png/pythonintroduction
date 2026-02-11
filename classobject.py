from functions import employees
#Class is just a blueprint of an object
#Object is an instance of a class
class Employee:
    #attributes/variables
    name  = "james"
    age = 45
    gender = "male"
    salary = 70000.00

    #Behavior/Function
    def eat(self):
        print("Employee eats")

employee1 = Employee()
print(employee1.name)
#creating an object
employee2 = Employee()
employee3 = Employee()