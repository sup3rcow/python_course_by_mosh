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

# zip
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2))) # [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]