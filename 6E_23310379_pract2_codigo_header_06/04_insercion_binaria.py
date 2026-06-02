# Inserción binaria, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def ubicar_con_busqueda_binaria(zona, valor):
    izquierda = 0
    derecha = len(zona)

    # La búsqueda binaria encuentra más rápido el lugar donde debe insertarse el valor.
    # No ordena por sí sola, solo calcula la posición correcta dentro de la parte ordenada.
    while izquierda < derecha:
        centro = (izquierda + derecha) // 2

        if zona[centro] <= valor:
            izquierda = centro + 1
        else:
            derecha = centro

    return izquierda


def insercion_binaria(elementos):
    ordenados = []

    for candidato in elementos:
        indice = ubicar_con_busqueda_binaria(ordenados, candidato)

        # insert coloca el número en el punto calculado y recorre lo demás.
        # Así la lista ordenados se conserva acomodada después de cada paso.
        ordenados.insert(indice, candidato)

    return ordenados


prueba = [31, 14, 55, 2, 9, 14, 20]
print("Antes de ordenar:", prueba)
print("Inserción binaria:", insercion_binaria(prueba))
