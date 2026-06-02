# Stooge Sort, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def stooge_recursivo(grupo, primero, ultimo):
    # Se asegura que el extremo menor quede antes que el extremo mayor.
    if grupo[primero] > grupo[ultimo]:
        grupo[primero], grupo[ultimo] = grupo[ultimo], grupo[primero]

    # Cuando hay más de dos elementos, se ordenan secciones traslapadas.
    if ultimo - primero + 1 > 2:
        tercio = (ultimo - primero + 1) // 3

        stooge_recursivo(grupo, primero, ultimo - tercio)
        stooge_recursivo(grupo, primero + tercio, ultimo)
        stooge_recursivo(grupo, primero, ultimo - tercio)


def stooge_sort(datos):
    copia = datos[:]

    if len(copia) > 1:
        stooge_recursivo(copia, 0, len(copia) - 1)

    return copia


valores = [8, 6, 7, 3, 1, 4]
print("Entrada:", valores)
print("Stooge sort:", stooge_sort(valores))
