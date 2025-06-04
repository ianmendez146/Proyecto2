import os
import random
n2 = 2
n4 = 4
def clear_screen():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu ():
    print ("        2048         ")
    print ("---------------------")
    print ("   modos de juegos   ")
    print ("1. Juego  ")
    print ("2. 1 vs 1")
    print ("3. Jugador vs IA")
    print ("---------------------")
    return input ("selecciona tu modo de juego: ")

def juego (menu):
    clear_screen()
    print ("  SCORE :")
    print ("---------------------")

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
def mover_arriba(tablero):
def tecla(tablero):
    while True:
        tecla = input("Para moverse usa a, s, w, d: ").lower()
        if tecla == 'w':
            mover_arriba(tablero)
            print("Movimiento hacia arriba hecho")
        elif tecla == 'a':
            print("Mover hacia la izquierda")
        elif tecla == 's':
            print("Mover hacia abajo")
        elif tecla == 'd':
            print("Mover hacia la derecha")
        elif tecla == 'arriba':
            print("Mover hacia arriba")
        elif tecla == 'abajo':
            print("Mover hacia abajo")
        elif tecla == 'izquierda':
            print("Mover hacia la izquierda")
        elif tecla == 'derecha':
            print("Mover hacia la derecha")
        elif tecla == 'salir':
            print("Saliendo...")
            break
        else:
            print("Tecla no reconocida")

    for col in range(4):
        # Extraer los números no cero en la columna
        valores = [tablero[fila][col] for fila in range(4) if tablero[fila][col] != 0]

        # Combinar números iguales consecutivos
        i = 0
        while i < len(valores) - 1:
            if valores[i] == valores[i + 1]:
                valores[i] *= 2      # sumar
                del valores[i + 1]   # eliminar el siguiente ya sumado
                valores.append(0)    # agregar un cero al final para mantener tamaño
            i += 1

        # Rellenar con ceros para que la columna tenga tamaño 4
        while len(valores) < 4:
            valores.append(0)

        # Poner de nuevo los valores en la columna del tablero
        for fila in range(4):
            tablero[fila][col] = valores[fila]


def main():
    clear_screen()
    modo = menu()
    tablero = crear_tablero()
    #dibujar_tablero(tablero)
    #tablero = crear_tablero()
    numeros_aleatorios(tablero) 
    numeros_aleatorios(tablero)
    tablero = numeros_aleatorios(tablero)
    #generar_nuevo_numero()
    #obtener_casilla_vacia(tablero)

    dibujar_tablero(tablero)  
    tecla(tablero)
    mover_arriba(tablero)
    dibujar_tablero(tablero)
if __name__ == "__main__":
    main()

