class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"This {self.brand} is moving"

class Car(Vehicle):
    def move(self):
        return f"This {self.brand} is driving"


class Train(Vehicle):
    def move(self):
        return f"This {self.brand} is speeding"


class Ship(Vehicle):
    def move(self):
        return f"This {self.brand} is sailing"


for _ in [Car("Toyota"), Train("Boeing205"), Ship("Titanic")]:
    print (_.move())

myVehicle = Vehicle("Gwagon")
print (myVehicle.move())