import random

def minMax(lista, longi):
    if longi % 2 == 0:
        i = 2
        maximo = max(lista[0], lista[1])
        minimo = min(lista[0], lista[1])
    else:
        i = 1
        maximo = minimo = lista[0]
        while i < longi - 1:
            if lista[i] < lista[i + 1]:
                maximo = max(maximo, lista[i + 1])
                minimo = min(minimo, lista[i])
            else:
                maximo = max(maximo, lista[i])
                minimo = min(minimo, lista[i + 1])
                i += 2
    return [maximo, minimo]


lista = [random.randint(0,100) for i in range(20)]
print(lista)
long = len(lista)
numeros = minMax(lista, long)
print("Minimo: ", numeros[1], " Maximo: ", numeros[0])
