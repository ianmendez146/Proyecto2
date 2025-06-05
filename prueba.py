#__________proyecto2___________#
#Ian Méndez        Emelie Perez#
#24000146 - C      24000255 - D#

import random 
import os
import math 
from copy import deepcopy 

n2 = random.randint(2,2)
n4 = random.randint(4,4)

def bienvenida():
    print("Bienvenido a nuestro Videojuego :D")
    c = input("Ingrese su nombre: ")
    print("bienvenido querido jugador ",c)

def modo_de_juego():
    print("¿Qué tipo de modo de juego te gustaría? ")
    while True:
        modo_de_juego_ele = input("|| 1. Individual || 2. 1 VS 1 || 3. VS IA || 4. Istrucciones || 5. No quiero jugar || : ").strip()

        if modo_de_juego_ele == "1":
            print("Juega como lobo Solitario entonces :D ")
            modo_solitario()
        elif modo_de_juego_ele == "2":
            print("WOOOW TIENES AMIGOS!? ")
            modo_1vs1 ()
        elif modo_de_juego_ele == "3":
            print("Humano VS Máquina!!!!! ")
            modo_IA()
        elif modo_de_juego_ele == "4": 
            limpiar_consola()
            mostrar_instrucciones() 
            limpiar_consola()
        elif modo_de_juego_ele == "5":
            print("Pues no, te pierdes de un buen Juego... ¡ADIOS!!!")
            break
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
        # TECLA W
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
        #TECLA A
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
        #TECLA S
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
        #TECLA D
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
        #TECLA INVALIDA
        else :
            print("Tecla no valida")

def limpiar_consola():
    if os.name == 'nt': 
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def Puntuación():
    print(f"{nombre} ¡¡¡VAMOS TU PUEDES!!!")
    suma = puntosw + puntosa + puntoss + puntosd
    print ("Puntuación: ",suma)
    if suma == 2048:
        print(f"{nombre} ¡¡¡HAS CONSEGUIDO EL RETO!!!!! ")

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

def modo_solitario ():
    tablero = crear_tablero()
    tablero = numeros_aleatorios(tablero)
    tablero = numeros_aleatorios(tablero)

    while True:
        limpiar_consola()
        dibujar_tablero(tablero)
        Puntuación()
        
        # Comprobar si se alcanzó 2048
        for r in range(4):
            for c in range(4):
                if tablero[r][c] == 2048:
                    limpiar_consola()
                    dibujar_tablero(tablero)
                    print("\n¡FELICIDADES! ¡Has llegado al 2048!")
                    input("Presiona Enter para volver al menú principal...")
                    return 

        # Comprobar si el juego ha terminado
        if not hay_movimientos_posibles(tablero):
            limpiar_consola()
            dibujar_tablero(tablero)
            print("\n¡Juego Terminado! No hay movimientos posibles.")
            print(f"Tu puntuación final: {puntuacion}")
            #print(f"Tu máxima ficha: {max_ficha}")
            input("Presiona Enter para volver al menú principal...")
            break 

        resultado_movimiento = tecla(tablero) 

        if resultado_movimiento is None: 
            print("Volviendo al menú principal...")
            break
        else:
            tablero_despues_mov, puntos_ganados = resultado_movimiento
            
            if tablero_despues_mov != tablero:
                tablero = tablero_despues_mov 
                tablero = numeros_aleatorios(tablero) 
            else:
                pass 


def modo_1vs1():
    puntuacion_jugador1 = 0
    puntuacion_jugador2 = 0
    movimientos_jugador1 = 0
    movimientos_jugador2 = 0
    max_tile_jugador1 = 0
    max_tile_jugador2 = 0
    jugador_actual = 1

    nombre_jugador1 = input("Introduce el nombre del Jugador 1: ").strip()
    nombre_jugador2 = input("Introduce el nombre del Jugador 2: ").strip()

    jugador_actual = random.choice([1, 2])
    if jugador_actual == 1 :
        jugador_primero = nombre_jugador1
    else:
        jugador_primero = nombre_jugador2 
        print(jugador_primero, "empieza primero!!")
        input("Presiona Enter para comenzar el juego...")

    print(f"{nombre_jugador1}: Puntuación: {puntuacion_jugador1} | Movimientos: {movimientos_jugador1} | Máxima Ficha: {max_tile_jugador1}")
    print(f"{nombre_jugador2}: Puntuación: {puntuacion_jugador2} | Movimientos: {movimientos_jugador2} | Máxima Ficha: {max_tile_jugador2}")
    print(jugador_primero, "es tu turno.")

    tecla_input = tecla(tablero)
    if tecla_input == "q":
        print(jugador_primero, "ha abandonado el juego.")
        game_over = True

    tablero, hubo_cambio, puntos_ganados_en_turno = mover_tablero(tablero, tecla_input)
    if hubo_cambio:
        # Sumar puntos y movimientos al jugador actual
        if jugador_actual == 1:
            puntuacion_jugador1 += puntos_ganados_en_turno
            movimientos_jugador1 += 1
        else:
            puntuacion_jugador2 += puntos_ganados_en_turno
            movimientos_jugador2 += 1
                        
        # --- Actualizar ficha máxima para el jugador actual ---
        ficha_maxima = 0
        for r in range(4):
            for c in range(4):
                if tablero[r][c] > ficha_maxima:
                    ficha_maxima = tablero[r][c]
                                
                if jugador_actual == 1:
                    if ficha_maxima > max_tile_jugador1:
                        max_tile_jugador1 = ficha_maxima
                else:
                    if ficha_maxima > max_tile_jugador2:
                        max_tile_jugador2 = ficha_maxima
                    # Alternar turno
                    jugador_actual = 3 - jugador_actual 
    else:
        print("Movimiento inválido o no hubo cambios. Pierdes el turno.")
        input("Presiona Enter para que el otro jugador tome su turno...")
        jugador_actual = 3 - jugador_actual 

def modo_IA ():
    def movimientos_ia (linea_ia):
                direcciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]
                mejor_puntuacion_evaluada = -float('inf')
                mejor_direccion = None

                for direccion in direcciones_posibles:
                        tablero_simulauacion_evaluada = puntuacion_actual_evaluada
                        mejor_direccion = direccion
                        #mejor_direccion = deepcopy(tablero)
                return mejor_direccion 
                
                hubo_cambio_simulado, _ = mover_tablero(tablero_simulado, direccion) 
                if hubo_cambio_simulado:
                        puntuacion_actual_evaluada = evaluar_tablero(tablero_simulado)
                                
                        if puntuacion_actual_evaluada > mejor_puntuacion_evaluada:
                                mejor_punt

    def analizar_tablero (tablero):
        score = 0
        
        # Priorizar casillas vacías
        vacios = 0
        for r in range(4):
            for c in range(4):
                if tablero[r][c] == 0:
                    vacios += 1
        score += vacios * 20 

        # Suma total de los valores del tablero
        suma_total_valores = 0
        for r in range(4):
            for c in range(4):
                suma_total_valores += tablero[r][c]
        score += suma_total_valores * 0.5 

        # Monotonicidad (orden) y Suavidad (diferencias pequeñas entre vecinos)
        monotonicidad_puntaje = 0
        penalisacion_s = 0

        dr = [0, 1] 
        dc = [1, 0] 

        for r in range(4):
            for c in range(4):
                if tablero[r][c] == 0:
                    continue
                current_val = tablero[r][c]
                
                for i in range(2): 
                    nr, nc = r + dr[i], c + dc[i]
                    
                    if 0 <= nr < 4 and 0 <= nc < 4 and tablero[nr][nc] != 0:
                        neighbor_val = tablero[nr][nc]
                        penalisacion_s -= abs(math.log2(current_val) - math.log2(neighbor_val)) * 2

                        if current_val > neighbor_val:
                            monotonicidad_puntaje += 1
                        elif current_val < neighbor_val:
                            monotonicidad_puntaje += 1
        
        score += monotonicidad_puntaje * 5 
        score += penalisacion_s      

        # Priorizar el numero mas grande en una esquina 
        max_val = 0
        for r in range(4):
            for c in range(4):
                if tablero[r][c] > max_val:
                    max_val = tablero[r][c]

        corner_bonus = 0
        if tablero[0][0] == max_val: 
            corner_bonus = 500
        elif tablero[0][3] == max_val or tablero[3][0] == max_val or tablero[3][3] == max_val:
            corner_bonus = 200 
        score += corner_bonus

        # Contar posibles fusiones para el siguiente turno
        potential_merges = 0
        for r in range(4):
            for c in range(3): 
                if tablero[r][c] != 0 and tablero[r][c] == tablero[r][c+1]:
                    potential_merges += 1
            for c in range(4):
                if r < 3 and tablero[r][c] != 0 and tablero[r][c] == tablero[r+1][c]:
                    potential_merges += 1
        
        score += potential_merges * 15

        return score

def main():
    bienvenida()
    modo_de_juego()
    crear_tablero()
    tablero = crear_tablero()
    tablero = numeros_aleatorios(tablero)
    tablero = numeros_aleatorios(tablero)
    limpiar_consola()
    tecla(tablero)
    dibujar_tablero(tablero)    
    limpiar_consola()

if __name__ == "__main__":
    main()
