""" Programa para juegos TOY & JOY"""
encestadas=int(input())
def habilidad(x):   
  puntaje_base=4
  puntos_habilidad=puntaje_base+2*x
  return puntos_habilidad
def calificacion_final(x,y):
    puntuacion_final=(y+encestadas)/5
    return puntuacion_final
def calificacion_participante():
    y=habilidad(encestadas)
    puntuacion_final=calificacion_final(encestadas,y)
    print(encestadas,y,int(puntuacion_final))
    if puntuacion_final>50:
      print("Cuatro")
    else:
        if puntuacion_final>30:
            print("Tres")
        else:
              if puntuacion_final>20:
                print("Dos")
              else:
                  print("Uno")
calificacion_participante()

