# working with paths
from pathlib import Path

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