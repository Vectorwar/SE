# -*- coding: utf-8 -*-
"""
Sistema experto: recomendador de técnicas de estudio
Instituto Tecnológico de Ensenada - Programación Lógica

Estructura del proyecto:
    cuestionario.py       -> preguntas y opciones
    base_conocimiento.py  -> hechos, reglas y textos
    motor_inferencia.py   -> puntajes, hechos e inferencia
    salida.py             -> formato del resultado
    interfaz.py           -> interfaz gráfica (tkinter)
    main.py               -> este archivo: arranca todo
"""
import sys

from cuestionario import PREGUNTAS
from motor_inferencia import contar_puntajes, generar_hechos, inferir
from salida import formatear_resultado


# ============================================================
# MODO CONSOLA
# ============================================================
def preguntar(pregunta, numero):
    """Muestra una pregunta, valida la opción elegida y devuelve su valor."""
    print(f"\n{numero}. {pregunta['texto']}")
    for i, (texto, _) in enumerate(pregunta["opciones"], 1):
        print(f"   {i}) {texto}")
    while True:
        entrada = input("   Tu respuesta: ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= len(pregunta["opciones"]):
            return pregunta["opciones"][int(entrada) - 1][1]
        print("   Opción no válida, intenta de nuevo.")


def modo_consola():
    print("=== Sistema experto: técnicas de estudio ===")
    respuestas = [preguntar(p, n) for n, p in enumerate(PREGUNTAS, 1)]

    # Se muestra el razonamiento del motor (qué reglas se cumplieron)
    print("\n--- Razonamiento del motor de inferencia ---")
    puntajes, contexto = contar_puntajes(respuestas)
    generar_hechos(puntajes, contexto)
    inferir(mostrar=True)

    print("\n--- Resultado ---")
    print(formatear_resultado(puntajes))


# ============================================================
# MODO GRÁFICO
# ============================================================
def modo_grafico():
    # La importación va aquí adentro para que el modo consola funcione
    # aunque tkinter no esté instalado.
    try:
        from interfaz import App
    except ImportError as error:
        print(f"No se pudo abrir la interfaz gráfica ({error}).")
        print("Continuando en modo consola...\n")
        modo_consola()
        return
    App().mainloop()


# ============================================================
# ARRANQUE
# ============================================================
def main():
    if "--consola" in sys.argv:
        modo_consola()
    else:
        modo_grafico()


if __name__ == "__main__":
    main()
