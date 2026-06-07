# Prim aplicado a una red de lugares.
# Elsy Valeria Cuevas de la Torre (6E) - registro 23310379.

def buscar_conexion_mas_barata(red, incluidos):
    mejor_opcion = None

    # Se revisan todas las conexiones que salen desde los puntos ya incluidos.
    # La regla de Prim es escoger la arista mas barata que conecte con un punto nuevo.
    for punto in incluidos:
        for vecino, costo in red[punto].items():
            if vecino in incluidos:
                continue

            if mejor_opcion is None or costo < mejor_opcion["costo"]:
                mejor_opcion = {
                    "desde": punto,
                    "hacia": vecino,
                    "costo": costo
                }

    return mejor_opcion


def prim_red_lugares(red, inicio):
    incluidos = {inicio}
    seleccionadas = []
    total = 0
    registro = []

    registro.append(f"Inicio: se toma {inicio} como primer punto del arbol.")

    vuelta = 1

    # El ciclo termina cuando todos los puntos ya quedaron conectados.
    while len(incluidos) < len(red):
        conexion = buscar_conexion_mas_barata(red, incluidos)

        if conexion is None:
            registro.append("No hay mas conexiones disponibles. El grafo no esta conectado.")
            break

        incluidos.add(conexion["hacia"])
        seleccionadas.append(conexion)
        total += conexion["costo"]

        # Se guarda una descripcion sencilla para poder mostrar el avance en consola.
        registro.append(
            f"Vuelta {vuelta}: se agrega {conexion['desde']} - {conexion['hacia']} "
            f"con costo {conexion['costo']}."
        )

        registro.append(f"   Puntos conectados hasta ahora: {', '.join(sorted(incluidos))}")
        vuelta += 1

    return seleccionadas, total, registro


def imprimir_practica(conexiones, total, registro):
    print("\nPRACTICA 4 - ALGORITMO DE PRIM\n")

    print("Paso a paso:")
    for linea in registro:
        print(linea)

    print("\nConexiones del arbol parcial minimo:")
    for dato in conexiones:
        print(f"  {dato['desde']} -> {dato['hacia']}  costo: {dato['costo']}")

    print("\nCosto total:", total)


def crear_html(red, conexiones, nombre_archivo):
    # El HTML sirve como parte grafica de la practica.
    # Las conexiones elegidas por Prim se marcan con color mas fuerte.
    ubicacion = {
        "Entrada": (95, 190),
        "Oficina": (235, 95),
        "Almacen": (250, 280),
        "Calidad": (420, 110),
        "Produccion": (440, 280),
        "Embarque": (625, 190),
    }

    usadas = {tuple(sorted((dato["desde"], dato["hacia"]))) for dato in conexiones}

    partes = [
        "<!DOCTYPE html>",
        "<html lang='es'>",
        "<head><meta charset='UTF-8'><title>Prim</title></head>",
        "<body style='font-family:Arial;background:#fbf4f7;'>",
        "<h2>Arbol parcial minimo con Prim</h2>",
        "<svg width='730' height='360' style='background:white;border:1px solid #ddd;'>"
    ]

    dibujadas = set()

    for punto, vecinos in red.items():
        for vecino, costo in vecinos.items():
            clave = tuple(sorted((punto, vecino)))

            if clave in dibujadas:
                continue

            dibujadas.add(clave)
            x1, y1 = ubicacion[punto]
            x2, y2 = ubicacion[vecino]

            es_usada = clave in usadas
            color = "#be123c" if es_usada else "#9ca3af"
            ancho = 5 if es_usada else 2

            partes.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{ancho}' />")
            partes.append(f"<text x='{(x1+x2)//2}' y='{(y1+y2)//2 - 8}' font-size='13'>{costo}</text>")

    for punto, (x, y) in ubicacion.items():
        partes.append(f"<circle cx='{x}' cy='{y}' r='28' fill='#fce7f3' stroke='#9d174d' stroke-width='3' />")
        partes.append(f"<text x='{x}' y='{y+5}' text-anchor='middle' font-size='10'>{punto}</text>")

    partes.extend(["</svg>", "</body>", "</html>"])

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(partes))


if __name__ == "__main__":
    # Red de ejemplo. Los nombres representan zonas de una empresa.
    # Los valores representan el costo de conectar una zona con otra.
    red_empresa = {
        "Entrada": {"Oficina": 6, "Almacen": 3},
        "Oficina": {"Entrada": 6, "Almacen": 2, "Calidad": 5},
        "Almacen": {"Entrada": 3, "Oficina": 2, "Produccion": 7},
        "Calidad": {"Oficina": 5, "Produccion": 4, "Embarque": 6},
        "Produccion": {"Almacen": 7, "Calidad": 4, "Embarque": 2},
        "Embarque": {"Calidad": 6, "Produccion": 2},
    }

    conexiones, costo_total, bitacora = prim_red_lugares(red_empresa, "Entrada")

    imprimir_practica(conexiones, costo_total, bitacora)
    crear_html(red_empresa, conexiones, "resultado_prim_elsy.html")

    print("\nSe creo el archivo visual: resultado_prim_elsy.html")
