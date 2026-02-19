#Encapsulation is about protecting data inside a class.
#It is done by using a double underscore __ prefix



class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error