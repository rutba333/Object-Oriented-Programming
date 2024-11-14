#create a class
class Vehicle:
          #create init method
          def __init__(self,max_speed,milaeage):
                  #blind the arguments
                  self.max_speed=max_speed
                  self.milaeage=milaeage

#obj creation
model1X=Vehicle(240,18)

#access the vehicle method inside the init method
print("Model Max speed:",model1X.max_speed)
print("Model milaeage: ",model1X.milaeage)

