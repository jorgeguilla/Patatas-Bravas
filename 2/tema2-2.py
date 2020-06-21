import random


# Se trata de maximizar tasa/tamaño
def ordenar(lista):
    lista.sort(key=lambda elem: elem[0] / elem[1], reverse=True)
    return lista


ejemplo = [[random.randint(0, 100), random.randint(1, 100)] for i in range(6)]
print("Sean los ficheros ([tasa, tamaño]):", ejemplo)
print("Su orden en el disco debería ser:", ordenar(ejemplo))
