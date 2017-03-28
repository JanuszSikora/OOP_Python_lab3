from time import sleep
import pickle


class Comment():
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return str(self.info())

    def info(self):
        self.informacja = 'Użytkownik: ', self.name, 'Komentarz: ', self.content
        return self.informacja


class User(Comment):
    def __init__(self, name, content):
        super().__init__(name, content)

    def info(self):
        self.informacja = 'Użytkownik: ', self.name, 'Komentarz: ', self.content, 'edytor: ', self.editor
        return self.informacja


class User_regular(User):
    def __init__(self, name, content, editor = False):
        super().__init__(name, content)
        self.editor = editor


class Admin(User):
    def __init__(self, name, content, editor = True):
        super().__init__(name, content)
        self.editor = editor


# zapis obiektów do pliku
def plik_zapisz(dane, plik_zapisu, plik_zapisu_dl):
    plik = open(plik_zapisu, 'wb')
    k = 0
    for i in dane:
        pickle.dump(i, plik)
        k += 1
    plik.close()
    plik_dl = open(plik_zapisu_dl, 'wb')
    pickle.dump(k, plik_dl)
    plik_dl.close()


# odczyt obiektów z pliku
def plik_czytaj(plik_zapisu, plik_zapisu_dl):
    plik_dl = open(plik_zapisu_dl, 'rb')
    plik_dlug = pickle.load(plik_dl)
    plik_dl.close()
    plik = open(plik_zapisu, 'rb')
    for j in range(plik_dlug):
        dane_1.append(pickle.load(plik))
    plik.close()


# main
# Tworzenie obiektów
comment_user = []
comment_admin = []
users = []
admins = []

#comment_user.append(User_regular('user_1', ' Ala ma kota'))
#comment_user.append(User_regular('user_2', ' To kot ma Alę'))
#comment_user.append(User_regular('user_3', ' Nikt nie ma kogokolwiek'))
#for i in comment_user:
 #   users.append(i.name)

#comment_admin.append(Admin('admin_1', '  nieprawda'))
#comment_admin.append(Admin('admin_2', '  prawda'))
#comment_admin.append(Admin('admin_3', '  komentarz niedozwolony'))
#for i in comment_admin:
 #   admins.append(i.name)


# obsługa odczytu z pliku i częściowo zapisu; tylko ostatnia linia nieaktywna przy tworzeniu obiektów
dane_1 = []
plik_zapisu = 'plik_3.dat'
plik_zapisu_dl = 'plik_3_dl.dat'
plik_czytaj(plik_zapisu, plik_zapisu_dl) # przy odczycie danych z pliku nie #-ować

# ten moduł aktywny tylko przy odczycie z pliku
for i in dane_1:
    if i.editor == True:
        comment_admin.append(i)
        admins.append(i.name)
    else:
        comment_user.append(i)
        users.append(i.name)

for i in comment_user:
    print(i)

for i in comment_admin:
    print(i)

print(users,admins)

# rozpoznanie klasy usera i obsługa interakcji z użytkownikiem
print('Tu będziesz mógł/mogła wprowadzić swój komentarz')
user_type = input('Podaj nazwę użytkownika')
if user_type in admins:
    choice = int(input('Podaj, co chcesz zrobić: 1 - napisać swój komentarz, 2 - edytować komentarz innego użytkownika'))
    if choice == 1:
        comment_admin.append(Admin(user_type,input('Wprowadź komentarz: ')))
    elif choice == 2:
        for count, elem in enumerate(comment_user):
            print(count, elem)
        comment_to_edit = int(input('Z powyższej listy podaj nr komentarza, który chcesz zmienić: '))
        comment_user[comment_to_edit] = User_regular(comment_user[comment_to_edit].name, input('Wprowadź wersję komentarza po edycji: '))
    else:
        print('Ta opcja jest niedostępna')

elif user_type in users:
    comment_user.append(User_regular(user_type, input('Wprowadź komentarz: ')))
else:
    comment_user.append(User_regular(user_type, input('Wprowadź komentarz: ')))

dane_1 = []
for i in comment_user:
   dane_1.append(i)
for i in comment_admin:
   dane_1.append(i)

plik_zapisz(dane_1, plik_zapisu, plik_zapisu_dl)

for i in comment_user:
    print(i)

for i in comment_admin:
    print(i)

sleep(2)
