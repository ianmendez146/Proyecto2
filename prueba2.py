import random
import os

n2 = 2
n4 = 4
puntuacion_global = 0

def limpiar_consola():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def bienvenida():
    print("Bienvenido a nuestro Videojuego 😃")

def modo_de_juego():
    print("¿Qué tipo de modo de juego te gustaría?")
    modo_de_juego_ele = input("|| 1. Individual || 2. 1 VS 1 || 3. VS IA || 4. No quiero jugar || : ")
    if modo_de_juego_ele == "1":
        print("Juega como lobo solitario entonces 😃")
    elif modo_de_juego_ele == "2":
        print("¡WOOOW TIENES AMIGOS!?")
    elif modo_de_juego_ele == "3":
        print("¡Humano VS Máquina!")
    elif modo_de_juego_ele == "4":
        print("Pues no pues, te pierdes de un buen juego... ¡ADIOS!")
        print("Nos vemos hasta la próxima :´D")
        exit()

def crear_tablero():
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
    posiciones_vacias = [(i, j) for i in range(4) for j in range(4) if tablero[i][j] == 0]
    if not posiciones_vacias:
        return tablero
    i, j = random.choice(posiciones_vacias)
    tablero[i][j] = n2 if random.random() < 0.9 else n4
    return tablero

def _mover_linea(linea):
    global puntuacion_global
    original_linea = list(linea)
    nueva_linea = [num for num in linea if num != 0]
    for i in range(len(nueva_linea) - 1):
        if nueva_linea[i] != 0 and nueva_linea[i] == nueva_linea[i + 1]:
            nueva_linea[i] *= 2
            puntuacion_global += nueva_linea[i]
            nueva_linea[i + 1] = 0
    linea_final = [num for num in nueva_linea if num != 0]
    linea_final.extend([0] * (len(linea) - len(linea_final)))
    cambio = (original_linea != linea_final)
    return linea_final, cambio

def transponer_tablero(tablero):
    return [list(col) for col in zip(*tablero)]

def mover_tablero(tablero, direccion):
    cambio_global = False
    if direccion == "izquierda":
        for r in range(4):
            nueva, cambio = _mover_linea(tablero[r])
            tablero[r] = nueva
            if cambio:
                cambio_global = True
    elif direccion == "derecha":
        for r in range(4):
            invertida = tablero[r][::-1]
            nueva, cambio = _mover_linea(invertida)
            tablero[r] = nueva[::-1]
            if cambio:
                cambio_global = True
    elif direccion == "arriba":
        transpuesto = transponer_tablero(tablero)
        for c in range(4):
            nueva, cambio = _mover_linea(transpuesto[c])
            transpuesto[c] = nueva
            if cambio:
                cambio_global = True
        tablero[:] = transponer_tablero(transpuesto)
    elif direccion == "abajo":
        transpuesto = transponer_tablero(tablero)
        for c in range(4):
            invertida = transpuesto[c][::-1]
            nueva, cambio = _mover_linea(invertida)
            transpuesto[c] = nueva[::-1]
            if cambio:
                cambio_global = True
        tablero[:] = transponer_tablero(transpuesto)
    return cambio_global

def tecla():
    tecla_press = input("Usa WASD para mover (q para salir): ").lower()
    if tecla_press == "w":
        return "arriba"
    elif tecla_press == "a":
        return "izquierda"
    elif tecla_press == "s":
        return "abajo"
    elif tecla_press == "d":
        return "derecha"
    elif tecla_press == "q":
        return "salir"
    else:
        print("Tecla no válida.")
        return None

def movimientos_posibles(tablero):
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == 0:
                return True
            if j < 3 and tablero[i][j] == tablero[i][j + 1]:
                return True
            if i < 3 and tablero[i][j] == tablero[i + 1][j]:
                return True
    return False

def main():
    global puntuacion_global
    puntuacion_global = 0
    bienvenida()
    modo_de_juego()

    tablero = crear_tablero()
    numeros_aleatorios(tablero)
    numeros_aleatorios(tablero)

    jugando = True
    while jugando:
        limpiar_consola()
        dibujar_tablero(tablero)
        print(f"Puntuación: {puntuacion_global}")

        if not movimientos_posibles(tablero):
            print("¡No hay más movimientos posibles! Fin del juego.")
            break

        movimiento = tecla()
        if movimiento == "salir":
            print("¡Gracias por jugar!")
            break
        if movimiento:
            hubo_cambio = mover_tablero(tablero, movimiento)
            if hubo_cambio:
                numeros_aleatorios(tablero)

if __name__ == "__main__":
    main()
