# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**:Gemini 

**Prompt usado**:
Quiero que completes cada una de las funciones sin implementar, presta atención a los comentarios dentro de las funciones y sigue sus instrucciones al pie de la letra, luego elimina los comentarios (ya sean comentarios con comillas o con numerales, deja el codigo limpio)
> 

**Resultado obtenido**:
```py
def crear_saludo(nombre: str) -> str:
    return f"Hola, {nombre}!"

def suma_enteros(a: int, b: int) -> int:
    return a + b

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def tipo_de_dato(valor) -> str:
    return type(valor).__name__

def convertir_a_float(valor: str) -> float:
    return float(valor)
```

**¿Lo usaste tal cual o lo modificaste?**: No hice cambios

---

### 2 - condicionales.py

### Ejercicio 1: Clasificar Número (`evaluar_numero`)

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que clasifique un numero automaticamente. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: Activación del patrón de Interacción Invertida. La IA generó preguntas de aclaración sobre los criterios matemáticos, el formato exacto del texto de retorno y el manejo del cero. Una vez respondidas las preguntas, se obtuvo el código exacto de la función `evaluar_numero(n: int) -> str` con la estructura `if/elif/else` necesaria.

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### Ejercicio 1: Mayor de tres

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que calcule el mayor de tres números. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: La IA solicitó confirmar los tipos de datos de las variables, el comportamiento esperado en caso de empate y si estaba permitido el uso de funciones nativas. Tras responder, devolvió la función `mayor_de_tres(a, b, c)` resuelta de manera óptima utilizando `max()`.

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### Ejercicio 2: Clasificar Nota

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que clasifique una nota automaticamente. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: La IA preguntó por la escala de notas válida, los textos exactos a retornar para cada rango y cómo manejar valores fuera de la escala. El resultado fue la función `clasificar_nota(nota: float) -> str` que evalúa los rangos solicitados y retorna un mensaje de error específico si el número no está entre 0 y 10.

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### Ejercicio 3: Año Bisiesto

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que verifique si un año es o no bisiesto. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: Consultas de la IA sobre la regla matemática a aplicar (estándar gregoriana) y el manejo de años inválidos. Se obtuvo la función `es_bisiesto(anio: int) -> bool` con la lógica matemática correcta y validaciones mediante el levantamiento de excepciones (`raise TypeError` y `raise ValueError`).

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.


---

### 3 - listas.py

**Herramienta**: Gemini

**Prompt usado**:
> Tengo que escribir una funciones en Python: que Dada una lista de listas, retorna todos los elementos en una sola lista. Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]. Mi lógica es utilizar el metodo chain() de python. [Requerimientos: anidamiento multinivel, elementos solos permitidos, sin librerías externas].

**Resultado obtenido**:
```python
def aplanar_lista(lista: list) -> list:
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)
    return resultado
```
**¿Lo usaste tal cual o lo modificaste?**
Se usó tal cual. Se validó la inicialización del producto en 1 para evitar que el resultado fuera siempre 0.

PD: Habia mas prompts pero le pedi a la IA que olvide una solicitud que le hice y BORRO TODA LA CONVERSACION antes de esa solicitud.
---

### 4 - diccionarios.py

**Herramienta**: Gemini

**Prompt usado**:
> Aplicá la Estrategia de Generación Infinita: Generá 10 ejemplos de diccionarios en Python que representen palabras con valores diversos. Luego, completá las funciones contar_palabras, invertir_diccionario, merge_diccionarios y filtrar_por_valor siguiendo las instrucciones detalladas, eliminando comentarios y docstrings para dejar el código limpio.

**Resultado obtenido**:
```py
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
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. La estrategia de generación previa permitió entender la versatilidad de los valores en los diccionarios. Se optó por el operador | para el merge y comprensiones de diccionario para el filtrado e inversión, priorizando la sintaxis moderna de Python 3.13 y la eficiencia $O(n)$.


---

### 5 - loops.py

### Ejercicio 1
**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función contar_hasta(n: int) -> list que retorne una lista con los números del 1 al n (inclusive). Pero antes de escribir el código, haceme preguntas clave para que la función sea lo más robusta posible para un entorno de producción. [Respuestas: 1. Lista vacía para n <= 0, 2. Conversión de tipos con manejo de excepciones, 3. Límite de 10,000 valores, 4. Rango inclusivo].

**Resultado obtenido**:
```py
def contar_hasta(n: int) -> list:
    try:
        limite = int(n)
        if limite <= 0: return []
        if limite > 10000: limite = 10000
        return list(range(1, limite + 1))
    except (ValueError, TypeError):
        return []
```


**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. El refinamiento permitió establecer un "techo" de seguridad (10k) para evitar desbordamientos de memoria en el servidor de autograding.

### Ejercicio 2
**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función tabla_multiplicar(n: int) -> list que retorne una lista con los primeros 10 múltiplos de n. Pero antes de escribir el código, haceme preguntas clave para que la función sea lo más robusta posible. [Respuestas: 1. Error detallado para n=0, 2. Permitir progresión negativa, 3. Redondear floats, 4. Cantidad como parámetro opcional].

**Resultado obtenido**:
```py
def tabla_multiplicar(n: float, cantidad: int = 10) -> list:
    try:
        base = int(round(float(n)))
        if base == 0: return ["Error: La base no puede ser cero."]
        return [base * i for i in range(1, cantidad + 1)]
    except (ValueError, TypeError):
        return ["Error: Entrada no válida."]
```


**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. La decisión de usar round() en lugar de truncar con int() mejora la precisión esperada por un usuario final al ingresar decimales.

### Ejercicio 3
**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función suma_digitos(n: int) -> int que retorne la suma de los dígitos de un número entero positivo. Pero antes de escribir el código, haceme preguntas clave. [Respuestas: 1. Usar valor absoluto, 2. Enfoque matemático (módulo/división), 3. Manejo de excepciones, 4. Límite de 10 dígitos].

**Resultado obtenido**:
```py
def suma_digitos(n: int) -> int | str:
    try:
        num = abs(int(n))
        if num >= 10**10: return "Error: Supera el límite de 10 dígitos."
        suma = 0
        while num > 0:
            suma += num % 10
            num //= 10
        return suma
    except (ValueError, TypeError):
        return "Error: Entrada no válida."
```


**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se priorizó el enfoque matemático sobre el uso de strings para demostrar un manejo eficiente de recursos de CPU ($O(\text{dígitos})$).

### Ejercicio 4
**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función es_primo(n: int) -> bool que retorne True si n es un número primo. Antes, haceme preguntas clave. [Respuestas: 1. False para n < 2, 2. Máxima eficiencia (raíz cuadrada), 3. Intentar conversión de tipos, 4. Límite de 10M].

**Resultado obtenido**:
```py
def es_primo(n: int) -> bool:
    try:
        num = int(n)
        if num < 2: return False
        if num == 2: return True
        if num % 2 == 0: return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0: return False
        return True
    except (ValueError, TypeError):
        return False
```

### Ejercicio 5
**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función fibonacci(n: int) -> list que retorne los primeros n números de la serie. Antes, haceme preguntas clave. [Respuestas: 1. Excepción detallada, 2. Enfoque iterativo, 3. Límite de 500, 4. Intento de conversión].

**Resultado obtenido**:
```py
def fibonacci(n: int) -> list | str:
    try:
        limite = int(n)
        if limite <= 0: return []
        if limite > 500: return "Error: Límite máximo 500."
        resultado, a, b = [], 0, 1
        for _ in range(limite):
            resultado.append(a)
            a, b = b, a + b
        return resultado
    except (ValueError, TypeError):
        return "Error: Entrada no válida."
```


**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. El enfoque iterativo garantiza que no se alcance el límite de recursión de Python al procesar hasta 500 términos.

---

### 6 - funciones.py
### Ejercicio 1
**Herramienta**: Gemini

**Prompt usado**:
> Necesito una función contar_palabra(texto: str, palabra: str) -> int en Python 3.13. Cada vez que generes una respuesta, explicame el razonamiento y asunciones detrás de la selección de frameworks. De ser posible utilizá ejemplos o evidencia asociados a muestras de código para apoyar tu respuesta sobre por qué el framework es la mejor opción para determinada tarea.

**Resultado obtenido**:
```py
def contar_palabra(texto: str, palabra: str) -> int:
    texto_limpio = texto.lower()
    palabra_buscada = palabra.lower()
    listado_palabras = texto_limpio.split()
    return listado_palabras.count(palabra_buscada)
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. El razonamiento para elegir la librería estándar fue evitar dependencias pesadas como NLTK. Se optó por .split() en lugar de .count() sobre el string para evitar falsos positivos con subcadenas (ej. "sol" en "soldado").

### Ejercicio 2
**Herramienta**: Gemini

**Prompt usado**:
> Necesito una función aplicar_funcion(lista: list, func) -> list en Python 3.13. Aplica func a cada elemento de la lista y retorna la nueva lista. Verifica que pase el siguiente test: assert aplicar_funcion([1, 2, 3], lambda x: x * 2) == [2, 4, 6]. Explicame el razonamiento y asunciones detrás de la selección de frameworks.

**Resultado obtenido**:
```py
def aplicar_funcion(lista: list, func) -> list:
    return [func(elemento) for elemento in lista]
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se seleccionó la List Comprehension de Python nativo por sobre map() o librerías como NumPy. La asunción es que para el volumen de datos del TP, la sintaxis nativa es más legible y eficiente al no requerir la carga de módulos externos.

### Ejercicio 3
**Herramienta**: Gemini

**Prompt usado**:
> Necesito una función componer(f, g) en Python 3.13. Retorna una nueva función que aplica g y luego f. Ejemplo: componer(f, g)(x) == f(g(x)). Explicame el razonamiento y asunciones detrás de la selección de frameworks.

**Resultado obtenido**:
```py
def componer(f, g):
    def funcion_compuesta(x):
        return f(g(x))
    return funcion_compuesta
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se utilizó el concepto de Closures nativos de Python. Se asumió que no es necesario usar frameworks de programación funcional como toolz ya que Python trata a las funciones como objetos de primera clase, permitiendo capturar el estado de f y g de forma eficiente.

### Ejercicio 4
**Herramienta**: Gemini

**Prompt usado**:
> Necesito una función memoizar(func) en Python 3.13. Retorna una versión de func que cachea sus resultados. Si se llama con los mismos argumentos, retorna el resultado cacheado. Explicame el razonamiento y asunciones detrás de la selección de frameworks.

**Resultado obtenido**:
```py
def memoizar(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.


### Ejercicio 5
**Herramienta**: Gemini

**Prompt usado**:
> Necesito una función reducir(lista: list, func, inicial) en Python 3.13. Aplica func acumulativamente a los elementos de lista, comenzando con inicial. Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6. NO uses functools.reduce. Explicame el razonamiento y asunciones detrás de la selección de frameworks.

**Resultado obtenido**:
```py
def reducir(lista: list, func, inicial):
    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### 7 - operaciones.py

### Ejercicio 1

**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función es_palindromo(texto: str) -> bool. Realizá una lista con las mejores alternativas comparando los pros y contras de cada enfoque con respecto a eficiencia, velocidad y legibilidad. Luego, implementá la versión elegida limpiando comentarios y docstrings.

**Resultado obtenido**:
```py
def es_palindromo(texto: str) -> bool:
    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto_limpio == texto_limpio[::-1]
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se compararon enfoques de slicing, iterativos (dos punteros) y funcionales. Se optó por el slicing por su balance entre legibilidad y la optimización nativa de Python para el manejo de cadenas, sumando una normalización con isalnum().

### Ejercicio 2

**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función capitalizar_palabras(texto: str) -> str. Debe capitalizar la primera letra de cada palabra. Realizá una lista con las mejores alternativas comparando los pros y contras con respecto a eficiencia, velocidad y legibilidad. Luego, implementá la versión elegida limpiando comentarios y docstrings.

**Resultado obtenido**:
```py
def capitalizar_palabras(texto: str) -> str:
    return " ".join(palabra.capitalize() for palabra in texto.split())
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se descartó el método .title() debido a comportamientos inesperados con apóstrofes. El uso de .split() con .capitalize() resultó ser el enfoque más robusto para un entorno de producción, garantizando que solo la primera letra de cada término sea afectada.

### Ejercicio 3

**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función contar_vocales(texto: str) -> int. Debe retornar la cantidad de vocales (a,e,i,o,u) en el texto, sin distinguir mayúsculas/minúsculas. Realizá una lista con las mejores alternativas comparando pros y contras. Luego, implementá la versión elegida.

**Resultado obtenido**:
```py
def contar_vocales(texto: str) -> int:
    vocales = "aeiou"
    return sum(1 for caracter in texto.lower() if caracter in vocales)
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se seleccionó el enfoque de expresión generadora con sum() debido a su eficiencia de memoria ($O(1)$ de espacio extra) y su estilo "Pythonic", superando en legibilidad a las expresiones regulares para una tarea de conteo simple.

### Ejercicio 4

**Herramienta**: Gemini

**Prompt usado**:
> Quiero hacer una función caesar_cipher(texto: str, desplazamiento: int) -> str. Debe aplicar el cifrado César al texto (a-z, A-Z). Realizá una lista con las mejores alternativas comparando pros y contras. Luego, implementá la versión elegida limpiando comentarios.

**Resultado obtenido**:
```py
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
```

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual. Se analizó el uso de tablas de traducción (maketrans) frente a aritmética modular. Se eligió la aritmética modular por su precisión pedagógica y flexibilidad para manejar desplazamientos variables sin pre-procesamiento de alfabetos.

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
