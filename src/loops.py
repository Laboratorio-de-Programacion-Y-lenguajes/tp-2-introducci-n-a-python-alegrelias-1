# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    try:
        limite = int(n)
        if limite <= 0:
            return []
        if limite > 10000:
            limite = 10000
        return list(range(1, limite + 1))
    except (ValueError, TypeError):
        return []


def tabla_multiplicar(n: float, cantidad: int = 10) -> list:
    try:
        base = int(round(float(n)))
        if base == 0:
            return ["Error: La base de la tabla no puede ser cero."]
        return [base * i for i in range(1, cantidad + 1)]
    except (ValueError, TypeError):
        return ["Error: Entrada no válida para la tabla."]


def suma_digitos(n: int) -> int | str:
    try:
        num = abs(int(n))
        if num >= 10**10:
            return "Error: El número supera el límite de 10 dígitos."
        suma = 0
        while num > 0:
            suma += num % 10
            num //= 10
        return suma
    except (ValueError, TypeError):
        return "Error: Entrada no válida. Debe ser un número entero."


def es_primo(n: int) -> bool:
    try:
        num = int(n)
        if num < 2:
            return False
        if num > 10000000:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    except (ValueError, TypeError):
        return False


def fibonacci(n: int) -> list | str:
    try:
        limite = int(n)
        if limite <= 0:
            return []
        if limite > 500:
            return "Error: El límite máximo para la serie de Fibonacci es 500 por razones de performance."
        
        resultado = []
        a, b = 0, 1
        for _ in range(limite):
            resultado.append(a)
            a, b = b, a + b
        return resultado
    except (ValueError, TypeError):
        return "Error: Entrada no válida. Se esperaba un número entero."
