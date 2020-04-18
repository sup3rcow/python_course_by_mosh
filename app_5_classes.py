class Point: # PascalNamingConvetion
    def __init__(self, x, y): # constructor, self is reference this, curent object
        self.x = x
        self.y = y
    def draw(self):
        print(f"Point {self.x} {self.y}")

point = Point(1, 2)
print(type(point)) # <class '__main__.Point'> --> "__main__" is name of module
print(isinstance(point, Point)) # true
point.draw()
