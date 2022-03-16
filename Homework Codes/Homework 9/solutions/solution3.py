class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.gear = 0
        self.odometer = 0.

    def increment_gear(self):
        self.gear += 1

    def decrement_gear(self):
        self.gear -= 1

    def drive(self, number_of_hours_traveled, kilometers_traveled_per_hour):
        self.odometer += number_of_hours_traveled * kilometers_traveled_per_hour

    def display(self):
        print("The brand of the car is ", self.brand, ".", sep="")
        print("The color of the car is ", self.color, ".", sep="")
        print("Current gear is ", self.gear, ".", sep="")
        print("Current value of odometer is ", self.odometer, ".", sep="")


car = Car("Mercedes", "yellow")
assert car.odometer == 0.
assert car.gear == 0
car.increment_gear()
assert car.gear == 1
car.increment_gear()
assert car.gear == 2
car.decrement_gear()
assert car.gear == 1
car.drive(2, 90)
assert car.odometer == 180
car.drive(3, 70)
assert car.odometer == 390

car1 = Car("Mercedes", "yellow")
car2 = Car("Volkswagen", "pink")
car3 = Car("Ferrari", "red")

car1.display()
car2.display()
car3.display()
