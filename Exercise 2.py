#intento 2
def juego_cine():
  empleado1=input("Ingrese filas empleado1 :")
  empleado1=empleado1.upper()
  empleado2=input("Ingrese filas empleado2 :")
  empleado2=empleado2.upper()
  filas_preferencia=input("Ingrese filas al final de dia :")
  filas_preferencia=filas_preferencia.upper()
  ventaja1,ventaja2,tablero=0,0,""
  for i in filas_preferencia:
    if i in empleado1:
      ventaja1+=1
    if i in empleado2:
      ventaja2+=1
    if ventaja1>ventaja2:
        tablero+="E"
    elif ventaja1<ventaja2:
        tablero+="T"
    else:
        tablero+="N"
  print(tablero)

juego_cine()
