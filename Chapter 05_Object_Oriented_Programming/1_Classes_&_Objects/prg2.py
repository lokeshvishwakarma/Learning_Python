class Circle:
    PI = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.test = radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) or isinstance(new_radius, float):
            self.test = new_radius
        else:
            print("Wrong Values Passed")

    def calc_area(self):
        return self.PI * self.radius * self.radius

    def __repr__(self):
        return "Circle Created. Radius: {}".format(self.radius)


circle_1 = Circle()
circle_2 = Circle(3)
circle_1.set_radius(10)
print(circle_1)
print(circle_2.calc_area())
