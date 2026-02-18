
class Dog:
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color


    def speak(self):
        print("Dog is barking")

#Object
dog1 = Dog("German Shepherd",3,"White")

dog2 = Dog("Chihuahua", 5 , "Brown")

dog3 = Dog("Siberian Husky", 7 , "Black")

print(dog1.breed , dog1.age , dog1.color)