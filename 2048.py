 ##proyecto2##
#Ian Méndez
#24000146 - C
 
import random 
import math 
import re 
import os


n2 = random.randint(2,2)
n4 = random.randint(4,4)

def bienvenida():
    print("Bienvenido a nuestro Videojuego :D")
    c = input("Ingrese su nombre: ")
    print("bienvenido querido jugador ",c)

def modo_de_juego():
    print("Que tipo de modo de juego te gustaría? ")
    modo_de_juego_ele= input("|| 1. Individual || 2. 1 VS 1 || 3. VS IA || 4. No queiro jugar || : ") ##Cual es el tipo de modo de juego quiera el usuario
    if modo_de_juego_ele == "1":
        print("Juega como lobo Solitario entonces :D ")
    elif modo_de_juego_ele == "2":
        print("WOOOW TIENES AMIGOS!? ")
    elif modo_de_juego_ele == "3":
        print("Humano VS Maquina!!!!! ")
    elif modo_de_juego_ele == "4":
        print(" Pues no pues, te pierdes de un buen Juego... ADIOS!!!")
        print(" Nos vemos hasta la proxima!! :´D")

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
        tecla = input("Para moverse usa  a, s, w, d. o flechas:  ").lower()
        if tecla == "w":
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
                    tablero[j][i] = valor[i]
            dibujar_tablero(tablero)

            print("arriba")
        elif tecla == "a":
            print("izquierda")
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
            dibujar_tablero(tablero)
            print("atras")
        elif tecla == "d":
            print("derecha")
        else:
            print("Tecla no valida")
def limpiar_consola():
    if os.name == 'nt': 
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def modo_1v1():
    print("Necesitas amigos para jugar este juego??? ")
    
def main():
    bienvenida()
    modo_de_juego()
    tablero = crear_tablero()
    tablero = numeros_aleatorios(tablero)
    tablero = numeros_aleatorios(tablero)
    tablero = numeros_aleatorios(tablero)
    dibujar_tablero(tablero)
    limpiar_consola()
    tecla(tablero)
    dibujar_tablero(tablero)    
    limpiar_consola()

    
main()