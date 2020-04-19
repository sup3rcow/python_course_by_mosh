from abc import ABC, abstractmethod
from collections import namedtuple

class Point:  # PascalNamingConvetion
    default_color = "red"  # class attribute

    def __init__(self, x, y):  # constructor, self is reference this, curent object
        # instance attributes
        self.x = x
        self.y = y

    @classmethod  # decorator
    def zero(cls):  # class method, cls reference to class
        return cls(0, 0)  # isto kao da smo zvali Point(0, 0)

    def __str__(self):  # slicno kao override to string metode
        return f"({self.x}, {self.y})"

    def __eq__(self, other):  # override compare metode
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)  # kreiras novi objekt

    # instance method
    def draw(self):
        print(f"Point {self.x} {self.y}")


point = Point(1, 2)
point.z = 10  # dynamic attributes
print(type(point))  # <class '__main__.Point'> --> "__main__" is name of module
print(isinstance(point, Point))  # true
point.draw()

Point.default_color = "yellow"
print(point.default_color)  # yellow
print(Point.default_color)  # yellow

point.default_color = "blue"
print(point.default_color)  # blue
print(Point.default_color)  # yellow


point = Point.zero()  # class method, slicno kao konstruktori

# https://rszalski.github.io/magicmethods/
# magix methods __method__
print(point)  # (0, 0)
print(str(point))  # (0, 0)

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(2, 3)
print(point1 == point2)
print(point2 < point3)
print(point1 + point2)  # (2, 4)

# custom containers


class TagCloud:
    def __init__(self):
        self.__tags = {}  # private prefix "__"

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):  # mogucis tags["python"]
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):  # omogucis len metodu nad objektom
        return len(self.__tags)

    def __iter__(self):  # omoguci iteraciju
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.tags) # private # {'python': 3}
# mora se pristupiti sa malim slovima!? inace je KeyError:
print(cloud["PyThOn"])
print(cloud["PyThOn"])  # mozes kako hoce zbog lower
cloud["PyThOn"] = 100
print(cloud["PyThOn"])  # 100
print(len(cloud))  # 1
for tag in cloud:
    print(tag)  # python

# access private attributes
print(cloud.__dict__)  # {'_TagCloud__tags': {'python': 100}}
print(cloud._TagCloud__tags)  # {'python': 100}

# properties, get set

# ovako bi napisali u c# ili javi


class Product1:
    def __init__(self, price):
        # self.__price = price
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        else:
            self.__price = value


print(Product1(50).get_price())

# ovako mozes pisati u pythonu, ali ipak nemoj


class Product2:
    def __init__(self, price):
        # self.__price = price
        self.__set_price(price)

    def __get_price(self):
        return self.__price

    def __set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        else:
            self.__price = value
    price = property(__get_price, __set_price)


print(Product2(51).price)

# ovako pisi u pythonu


class Product3:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        else:
            self.__price = value


print(Product3(52).price)

# inheritance, overriding


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):  # override Animal constructora
        super().__init__()  # da ovo nisi napisao ne bi se izvrsila base constructor metoda Animala
        self.weight = 2

    def walk(self):
        print("walk")


class Chicken(Animal):  # empty class
    pass


m = Mammal()
m.eat()
#m.age = 2
print(m.age)
print(isinstance(m, Animal))  # True
print(isinstance(m, Mammal))  # True
print(isinstance(m, object))  # True
obj = object()  # base object class
print(issubclass(Mammal, Animal))  # True

# multiple inheritance
# avoid multi level inheritace!! Employee - Persosn - LivingCreature -Thing, max 1 - 2 levels

# bad example, same methods


class Employee:
    def greet(self):
        print("Employee greet")


class Person:
    def greet(self):
        print("Person greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()  # Employerr greet, a ne Person greet

# good example of inheritance


# by convetnion, all custom Errors must end with Error sufix
class InvalidOperationError(Exception):
    pass

# ABC - abstract base class!
class Stream(ABC): # abstract, ne mozes instancirati klasu
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        else:
            self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        else:
            self.opened = False
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")

# Polymorphism
# The word polymorphism means having many forms. ... 
# Real life example of polymorphism: A person at the same time can have different characteristic. 
# Like a man at the same time is a father, a husband, an employee.
# So the same person posses different behaviour in different situations. This is called polymorphism.

# Polymorphism, duck typing
# npr neka metoda prima listu razlicitih objekata koji imaju implementiranu istu metodu, i onda se ona izvrsava.

# extending builtin types
class Text(str): # napravis duplicate metodu nad string objektom
    def duplicate(self):
        return self + self

text = Text("Python")
print(text.lower())
print(text.duplicate()) #nova metoda

class TrackableList(list):
    def append(self, object):
        print("Append called.")
        super().append(object)

list = TrackableList()
list.append(1)

# data classes, class with no methods

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# da ne moras ovo raditi, postoji namedtuple.. gledaj ispod
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = MyPoint(1, 2)
p2 = MyPoint(1, 2)
print(p1 == p2) # False, True zbog custom __eg__ magic metode
print(id(p1)) # 14899760 address in memory
print(id(p2)) # 14899808 address in memory

# custom namedtuple type, PascalCase
MyTuplePoint = namedtuple("Point", ["x", "y"])
p1 = MyTuplePoint(x=1,y=2)
p2 = MyTuplePoint(y=2,x=1)
print(p1 == p2) # True
