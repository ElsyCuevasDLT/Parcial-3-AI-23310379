# Bead Sort, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def bead_sort(datos):
    if any(numero < 0 for numero in datos):
        raise ValueError("Bead Sort solo se usa aquí con enteros no negativos.")

    if not datos:
        return []

    mayor = max(datos)

    # Se representa cada número como una fila de cuentas.
    # Por ejemplo, el 4 se guarda como cuatro cuentas activas.
    tablero = [[1 if columna < numero else 0 for columna in range(mayor)] for numero in datos]

    # Las cuentas caen por gravedad: se cuentan por columna y se mandan hacia abajo.
    for columna in range(mayor):
        cuentas = sum(fila[columna] for fila in tablero)

        for fila in range(len(datos)):
            tablero[fila][columna] = 0

        for fila in range(len(datos) - cuentas, len(datos)):
            tablero[fila][columna] = 1

    # Cada fila se convierte otra vez en número contando sus cuentas.
    resultado = [sum(fila) for fila in tablero]
    return resultado


muestra = [5, 3, 1, 7, 4, 2]
print("Serie inicial:", muestra)
print("Bead sort:", bead_sort(muestra))
