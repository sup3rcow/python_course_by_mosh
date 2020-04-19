# preporuka je da se koristi absolute import
from ecommerce.customer import contact # absolute import paketa
from ..customer import contact # related import paketa

print("Sales initialized.", __name__)

def calc_tax():
    print("calc_tax")
    pass

def calc_shipping():
    print("calc_shipping")
    pass

# ako se kod direktno pokrene, izvrsi ovu skrptu, ako se importa kao modul onda ne
if __name__ == "__main__":
    print("Sales started")
    calc_tax()