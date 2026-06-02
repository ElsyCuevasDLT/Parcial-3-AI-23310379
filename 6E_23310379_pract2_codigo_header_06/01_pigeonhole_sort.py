# Pigeonhole Sort, práctica de Programación.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def acomodar_por_casilleros(paquete):
    if not paquete:
        return []

    limite_bajo = min(paquete)
    limite_alto = max(paquete)
    cantidad_casillas = limite_alto - limite_bajo + 1

    # Cada casillero representa un valor posible dentro del rango encontrado.
    # Si aparece un número, se guarda en el casillero que le corresponde.
    casilleros = [[] for _ in range(cantidad_casillas)]

    for pieza in paquete:
        posicion = pieza - limite_bajo
        casilleros[posicion].append(pieza)

    # Al leer los casilleros desde el primero hasta el último,
    # los valores salen automáticamente en orden ascendente.
    salida = []
    for casilla in casilleros:
        for pieza in casilla:
            salida.append(pieza)

    return salida


muestra = [6, 3, 2, 6, 1, 4, 3]
print("Entrada usada:", muestra)
print("Pigeonhole:", acomodar_por_casilleros(muestra))
