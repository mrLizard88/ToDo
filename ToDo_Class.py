import pickle
from datetime import datetime


class zadanie:

    def __init__(self, numer_zadania, priorytet, opis):
        self.data = datetime.now()
        self.numer_zadania = numer_zadania
        self.priorytet = priorytet
        self.opis = opis

    def __str__(self):
        data_utworzenia = datetime.strftime(self.data, "%Y-%m-%d")
        dni_temu = (datetime.now() - self.data).days

        return (
                f"Zadanie: {self.numer_zadania}\nPriorytet: {self.priorytet}"
                f"\nOpis: {self.opis}\nCzas utworzenia: {data_utworzenia}\n"
                f"Dni temu: {dni_temu}\n"
                )


class lista_zadan:

    lista = []
    numer_zadania = 0

    def __init__(self, plik):
        self.plik = plik
        try:
            with open(self.plik, "rb") as f:
                self.lista = pickle.load(f)
                print("Czytam")
                self.numer_zadania = max(x.numer_zadania for x in self.lista)
        except:
            print("Plik z zadaniami nie istnieje!")

    def wyswietl_zadania(self):
        for x in self.lista:
            print(x)

    def dodaj_zadanie(self, priorytet, opis):
        self.numer_zadania += 1
        nowe_zadanie = zadanie(self.numer_zadania, priorytet, opis)
        self.lista.append(nowe_zadanie)

    def usun_zadanie(self, skasuj):
        for a, b in enumerate(self.lista):
            if b.numer_zadania == int(skasuj):
                del self.lista[a]
                return

    def zapisz_listę(self):
        with open(self.plik, "wb") as f:
            pickle.dump(self.lista, f)
