from time import sleep
import pickle


class Mapa():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        self.info()
        return str(self.informacja)

    def info(self):
        self.informacja = 'Współrzędne: ', self.x, self.y
        return self.informacja


class Pokoj(Mapa):
    def __init__(self, x, y, locked): # locked może być True lub False
        super().__init__(x, y)
        self.locked = locked

    def info(self):
        self.informacja = 'Współrzędne pokoju i stan: ', self.x, self.y, self.locked
        return self.informacja


class Gracz(Mapa):
    def __init__(self, x, y, stuff):
        super().__init__(x, y)
        self.stuff = stuff

    def move_n_pick(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change
        for i in pokoje:
            if i.x == self.x and i.y == self.y and i.locked == False:
                for j in przedmioty:
                    if j.x == self.x and j.y == self.y:
                        self.stuff.append(j)
        return self.x, self.y, self.stuff

    def display(self):
        for i in self.stuff:
            print(i)

    def info(self):
        self.informacja = 'Współrzędne gracza: ', self.x, self.y, 'Przedmioty: '
        return self.informacja


class Przedmiot(Mapa):
    def __init__(self, x, y):
        super().__init__(x, y)

    def info(self):
        self.informacja = 'Współrzędne przedmiotu: ', self.x, self.y, 'wartość: ', self.wartosc
        return self.informacja


class Wartosciowy(Przedmiot):
    def __init__(self, x, y, wartosc):
        super().__init__(x, y)
        self.wartosc = wartosc


class Smiec(Przedmiot):
    def __init__(self, x, y, wartosc):
        super().__init__(x, y)
        self.wartosc = wartosc

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
pokoje = [Pokoj(5, 2, True), Pokoj(4, 7, False), Pokoj(12, 60, False), Pokoj(15, 2, True)]
for i in pokoje:
    print(i, '\n')

przedmioty = [Wartosciowy(4, 7, 'złoto'), Smiec(12, 60, 'śmieć')]
for i in przedmioty:
    print(i, '\n')

gracz = [Gracz(1, 1, []), Gracz(5, 5, [])]
for i in gracz:
    print('Nr gracza: ', gracz.index(i), '\n', i, '\n')


# gra
k = int(input('Podaj nr gracza z listy powyżej'))
while input('Jeżeli chcesz zakończyć, naciśnij "s"') != 's':
    gracz[k].move_n_pick(int(input('Podaj przesunięcie "x"')), int(input('Podaj przesunięcie "y"')))

print(gracz[k])
gracz[k].display()

# zapis najświeższych danych gry
dane_1 = [pokoje, przedmioty, gracz]
plik_zapisu = 'plik_2.dat'

plik_zapisz(dane_1, plik_zapisu)
plik_czytaj(plik_zapisu)
for i in dane_1:
    print(i)


sleep(2)
