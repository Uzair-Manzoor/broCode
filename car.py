class Car:

    wheels = 4 #class variable

    def __init__(self,make,model,year,color):
        self.make = make        #instance variable
        self.model = model      #instance variable
        self.year = year        #instance variable
        self.color = color      #instance variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

# _______________________________________________________________________________________________________________________
# method chaining = calling multiple methods sequentially each call performs an action on the same object and return self


class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes   ")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#car.turn_on()
#car.drive()
#car.brake()
#car.turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
