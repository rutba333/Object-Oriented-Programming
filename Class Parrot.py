#create a class
class Parrot:
    #class atribute
    species="bird"

    #instance atribue
    def __init__(self,name,age):
        self.name=name
        self.age=age

#instantiate the parrot class
blu=Parrot("Blu",10)
woo=Parrot("Woo",15)

#access the class atributes
print("Blu is a {}".format(blu.species))
print("woo is also a {}".format(woo.species))

#access the instance attribute
print("{} is a {}".format(blu.name,blu.age))
print("{} is a {}".format(woo.name,woo.age))