#lista_compras_partes_computador_version2
import ast
def compra(diccionario):
  diccionario=ast.literal_eval(diccionario)
  lista_producto_deseado=[x for x in input("Ingrese los codigos de los productos deseados separados con un espacio").split()]
  producto=[]
  precio=0
  for k in lista_producto_deseado:
    if k in diccionario:
      precio+=diccionario[k]
      producto.append(k)
  precio=str(precio)
  precio="\n"+precio
  print(precio)
  for x in producto:
    print(x,end=(" "))

compra(diccionario=input())
