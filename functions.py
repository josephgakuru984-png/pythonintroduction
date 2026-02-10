#funnctions/Methods - A block of code use to perform a task.

# 1. Standard Library/Inbuilt function - already existing

y = max(56, 98, 100, 101)
print(y)

x = min(2, 4, 1, 89, 79)
print(x)

# 2. User defined functions
def school():
    print("eMobilis")

school() #calling a function

def multiply():
    print(15*5)
multiply()

 #parameters/variables
def multiply(X,Y):
    print(X * Y)

# Python program to display of 5 employees a use a user defined function with help of parameters and arguments
# details - fullname, position, age, gender

def employees(fullname, position, age, gender):
    print(fullname, position, age, gender)
employees(fullname="james", position="lecture", age=90, gender="male")
employees(fullname="moses", position="lecture", age=40, gender="male")
employees(fullname="lewis", position="department manager", age=50, gender="male")
employees(fullname="glory", position="lecture", age=80, gender="female")
employees(fullname="kipara", position="lecture", age=40, gender="male")


