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
first, *other, last = numbers_three # other, list item
print(first, other, last)
