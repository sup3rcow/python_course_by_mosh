# working with paths
from pathlib import Path
from time import ctime
import shutil

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