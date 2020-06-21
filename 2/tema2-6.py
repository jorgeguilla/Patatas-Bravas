import random


def shrek(longitudes):
    suma = 0
    while len(longitudes) != 1:
        longitudes.sort()  # Toca ordenar a cada vuelta, los elementos cambian!
        tramo = sum(longitudes[:2])
        print(longitudes[:2], "=", tramo)
        longitudes = longitudes[2:]
        longitudes.append(tramo)
        suma += tramo

    print("El coste total es de", suma)


ejemplo = [random.randint(1, 10) for i in range(8)]
print("Tramos:", ejemplo)

shrek(ejemplo)
