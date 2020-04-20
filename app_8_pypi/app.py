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