# working with paths
from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta
import random
import string
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
import sys
import subprocess

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
print(time.time()) # 1587372677.7349, number of seconds after 1.1.1970

# datetime
print(datetime(2020, 1, 31)) # 2020-01-31 00:00:00
print(datetime.now()) # 2020-04-20 11:14:41.690266
print(datetime.strptime("2020.01.31", "%Y.%m.%d")) # 2020-01-31 00:00:00
print(datetime.now().strftime("%y.%m.%d")) # 20.04.20

# timedelta

dt1 = datetime(2020, 2, 1) + timedelta(days=-1, seconds=1) # add -1 day
dt2 = datetime(2020, 3, 1)
duration = dt2 - dt1
print(duration) # 29 days, 23:59:59
print("days:", duration.days) # 29
print("seconds (vrijednost od sati, minuti, sekunde):", duration.seconds) # 86399
print("total_seconds (u vrijednost uracunati i dani pretvoreni u sekunde):", duration.total_seconds()) # 2591999.0

# random values

print(random.random()) # 0-1
print(random.randint(1, 10 )) # 1-10
print(random.choice([1, 2, 3, 4])) # 1 or 2 or 3 or 4
print(random.choices([1, 2, 3, 4], k=2)) # [4, 2]
print(random.choices("abcdefghi", k=4)) # ['d', 'i', 'g', 'd']
print("".join(random.choices("abcdefghi", k=4))) # efhf
print("".join(random.choices(string.ascii_letters + string.digits, k=4))) # Ab6K

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers) # [2, 1, 4, 5, 3]

# opening browser
# webbrowser.open("http://google.com")

# email
messsgae = MIMEMultipart()
messsgae["from"] = "My name"
messsgae["to"] = "dasdas@gmail.com"
messsgae["subject"] = "Single line title"
# messsgae.attach(MIMEText("Body", "plain"))
# messsgae.attach(MIMEText("<div>Body</div>", "html"))

# email templates
template = Template(Path("template.html").read_text())
# body = template.substitute({ "name": "John" }) # 1. nacin, replace name, podmetnes dict
body = template.substitute(name="John") # 2. nacin, replace name
messsgae.attach(MIMEText(body, "html"))

#messsgae.attach(MIMEImage(Path("..putanja do slike.png").read_bytes()))


# radi u try bloku za svaki slucaj
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo() # kazemo smtp serveru da zelimo poslati email
#     smtp.starttls() # tip konekcije, transport layer security, eknripcija
#     smtp.login("myusername", "mypassword")
#     smtp.send_message(messsgae)
#     print("Sent...")

# comand line arguments
print(sys.argv) # ['app.py']

if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password) # ispise 2. parametar iz comand line-a

# external programs
# os commands, linux: ls, windows: dir

# helper methods

# nova metoda, koristi
# subprocess.run

# legacy, nemoj koristiti
# subprocess.call
# subprocess.check_call
# subprocess.check_output

# subprocess.Popen # process open class
# subprocess.run(["dir", "-l"]) # linux
result = subprocess.run(["dir", "/s"], shell=True) # The dir command displays a list of files and subdirectories in a directory. With the /S option, it recurses subdirectories and lists their contents as well.
print(result.args) # ['dir', '/s']
print(result.returncode) # 0, -> no error
print(result.stderr) # None, error message
print(result.stdout) # None, output is printed on window

result = subprocess.run(["dir", "/s"], shell=True, capture_output=True, text=True)
print(result.stdout) # string output..

completed2 = subprocess.run(["python", "other.py"], capture_output=True, text=True)
print(completed2.stdout) # Other.py script.
if completed2.returncode != 0:
    print(completed2.stderr)

try:
    completed3 = subprocess.run("sdas", capture_output=True, text=True, check=True) # check=True, if there is an error, run method will raise an exception
except subprocess.CalledProcessError as ex:
    print(ex)
