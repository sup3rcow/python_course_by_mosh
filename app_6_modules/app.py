from ecommerce.shopping.sales import calc_shipping, calc_tax # objekte iz modula
from ecommerce.shopping import sales # importas modul kao objekt iz packagea
import sys # importas modul kao objekt

# nemoj ovako importati sve iz modula jer se moze desiti da importas neki naziv koji vec imas..
# from modulename import *

# u __pycache__ folderu, python sprema kompajlirane module za brzi load
# ako vec postoji u folderu, nece ga opet kompajlirati
# po date time-u .py i ..38(verzija pytona).pyc fajla, kompajler zna da li je najnovija verzija u __pycache__ folderu

# modul koji se okida kroz cmd, se uvijek rekompajla
# i zato se ne kesira app.py

print(__name__) # modul od kuda starta aplikacija je uvijek "__main__"


calc_shipping()
sales.calc_shipping()
# print(sys.path) # path varijabla od pythona gdje trazi module

print(dir(sales)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax', 'contact']  
print(sales.__name__) # ecommerce.shopping.sales
print(sales.__package__) # ecommerce.shopping
print(sales.__file__) # C:\projects_vs\python\first_python_project\app_6_modules\ecommerce\shopping\sales.py