class Student:
    def __init__(self, name,age, height, number):
        self.height = height
        self.name=name
        self.number=number
        self.age=age
    def grow(self,height = 1):
        self.height += height

anton = Student("Anton",12,166,38038038086)

print("Name - ", anton.name)
print("Age - ", anton.age)
print("Height - ", anton.height)
print("Number - ", anton.number)

anton.grow(height=1)
print(anton.height)