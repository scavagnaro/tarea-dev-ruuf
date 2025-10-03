# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Analizando el problema, se identificó que el principal inconveniente son los espacios vacíos que pueden quedar al simplemente añadir una fila de paneles de un tamaño determinado.

Por ejemplo, con un techo 3x4 y paneles A de 1x3, si simplemente coloco los paneles uno arriba del otro, quedará una columna vacía al final.

AAAX <br>
AAAX <br>
AAAX

Pero lo óptimo es aprovechar el espacio que queda en la columna final, dado que en ese espacio cabe otro panel.

Esto llevó a pensar que si sobra un espacio de techo, este puede ser tratado de manera equivalente a un techo del mismo tamaño. Es decir, el techo 3x4 puede ser separado en dos techos: 3x3 y 3x1 para el panel dado. Esto significa que se puede reducir el problema al separarlo por sus partes individuales.

Para un problema pequeño, es fácil imaginar cómo se podría separar en partes. Pero mientras el problema crece, se vuelve necesario encontrar un algoritmo que permita buscar una buena combinación de techos, que se acerque al óptimo.

Se creó el siguiente algoritmo recursivo para esto:

    1. En la primera fila del techo, se obtienen cuántos paneles caben, y se vuelve a llamar a la función de forma recursiva para el techo sobrante.
    2. Se repite el paso 1, pero rotando el panel 90°.
    3. Se repite el paso 1, pero rotando el techo 90°.
    4. Se repite el paso 1, pero rotando el techo 90° y el panel 90°.
    5. Se retorna el máximo entre las cuatro alternativas.

Al aplicarlo al techo completo, el algoritmo va a avanzar hasta la última fila, ver si es preferible el panel normal o rotarlo, e ir retrocediendo hasta completar el techo. Cuando llega al inicio, ya tiene el óptimo encontrado de todos los subtechos, lo que permite hacer lo mismo para el techo inicial.

La solución fue implementada usando programación dinámica. Esto implica ir guardando el resultado de la función, para reducir el consumo computacional y acelerar el proceso.

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado

Opción 1: Techo triangular

### Solución en Python
```bash
cd python
python3 triangle.py
```

### Explicación del Bonus

Primero, hay que considerar que los triangulos isoceles pueden se recortados. Es decir, si se traza una linea paralela a la base dentro del triangulo isoceles, se obtiene un nuevo triángulo isósceles más pequeño en la parte superior, y un trapecio en la parte inferior. El trapecio puede ser recortado para formar un rectángulo, lo cual nos da el area útil del techo en la que colocar los paneles.

El algoritmo aplicado es similar al del rectángulo.
    1. En la base del triangulo, se obtienen cuántos paneles caben, y se vuelve a llamar a la función de forma recursiva para el techo sobrante.
    2. Se repite el paso 1, pero rotando el panel 90°.
    3. Se retorna el máximo entre las dos alternativas.

Usando esto de forma recursiva, se va subiendo hasta la punta del triángulo, donde ya no caben paneles. Al ir retrocediendo, se va obteniendo el óptimo para cada sección del triángulo, hasta llegar a la base.

Importante tomar en cuenta que para obtener el largo de la base del triángulo en cada nivel, se uso trigonometría.

---

## 🤔 Supuestos y Decisiones

*[Si tuviste que tomar algún supuesto o decisión de diseño, explícalo aquí]*

- Estaba la opción de hacerlo como array, y hacer una fuerza bruta de todas las opciones posibles, o incluso hacer backtracking dentro del array.
No quise hacerlo de esta manera, por dos razones principales:
    1. Una solución con listas dificultaría el uso de decimales. Me fijé que el tipeo de Python y de TS indica que el problema es solo para enteros, pero me hizo mucho ruido esto, ya que lo dificultaría para usar medidas como centímetros, pulgadas o yardas. Es por esto que preferí que el algoritmo soportara decimales.
    2. El uso de arrays me pareció que podría ser exponencial en memoria. Al mantenerlo como código funcional, puedo guardar el resultado de las funciones y acelerar el proceso.
