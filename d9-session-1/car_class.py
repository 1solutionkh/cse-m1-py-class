class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.is_running = False

    def start(self):
        if self.is_running:
            print(f"{self.brand} {self.model} is already running.")
        else:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")

    def stop(self):
        self.is_running = False
        self.speed = 0
        print(f"{self.brand} {self.model} stopped.")

    def accelerate(self, amount):
        if not self.is_running:
            print("Start the car first!")
            return
        self.speed += amount
        print(f"Speed is now {self.speed} km/h")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Speed is now {self.speed} km/h")

    def show_info(self):
        print(f"{self.year} {self.color} {self.brand} {self.model}")


car1 = Car("Toyota", "Corolla", 2022, "White")
car1.show_info()
car1.start()
car1.accelerate(40)
car1.accelerate(30)
car1.brake(20)
car1.stop()
