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

# class Vehicle():
#     def __init__(self, make, model, running=False):
#         self.make = make
#         self.model = model
#         self.running = running

#     def start(self):
#         self.running = True
#         print("Starting up!")

#     def stop(self):
#         self.running = False
#         print("Turning off.")

#     def __str__(self):
#         return f'The vehicle is a {self.make} {self.model}.'


# car = Vehicle("Toyota", "RAV4")

# print(car)
# # prints: The vehicle is a Toyota RAV4.

# print(car.running)
# # prints: False

# car.start()
# # prints: Starting up!

# print(car.running)
# # prints: True


class Dog():
    next_id = 1

    test = 'hello'

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        # assign the current value of `next_id` to this instance
        self.id = Dog.next_id
        # increment the class attribute `next_id` so the next dog gets a new ID
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'Dog #{self.id} named {self.name} is {self.age} years old.'

    @classmethod
    def get_total_dogs(cls):
        # cls represents the Dog class
        print(cls.test)
        return cls.next_id - 1

class ShowDog(Dog):
    # add additional parameters AFTER those in the superclass
    def __init__(self, name, age=0, total_earnings=0):
        # always call the superclass's __init__ first
        Dog.__init__(self, name, age)
        # then add any new attributes
        self.total_earnings = total_earnings

    # add additional methods
    def add_prize_money(self, amount):
        self.total_earnings += amount
        print(f'{self.name}\'s new total earnings are ${self.total_earnings}')




winky = ShowDog('Winky', 3, 1000)
winky1 = ShowDog('Winky', 3, 1000)
winky2 = ShowDog('Winky', 3, 1000)

print(winky)
# prints: Dog #3 named Winky is 3 years old.

winky.bark()
# prints: Winky says woof!
# the `ShowDog` class inherited the `Dog` class' `__str__()` and `bark()` method

print(winky.total_earnings)
# prints: 1000

winky.add_prize_money(500)
# a new method that instances of the 'Dog' class don't have

print(winky.total_earnings)

print(ShowDog.get_total_dogs())
# prints: 1500
# go Winky go!
# harry = Dog('Harry', 2)
# harry2 = Dog('Harry', 2)
# harry3 = Dog('Harry', 2)
# harrydas = Dog('Harry', 2)
# harrdy = Dog('Harry', 2)
# harrdasy = Dog('Harry', 2)
# harrydgs = Dog('Harry', 2)
# harrgfgdfy = Dog('Harry', 2)
# harrgffgsgdy = Dog('Harry', 2)
# harrgffgsgdy = Dog('Harry', 2)

# print(harry)

# maggie = Dog('Maggie')

# print(maggie)

# print(Dog.next_id)

# print('----------------')
# # print(Dog.get_total_dogs())
# print(maggie.get_total_dogs())