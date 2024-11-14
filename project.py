#create a class
class Dog:
         
    #instance atribute
    def __init__(self,breed,color):
              self.breed=breed
              self.color=color

#instantiate the parrot class
poodle=Dog("Poodle","white")
bulldog=Dog("Bulldog","brown")

#access the instance attribute
print("{} is have a {} color".format(poodle.breed,poodle.color))
print("{} is have a {} color".format(bulldog.breed,bulldog.color))


