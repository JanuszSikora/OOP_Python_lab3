from time import sleep
import pickle


class Ksztalt():
    def __init__(self, center, outer_radius):
        self.center = center
        self.outer_radius = outer_radius

    def __str__(self):
        self.info()
        return str(self.informacja)

    def info(self):
        self.informacja = 'Środek: ', self.center, ' promień: ', self.outer_radius
        return self.informacja


class Rozmiar():
    def __init__(self, change_radius):
        self.change_radius = change_radius

    def change_size(self, change_radius):
        self.outer_radius = change_radius
        return self.outer_radius


class Kwadrat(Ksztalt, Rozmiar):
    def __init__(self, center, outer_radius):
        super().__init__(center, outer_radius)


class Kolo(Ksztalt, Rozmiar):
    def __init__(self, center, outer_radius):
        super().__init__(center, outer_radius)



# zapis obiektów do pliku
def plik_zapisz(dane, plik_zapisu):
    plik = open(plik_zapisu, 'wb')
    k = 0
    for i in dane:
        pickle.dump(i, plik)
        k += 1
    plik.close()

# odczyt obiektów z pliku
def plik_czytaj(plik_zapisu):
    plik = open(plik_zapisu, 'rb')
    pickle.load(plik)
    plik.close()


# main
# Tworzenie obiektów
kw_1 = Kwadrat(10, 20)
ko_1 = Kolo(5, 15)
kw_2 = Kwadrat(7, 16)
ko_2 = Kolo(6, 10)
print(kw_1, '\n', kw_2, '\n', ko_1, '\n', ko_2)

kw_1.change_size(40)
kw_2.change_size(100)
ko_2.change_size(20)
ko_1.change_size(111)
print(kw_1, '\n', kw_2, '\n', ko_1, '\n', ko_2)

# zapis figur
dane_1 = [kw_1, kw_2, ko_1, ko_2]
plik_zapisu = 'plik_1.dat'

plik_zapisz(dane_1, plik_zapisu)
plik_czytaj(plik_zapisu)
for i in dane_1:
    print(i)


sleep(2)
