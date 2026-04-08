# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    if not isinstance(numeros, list):
        raise TypeError("El argumento debe ser una lista.")
    
    if not numeros:
        return 0.0
    
    try:
        resultado = sum(numeros)
        return resultado
    except TypeError:
        raise TypeError("La lista debe contener únicamente números (int o float).")


def filtrar_pares(numeros: list) -> list:
    if not isinstance(numeros, list):
        raise TypeError("El argumento debe ser una lista.")
    
    try:
        return [n for n in numeros if n % 2 == 0]
    except TypeError:
        raise TypeError("La lista debe contener únicamente números para calcular la paridad.")


def invertir_lista(lista: list) -> list:
    lista_auxiliar = lista.copy()
    
    lista_auxiliar.reverse()
    
    return lista_auxiliar

def eliminar_duplicados(lista: list) -> list:
    return list(dict.fromkeys(lista))


def aplanar_lista(lista: list) -> list:
    resultado = []
    for elemento in lista:
        # Verificamos si el elemento es una lista para volver a aplanar
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            # Si es un elemento solo, lo agregamos directamente
            resultado.append(elemento)
    return resultado
