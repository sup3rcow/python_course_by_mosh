import requests
import config
import PyPDF2

# steps
# pip install pipenv
# pipenv install requests
# zatvori/otori vs code, ako klikom dole lijevo se ne nudi env verzija pythona od projekta
# promijenis verziju pythona da koristi env python
# vs code ponudi da instaliras pylint, kliknes install
# ctrl+alt+f formatiraj text--> vs code install autopep8

# radi sve ok, ali se javlja greska priliko installa pylint i autopep8...
# greska, rijesi da se ne pojvaljuje
# virtualenv Scripts\Activate.ps1 cannot be loaded because running scripts is disabled
# rjesenje https://github.com/microsoft/vscode-python/issues/2559
# u cmd: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# i onda ti se otvori python sa prefixom (naziv env projekta)

url = "https://api.github.com/users/test"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "dummy": "test"
}
response = requests.get(url)  # get(url, headers=headers, params=params)
print(response.json()["avatar_url"])  # extract value from dict
# reminder -> [item for item in items if item[1] > 9]

# twilio send sms
# pipenv install twilio
# skip

# web scraping, extractiong from html, xml,
# pipenv install beautiflsoup4
# response = request.get("...")
# soup = BeautifulSoup(response.txt, "html.parser")
# questions = soup.select(".question-summary") -> filter po css klasi
# print(questions[0].attrs) -> dict.. id class
# print(questions[0].get("id", 0))
# print(questions[0].select(".asdasd"))
# skip

# browser automation - tests
# pipenv selunuim
# driver za automatizaciju odredjenog browsera
# odes na stranicu od selenium paketa i vidis koji se driveri nude za chrome, edge, firefox, safari..
# skip

# pdf files
# pipenv install pypdf2
with open("first.pdf", "rb") as file: # rb -read binary
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    # writer.insertPage(page, 2)
    with open("first-rotated.pdf", "wb") as output:
        writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")