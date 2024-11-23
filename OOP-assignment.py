# Design Your Own Class challenge

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
        self.battery_remaining = battery_life

    def make_call(self, duration):
        if self.battery_remaining >= duration:
            self.battery_remaining -= duration
            print(f"Call made for {duration} hours. Battery remaining: {self.battery_remaining} hours.")
        else:
            print("Not enough battery to make the call.")

    def browse_web(self, duration):
        if self.battery_remaining >= duration:
            self.battery_remaining -= duration
            print(f"Browsed the web for {duration} hours. Battery remaining: {self.battery_remaining} hours.")
        else:
            print("Not enough battery to browse the web.")

    def charge_battery(self):
        self.battery_remaining = self.battery_life
        print("Battery fully charged.")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system  # Boolean: True for advanced cooling

    def play_game(self, duration):
        if self.battery_remaining >= duration:
            self.battery_remaining -= duration
            print(f"Played games for {duration} hours. Battery remaining: {self.battery_remaining} hours.")
            if self.cooling_system:
                print("Advanced cooling system prevented overheating!")
        else:
            print("Not enough battery to play games.")


# Polymorphism Challenge

class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water. 🛥️")

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
