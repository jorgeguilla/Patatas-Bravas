def	transponer(origen,destino,fila,n_filas):
        if (n_filas == 1):
	        for	i	in range (len(origen[ 0 ])) :
                    destino [ i ] [fila] = origen [fila ] [ i ]
        else:
            n = int ( n_filas / 2)
            transponer (origen,destino,fila,n)
            transponer (origen,destino,fila+n,n_filas - n)