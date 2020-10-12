from random import randint

print ("JUEGO DE DADOS")
dado1=randint(1,6)
dado2=randint(1,6)
suma =dado1+dado2
 
otra="S"
while otra=="S" or otra=="s":
 print("El primer dado vale: ",dado1)
 print("El segundo dado vale: ",dado2)
 print("La suma de los dados es: ",suma)
 otra=input("¿Quieres volver a jugar?")
