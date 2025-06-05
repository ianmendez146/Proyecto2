#__________proyecto2___________#
#Ian Méndez        Emelie Perez
#24000146 - C      24000255 - D
 
import random 
import os
import math 
from copy import deepcopy 

n2 = random.randint(2,2)
n4 = random.randint(4,4)
n2 = random.randint(2,2)
n4 = random.randint(4,4)
nombreg = input("Ingrese su nombre: ")
def bienvenida():
    print("Bienvenido a nuestro Videojuego :D")
    
    print(f"bienvenido querido jugador {nombreg} ")


def modo_de_juego():
    print("¿Qué tipo de modo de juego te gustaría? ")
    while True:
        modo_de_juego_ele = input("|| 1. Individual || 2. 1 VS 1 || 3. VS IA || 4. Istrucciones || 5. No quiero jugar || : ").strip()

        if modo_de_juego_ele == "1":
            print("Juega como lobo Solitario entonces :D ")
            return modo_de_juego_ele
        elif modo_de_juego_ele == "2":
            print("WOOOW TIENES AMIGOS!? ")
            print("Este modo aún no está implementado.") 
        elif modo_de_juego_ele == "3":
            print("Humano VS Máquina!!!!! ")
            return modo_de_juego_ele
        elif modo_de_juego_ele == "4": 
            limpiar_consola()
            mostrar_instrucciones() 
            limpiar_consola()
        elif modo_de_juego_ele == "5":
            print("Pues no, te pierdes de un buen Juego... ¡ADIOS!!!")
            return modo_de_juego_ele
        else:
            print("Entrada inválida. Por favor, elige una opción válida.")


def crear_tablero ():
    return [[0] * 4 for _ in range(4)]

def dibujar_tablero(tablero):
    print("-" * 25) 
    for fila in tablero:
        print("|", end="")
        for celda in fila:
            if celda == 0:
                print(f"{' ':^5}|", end="")
            else:
                print(f"{celda:^5}|", end="")
        print()
        print("-" * 25)

def numeros_aleatorios(tablero):
    possicion_vacia = []
    for i in range(4):  ##filas
        for j in range(4):  ##Columnas 
            if tablero[i][j] == 0:
                possicion_vacia.append((i,j))  

    if len(possicion_vacia) == 0:
        return tablero
    
    i,j = random.choice(possicion_vacia)

    if random.random() < 0.9:
        tablero[i][j] = n2
    else:
        tablero[i][j] = n4
    return tablero

def tecla(tablero):
    while True:
        tecla = input("Para moverse usa  a, s, w, d, q . o flechas:  ").lower() 
        
        if tecla == "q":
            print("Si queires salir escribe enter  ") 
            input("¡¡¡PERDISTES!!! y sin jugar :/")
            
            break 

#################################################################
#####               ||||TECLAS "W" o "w"|||||||             #####
#################################################################

        elif tecla == "w":
            for j in range(4): ##columnas
                valor = []
                for i in range(4): ##filas 
                    if tablero[i][j] != 0:
                        valor.append(tablero[i][j])
                Li = 0 
                while Li < len(valor) -1:
                    if valor[Li] == valor[Li +1]:
                        valor[Li] *=2
                        valor[Li+1] = 0
                        Li += 2
                    else:
                        Li += 1
                valor = list(filter(lambda x: x!= 0, valor))
                valor += [0] * (4 - len(valor))
                for i in range(4):
                    tablero[i][j]=valor [i]

            tablero = numeros_aleatorios(tablero)   
            dibujar_tablero(tablero)

            print("arriba")

#################################################################
#####               ||||TECLAS "A" o "a"|||||||             #####
#################################################################

        elif tecla == "a":
            for i in range(4):
                valor=[]

                for j in range(4):
                    if tablero[i][j] != 0:
                        valor.append(tablero[i][j])
                Lia =0
                while Lia < len(valor) -1:
                    if valor[Lia] == valor[Lia +1]:
                        valor[Lia] *=2
                        valor[Lia+1] = 0
                        Lia += 2
                    else:
                        Lia += 1
                valor = list(filter(lambda x: x!= 0, valor))
                valor += [0] * (4 - len(valor))
                for j in range(4):
                    tablero[i][j] = valor [j]

            tablero = numeros_aleatorios(tablero)   
            dibujar_tablero(tablero)
                        
            print("izquierda")

#################################################################
#####               ||||TECLAS "S" o "s"|||||||             #####
#################################################################

        elif tecla == "s":
            for j in range(4):
                valor= []
                for i in range(3, -1, -1): ##filas pasa de abajo hacia arriba 
                    if tablero[i][j] != 0:
                        valor.append(tablero[i][j])
                li2 = 0
                while li2 < len(valor) - 1:
                    if valor[li2] == valor[li2 + 1]:
                        valor[li2] *= 2
                        valor[li2 + 1] = 0
                        li2 += 2
                    else:
                        li2 += 1
                valor = list(filter(lambda x: x != 0, valor))
                valor += [0] * (4 - len(valor))
                valor = valor[::-1]
                for i in range(4):
                    tablero[i][j] = valor[i]

            tablero = numeros_aleatorios(tablero)                      
            dibujar_tablero(tablero)
            print("atras")


#################################################################
#####               ||||TECLAS "D" o "d"|||||||             #####
#################################################################

            #TECLA D O d##

        elif tecla == "d":
            for i in range(4):
                valor=[]

                for j in range(3, -1, -1):
                    if tablero[i][j] != 0:
                        valor.append(tablero[i][j])
                Lid =0
                while Lid < len(valor) -1:
                    if valor[Lid] == valor[Lid +1]:
                        valor[Lid] *=2
                        valor[Lid+1] = 0
                        Lid += 2
                    else:
                        Lid += 1
                valor = list(filter(lambda x: x!= 0, valor))
                valor += [0] * (4 - len(valor))
                valor= valor[::-1]
                for j in range(4):
                    tablero[i][j] = valor [j]

            tablero = numeros_aleatorios(tablero)            
            dibujar_tablero(tablero)

            print("derecha")
        
#################################################################
#####               ||||TECLAS "INVALIDA"|||||||             #####
#################################################################

        else :
            print("Tecla no valida")
#############
def Puntuación():
    print(f"{nombreg} ¡¡¡VAMOS TU PUEDES!!!")
    suma = puntosw + puntosa + puntoss + puntosd
    print ("Puntuación: ",suma)
    if suma == 2048:
        print(f"{nombreg} ¡¡¡HAS CONSEGUIDO EL RETO!!!!! ")
         
def limpiar_consola():
    if os.name == 'nt': 
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def mostrar_instrucciones():
    print("\n--- Reglas de 2048 ---")
    print ("Juego clasico")
    print("Mueve las fichas en el tablero en cuatro direcciones (arriba, abajo, izquierda, derecha)")
    print("Cuando dos fichas con el mismo número se tocan, se fusionan en una sola ficha con el doble de valor")
    print("El objetivo es alcanzar la ficha 2048")
    print("El juego termina cuando el tablero está lleno y no quedan movimientos posibles\n")
    print("Juego 1v1")
    print("En este modo de juego coopetiras con un amigo por ver quien consigue el numero mas alto")
    print("Cada uno jugara una partida casual del juego 2048, y el que obtenga el numero mas grande gana")
    print("Si ambos jugadores llegan al mismo numero ganara el que lo alla logrado en menos movimientos\n")
    print("Juego 1vsIA")
    print("En este modo de juego competiras con una inteligencia artificial")
    print("Para poder ganar deberas superar a la IA")
    print("---------------------\n")
    input("Presiona Enter para volver al menú principal...")

def modo_1v1():
    print("Necesitas amigos para jugar este juego??? ")
    
def main():
    bienvenida()
    modo_de_juego()
    crear_tablero()
   # despedida()
    tablero = crear_tablero()
    tablero = numeros_aleatorios(tablero)
    tablero = numeros_aleatorios(tablero)
    #dibujar_tablero(tablero)
    limpiar_consola()
    tecla(tablero)
    dibujar_tablero(tablero)    
    limpiar_consola()

if __name__ == "__main__":
    main()
