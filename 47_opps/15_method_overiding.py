class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * 3.15


s1 = shape(21, 2)
print(s1.area())
s2 = circle(3)
print(s2.area())
