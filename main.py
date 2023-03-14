import math

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


#for element in zbior:
    #print(element)
#else:
    #print('Nie ma takiego elementu')


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

#Zadania 1
print(pow(math.e,10))
print(math.log1p(5 + (math.sin(8)**2) ** 1/6))
print(math.trunc(3.55))
print(math.ceil(4.80))

#Zadanie 2
a = 'JAKUB'
b = 'KOSIDOWSKI'
print(a.capitalize(),b.capitalize())

#Zadanie 3
song = 'gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang gucci gang '
print(song.count('gang'))

#Zadanie 4
word = 'jakieś losowe słowa z literkami'
print(word[1],word[-1])

#Zadanie 5
print(word.split())

#Zadanie 6
utrzyma = 2.43
struna = 'słowo'
szesnastkowe = 0x000214
print('{:f}'.format(utrzyma),'{:s}'.format(struna),'{:x}'.format(szesnastkowe))

#Zadanie 7
lista = ['kosz', 'nożna', 'ręczna', 'siata']
lista.reverse()
lista.append(['paletki','yoga'])
print(lista)

#Zadanie 8
slownik = {'itd':'i tak dalej','etc':'et cetera','PiS':'złodzieje'}
print(slownik)

#Zadanie 9
gierki = {'Skyrim':'Bethesda','CS:GO':'Valve','League of Legends':'Riot'}
print(gierki)

#Zadanie 10
user = input("Napisz mi jakieś ładne zdanie. PROSZĘ!!!!! \n")
print(user.count('a'))

#Zadanie 11
x = int(input('Daj jakąś liczbę byczq '))
y = int(input('Daj jakąś liczbę byczq '))
z = int(input('Daj jakąś liczbę byczq '))
print(max(x,y,z))

#Zadanie 12
liczby = [3,2.4,744,8.224]
for i in liczby:
    print(pow(i,2))

#Zadanie 13
c = []
itr = 0
while itr < 10:
    k = int(input("liczba jakaś "))
    itr+=1
    if k%2 == 0:
        c.append(k)
print(c)