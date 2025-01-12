class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

rd = Circle(100)
print(rd.get_radius())

rd.set_radius(101)
print(rd.get_radius())
