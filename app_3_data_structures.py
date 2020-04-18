from collections import deque
from array import array
from sys import getsizeof

letters = ["a", "b", "c"]
list_of_lists = [[0, 1], [2, 3]]
zeros = [0] * 5  # [0,0,0,0,0]
combined = zeros + letters  # list with diferent types
print(combined)
numbers_one = list(range(5))
print(numbers_one)
chars = list("Hello World")
print(chars)
print(len(chars))

# accesing items
letters[0] = letters[0].upper()
print(letters[0:2])  # A,b
print(letters[-2:-1])  # b
print(letters[::2])  # A,c - svaki drugi

numbers_two = list(range(20))
print(numbers_two[::-1])  # reverse

# unpacking list and packing.. *other, isto kao xargs kod funkcija
numbers_three = [1, 2, 3, 4, 5]
first, *other, last = numbers_three  # other, list item
print(first, other, last)

# looping
letters_loop = ["a", "b", "c"]
for ll in enumerate(letters_loop):
    # tuple zbog enumerate -> (index, item)
    print(f"index: {ll[0]}, value: {ll[1]}")

# unpacking da ne dobijes tuple
for ll_index, ll_value in enumerate(letters_loop):
    print(f"index: {ll_index}, value: {ll_value}")

# add, remove item from list
letters_loop.append("d")  # dodaj na kraj
letters_loop.insert(0, "-")  # dodaj na pocetak liste
letters_loop.pop()  # makne zadnji element
letters_loop.pop(0)  # makne prvi element
# makne prvi element koji je jednak slovu "b", ako hoces maknut sva slova "b", moras to raditi u loopu
letters_loop.remove("b")
del letters_loop[0:1]  # makne range of items
print(letters_loop)
letters_loop.clear()  # makne sve iz liste

# finding
letters_finding = ["a", "b", "c"]
print(letters_finding.index("a"))  # 0
if "d" in letters_finding:
    # mora unutar if-a, inace dobijes ValueError
    print(letters_finding.index("d"))
else:
    print("nema slova d")

letters_finding.count("d")  # 0, jer ga nema u listi

# sorting
numbers_sort = [1, 4, 6, 2, 7]
numbers_sort.sort()  # asc nad postojecom listom
numbers_sort.sort(reverse=True)  # desc nad postojecom listom
sorted(numbers_sort)  # asc, vrati novu listu
sorted(numbers_sort, reverse=True)  # desc, vrati novu listu

tuple_items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


def sort_tuple_items(item):
    return item[1]  # kazes po cemu da srtira, po broju


tuple_items.sort(key=sort_tuple_items)
print(tuple_items)

# lambda functions
tuple_items.sort(key=lambda item: item[1])
print(tuple_items)

# map
print(map(lambda item: item[1], tuple_items))  # map object
print(list(map(lambda item: item[1], tuple_items)))  # [9,10,12]

# filter
print(list(filter(lambda item: item[1] > 9, tuple_items)))

# comprehensions
# rezultat isti kao i map pa list samo brze
print([item[1] for item in tuple_items])
# rezultat isti kao i filter samo brze
print([item for item in tuple_items if item[1] > 9])

number_values = []
for x in range(5):
    number_values.append(x * 2)
print(number_values) # [0, 2, 4, 6, 8]
print([x *2 for x in range(5)]) # [0, 2, 4, 6, 8]

# zip
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list2)))

# stack
browsing_session = []
if not browsing_session:  # ne moras gledati count
    print("prazna lista")
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop()  # lifo

# queuse
queue = deque([])
if not queue:
    print("prazan queue")
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # fifo
print(queue)  # deque([2, 3])

# tuples, cannot modify tuple
point = 1, 2  # same as (1, 2)
# point = ()
# point = 1, 2,
# point = (1, 2) + (3, 4) # (1,2,3,4)
# point = (1, 2) * 3 # (1,2,1,2,1,2)
# x = 1, # ako je jedna znamenka,mora zadnje biti "," kako bi python skuzio da je tuple
print(point, type(point))  # <class 'tuple'>
point = tuple([1, 2])
ltters_from_tuple = tuple("Hello World")
print(ltters_from_tuple[0: 2])
if 2 in point:
    print("2 exists")

# swaping
x = 10
y = 11
x, y = y, x  # swaping
a, b = 1, 2  # unpacking tuple
print(x, y, a, b)

# arrays, objekti moraju biti istog tipa!! bolje preformanse od liste, koristi samo kad imas prefromase probleme i veliki broj itema
array_numbers = array("i", [1, 2, 3])  # "i" signed integers
array_numbers.append(4)
array_numbers.insert(0, 11)  # dodaj na odredjeni index
print(array_numbers)

# sets, unordered collection with no duplicates, can not acces using index
numbers_duplicates = [1, 1, 2, 3, 4]
numbers_sets = set(numbers_duplicates)  # {1, 2, 3, 4}
numbers_sets.add(5)
numbers_sets.remove(5)
print(list(numbers_sets), len(numbers_sets))

union_sets = {1, 2, 3, 4} | {3, 4, 5}
intersection_sets = {1, 2, 3, 4} & {3, 4, 5}
first_withou_second_sets = {1, 2, 3, 4} - {3, 4, 5}
symetric_diff_sets = {1, 2, 3, 4} ^ {3, 4, 5}
print(union_sets) # {1, 2, 3, 4, 5}
print(intersection_sets) # {3, 4}
print(first_withou_second_sets) # {1, 2}
print(symetric_diff_sets) # {1, 2, 5}
if 1 in union_sets:
    print("set has 1")

# dictionaries
dictionary = { "x": 1, "y": 2 }
dictionary = dict(x=1, y=2) # koriti ovaj nacin, elegantni je
dictionary["x"] # 1
dictionary["x"] = 10
dictionary["z"] = 30
# dictionary["a"] # error
dictionary.get("a") # None -> null u python jeziku
dictionary.get("a", 0) # 0, vrati default value
del dictionary["z"]
print(dictionary)
for key in dictionary:
    print(key, dictionary[key])

for key, value in dictionary.items():
    print(key, value)

# dictionary comprehensions comprehesive
set_values = {f"x{x}": x * 2 for x in range(5)} # {'x0': 0, 'x1': 2, 'x2': 4, 'x3': 6, 'x4': 8}
print(set_values)

# generator expresion, da ne cuvas velike podatke u memoriji, nego njihov opis.. tj generator
# ne znas koliko ima elemenata u generatoru, jedini nacin je da iteriras..
gen_values = (x * 2 for x in range(1000))
listt_values = [x * 2 for x in range(1000)]
print(type(gen_values)) # <class 'generator'>
print(getsizeof(gen_values)) # 56 ili neki drugi broj
print(getsizeof(listt_values)) # 4508 manji broj od gen_values


# unpacking operator, slicno kau u js-u destructor
unpck_numbers = [1, 2, 3]
print(unpck_numbers) # [1, 2, 3]
print(*unpck_numbers) # 1 2 3
print(1, 2, 3) # 1 2 3

print(range(3)) # range(0, 3)
print(*range(3)) # 0 1 2
print([*range(5), *"Hello"]) # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

dict1 = {"x": 1}
dict2 = dict(x=10, y=2)
print({**dict1, **dict2, "z": 1}) # {'x': 10, 'y': 2, 'z': 1}



