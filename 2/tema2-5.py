from math import inf


# Entrada: casilla de salida, casilla de llegada, matriz de caminos
# Salida: Lista con casillas que hay que recorrer para llegar a la meta
def dijkstra(salida, llegada, matriz):
    frontera = [[[salida], 0]]  # Almacena [camino, coste]
    n = len(matriz)
    conocidos = set()
    while len(conocidos) < n and len(frontera) > 0:
        [ruta, coste] = frontera.pop()
        actual = ruta[-1]
        if actual == llegada:  # Premio!
            return [ruta, coste]

        if actual in conocidos:  # Si ya hemos pasado por aquí, andamos en círculos
            continue
        else:
            conocidos.add(actual)

        for i in range(n):
            if matriz[actual][i] == inf or actual == i:  # Si es innacesible o es el propio nodo
                continue
            frontera += [[ruta + [i], coste + matriz[actual][i]]]

        frontera.sort(key=lambda l: l[1], reverse=True)  # Los caminos más bajos al final, (sacamos con pop)

    return False


matriz = [[0, 42, 5, 1],
          [3, 0, inf, inf],
          [inf, 3, 0, 7],
          [inf, inf, inf, 0]]

matriz2 = [[inf, 4, inf, inf, inf, inf, inf, 8, inf],
           [4, inf, 8, inf, inf, inf, inf, 11, inf],
           [inf, 8, inf, 7, inf, 4, inf, inf, 2],
           [inf, inf, 7, inf, 9, 14, inf, inf, inf],
           [inf, inf, inf, 9, inf, 10, inf, inf, inf],
           [inf, inf, 4, 14, 10, inf, 2, inf, inf],
           [inf, inf, inf, inf, inf, 2, inf, 1, 6],
           [8, 11, inf, inf, inf, inf, 1, inf, 7],
           [inf, inf, 2, inf, inf, inf, 6, 7, inf]
           ]

res = dijkstra(0, 1, matriz)

if res:
    print("Camino:", res[0], "\nCoste: ", res[1])
else:
    print("No hay camino!")
