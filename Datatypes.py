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
fruits = ("Banana","Mango","Orange","Grapes","Pineapple") #Tuple-ordered and unchangeable.
countries ={"Italy","Spain","Germany","France","Kenya","India"} #Set-Unordered
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