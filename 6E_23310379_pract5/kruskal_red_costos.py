# Kruskal para conectar una red con menor y mayor costo.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def representante(padres, punto):
    # Esta funcion camina hasta encontrar el representante del grupo.
    # Tambien va acortando el camino para que las siguientes consultas sean mas rapidas.
    while padres[punto] != punto:
        padres[punto] = padres[padres[punto]]
        punto = padres[punto]

    return punto


def unir_grupos(padres, tamanos, punto_a, punto_b):
    raiz_a = representante(padres, punto_a)
    raiz_b = representante(padres, punto_b)

    # Si las raices son iguales, ambos puntos ya estaban conectados.
    # Agregar esa conexion produciria un ciclo.
    if raiz_a == raiz_b:
        return False

    # Se pega el grupo pequeno al grupo grande para mantener la estructura mas estable.
    if tamanos[raiz_a] < tamanos[raiz_b]:
        raiz_a, raiz_b = raiz_b, raiz_a

    padres[raiz_b] = raiz_a
    tamanos[raiz_a] += tamanos[raiz_b]

    return True


def kruskal_red(puntos, conexiones, modo):
    padres = {punto: punto for punto in puntos}
    tamanos = {punto: 1 for punto in puntos}

    # En minimo se revisan los costos de menor a mayor.
    # En maximo se hace al contrario para elegir primero las conexiones mas caras.
    if modo == "minimo":
        lista = sorted(conexiones, key=lambda dato: dato["costo"])
    else:
        lista = sorted(conexiones, key=lambda dato: dato["costo"], reverse=True)

    elegidas = []
    acumulado = 0
    bitacora = []

    for numero, conexion in enumerate(lista, start=1):
        a = conexion["a"]
        b = conexion["b"]
        costo = conexion["costo"]

        bitacora.append(f"{numero}. Se analiza {a} - {b}, costo {costo}.")

        if unir_grupos(padres, tamanos, a, b):
            elegidas.append(conexion)
            acumulado += costo
            bitacora.append(f"   Se acepta porque conecta dos grupos diferentes. Total: {acumulado}.")
        else:
            bitacora.append("   Se descarta porque cerraria un ciclo.")

        if len(elegidas) == len(puntos) - 1:
            bitacora.append("   El arbol ya tiene las conexiones necesarias.")
            break

    return elegidas, acumulado, bitacora


def imprimir_resultado(nombre, elegidas, total, bitacora):
    print("\n" + nombre)
    print("=" * len(nombre))

    print("\nRevision paso a paso:")
    for linea in bitacora:
        print(linea)

    print("\nConexiones seleccionadas:")
    for conexion in elegidas:
        print(f"  {conexion['a']} - {conexion['b']}  costo: {conexion['costo']}")

    print("Costo total:", total)


def crear_html(puntos, conexiones, minimo, maximo, archivo):
    # La visualizacion ayuda a comparar las conexiones del arbol minimo y maximo.
    # Verde indica minimo y rosa indica maximo.
    coordenadas = {
        "Entrada": (90, 180),
        "Oficina": (220, 85),
        "Almacen": (235, 270),
        "Calidad": (410, 105),
        "Produccion": (445, 265),
        "Embarque": (620, 175),
    }

    min_usadas = {tuple(sorted((x["a"], x["b"]))) for x in minimo}
    max_usadas = {tuple(sorted((x["a"], x["b"]))) for x in maximo}

    partes = [
        "<!DOCTYPE html>",
        "<html lang='es'>",
        "<head><meta charset='UTF-8'><title>Kruskal</title></head>",
        "<body style='font-family:Arial;background:#fbf4f7;'>",
        "<h2>Kruskal: arbol minimo y maximo</h2>",
        "<p><span style='color:#15803d;'>Verde: minimo</span> | <span style='color:#be123c;'>Rosa: maximo</span></p>",
        "<svg width='730' height='360' style='background:white;border:1px solid #ddd;'>"
    ]

    for conexion in conexiones:
        a = conexion["a"]
        b = conexion["b"]
        costo = conexion["costo"]
        clave = tuple(sorted((a, b)))

        x1, y1 = coordenadas[a]
        x2, y2 = coordenadas[b]

        color = "#9ca3af"
        ancho = 2

        if clave in min_usadas:
            color = "#15803d"
            ancho = 5

        if clave in max_usadas:
            color = "#be123c"
            ancho = 5

        partes.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{ancho}' />")
        partes.append(f"<text x='{(x1+x2)//2}' y='{(y1+y2)//2 - 8}' font-size='13'>{costo}</text>")

    for punto in puntos:
        x, y = coordenadas[punto]
        partes.append(f"<circle cx='{x}' cy='{y}' r='28' fill='#fce7f3' stroke='#9d174d' stroke-width='3' />")
        partes.append(f"<text x='{x}' y='{y+5}' text-anchor='middle' font-size='10'>{punto}</text>")

    partes.extend(["</svg>", "</body>", "</html>"])

    with open(archivo, "w", encoding="utf-8") as documento:
        documento.write("\n".join(partes))


if __name__ == "__main__":
    puntos = ["Entrada", "Oficina", "Almacen", "Calidad", "Produccion", "Embarque"]

    conexiones = [
        {"a": "Entrada", "b": "Oficina", "costo": 6},
        {"a": "Entrada", "b": "Almacen", "costo": 4},
        {"a": "Oficina", "b": "Almacen", "costo": 3},
        {"a": "Oficina", "b": "Calidad", "costo": 8},
        {"a": "Almacen", "b": "Produccion", "costo": 7},
        {"a": "Calidad", "b": "Produccion", "costo": 2},
        {"a": "Calidad", "b": "Embarque", "costo": 5},
        {"a": "Produccion", "b": "Embarque", "costo": 9},
        {"a": "Almacen", "b": "Calidad", "costo": 6},
    ]

    minimo, total_minimo, pasos_minimo = kruskal_red(puntos, conexiones, "minimo")
    maximo, total_maximo, pasos_maximo = kruskal_red(puntos, conexiones, "maximo")

    imprimir_resultado("ARBOL DE MENOR COSTO", minimo, total_minimo, pasos_minimo)
    imprimir_resultado("ARBOL DE MAYOR COSTO", maximo, total_maximo, pasos_maximo)

    crear_html(puntos, conexiones, minimo, maximo, "resultado_kruskal_elsy.html")
    print("\nSe creo el archivo visual: resultado_kruskal_elsy.html")
