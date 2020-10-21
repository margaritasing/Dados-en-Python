import random
print ("JUEGO DE DADOS")
j1= input("Inserte el nombre del jugador uno: ")
j2= input("Inserte el nombre del jugador dos: ")

otra="S"
while otra=="S" or otra=="s":

   jugadoruno = random.randint(1,6)
   jugadordos = random.randint(1,6)
   print("El jugador",j1,"ha sacado : ", jugadoruno)
   print("El jugador",j2,"ha sacado : ", jugadordos)

   if jugadoruno==jugadordos:
        print ("Estan empatados")
        break
 
   elif jugadoruno>jugadordos:
         print ("El jugador",j1,"ha ganado")

   else:
          print ("El jugador",j2,"ha ganado")
     
   otra= input("¿Quieres jugar otra vez?")


