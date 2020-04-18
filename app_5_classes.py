class Point:  # PascalNamingConvetion
    default_color = "red" # class attribute

    def __init__(self, x, y):  # constructor, self is reference this, curent object
        # instance attributes
        self.x = x
        self.y = y

    @classmethod # decorator
    def zero(cls): # class method, cls reference to class
        return cls(0, 0) # isto kao da smo zvali Point(0, 0)

    def __str__(self): # slicno kao override to string metode
        return f"({self.x}, {self.y})"
    # instance method
    def draw(self):
        print(f"Point {self.x} {self.y}")


point = Point(1, 2)
point.z = 10  # dynamic attributes
print(type(point))  # <class '__main__.Point'> --> "__main__" is name of module
print(isinstance(point, Point))  # true
point.draw()

Point.default_color = "yellow"
print(point.default_color) # yellow
print(Point.default_color) # yellow

point.default_color = "blue"
print(point.default_color) # blue
print(Point.default_color) # yellow


point = Point.zero() # class method, slicno kao konstruktori

# https://rszalski.github.io/magicmethods/
# magix methods __method__
print(point) # (0, 0)
print(str(point)) # (0, 0)
