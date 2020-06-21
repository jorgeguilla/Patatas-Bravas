import random

def minimomaximo(lista):
    minimo = maximo = lista[0]
    for elem in lista:
        if elem > maximo:
            maximo = elem
        elif elem < minimo:
            minimo = elem
    return [minimo, maximo]


ejemplo = [random.randint(0,100) for i in range(20)]
print(ejemplo)
print(minimomaximo(ejemplo))