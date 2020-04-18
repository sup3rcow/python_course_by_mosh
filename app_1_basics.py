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
print(message)  # varijable unutar if-a pripadaju vanjskom scope-u!!!!!!!!!!!!!
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
if 18 <= age < 65:
    print("Eligible4")

# for loops
# (index - krece od ukljucujuci ga, index - ide do ne ukljucujuci ga, krece od 1 step) ??
for number in range(0, 9, 1):
    print("Attemp", number, "." * number)  # 0,1,2,3,4,5,6,7,8
    if False:
        break  # exit from for loop, print only 0
else:  # ako je uvucen ispod for-a a ne if-a, onda ce se ispisati samo jednom i to na kraju ako se ne dogodi break!!
    print("go")

# nasted loops
# for u for petlji

#iterables
print(type(5))
print(type(range(5)))

for x in "Python": # range(5), "Python", [1, 2, 3, 4, 5]
    print(x)

#while loops
number_w = 7
while number_w > 5:
    print(number_w)
    number_w -= 1
