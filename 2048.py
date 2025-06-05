#__________proyecto2___________#
#Ian Méndez        Emelie Perez
#24000146 - C      24000255 - D
 
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
    print("Que tipo de modo de juego te gustaría? ")
    modo_de_juego_ele= input("|| 1. Individual || 2. 1 VS 1 || 3. VS IA || 4. No queiro jugar || : ") ##Cual es el tipo de modo de juego quiera el usuario
    if modo_de_juego_ele == "1":
        print("Juega como lobo Solitario entonces :D ")
    elif modo_de_juego_ele == "2":
        print("WOOOW TIENES AMIGOS!? ")
    elif modo_de_juego_ele == "3":
        print("Humano VS Maquina!!!!! ")
        modo_IA()
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

def modo_IA ():
    def movimientos_ia (linea_ia):
        direcciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]
        mejor_puntuacion_evaluada = -float('inf')
        mejor_direccion = None

        for direccion in direcciones_posibles:
            tablero_simulado = deepcopy(tablero) 
            
            hubo_cambio_simulado, _ = mover_tablero(tablero_simulado, direccion) 
            
            if hubo_cambio_simulado:
                puntuacion_actual_evaluada = evaluar_tablero(tablero_simulado)
                
                if puntuacion_actual_evaluada > mejor_puntuacion_evaluada:
                    mejor_puntuacion_evaluada = puntuacion_actual_evaluada
                    mejor_direccion = direccion

        return mejor_direccion 

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
        monotonicity_score = 0
        smoothness_penalty = 0

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
                        smoothness_penalty -= abs(math.log2(current_val) - math.log2(neighbor_val)) * 2

                        if current_val > neighbor_val:
                            monotonicity_score += 1
                        elif current_val < neighbor_val:
                            monotonicity_score += 1
        
        score += monotonicity_score * 5 
        score += smoothness_penalty      

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
 
def casillas_vacias (tablero):
    contador_casillaV = 0
    for fila in tablero:
        for celda in tablero:
            if celda == 0:
                contador_casillaV += 1
    return contador
    
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
    casillas_vacias(tablero)

if __name__ == "__main__":
    main()
