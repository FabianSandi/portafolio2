#Función: devolver indices
#Entrada: 2 listas, la primera con los elementos, la segunda con los elementos que se deben encontrar en la lista 1
#Salida:los indices de los elementos de la lista 1 que indica la lista 2
#Restricción: deben ser listas exclusivamente, y no pueden ser listas vacias 
def devolverindices(lista1, lista2):
    if isinstance(lista1, list) and isinstance(lista2,list):
        return devolveraux(lista1,lista2,[],0)
    else:
        return ('Error en la entrada')
def devolveraux(lista1,lista2,resultado,sumatoria):
    if lista1==[] and lista2==[]:
        return resultado
    elif lista1[0]==lista2[0]:
        return devolveraux(lista1[1:],lista2[1:],resultado+[sumatoria],sumatoria+1)
    else:
        return devolveraux(lista1[1:],lista2,resultado,sumatoria+1)


