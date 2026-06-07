# Bitonic Sort, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def comparar_y_ajustar(vector, inicio, cantidad, ascendente):
    mitad = cantidad // 2

    # Se comparan pares separados por media sección.
    # Según la dirección deseada, se intercambian para acercarse al orden final.
    for k in range(inicio, inicio + mitad):
        debe_cambiar = (vector[k] > vector[k + mitad]) == ascendente

        if debe_cambiar:
            vector[k], vector[k + mitad] = vector[k + mitad], vector[k]


def unir_bitonico(vector, inicio, cantidad, ascendente):
    if cantidad > 1:
        comparar_y_ajustar(vector, inicio, cantidad, ascendente)
        mitad = cantidad // 2
        unir_bitonico(vector, inicio, mitad, ascendente)
        unir_bitonico(vector, inicio + mitad, mitad, ascendente)


def construir_bitonico(vector, inicio, cantidad, ascendente):
    if cantidad > 1:
        mitad = cantidad // 2

        # Una mitad se acomoda ascendente y la otra descendente.
        # Esa forma crea una secuencia bitónica que después se puede unir.
        construir_bitonico(vector, inicio, mitad, True)
        construir_bitonico(vector, inicio + mitad, mitad, False)

        unir_bitonico(vector, inicio, cantidad, ascendente)


def bitonic_sort(datos):
    copia = datos[:]

    # Esta versión requiere longitud potencia de 2 para mantener el ejemplo claro.
    if len(copia) == 0 or (len(copia) & (len(copia) - 1)) != 0:
        raise ValueError("La cantidad de datos debe ser potencia de 2.")

    construir_bitonico(copia, 0, len(copia), True)
    return copia


numeros = [19, 3, 11, 7, 2, 17, 5, 13]
print("Arreglo usado:", numeros)
print("Bitonic sort:", bitonic_sort(numeros))
