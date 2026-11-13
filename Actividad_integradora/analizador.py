import matplotlib.pyplot as plt

def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def main():
    ruta = "texto_integradora.txt"

    # Lectura del archivo con try/except (Clase 2)
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no fue encontrado.")
        return

    # Conteo de frecuencias (Clase 2 y 4)
    frecuencias = contar_frecuencias(texto)

    # Seleccion del top 10 de palabras mas frecuentes (Clase 2 y 3)
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]

    # Separacion en dos listas usando comprension de listas (Clase 3)
    palabras = [par[0] for par in top10]
    valores = [par[1] for par in top10]

    # Generacion y guardado del grafico de barras (Clase 3)
    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title("Top 10 palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    print("Grafico generado con exito como 'grafico_frecuencias.png'.")

if __name__ == "__main__":
    main()