def minimomaximo (lista):
        minimo = maximo = lista [ 0 ]
        for elem in lista:
                if(elem > maximo):
                        maximo = elem
                elif (elem < minimo):
                        minimo = elem
        return [ minimo , maximo ]
