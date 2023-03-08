lista = [1,2,3,4]

# dodać element na wybrane miejsce
lista.insert(5,9)
print(lista, "dodaję 9 na 5 miejsce")

# dodać kilka elementów
lista2=[1,2,3]
lista.extend(lista2)
print(lista, "dodaję 3 elementów na lista")

# usunąć element z listy o danej pozycji
lista.pop(3)
print(lista, "usuwam 3 element z listy o danej pozycji")

# usunąć element z listy o danej wartości
lista.remove(1)
print(lista, "usuwam 1 element z listy o danej wartości")

# odwrócić listę
lista.reverse()
print(lista, "odwracam listę")

# posortować listę
lista.sort()

print(lista, "sortuję listę")

slownik = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('a={},b={}'.format(12,12))

a = int(input('a: '))
b = int(input('b: '))
if a > b:
    print('a>b')
elif a < b:
    print('a<b')
else:
    print('a=b')