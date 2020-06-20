def	robot (botellas:list,tapones:list):
        izdaT = [ ]
        izdaB = [ ]
        dchaT = [ ]
        dchaB = [ ]
        tapon = tapones [0]
        botella = 0
        for	i	in range ( len ( tapones )):
	            if	botellas [ i ] == tapon :
                        botella = botellas [ i ]
        tapones.remove(tapon)
        botellas.remove( botella )

        for	i	in range ( len ( tapones )):
                if	tapones [i] < botella:
                        izdaT.append(tapones [i])
                else:
                        dchaT.append(tapones [i])

                if	botellas [i] < tapon:
                        izdaB.append(botellas [i])
                else:
                        dchaB.append( botellas [ i ])

        if ( len (izdaB)>0): robot (izdaB , izdaT)
        if ( len (dchaB)>0): robot (dchaB , dchaT)
