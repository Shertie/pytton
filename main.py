import math


#Zestaw A


print("Zestaw A")
#Zadanie 1


print("zadanie 1")
try:
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    wynik = a ** 2 + b ** 2 + 2 * a * b
    with open("zestaw_A.txt", "w") as f:
        f.write(str(wynik))
except ValueError:
    print("Nieprawidłowa wartość ")
print(wynik)


#Zadanie 2


print("Zadanie 2")
lista1 = [1,3,5,6,3]
lista2 = [2,5,7,4,2]
def suma(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        element = lista1[i] + lista2[i]
        lista3.append(element)
    print(lista3)
suma(lista1, lista2)

#Zadanie 3


print("Zadanie 3")
tekst = 'lorem ipsum dolor sit amet, consectetur adip eu fugiat nulla facilisis justo eu fugiat nulla facilisis justo eu fugiat nulla facilisis justo eu fugiat nulla facil  is justo eu fugiat nulla fac'

with open('tekst.txt', 'r', encoding='utf8') as f:
    rf = f.read()
    x = ''
    y = 0
    rf = rf[99:135]
    for i in rf:
        if i.isupper():
            y += 1
            x += i
    if y == 0:
        print("Error 404 Page not found")
    else:
        print(x, y)


#Zadanie 4

print("Zadanie 4")
list = [3,6,8,7,4,1,2]
a = 2
lista = [x for x in list if x > a]
print(lista)


#Zadanie 5

print("Zadanie 5")
num = pow(math.e**3 + math.cos(39)**2, 1/5) + pow(2/7, 3) + math.pi
print(num)


#Zestaw B


print("Zestaw B")
#Zadanie 1

print("Zadanie 1")
with open("tekst.txt", 'r',encoding='utf-8')as f:
    fr = f.read()
    fr = fr[70:110]
    itr = 0
    for i in fr:
        if fr.find(i) == 'A':
            itr += 1
    if itr == 0:
        print("Ni ma")
    else: print(itr)


#Zadanie 2

print("zadanie 2")
l = [1,4,6,3,7.1,8,9.4,6.3]
l1 = [x for x in l if isinstance(x, float)]
print(l1, '\n', l)



#Zadanie 3


print("zadanie 3")
listek = [1,2.4,5.3342]
def suma(listek):
    a = listek[0]
    for i in range(len(listek)):
        listek.append(a+listek[i])
    return listek

print(suma(listek))


#Zadanie 4

print("Zadanie 4")
wynik = math.sin(56)**2 + pow((4**2)/25 + math.log(85, 3), 1/4)
print(round(wynik, 2))

#Zadanie 5

print("Zadanie 5")
try:
    n = int(input("Podaj liczbę całkowitą: "))
    suma = 0
    for i in range(n):
        suma += i+1
    with open("zadanie5.txt", "w") as f:
        f.write(str(suma))
except ValueError:
    print("Złe wartośći byczq ")

