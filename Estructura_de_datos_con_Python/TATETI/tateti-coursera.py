
"""Tablero inicial"""
tablero = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# Diccionario de posiciones
posiciones = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}


def dibujar_tablero(tablero):
    """Dibuja el tablero pasado como argumento. Una matriz de 3x3."""
    for fila in tablero:
        print("|", "|".join(fila), "|", sep="")
    print("")


def asignar_simbolos():
    """Devuelve un diccionario con los simbolos validos elegidos por el jugador """
    while True:
        simbolo = input(
            'Jugador1 ingrese el símbolo "X" o el símbolo "O": ').upper()
        print("")
        if simbolo == "X":
            print('El Jugador1 juega con "X" y el Jugador2 con "O"', "\n")
            return {"X": "Jugador1", "O": "Jugador2"}
        elif simbolo == "O":
            print('El Jugador1 juega con "O" y el Jugador2 con "X"', "\n")
            return {"X": "Jugador2", "O": "Jugador1"}


def posicion_libre(posicion, tablero):
    """Devuelve un booleano verificando si la posicion pasada como argumento se encuentra libre en el tablero dado"""
    i, j = posiciones[posicion]
    return tablero[i][j] not in ["X", "O"]


def obtener_posicion(simbolo, tablero):
    """Devuelve una posicion valida ingresada por el usuario"""
    while True:
        try:
            posicion = int(input(
                "%s ingrese un numero del 1 al 9 para la posicion del simbolo %s: " % (jugadores[simbolo], simbolo)))
        except ValueError as error:
            print("ingreso invalido", error, "\n")
        else:
            if posicion > 0 and posicion < 10:
                if posicion_libre(posicion, tablero):
                    print("")
                    return posicion
                else:
                    print("Posicion ya ocupada", "\n")


def modificar_tablero(tablero, simbolo, posicion):
    """"Devuelve un tablero con el simbolo en la posicion pasada como argumento"""
    i, j = posiciones[posicion]
    tablero[i][j] = simbolo
    return tablero


def enumerate_reverse(sequence):
    """Agrega un contador descendiente al iterable pasado como argumento. 
    Parecido a lo que hace  enumerate() pero el contador es descendiente desde len(sequence)-1 """
    n = len(sequence) - 1
    for elem in sequence:
        yield n, elem
        n -= 1


def obtener_ganador(tablero):
    """Evalua el tablero para determinar un ganador """

    for index, fila in enumerate(tablero):
        for simbolo in ["O", "X"]:

            # evaluar filas
            if fila.count(simbolo) == 3:
                return simbolo

            # evaluar columnas
            # una lista con los simbolos en la columna
            columna = [fila[index] for fila in tablero]
            if columna.count(simbolo) == 3:
                return simbolo

            # evaluar diagonales
            # una lista con los simbolos en diagonal
            diagonal1 = [fila[diag_index]
                         for diag_index, fila in enumerate(tablero)]
            if diagonal1.count(simbolo) == 3:
                return simbolo
            # una lista con los simbolos en diagonal invertida
            diagonal2 = [fila[reverse_diag_index]
                         for reverse_diag_index, fila in enumerate_reverse(tablero)]
            if diagonal2.count(simbolo) == 3:
                return simbolo


print("- Juguemos TA-TE-TI", "\n")
dibujar_tablero(tablero)
jugadores = asignar_simbolos()

continuar_partida = True
turnos = 0
while continuar_partida:
    for simbolo in jugadores:
        turnos += 1
        posicion = obtener_posicion(simbolo, tablero)
        tablero = modificar_tablero(tablero, simbolo, posicion)
        dibujar_tablero(tablero)
        ganador = obtener_ganador(tablero)
        if ganador != None:
            print("El ganador es %s" % jugadores[ganador])
            continuar_partida = False
            break
        if turnos == 9:
            print("El resultado es empate.")
            continuar_partida = False
            break
