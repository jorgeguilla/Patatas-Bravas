def Prim (matriz) :
        n = len (matriz) #Una m a t r i z de nxn
        actual = 0
        visitados = [ 0 ]
        pila = [ ] #Manejar e l b a c k t r a c k i n g
        resultado = [[-1 for i in range ( n ) ] for e in range ( n ) ]

        while len ( visitados ) < n :
                coste = float ("inf")

                for i in range (len ( matriz) ) :
                        if matriz [actual ] [ i ] != -1 and i not in visitados and matriz [actual] [i] < coste:
                                coste = matriz [actual] [ i ]
                                siguiente = i
                if coste == float ("inf") : #S i nada , b a c k t r a c k i n g
                            actual = pila.pop ( )
                            if actual == 0 :
                                        print ("No se puede sacar el arbol")
                                        return matriz
                else: #S i se ha enc on t r a d o alg o , segu imos b a j an d o
                            resultado [actual] [siguiente] = coste #m a t r i z s i m e t r i c a
                            resultado [siguiente] [actual ] = coste

                            print ( str (actual) +"y" + str (siguiente) +
                                        "se han unido , coste :"+ str (coste))
                            visitados.append (siguiente)
                            pila.append(actual)
                            actual = siguiente
        return resultado
