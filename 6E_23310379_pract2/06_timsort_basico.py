# TimSort básico, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def insertar_en_tramo(conjunto, arranque, cierre):
    # Primero se ordenan pequeños bloques con inserción.
    # Esto es útil porque inserción trabaja bien en grupos reducidos.
    for actual in range(arranque + 1, cierre + 1):
        ficha = conjunto[actual]
        cursor = actual - 1

        while cursor >= arranque and conjunto[cursor] > ficha:
            conjunto[cursor + 1] = conjunto[cursor]
            cursor -= 1

        conjunto[cursor + 1] = ficha


def combinar_tramos(conjunto, inicio, medio, fin):
    izquierda = conjunto[inicio:medio + 1]
    derecha = conjunto[medio + 1:fin + 1]

    i = j = 0
    lugar = inicio

    # Se mezclan dos tramos que ya estaban ordenados.
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            conjunto[lugar] = izquierda[i]
            i += 1
        else:
            conjunto[lugar] = derecha[j]
            j += 1
        lugar += 1

    while i < len(izquierda):
        conjunto[lugar] = izquierda[i]
        i += 1
        lugar += 1

    while j < len(derecha):
        conjunto[lugar] = derecha[j]
        j += 1
        lugar += 1


def timsort_basico(datos):
    arreglo = datos[:]
    salto = 4
    total = len(arreglo)

    for comienzo in range(0, total, salto):
        insertar_en_tramo(arreglo, comienzo, min(comienzo + salto - 1, total - 1))

    tamano = salto
    while tamano < total:
        for inicio in range(0, total, 2 * tamano):
            medio = min(total - 1, inicio + tamano - 1)
            fin = min(total - 1, inicio + 2 * tamano - 1)

            if medio < fin:
                combinar_tramos(arreglo, inicio, medio, fin)

        tamano *= 2

    return arreglo


datos_de_clase = [23, 4, 18, 1, 7, 12, 3, 30, 9]
print("Datos:", datos_de_clase)
print("TimSort básico:", timsort_basico(datos_de_clase))
