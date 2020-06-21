

# Es una búsqueda binaria, se le han de pasar enteros inicio (x),
# longitud del segmento, una funcion para medir la distancia y el
# maximo error admitido
def busqueda(inicio, rango, funcion, error):
    if rango <= error:
        return inicio

    f1 = funcion(inicio + rango / 4)
    f2 = funcion(inicio + rango * 3 / 4)

    if (f1 <= f2):  # Mitad inferior
        return busqueda(inicio, rango / 2, funcion, error)
    else:  # Mitad superior
        return busqueda(inicio + rango / 2, rango / 2, funcion, error)


# Es una función lineal por trozos.
def funcion(x):
    inicio, fin, minimo = [0, 0], [100, 0], [60, -100]
    m1 = (minimo[1] - inicio[1]) / (minimo[0] - inicio[0])
    m2 = (minimo[1] - fin[1]) / (minimo[0] - fin[0])

    if inicio[0] <= x <= minimo[0]:
        return (x - inicio[0]) * m1 + inicio[1]
    elif minimo[0] < x <= fin[0]:
        return (x - minimo[0]) * m2 + minimo[1]


# Vamos a probar una función lineal a trozos entre entre [0,0] y [0,100],
# con mínimo en [30, -100], véase funcion(x).
print(busqueda(0, 100, funcion, 0.1))
