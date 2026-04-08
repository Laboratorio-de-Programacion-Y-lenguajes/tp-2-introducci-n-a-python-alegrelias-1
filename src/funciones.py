# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    return [func(elemento) for elemento in lista]


def componer(f, g):
    def funcion_compuesta(x):
        return f(g(x))
    
    return funcion_compuesta


def memoizar(func):
    cache = {}

    def wrapper(*args):
        # Usamos los argumentos como llave del diccionario
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper


def reducir(lista: list, func, inicial) -> int:
    acumulador = inicial
    
    for elemento in lista:
        # Aplicamos la función al acumulador actual y al elemento nuevo
        acumulador = func(acumulador, elemento)
        
    return acumulador
