# Simulador de la Jerarquía de Chomsky

Esta aplicación es una herramienta interactiva con Interfaz Gráfica de Usuario (GUI) desarrollada en Python, diseñada para visualizar, simular y validar el comportamiento paso a paso de los modelos computacionales representativos de los cuatro niveles de la Jerarquía de Chomsky.

## 🚀 Requisitos e Instalación

El proyecto está construido en Python y utiliza `customtkinter` para la interfaz gráfica.

1. **Clonar el repositorio:**
   ```bash
   git clone "https://github.com/JhoanG488/Simulador-jerarquia-chomsky"
   cd simulador-jerarquia-chomsky

2. **Crear y activar un entorno virtual (Recomendado en macOS/Linux):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Instalar dependencias:**
    ```bash
    pip install customtkinter

4. **Ejecutar la aplicación:**
    ```bash
    python3 main.py

## 🧪 Guía de Uso y Cadenas
Desde el panel principal, selecciona el nivel que deseas simular. Ingresa una de las cadenas de prueba, presiona **"Cargar"** y luego utiliza el botón **"Siguiente Paso"** para iterar a través del procesamiento del autómata.

**Nivel 3:**  Lenguajes Regulares (DFA)
**Lenguaje:** Expresión regular a*b* (cero o más 'a' seguidas de cero o más 'b').

Cadenas válidas: aabb, aab, bb, aaa

Cadenas inválidas: ba, aba, bba

**Nivel 2:** Lenguajes Libres de Contexto (PDA - Autómata de Pila)
**Lenguaje:** a^n b^n (misma cantidad de 'a' que de 'b', en ese orden).

Cadenas válidas: ab, aabb, aaabbb

Cadenas inválidas: aab, abb, baab

**Nivel 1:** Lenguajes Sensibles al Contexto (LBA - Autómata Linealmente Acotado)
**Lenguaje:** a^n b^n c^n (misma cantidad de 'a', 'b' y 'c', en ese orden).

Cadenas válidas: abc, aabbcc, aaabbbccc

Cadenas inválidas: aabcc, abbc, abcc

**Nivel 0:** Recursivamente Enumerables (MT - Máquina de Turing)
Lenguaje/Función: Suma unaria básica.

Cadenas válidas: 11+111 (resultado esperado: 11111), 1+1

Cadenas inválidas: 11-11, 11+, +11

## Detalles Técnicos por Autómata:
**DFA:** Implementado con un ciclo iterativo simple de transiciones de estados (q0, q1, q_error).

**PDA:** Utiliza una estructura de datos tipo Pila (list en Python usando append y pop) simulando la memoria LIFO. El símbolo Z0 representa el fondo de la pila.

**LBA:** Simula una cinta estrictamente acotada por los delimitadores virtuales [ y ]. Utiliza marcadores X, Y, Z para tachar los símbolos ya procesados mediante un cabezal bidireccional.

**Máquina de Turing:** Implementa una cinta dinámicamente expansible. Maneja símbolos en blanco (B) en los extremos, permitiendo al cabezal moverse sin límites para resolver la función de suma unaria reemplazando el operador y ajustando el resultado.