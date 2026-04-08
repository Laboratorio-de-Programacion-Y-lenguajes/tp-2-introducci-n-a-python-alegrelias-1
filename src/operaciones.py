# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto_limpio == texto_limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    return " ".join(palabra.capitalize() for palabra in texto.split())


def contar_vocales(texto: str) -> int:
    vocales = "aeiou"
    return sum(1 for caracter in texto.lower() if caracter in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    resultado = []
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            base = ord('a')
            nuevo = chr(base + (ord(caracter) - base + desplazamiento) % 26)
            resultado.append(nuevo)
        elif 'A' <= caracter <= 'Z':
            base = ord('A')
            nuevo = chr(base + (ord(caracter) - base + desplazamiento) % 26)
            resultado.append(nuevo)
        else:
            resultado.append(caracter)
    return "".join(resultado)
