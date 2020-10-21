def devolverindicesv2(lista,lista2):
    if isinstance(lista, list) and isinstance(lista2,list):
        return devolverv2aux(lista,0,lista2,[])
    else:
        return ("Error en la entrada")
def devolverv2aux(lista,a,lista2,res):
    if lista2==[]:
        return res
    else:
        if lista[a:]==[]:
            return devolverv2aux(lista, 0,lista2[1:], res)
        else:
            if lista[a]==lista2[0]:
                return devolverv2aux(lista, a+1,lista2, res + [a])
            else:
                return devolverv2aux(lista, a+1,lista2, res)
