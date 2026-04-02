# COMPARACIO-CYK-ALGORITMOLINEAL


**INTRODUCCION**

Este proyecto compara el rendimiento real entre el Algoritmo CYK $$(O(n^3))$$ y el analizador Bison (LALR). A través de un programa automatizado en Python, se miden los tiempos de ejecución de ambos métodos al procesar expresiones cada vez más largas, demostrando cómo Bison mantiene una eficiencia lineal frente al crecimiento exponencial de CYK. Además, el sistema permite ingresar operaciones matemáticas mediante un archivo de texto para generar automáticamente sus árboles sintácticos usando la librería Lark y Graphviz.

**COMO EJECUTARLO**

PASO 1-Compilación del Parser (Bison)

Primero, debemos generar el ejecutable de C que el script de Python utilizará para las mediciones de tiempo:

```bash
flex lexer.l

bison -d parser.y
```
PASO 2-Compilar el ejecutable final
```bash
gcc lex.yy.c parser.tab.c -o bison_parser
```

PASO 3-Ejecución del programa Python

```bash
python3 comparador.py
```

**DESCRIPCION DE LOS CODIGOS**

1.Motor C (Flex & Bison)

Esta es la parte encargada de la velocidad bruta. Usamos Flex para despedazar la entrada en piezas pequeñas (tokens) y Bison para validar que esas piezas formen una operación matemática válida. Como está escrito en C y usa algoritmos de tabla, procesa miles de datos en una fracción de milisegundo. Es el estándar que usan los lenguajes de programación reales por su eficiencia lineal $O(n)$.

2.El comparador de rendimiento (comparador.py)

Este script es el cerebro de las pruebas. Aquí programamos a mano el Algoritmo CYK $$(O(n^3))$$ para ver cómo se comporta frente a Bison. El script lanza pruebas automáticas: crea operaciones cada vez más largas, se las pasa a Bison, luego las corre en CYK y mide cuánto tarda cada uno. Al final, te escupe una gráfica que muestra cómo CYK se rinde ante entradas grandes mientras Bison ni se despeina.

**RESULTADOS Y PRUEBA**

Pusimos a prueba ambos métodos con expresiones cada vez más largas para ver en qué punto el algoritmo CYK ($O(n^3)$) empezaba a sufrir. Los resultados en la terminal de Ubuntu son claros:


