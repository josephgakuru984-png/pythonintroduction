age =18  #integer
length =45.6 #float
greetings = "hello there" #string
hasfeathers = True #Boolean



#Data structures- Multiple values stored in one variable.
fruits = ["banana", "mango","pineapple"] # list - Ordered and changeable
courses = ["MIT", "Datascience"] #array - similar datatypes
cars = ("Mercedes", "ford", "Nissan", "G-Wagon",) #Turple - Ordered and unchageable
countries = {"Zambia", "Canada", "India"} #Sets - unordered ad unchangeable
student = {
    "firstname" : "joseph" ,
    "courses" : "MIT" ,
    "Age" : 18 ,
    "nationality" : "kenya"
}

print(age)
print("the length is",length)
print(fruits)
print(countries)
print(student)


#typecasting - converting one data type to another
print(float(age))
print(int(length))