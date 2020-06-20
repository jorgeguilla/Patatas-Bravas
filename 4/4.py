'''
Problema 4.4:

Alí Babá ha conseguido entrar en la cueva de los ciento un mil ladrones, y
ha llevado consigo su camello junto con dos grandes alforjas; el problema es
que se encuentra con tanto tesoro que no sabe ni qué llevarse. Los tesoros
son joyas talladas, obras de arte, cerámica... es decir, son objetos únicos que
no pueden partirse ya que entonces su valor se reduciría a cero.
Afortunadamente los ladrones tienen todo muy bien organizado y se
encuentra con una lista de todos los tesoros que hay en la cueva, donde se
refleja el peso de cada pieza y su valor en el mercado de Damasco. Por su
parte, Alí sabe la capacidad de peso que tiene cada una de las alforjas.
Diseñar un algoritmo que, teniendo como datos los pesos y valor de las
piezas, y la capacidad de las dos alforjas, permita obtener el máximo
beneficio que podrá sacar Alí Babá de la cueva de las maravillas.
'''


# Devuelve los mejores objetos a llevar en una bolsa
# Input: p1: capacidad bolsa; elementos: Lista de [peso_i, valor_i]
# Output:  lista con [peso_i, valor_i]
def ladron(p1, elementos):
    n = len(elementos)

    # Rellena la tabla de casos posibles
    tabla = [[0 for i in range(p1 + 1)] for e in range(n)]
    for i in range(p1 + 1):
        for e in range(n):
            v1 = 0 if (e == 0) else tabla[e - 1][i]
            v2 = 0

            if i >= elementos[e][0]:
                v2 += elementos[e][1]
                if e > 0:
                    v2 += tabla[e - 1][i - elementos[e][0]]
            tabla[e][i] = max(v1, v2)

    # Leyendo la tabla averigua los objetos escogidos.
    res = []
    n -= 1
    while p1 > 0 and n>=0:
        abajo = tabla[n - 1][p1] if n > 0 else 0
        if abajo == tabla[n][p1]:
            n -= 1

        else:
            aux = 0 if (n < 0 or p1 < elementos[n][0]) else tabla[n - 1][p1 - elementos[n][0]]
            peso = elementos[n][0]

            if aux + elementos[n][1] == tabla[n][p1]:
                res.append(elementos[n].copy())
                elementos.pop(n)

            p1 -= peso
            if n > 0:
                n -= 1

    return res


# ============================ENTRADA====================================
p1 = int(input("Capacidad de la bolsa 1: "))
p2 = int(input("Capacidad de la bolsa 2: "))

n = int(input("Cantidad de objetos: "))

elementos = []
for i in range(n):
    elementos.append(
        [int(input("Peso del objeto " + str(i + 1) + ": ")), int(input("Valor del objeto " + str(i + 1) + ": "))])

# Se analizan dos escenarios en función de cual de las bolsas se carga en primer lugar.
elem2 = elementos.copy()

b1 = ladron(p1, elementos)
b2 = ladron(p2, elementos)

b3 = ladron(p2, elem2)
b4 = ladron(p1, elem2)

# Se computa cuál de los dos tiene mejor resultado.
p1 = 0
for i in b1:
    p1 += i[1]
for i in b2:
    p1 += i[1]

p2 = 0
for i in b3:
    p2 += i[1]
for i in b4:
    p2 += i[1]

# ==========================SALIDA=========================
if p1 > p2:
    print("Bolsa 1: " + str(b1) + "\nBolsa 2: " + str(b2))
else:
    print("Bolsa 1: " + str(b4) + "\nBolsa 2: " + str(b3))
