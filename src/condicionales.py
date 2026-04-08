# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    if n > 0:
        return 'positivo'
    elif n < 0:
        return 'negativo'
    else:
        return 'cero'


def mayor_de_tres(a: int, b: int, c: int) -> int:
    return max(a, b, c)


def clasificar_nota(nota: float) -> str:
    if nota < 0 or nota > 10:
        return "ERROR: La nota ingresada es inválida. Debe ser un valor numérico entre 0 y 10."
    elif nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    if not isinstance(anio, int):
        raise TypeError("El año debe ser un número entero.")
    if anio <= 0:
        raise ValueError("El año ingresado debe ser mayor a cero.")
        
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
