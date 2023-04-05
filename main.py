import math
import random

# lista = [1,2,3,4]
#
# # dodać element na wybrane miejsce
# lista.insert(5,9)
# print(lista, "dodaję 9 na 5 miejsce")
#
# # dodać kilka elementów
# lista2=[1,2,3]
# lista.extend(lista2)
# print(lista, "dodaję 3 elementów na lista")
#
# # usunąć element z listy o danej pozycji
# lista.pop(3)
# print(lista, "usuwam 3 element z listy o danej pozycji")
#
# # usunąć element z listy o danej wartości
# lista.remove(1)
# print(lista, "usuwam 1 element z listy o danej wartości")
#
# # odwrócić listę
# lista.reverse()
# print(lista, "odwracam listę")
#
# # posortować listę
# lista.sort()
#
# print(lista, "sortuję listę")
#
# slownik = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# print('a={},b={}'.format(12,12))
#
# a = int(input('a: '))
# b = int(input('b: '))
# if a > b:
#     print('a>b')
# elif a < b:
#     print('a<b')
# else:
#     print('a=b')


# for element in zbior:
# print(element)
# else:
# print('Nie ma takiego elementu')


# for i in range(len(lista)):
#     print(lista[i])
# else:
#     print('Nie ma takiego elementu')
# licznik = 0
#
# # while licznik != len(lista):
# #     print(lista[licznik])
# #     licznik += 1
# liczby = [3,2,5,6,2]
# a = int(input('a: '))
# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#         break
#     licznik += 1
# i = 0
# liczby = [1,2,2,2,2,4,3,2]
# while i < len(liczby):
#     if liczby[i] == 2:
#         liczby.remove(2)
#         print(liczby)
#     else:
#         i+=1
#
# #Zadania 1
# print(pow(math.e,10))
# print(math.log1p(5 + (math.sin(8)**2) ** 1/6))
# print(math.trunc(3.55))
# print(math.ceil(4.80))
#
# #Zadanie 2
# a = 'JAKUB'
# b = 'KOSIDOWSKI'
# print(a.capitalize(),b.capitalize())
#
# #Zadanie 3
# song = 'gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang '
# print(song.count('gang'))
#
# #Zadanie 4
# word = 'jakieś losowe słowa z literkami'
# print(word[1],word[-1])
#
# #Zadanie 5
# print(word.split())
#
# #Zadanie 6
# utrzyma = 2.43
# struna = 'słowo'
# szesnastkowe = 0x000214
# print('{:f}'.format(utrzyma),'{:s}'.format(struna),'{:x}'.format(szesnastkowe))
#
# #Zadanie 7
# lista = ['kosz', 'nożna', 'ręczna', 'siata']
# lista.reverse()
# lista.append(['paletki','yoga'])
# print(lista)
#
# #Zadanie 8
# slownik = {'itd':'i tak dalej','etc':'et cetera','PiS':'złodzieje'}
# print(slownik)
#
# #Zadanie 9
# gierki = {'Skyrim':'Bethesda','CS:GO':'Valve','League of Legends':'Riot'}
# print(gierki)
#
# #Zadanie 10
# user = input("Napisz mi jakieś ładne zdanie. PROSZĘ!!!!! \n")
# print(user.count('a'))
#
# #Zadanie 11
# x = int(input('Daj jakąś liczbę byczq '))
# y = int(input('Daj jakąś liczbę byczq '))
# z = int(input('Daj jakąś liczbę byczq '))
# print(max(x,y,z))
#
# #Zadanie 12
# liczby = [3,2.4,744,8.224]
# for i in liczby:
#     print(pow(i,2))
#
# #Zadanie 13
# c = []
# itr = 0
# while itr < 10:
#     k = int(input("liczba jakaś "))
#     itr+=1
#     if k%2 == 0:
#         c.append(k)
# print(c)


# LABOREK DRUGI

# Zadanie 1
a = [x - 1 for x in range(1, 11)]
b = [4 ** i for i in range(8)]
c = [y for y in b if y % 2 == 0]
print('Zadanie 1 ', a, b, c)

# Zadanie 2
lista1 = []
for i in range(9):
    a = random.randint(0, 482)
    lista1.append(a)
lista2 = [h for h in lista1 if h % 2 == 0]
print('Zadanie 2 ', lista1, lista2)

# Zadanie 3
zakupy = {'kalafiory': 'kg', 'śrubki': 'szt', 'mleko': 'l'}
sztuki = [j for j, i in zakupy.items() if i == 'szt']
print('Zadanie 3 ', sztuki)


# Zadanie 4


def pita(a, b, c):
    if ((a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (
            b ** 2 + c ** 2 == a ** 2)) and a > 0 and b > 0 and c > 0:
        return print("Zadanie 4 Trójkąt jest prostokątny")
    else:
        return print("Zadanie 4 Trójkąt nie jest prostokątny")


pita(2, 4, 3)


# Zadanie 5


def trapez(a, b, h):
    return print('Zadanie 5 ', ((a + b) * h) / 2)


trapez(2, 5, 7)


# Zadanie 6


def iloczyn_ciagu(a=1, b=4, ile=10):
    for i in range(ile + 1):
        a *= b
    return a


print('Zadanie 6 ', iloczyn_ciagu())


# Zadanie 7


def ciag(*args):
    if args == 0 or args == 1 or args == 2 or len(args) > 3:
        return 0
    else:
        a = args[0]
        b = args[1]
        ile = args[2]
        for i in range(ile + 1):
            a *= b
        return a


print('Zadanie 7 ', ciag(2, 4, 7))


# Zadanie 8


def value(**arg):
    suma: float = 0
    produkt = []
    for i in arg:
        suma += arg[i]
        produkt.append(i)
    return suma


print('Zadanie 8 ', value(koszt=2.3, koszt1=5))

# Zadanie 9
a = int(input("Podaj liczbę dodatnią "))
try:
    wynik = math.sqrt(a)
    print('Zadanie 9 ', wynik)
except:
    print('nie ma pierwiastka z liczby ujemnej')

# lab 4
# Zadanie 1
with open('new.txt', 'w', encoding='utf-8') as plik:
    for i in range(5):
        h = random.randint(0, 30)
        h *= 2
        plik.write(str(h))

# Zadanie 2
with open('new.txt', 'r', encoding='utf-8') as txt:
    for i in txt:
        print(i)

# Zadanie 3
with open('new.txt', 'a+', encoding='utf-8') as plik:
    x = 'jakieś linie'
    y = 'i kolejne'
    z = 'i następne'
    plik.write(x)
    plik.write(y)
    plik.write(z)
    print(plik.readlines())


# Zadanie 4


class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jedn):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jedn = cena_jedn

    def wyświetl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jedn)

    def ile_produktu(self):
        return self.ilosc + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jedn


kalafior = NaZakupy('Kalafior', 5, 'kg', 3.64)


# Zadanie 5
class Ciągi_Arytmetyczne:
    pierwszy_wyraz = 2
    różnica = 2
    wyrazy = []

    def __init__(self, pierwszy_wyraz, ostatni_wyraz, różnica, długość_ciągu):
        self.pierwszy_wyraz = pierwszy_wyraz
        self.ostatni_wyraz = ostatni_wyraz
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu

    def wyświetl_dane(self):
        print(self.pierwszy_wyraz, self.ostatni_wyraz, self.różnica, self.długość_ciągu)

    def pobierz_elementy(self):
        self.ostatni_wyraz = int(input("Podaj wartość elementu ciągu: "))

        print(self.ostatni_wyraz)

    def pobierz_parametry(self):
        pierwszy_wyraz = int(input("Podaj pierwszy wyraz ciągu arytmetycznego: "))
        różnica = int(input("Podaj różnicę ciągu arytmetycznego: "))
        długość_ciągu = int(input("Podaj długość ciągu arytmetycznego: "))
        print(pierwszy_wyraz, różnica, długość_ciągu)

    def policz_sumę(self):
        suma = ((self.pierwszy_wyraz + self.ostatni_wyraz) / 2) * self.długość_ciągu
        return suma

    def policz_elementy(self):
        if self.pierwszy_wyraz is not None and self.różnica is not None:
            n = 0
            for i in self.wyrazy:
                n = 1
        return n


# Zadanie 6
class Robaczek:
    krok = 10

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def w_górę(self, ile_kroków):
        self.y += ile_kroków * self.krok

    def w_dol(self, ile_kroków):
        self.y -= ile_kroków * self.krok

    def w_prawo(self, ile_kroków):
        self.x += ile_kroków * self.krok

    def w_lewo(self, ile_kroków):
        self.x -= ile_kroków * self.krok

    def pokaz_gdzie_jestes(self):
        print(x, y)

# 29.03.2022
