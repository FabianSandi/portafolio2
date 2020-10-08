
#Ejercicios de listas, recibe una lista que se salta los negativos
def partirLista(lista):
    return PartirListaAux(lista,[],[])
def PartirListaAux(lista,sublista,resultado):
    if lista==[]:
        return resultado + [sublista]
    elif lista[0]>=0:
        return PartirListaAux(lista[1:],sublista+[lista[0]],resultado)
    else:
         return PartirListaAux(lista[1:],[],resultado + [sublista])

def partirListav2(lista):
    return PartirListaAuxv2(lista,[],[])
def PartirListaAuxv2(lista,sublista,resultado):
    if lista==[]:
        if sublista==[]:
            return resultado
        else:
            return resultado + [sublista]
    elif lista[0]>=0:
        return PartirListaAuxv2(lista[1:],sublista+[lista[0]],resultado)
    else:
         return PartirListaAuxv2(lista[1:],[],resultado + [sublista])

def partirListav3(lista):
    return PartirListaAuxv3(lista,[],[],[])
def PartirListaAuxv3(lista,sublista1,sublista2,resultado):
    if lista==[]:
        return resultado + [sublista1] + [sublista2]
    elif lista[0]>=0:
        return PartirListaAuxv3(lista[1:],sublista1+[lista[0]],sublista2,resultado)
    else:
         return PartirListaAuxv3(lista[1:],[],sublista2+[lista[0]],resultado + [sublista1])
