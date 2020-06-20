'''
Autores: Jorge Guillamón Y Miguel Ángel Guerrero

Problema 6
Se tiene la tabla de sustitución que aparece a continuación
    a   b   c   d
    =============
a|  b   b   a   d
b|  c   a   d   a
c|  b   a   c   c
d|  d   c   d   b

que se usa de la manera siguiente: en una cadena cualquiera, dos caracteres
consecutivos se pueden sustituir por el valor que aparece en la tabla,
utilizando el primer carácter como fila y el segundo carácter como columna.
Por ejemplo, se puede cambiar la secuencia ca por una b, ya que M[c,a]=b.
Implementar un algoritmo Backtracking que, a partir de una cadena no vacía
texto y utilizando la información almacenada en una tabla de sustitución M,
sea capaz de encontrar la forma de realizar las sustituciones que permite
reducir la cadena texto a un carácter final, si es posible.
Ejemplo: Con la cadena texto=acabada y el carácter final=d, una posible
forma de sustitución es la siguiente (las secuencias que se sustituyen se
marcan para mayor claridad): acabada  acacda  abcda  abcd  bcd
 bc  d.

'''

#Recibe una cadena de dos caracteres y devuelve una letra.
def sustituye(str0):
    matriz = [['b','b','a','d'],['c','a','d','a'],['b','a','c','c'],['d','c','d','b']]
    a = ord(str0[0]) - 97
    b = ord(str0[1]) - 97
    return matriz[a][b]

s = input("Introduce una cadena: ")

#¿Es la cadena reducible?
for i in s:
    if(ord(i) - 97 >  4): # Si mayores que 'd' en ASCII
        print("La cadena es irreducible con esta matriz")
        exit(-1)

pila = [s] #Usaremos una pila en memoria para backtracking
res = []

while len(pila) != 0:
    actual = pila.pop()
    for i in range(len(actual) - 1):
        aux = actual[:i] + sustituye(actual[i:i+2]) + actual[i+2:]
        if(len(aux) == 1): #Uno más al resultado
            res.append(aux)
        else: #Toca seguir reduciendo
            pila.append(aux)

print(str(len(res)) + " resultados: " + str(res))