# Partes
'''
Podemos observar como se define una funcion, como se usa el for para recorrer los elementos de una lista
, como llamar un elmento de una lista y como añadir un nuevo elemnto a esta.
'''
def clasificaciones(clasificacion):
    lista_clasificada = []
    for i in clasificacion:
        if i not in lista_clasificada:
            lista_clasificada.append(i)
    return (lista_clasificada)


def mefaltandelapartes(numeropartesf, listacf, cf_especifica):
    lista_num_clasificacion = []
    for i in numeropartesf:
        if cf_especifica == listacf[i]:
            lista_num_clasificacion.append(i)
    return lista_num_clasificacion


def notengopartes(partes_distribuidor, partestienda):
    lista_partes_compra = []
    for i in partes_distribuidor:
        if i not in partestienda:
            lista_partes_compra.append(i)
    return lista_partes_compra


def partesacambiar(partes_otratienda, partes_lamaquina):
    lista_deseo_otratienda = []
    lista_deseo_lamaquina = []
    for i in partes_lamaquina:
        if i not in partes_otratienda:
            lista_deseo_otratienda.append(i)
    for i in partes_otratienda:
        if i not in partes_lamaquina:
            lista_deseo_lamaquina.append(i)
    return min(len(lista_deseo_otratienda), len(lista_deseo_lamaquina))


