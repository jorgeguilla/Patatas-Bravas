import random


def robot(botellas: list, tapones: list):
    izdaT, izdaB, dchaT, dchaB = [], [], [], []
    tapon = tapones[0]
    botella = 0
    for i in range(len(tapones)):
        if botellas[i] == tapon:
            botella = botellas[i]
            print(tapon, "con", botella)
            break
    tapones.remove(tapon)
    botellas.remove(botella)

    for i in range(len(tapones)):
        if tapones[i] < botella:  # Dividimos tapones
            izdaT.append(tapones[i])
        else:
            dchaT.append(tapones[i])

        if botellas[i] < tapon:  # Dividimos botellas
            izdaB.append(botellas[i])
        else:
            dchaB.append(botellas[i])

    if len(izdaB) > 0:
        robot(izdaB, izdaT)
    if len(dchaB) > 0:
        robot(dchaB, dchaT)


tapones = [random.randint(0, 100) for i in range(70)]
botellas = tapones.copy()
botellas.sort(key = lambda l : random.randint(0,10)) #tapones desordenada

robot(tapones, botellas)