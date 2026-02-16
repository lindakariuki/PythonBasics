#They include the integers,float,string and bullian
age= 56 #Integer
temperature = 36.8 #Float
greeting = "Hi!" #String
isMarried = True #Boolean

print("I am",age,"years old")
print("The body temperature of the patient is",temperature,"degrees Celsius")
print(greeting,"Cecil")
print("Are you Married?",isMarried)


#Data Structures.
#They are multiple values representing a single value.
cars = ["Toyota","Audi","BMW","G-Wagon","Jeep","Mercedes"] #List-ordered and changeable.
languages =["Python","Java","C++"] #Array -similar data types
fruits = ("Banana","Mango","Orange","Grapes","Pineapple") #Tuple-ordered and unchangeable.
countries ={"Italy","Spain","Germany","France","Kenya","India"} #Set-Unordered
#Dictionary
student = {
    "First Name": "John Smith",
    "Age" :19,
    "Course":"FullStack",
    "Gender":"Male",

}

print(cars)
print("I bought some",fruits)
print(countries)
print(student)
print(student["First Name"])

#Type Casting - It is the converting from one data type from another
# Python automatically converts 'a' to int
a = 7
print(type(a))

# Python automatically converts 'b' to float
b = 3.0
print(type(b))

# Python automatically converts 'c' to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Python automatically converts 'd' to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

#Example 2:
print(int(temperature))