import ToDo_Class

if __name__ == "__main__":

    lista = ToDo_Class.lista_zadan('C:/plik.pcl')

    while True:
        polecenie = int(input(
                              "1 - Dodaj zadanie\n"
                              "2 - Skasuj zadania\n"
                              "3 - Wyświetl zadania\n"
                              "0 - Zakończ program\n"
                              ))

        if polecenie == 1:
            priorytet = input("Podaj priorytet: ")
            opis = input("Podaj opis: ")
            lista.dodaj_zadanie(priorytet, opis)

        elif polecenie == 2:
            skasuj = int(input("Które zadanie chcesz skasować?\n"))
            lista.usun_zadanie(skasuj)

        elif polecenie == 3:
            print("Twoje zadania:\n")
            lista.wyswietl_zadania()

        elif polecenie == 0:
            print("Koniec programu")
            lista.zapisz_listę()
            break
