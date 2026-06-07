# Dijkstra aplicado a una red de puntos.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def seleccionar_pendiente_mas_corto(pendientes, acumulados):
    # Se busca a mano el nodo pendiente con menor costo guardado.
    # En esta versión no se usa heapq para que el procedimiento se vea más directo.
    elegido = None
    costo_elegido = None

    for punto in pendientes:
        costo = acumulados[punto]

        if costo_elegido is None or costo < costo_elegido:
            elegido = punto
            costo_elegido = costo

    return elegido


def aplicar_dijkstra(red, salida):
    # acumulados guarda el menor costo conocido desde la salida hasta cada punto.
    # padres ayuda a recordar de dónde viene cada mejor camino.
    acumulados = {punto: float("inf") for punto in red}
    padres = {punto: "" for punto in red}
    pendientes = list(red.keys())
    apuntes = []

    acumulados[salida] = 0
    numero_vuelta = 1

    while pendientes:
        punto_actual = seleccionar_pendiente_mas_corto(pendientes, acumulados)

        if acumulados[punto_actual] == float("inf"):
            break

        pendientes.remove(punto_actual)
        apuntes.append(f"Vuelta {numero_vuelta}: se revisa {punto_actual}, costo acumulado {acumulados[punto_actual]}.")
        numero_vuelta += 1

        # Se revisan los vecinos del punto actual.
        # Si pasar por aquí reduce el costo, se actualizan la distancia y el padre.
        for vecino, distancia in red[punto_actual].items():
            if vecino not in pendientes:
                apuntes.append(f"   {vecino} ya quedó cerrado, no se modifica.")
                continue

            nuevo_costo = acumulados[punto_actual] + distancia

            if nuevo_costo < acumulados[vecino]:
                acumulados[vecino] = nuevo_costo
                padres[vecino] = punto_actual
                apuntes.append(f"   mejora para {vecino}: {nuevo_costo}, llega desde {punto_actual}.")
            else:
                apuntes.append(f"   {vecino} no mejora porque quedaría en {nuevo_costo}.")

    return acumulados, padres, apuntes


def armar_ruta(padres, origen, llegada):
    camino = [llegada]
    actual = llegada

    # Se reconstruye desde la llegada hacia el origen.
    # Después se invierte para mostrarlo en el sentido correcto.
    while actual != origen:
        actual = padres[actual]

        if actual == "":
            return []

        camino.append(actual)

    camino.reverse()
    return camino


def mostrar_en_consola(apuntes, costos, padres, ruta, destino):
    print("\nPRACTICA 3 - SIMULADOR DE DIJKSTRA\n")

    print("Desarrollo paso a paso:")
    for texto in apuntes:
        print(texto)

    print("\nTabla obtenida:")
    for punto in sorted(costos):
        print(f"{punto:>3} | costo: {costos[punto]:>4} | viene de: {padres[punto]}")

    print("\nCamino final:")
    print(" -> ".join(ruta))
    print("Costo total:", costos[destino])


def crear_html_visual(red, ruta, nombre_archivo):
    # El archivo HTML funciona como la parte gráfica.
    # Muestra los puntos del grafo y marca el camino mínimo con línea más fuerte.
    lugares = {
        "Casa": (90, 190),
        "Parada": (220, 90),
        "Tienda": (245, 270),
        "Escuela": (410, 110),
        "Trabajo": (440, 270),
        "Destino": (620, 185),
    }

    conexiones_ruta = set()
    for i in range(len(ruta) - 1):
        conexiones_ruta.add(tuple(sorted((ruta[i], ruta[i + 1]))))

    partes = [
        "<!DOCTYPE html>",
        "<html lang='es'>",
        "<head><meta charset='UTF-8'><title>Dijkstra</title></head>",
        "<body style='font-family:Arial;background:#fdf2f8;'>",
        "<h2>Ruta mínima con Dijkstra</h2>",
        "<svg width='730' height='360' style='background:white;border:1px solid #ddd;'>"
    ]

    dibujadas = set()

    for punto, vecinos in red.items():
        for vecino, peso in vecinos.items():
            clave = tuple(sorted((punto, vecino)))

            if clave in dibujadas:
                continue

            dibujadas.add(clave)

            x1, y1 = lugares[punto]
            x2, y2 = lugares[vecino]
            color = "#be123c" if clave in conexiones_ruta else "#9ca3af"
            ancho = 5 if clave in conexiones_ruta else 2

            partes.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{ancho}' />")
            partes.append(f"<text x='{(x1+x2)//2}' y='{(y1+y2)//2 - 8}' font-size='13'>{peso}</text>")

    for punto, (x, y) in lugares.items():
        esta_en_ruta = punto in ruta
        relleno = "#ffe4e6" if esta_en_ruta else "#f3e8ff"
        borde = "#be123c" if esta_en_ruta else "#7e22ce"

        partes.append(f"<circle cx='{x}' cy='{y}' r='27' fill='{relleno}' stroke='{borde}' stroke-width='3' />")
        partes.append(f"<text x='{x}' y='{y+5}' text-anchor='middle' font-size='11'>{punto}</text>")

    partes.extend(["</svg>", "</body>", "</html>"])

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(partes))


if __name__ == "__main__":
    mapa = {
        "Casa": {"Parada": 3, "Tienda": 4},
        "Parada": {"Casa": 3, "Escuela": 7, "Tienda": 2},
        "Tienda": {"Casa": 4, "Parada": 2, "Trabajo": 6},
        "Escuela": {"Parada": 7, "Trabajo": 2, "Destino": 5},
        "Trabajo": {"Tienda": 6, "Escuela": 2, "Destino": 4},
        "Destino": {"Escuela": 5, "Trabajo": 4},
    }

    origen = "Casa"
    final = "Destino"

    costos, padres, apuntes = aplicar_dijkstra(mapa, origen)
    ruta = armar_ruta(padres, origen, final)

    mostrar_en_consola(apuntes, costos, padres, ruta, final)

    crear_html_visual(mapa, ruta, "resultado_dijkstra_elsy.html")
    print("\nSe creó el archivo visual: resultado_dijkstra_elsy.html")
