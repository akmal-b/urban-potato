# nasledovaniye

# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Horse(Animal):
#     pass

# pony=Horse()
# pony.make_sound('igogo')

# class Car:
#     def __init__(self, model, color, year):
#         self.model=model
#         self.color=color
#         self.year=year
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor=sponsor

# class Calculate:
#     @classmethod
#     def summary(cls, a, b):
#         return a+b
# print(Calculate.summary(2, 4))

# @property

# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height
#
#     @property
#     def area(self):
#         return self.width * self.height
# rectangle = Rectangle(4,5)
# print(rectangle.area)
#
# rectangle.width=6
# print(rectangle.area)


# class Worker:
#     def __inti__(self, name, position):
#         self.name=name
#         self.position=position
#
# class HR(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#
#     def show_position(self, worker):
#         print(worker.name, worker.position)
#
# Jordan = Worker('Jordan', 'Junior')
# Pavel = HR('Pavel', 'HR')

# class Player:
#     def __init__(self, power, speed, accuracy, stamina):
#         self.power = power
#         self.speed = speed
#         self.accuracy = accuracy
#         self.stamina = stamina
#
# class Goalkeeper(player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().__init__(power, speed, accuracy, stamina)
#
#     def goal(self):
#         print('zabil myach v vorota')
#
# class Forward(player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().__init__(power, speed, accuracy, stamina)
#
#     def goal(self):
#         print('zabil myach v vorota 2 razaz')
#
# class Middle(player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().__init__(power, speed, accuracy, stamina)
#
#     def goal(self):
#         print('begaet bistro')
#
# class Defender(player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().__init__(power, speed, accuracy, stamina)
#
#     def goal(self):
#         print('zashitil vorota')


