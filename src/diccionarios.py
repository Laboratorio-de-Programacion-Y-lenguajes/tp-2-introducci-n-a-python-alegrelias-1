def contar_palabras(texto: str) -> dict:
    frecuencias = {}
    for palabra in texto.lower().split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def invertir_diccionario(d: dict) -> dict:
    return {valor: clave for clave, valor in d.items()}


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    return d1 | d2


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    return {k: v for k, v in d.items() if v >= minimo}