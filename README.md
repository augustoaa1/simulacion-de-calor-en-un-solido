# Simulación de calor en un sólido (Python)

Este proyecto consiste en una simulación sencilla en Python del calor absorbido
por un cuerpo sólido (cobre) cuando su temperatura aumenta.

El objetivo principal del código es **practicar conceptos básicos de programación**
aplicados a la física.

## Conceptos de programación utilizados

- Definición de variables
- Uso de bucles `while`
- Condiciones de parada
- Operaciones aritméticas
- Impresión de resultados en pantalla

## Modelo físico

Se utiliza la expresión del calor sensible:

Q = m · c · (Tf − Ti)

donde:
- Q es el calor absorbido (J)
- m es la masa del cuerpo (g)
- c es el calor específico del cobre
- Ti es la temperatura inicial (°C)
- Tf es la temperatura final (°C)

La simulación incrementa la temperatura final en pasos discretos de 10 °C
hasta que el calor absorbido supera los 100000 J.

## Consideraciones y simplificaciones

- El movimiento térmico se modela de forma unidimensional.
- El calor específico se considera constante.
- No se tienen en cuenta pérdidas de calor al entorno.
- No se consideran cambios de fase.
- El objetivo del código es didáctico y no un modelo físico completo.

