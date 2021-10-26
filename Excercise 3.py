#Boleta alcaldia
def sorteo_boleta():
  primer_digito=input("Ingrese los primeros digitos separado por un espacio:").upper()#leo la entrada, y la estandarizo a mayuscula
  digito=[x for x in primer_digito.split()]#Rompo la cadena donde haya algun espacio(), luego la almaceno en una lista
  m=[""]
  digitos_viendo=[]
  contador=0
  acumulado=0
  lista_contador=[]
  for i in digito:
    acumulado+=1
    if i!=m[0]:
      m[0]=i
      digitos_viendo.append(i)
      if contador!=0:
        lista_contador.append(contador)
      contador=1
      if acumulado==len(digito):
        lista_contador.append(contador)
    else:
      contador+=1
      if acumulado==len(digito):
        lista_contador.append(contador)
  print(digitos_viendo)
  print(lista_contador)

sorteo_boleta()
