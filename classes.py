# class Dog():
#     def __init__(self, name="NOT PROVIDED", age=0):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f'{self.name} says woof!')

#     def __str__(self):
#         return f'The dog named {self.name} is {self.age} years old.'


# test = Dog()
# print(test)
# barky = Dog("barky", 3)
# fluffy = Dog("fluffy", 2)
# smelly = Dog("smelly")

# print(barky)

# print(barky.name, barky.age)
# print(smelly.name, smelly.age)
# print(test.name, test.age)

# barky.bark()
# fluffy.bark()

# print(smelly.__str__())

# # print(dir([1,2,3]))
# print(dir(barky))


# VEHICLE CLASS

class Vehicle():
    def __init__(self, make, model, running=False):
        self.make = make
        self.model = model
        self.running = running

    def start(self):
        self.running = True
        print("Starting up!")

    def stop(self):
        self.running = False
        print("Turning off.")

    def __str__(self):
        return f'The vehicle is a {self.make} {self.model}.'


car = Vehicle("Toyota", "RAV4")

print(car)
# prints: The vehicle is a Toyota RAV4.

print(car.running)
# prints: False

car.start()
# prints: Starting up!

print(car.running)
# prints: True