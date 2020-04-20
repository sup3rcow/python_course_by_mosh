# working with paths
from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
import csv
import json
import sqlite3

# Path("C:\\Program Files\\Microsoft")
# Path(r"C:\Program Files\Microsoft") # raw path "r", ne moras pisati \\ umjesto \
# Path("C:/Program Files/Microsoft")
# Path() / "ecommerce" / "__init_.py" # path combine

print(Path.home()) # user home dir

path = Path("ecommerce/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name) # __init__.py
print(path.stem) # __init__
print(path.suffix) # .py
print(path.parent) # ecommerce
path = path.with_name("file.txt") # only change name and extension of file in path
print(path) # ecommerce\file.txt

# jer pokreces python iz direktorija: C:\projects_vs\python\first_python_project\app_7_py_standard_library
# a path je (line 11): ecommerce/__init__.py
print(path.absolute()) # C:\projects_vs\python\first_python_project\app_7_py_standard_library\ecommerce\file.txt
print(path.with_suffix(".mp3")) # ecommerce\file.mp3

path = Path("ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce")

# iterdir metoda, ne mozemo pretrazivati po paternu ili rekurzivno

#list of files and dirs
print(path.iterdir()) # <generator object Path.iterdir at 0x02CBE028>, moras iterirati
for p in path.iterdir():
    print(p)

print(list(path.iterdir())) # [WindowsPath('ecommerce/__init__.py')], na unix os-u ce biti PosixPath
print([p for p in path.iterdir()]) # [WindowsPath('ecommerce/__init__.py')], na unix os-u ce biti PosixPath

print([p for p in path.iterdir() if p.is_dir()]) # filter only dirs # []

# glob, podrzava rekurzivno pretrazivanje (**/), ili rglob
print([p for p in path.glob("**/*.py")]) # [WindowsPath('ecommerce/__init__.py')]
print([p for p in path.rglob("*.py")]) # [WindowsPath('ecommerce/__init__.py')]

# files

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()

print(path.stat()) # file info
print(ctime(path.stat().st_ctime)) # Sun Apr 19 16:41:09 2020
# path.read_bytes()
# path.read_text() # content of a file as a string
print(path.read_text()) # jednostavni je od file open, read, close, with
# path.write_text("dummy")

# copy file
source = Path("ecommerce/__init__.py")
target = Path() / "ecommerce/copy_of__init__.py" # curent dir + ecommerce/copy_of__init__.py

# target.write_text(source.read_text()) # ne bas najbolji nacin
shutil.copy(source, target) # bolji nacin

# write to zip files
# zip = ZipFile("files.zip", "w")
with ZipFile("files.zip", "w") as zip: # ne moras zip.close(), ni try/finally
    print([p for path in Path("ecommerce").rglob("*.*")]) # *.* all files and its children # [WindowsPath('ecommerce/__init__.py'), WindowsPath('ecommerce/__init__.py')]
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
# zip.close()

# read from zip files
with ZipFile("files.zip") as zip:
    print(zip.namelist()) # print filenames in zip file # ['ecommerce/copy_of__init__.py', 'ecommerce/__init__.py']
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    # zip.extractall("extract")

# csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

with open("data.csv") as file:
    reader = csv.reader(file)

    # print(list(reader)) # [['transaction_id', 'product_id', 'price'], ['1000', '1', '5'], ['1001', '2', '15']]
    # ne mozes 2 puta zaredom citati file, zato je zakomentirana lijia iznad
    for row in reader:
        print(row)

# json
movies = [ # dict array u pythonu jako lici na json format
    { "id": 1, "title": "Terminator", "year": 1989 },
    { "id": 2, "title": "Kindergarten", "year": 1990 }
]

# create json obj as text
jsondata = json.dumps(movies)
print(jsondata)

# write text json file
Path("movies.json").write_text(jsondata)

# read text json file
textdata = Path("movies.json").read_text()
dictdata = json.loads(textdata) # same as movies obj
print(dictdata)

# sqlite db
movies_from_json = json.loads(Path("movies.json").read_text())
print(movies_from_json) # dict list
# with sqlite3.connect("db.sqlite3") as connection: # ako file ne postoji, kreirat ce ga
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies_from_json:
#         print(movie.values()) # dict_values([1, 'Terminator', 1989])  .. svaki red
#         print(tuple(movie.values())) # (1, 'Terminator', 1989) ..
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()

with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command) # return cursor

    # for row in cursor:
    #     print(row) # tuple (1, 'Terminator', 1989)

    # dvije linije iznad zakomentirane jer ne mozes 2 puta citati isti kursor
    movies = cursor.fetchall() # procitaj sve odjednom
    print(movies) # list of tuples [(1, 'Terminator', 1989), (2, 'Kindergarten', 1990)]

# timestamps