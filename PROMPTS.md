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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
