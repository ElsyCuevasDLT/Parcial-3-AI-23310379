# Strand Sort, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def fusionar_ascendente(serie_a, serie_b):
    mezcla = []

    while serie_a and serie_b:
        # Siempre se toma el valor menor de las dos series ordenadas.
        if serie_a[0] <= serie_b[0]:
            mezcla.append(serie_a.pop(0))
        else:
            mezcla.append(serie_b.pop(0))

    mezcla.extend(serie_a)
    mezcla.extend(serie_b)
    return mezcla


def ordenar_por_hebras(datos):
    bolsa = datos[:]
    resultado = []

    while bolsa:
        hebra = [bolsa.pop(0)]
        sobrantes = []

        # Se forma una hebra creciente con los datos que puedan continuarla.
        for numero in bolsa:
            if numero >= hebra[-1]:
                hebra.append(numero)
            else:
                sobrantes.append(numero)

        bolsa = sobrantes

        # Cada hebra creciente se combina con el resultado acumulado.
        resultado = fusionar_ascendente(resultado, hebra)

    return resultado


entrada = [12, 5, 6, 3, 9, 1, 10, 2]
print("Secuencia:", entrada)
print("Strand sort:", ordenar_por_hebras(entrada))
