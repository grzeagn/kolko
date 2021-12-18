#%%
class Zwierze:
    def __init__(self,nazwa, wiek, waga):
        self.nazwa = nazwa
        self.waga = waga
        self.wiek = wiek

    def podaj_dane(self):
        print(f'jestem zwierzeciem {self.nazwa}, mam {self.wiek} lat i waze {self.waga} kg.')

class Slon(Zwierze):
    pass

class Lew(Zwierze):
    def __init__(self):
        self.iloscKlow=4

Dumbo=Slon()
Dumbo.nazwa="Slonik Dumbo"
Dumbo.waga=300
Dumbo.wiek=400
Simba=Lew()
Simba.iloscKlow=3
Simba.wiek=34
Simba.nazwa="Lew Simba"


