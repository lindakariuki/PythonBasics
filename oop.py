#Class is a blueprint of an object
#Object is an instance of a class


class Student:
    #Attributes
    name = "Daniel"
    age = 18
    gender = "Male"


    #Behaviour/Functions
    def study(self):
        print("Student is studying")


    def movement(self):
        print("The student is walking")

#Creating  objects
student1 = Student()
print(student1.name)





student2 = Student()
student3 = Student()