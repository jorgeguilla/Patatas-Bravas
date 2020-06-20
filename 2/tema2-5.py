def dijkstra ( matriz ,	nodo_destino ):
        n = len( matriz )
        costes = [ float ("inf") for i in range(n)]
        caminos = [[] for i in range(n)]

        #Configuracion i n i c i a l
        costes [0] = 0
        caminos [0] = [0]
        frontera = [0]
        actual = 0

        #Resultado hallado o no existe
        while( actual!=nodo_destino or not frontera ):
                actual = frontera [costes.index (min(costes) )]
                frontera.remove(actual)
                camino_actual = caminos[actual]

                for i in range(n):
                        if matriz [ actual ] [ i ] != -1: #Si el nodo es accesible
                                 if costes [ i ] == float ("inf" ): #No se ha visitado
                                        frontera . append( i )
                                        costes [ i ] = costes [ actual ] + matriz [ actual ] [ i ]
                                        caminos [ i ] = caminoactual.copy()
                                        caminos [ i ].append(i)
                            #Coste mejorable
                                 elif costes [ i ] > costes[actual] + matriz [actual] [i] :
                                    costes[i] = costes[actual] + matriz [actual] [i]
                                    caminos [ i ] = camino_actual.copy ()
                                    caminos [ i ].append(i)

        print(costes[nodo_destino], caminos [ nodo_destino ])
