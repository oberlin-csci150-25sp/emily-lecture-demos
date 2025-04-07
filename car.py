# # 25.1
# class Car:
#   ...
#   def message(self):
#     print("I'm basic")

# class FancyCar(Car):
#   ...
#   def message(self):
#     print("I'm fancy")

# c = FancyCar()
# c.message()

# # 25.2
# class Car:
#   ...
#   def horn(self):
#     print("*beep beep*")

# class FancyCar(Car):
#   ...
#   def message(self):
#     print("I'm fancy")

# c = FancyCar()
# c.horn()

# A --> Car
# B --> FancyCar

# self.x --> self.sound
# self.y --> self.color

# a -->
# b -->

# bar() -->
# foo() -->

# # 25.3
# class Car:
#   def __init__(self, s):
#     self.sound = s

#   def horn(self):
#     print(self.sound)

# class FancyCar(Car):
#   def __init__(self, c):
#     self.color = c

#   def showColor(self):
#     print(self.color)

# c = Car("*beep beep*")
# f = FancyCar("turquoise")
# f.horn()

# # 25.4
# class Car:
#   def __init__(self, s):
#     self.sound = s

#   def horn(self):
#     print(self.sound)

# class FancyCar(Car):
#   def __init__(self, s, c):
#     super().__init__(s)
#     self.color = c

#   def showColor(self):
#     print(self.color)

# c = Car("*beep beep*")
# f = FancyCar("~fancy beep~", "turquoise")
# f.horn()
