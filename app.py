course = f"Python \"Programming {2019 + 1}"
print("*" * 10)
print(len(course))
print(course[0:2])
print(course[1:])
print(course.upper())
print(course.find("thon"))
print("ython" not in course)
print(10 / 3)
print(10 // 3)
print(10 * 3)
print(10 ** 3)
# x = input("x: ") # input je string
# print(x + str(1))

if 12 > 11:
    print("12 > 11")
elif 12 < 11:
    print("not true")
else:
    print("blaa")
print("end if")

age = 22
if age >= 18:
    message = "Eligible1"
else:
    message = "Not eligible"
print(message) # nema scope-a?!?!?!

# ternary operator
message_2 = "Eligible2" if age >= 18 else "Not eligible"
print(message_2)

# logical operator "and" "or" "not"
high_income = True
good_credit = True
student = False
if high_income and good_credit and not student:
    print("Eligible3")

# chain operators


