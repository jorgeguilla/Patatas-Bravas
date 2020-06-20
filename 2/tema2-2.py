import random

def ordenar(lista):
    puntos = 0
    valor = lambda elem: elem[0] / elem[1]
    lista.sort(key=valor, reverse=True)
    return lista


ejemplo = []
for i in range(4):
    ejemplo.append([random.randint(0,100), random.randint(0,100)])

print("Sean los ficheros ([tasa, tamaño]):", ejemplo)
print("Su orden en el disco debería ser:", ordenar(ejemplo))