import re

#Entrada: dos strings
#Salida: lista con indices de ocurrencias de s1 en s2
def apariciones(s1, s2):
    return [m.start() for m in re.finditer(s1, s2)]

s1 = input("Cadena 1: ")
s2 = input("Cadena 2: ")

#Las subcadenas se almacenan de la forma [indice_s1, indice_s2, size]
#Se comienza con el producto cartesiano de apariciones de 1s de ambas cadenas (substring más pequeña).
unos = [[i,j,1] for i in apariciones("1", s1) for j in apariciones("1", s2)]
ceros =  [[i, j, 1] for i in apariciones("0", s1) for j in apariciones("0", s2)]

subs = unos + ceros
s = 2
res = i = 0
#Se va ampliando la longitud de las cadenas, las que no son substrings de N+1 caracteres
#se desechan.
while len(subs) > 0:
    res = subs[0].copy()
    while i < len(subs):
        try:
            t = subs[i]
            if s1[t[0] + t[2]] == s2[t[1] + t[2]]:
                subs[i][2]+=1
                i+=1
            else:
                subs.pop(i)
        except:
            subs.pop(i)
    i=0
    s+=1

print(s1[res[0]:res[0]+s])