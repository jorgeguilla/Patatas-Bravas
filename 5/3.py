'''
Autores: Jorge Guillamón Y Miguel Ángel Guerrero

Problema 3
Se tiene un número de Tam cifras almacenado en una cadena de texto; por
ejemplo, la cadena dato = 1151451.
Diseñar un algoritmo que mediante técnicas de Backtracking encuentre, de
la manera más eficiente posible, todos los números distintos de N cifras que
puedan formarse con los números de la cadena sin alterar su orden relativo
dentro de la misma.
Por ejemplo, si N = 4, son números válidos 1151, 1511 y 1541, pero no 4551
o 5411 que aunque pueden formarse con los dígitos de la cadena dato
implican una reordenación.
'''



original = input("Cadena: ")
n = int(input("Número de caracteres de los resultados: "))

#Se usara una pila en lugar de recursividad
pila = [[]]
resultado = set() #Para eliminar resultados duplicados


while len(pila) != 0:
    actual = pila.pop()
    ultimo = -1 if len(actual) == 0 else actual[-1] #Correccion de caso inicial
    for i in range(ultimo +1, len(original) - (n - len(actual)) + 1): #Desde la pos actual hasta la ultima que permita formar mas cadenas en el futuro
        nuevo = actual.copy()
        nuevo.append(i)
        if(len(nuevo) == n): #Tenemos un nuevo resultado
            res = ""
            for i in nuevo:
                res+=original[i]
            resultado.add(res)
        else: #Hay que seguir elaborando
            pila.append(nuevo)

print(str(len(resultado)) + " resultados distintos: " + str(resultado))

