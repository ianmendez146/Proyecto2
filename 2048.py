 ##proyecto2##
#Ian Méndez
#24000146 - C
 
import random 
import math 
import re 

def bienvenida():
    print("Bienvenido a nuestro Videojuego :D")

def modo_de_juego():
    print("Que tipo de modo de juego te gustaría? ")
    modo_de_juego_ele= input("|| 1. Individual || 2. 1 VS 1 || 3. VS IA || 4. No queiro jugar || : ") ##Cual es el tipo de modo de juego quiera el usuario
    ##modo_de_juego_ele = input( "1 , 2 , 3 : ")
    if modo_de_juego_ele == "1":
        print("Juega como lobo Solitario entonces :D ")
    elif modo_de_juego_ele == "2":
        print("WOOOW TIENES AMIGOS!? ")
    elif modo_de_juego_ele == "3":
        print("Humano VS Maquina!!!!! ")
    elif modo_de_juego_ele == "4":
        print(" Pues no pues, te pierdes de un buen Juego... ADIOS!!!")
        print(" Nos vemos hasta la proxima!! :´D")

##def despedida():
  ##  print("Nos vemos hasta la proxima!! :´D")

def main():
    bienvenida()
    modo_de_juego()
   # despedida()

if __name__ == "__main__":
    main()