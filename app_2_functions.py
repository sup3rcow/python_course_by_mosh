def greet(first_name, last_name="Annonymus"):  # pararmeters
    print(f"Hi {first_name} {last_name}, this is My first py function.")


# two lines break after end of function - convention
greet("Mosh", last_name="Hamedani")  # arguments - values
greet("Mosh")

# 1 - funtion perform a task
# 2 - function return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("app_2_content.txt", "w")
file.write(message)
file.close()
file = open("app_2_content.txt", "r")
print(file.read())  # read from file

# xargs -> tuple argument


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4))

# xxargs -> dictionary argument - key value pairs


def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age="3")

# scopes, parametri zive samo unutar funkcije

message = "a"


def method_one(name):
    # bad practive, dont do this
    global message  # kazes da ne kreira lokalnu vraijabu i da koristi globalnu
    message = "b"


method_one("blaa")
print(message)  # output b
