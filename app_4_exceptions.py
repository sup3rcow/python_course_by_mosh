from timeit import timeit
# try:
#     pass
# except expression as identifier:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass # dogodi se samo kad nema exceptiona
# finally:
#     pass # dogodi se uvijek, npr kad treba file.close()

try:
    with open("app_2_content.txt") as file, open("app_2_functions.py") as file2: # nemoras file.close() jer ce python sam zatvoriti file, jer file ima __enter__ i __exit__ metode
        print("Files opened.")
        file
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as identifier:
    print("Not a valid age!")
# finally:
#     file.close()
#     file2.close()

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as identifier:
    # print(identifier)
    pass
else:
    pass
finally:
    pass

"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as identifier:
    # print(identifier)
    pass
else:
    pass
finally:
    pass

"""
# cost of raising exceptions.. slower with raising exception

print("code1 timeit: ", timeit(code1, number=10000)) # code1 timeit:  0.013336799999999926
print("code2 timeit: ", timeit(code2, number=10000)) # code2 timeit:  0.006856000000000084


# https://docs.python.org/3/library/exceptions.html
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning
