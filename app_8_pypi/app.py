import requests

# pypi - python package index https://pypi.org

# pip - tool for installing packages
# cmd: pip install requests
# cmd: pip install requests==2.23.0 --specify exact version
# cmd: pip install requests==2.23.* --specify latest compatible version 2.23
# cmd: pip install requests~2.23.0 --specify latest compatible version 2.23, same as "==2.23.*"
# watning, upgrade pip: python -m pip install --upgrade pip

# list all packages: pip list

request = requests.get("http://google.com")
print(request.status_code) # 200



# virtual environment, kada imas logiku koja ovisi o staroj verziji paketa

# nemoj ovako
# cmd: python -m venv env --> po konvenciji folder nazives "env"
# cmd: env\bin\activate.bat  --> linux: source env/bin/activate
# nakon toga se nalazis u konzoli od envirnomenta i mozes instalirati starije verzije paketa pomocu pip komande
# cmd: deactivate -> izlaz iz env konzole

# ovo je bolje
# pipenv - tool za automatsko kreiranje virtualnog direktorija i instaliranje paketa
# pip install pipenv
# pipenv install requests
# pipenv --venv --> path gdje se nalazi virtualni direktorij, nije vise u projektu, sto je dobro!
# pipenv shell --> aktiviras virtualni cmd i iz nje mozes pokrenuti python program: python app.py, tako da kuzi gdje su dependeciji
# exit --> izadjes env cmd-a

# vs code, py runner, kazes koji python da koristi
# pipenv --venv -> env folder
# onda u vs code settings.json, nadjes code-runner.executorMap i nadjes "python".. stavis putanju od env pythona (na linuxu je naziv fajla python3 na win samo python)

# py runner postavke.. kad ti bude trebalo, pogledaj opet video.

# pipenv

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# cmd moras se nalaziti u direktoriju gdje je app.py, mora biti kativiran env python -dolje lijevo i u shellu treba biti env python aktiviran.. prefix (envi naziv pythona)
# i tek onda mozes instalirati pypi pakete
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# PipFile, popis papketa i struktura, slicno kao npm package.js
# PipFile.lock slicno kao npm package-lock.lock # popis tocnih verzija paketa

# pipenv install, slicno kao npm install
# pipenv install --ignore-pipfile --> instalira tocne verzije paketa koje su definrane u Pipfile.lock fajlu

# managing dependencies
# pipenv graph --> izlista sve dependecije i njihove dependencije
# pipenv uninstall packagename, makne packagename ali ne makne njegove dependecije jer ne zna da li ih neko koristi
# pipenv graph --> prikaze dependecije koje nije maknio, ako se projekt instalira negde drugde, tih dependecija vise nece biti

# update paketa
# pipenv update --outdated

# update pojedinog paketa
# pipenv update packagename


# publishig package
# skip

# document published package, docstring
# skip

# pydoc utility, see documentation of module
# pydoc math
