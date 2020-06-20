def busqueda(inicio,rango,funcion:Funcion,error):
        if (rango <= error ):
            print ( inicio )
            return

        f1 = funcion.calcula ( inicio + rango/4)
        f2 = funcion.calcula ( inicio + rango * 3/4)

        if ( f1 < f2 ): #Mitad inferior
                busqueda( inicio , rango /2 , funcion , error )
        else:           #Mitad superior
	            busqueda( inicio+rango /2 , rango /2 , funcion ,	error )