# Cycle Sort, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def ordenar_por_ciclos(coleccion):
    arreglo = coleccion[:]

    for origen in range(0, len(arreglo) - 1):
        elemento = arreglo[origen]
        destino = origen

        # Se cuenta cuántos valores son menores al elemento actual.
        # Esa cuenta indica la posición real que debe ocupar.
        for revision in range(origen + 1, len(arreglo)):
            if arreglo[revision] < elemento:
                destino += 1

        if destino == origen:
            continue

        # Si hay repetidos, se avanza hasta encontrar un lugar libre.
        while elemento == arreglo[destino]:
            destino += 1

        arreglo[destino], elemento = elemento, arreglo[destino]

        # El ciclo continúa hasta regresar al punto inicial.
        # En cada vuelta se coloca un elemento en su posición correcta.
        while destino != origen:
            destino = origen

            for revision in range(origen + 1, len(arreglo)):
                if arreglo[revision] < elemento:
                    destino += 1

            while elemento == arreglo[destino]:
                destino += 1

            arreglo[destino], elemento = elemento, arreglo[destino]

    return arreglo


valores_base = [9, 4, 7, 4, 1, 8, 2]
print("Datos iniciales:", valores_base)
print("Cycle sort:", ordenar_por_ciclos(valores_base))
