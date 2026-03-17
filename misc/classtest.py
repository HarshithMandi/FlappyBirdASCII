from classes.Vehicle import Vehicle

class Bike(Vehicle):
    def Start(self):
        print(f"{self.brand} bike is starting at speed {self.get_speed()} km/h")

class Car(Vehicle):
    def Start(self):
        print(f"{self.brand} car is starting at speed {self.get_speed()} km/h")

print("Testing Bike class:")
bike = Bike("Yamaha", 60)
bike.Start()
