# -*- coding: utf-8 -*-
"""
Fase 4 (parte 1): Salida.
Arma el texto final con puntajes, preferencia y recomendaciones.
Lo usan tanto la consola como la interfaz de tkinter.
"""
from base_conocimiento import (
    hechos, SUJETO, TEXTOS, NOMBRES_PREFERENCIA, NOMBRES_MODALIDAD, AVISO,
    FUENTE_DE_REC, SUJETO_VARK, NOMBRES_RECURSO,
)
from motor_inferencia import contar_puntajes, generar_hechos, inferir
from hechos import buscar, objetos_de


# ============================================================
# SALIDA
# ============================================================
def obtener_recomendaciones(sujeto=SUJETO):
    """Devuelve (preferencias, recomendaciones) a partir de los hechos.
    Cada recomendación es (texto, fuente): la fuente es la referencia bibliográfica
    que se le muestra al usuario junto a la recomendación."""
    preferencias = [n for h, n in NOMBRES_PREFERENCIA.items() if (h, sujeto) in hechos]
    # Se recorre TEXTOS (en el orden en que fue escrito) para que la salida sea estable
    recomendaciones = [(texto, FUENTE_DE_REC[h]) for h, texto in TEXTOS.items()
                       if (h, sujeto) in hechos]
    return preferencias, recomendaciones


def obtener_recursos(sujeto=SUJETO):
    """Recursos asociados a cada preferencia detectada, tomados de los hechos
    F2 a F5 de hechos.py. Devuelve [(nombre_preferencia, [recursos])]."""
    recursos = []
    for h, nombre in NOMBRES_PREFERENCIA.items():
        if (h, sujeto) not in hechos:
            continue
        for hecho in buscar("se_relaciona_con", SUJETO_VARK[h]):
            recursos.append((nombre, [NOMBRES_RECURSO.get(r, r.replace("_", " ")) for r in objetos_de(hecho)]))
    return recursos


def formatear_resultado(puntajes):
    """Arma el texto final (lo usan la consola y tkinter)."""
    preferencias, recomendaciones = obtener_recomendaciones()
    lineas = []
    lineas.append("PUNTAJES: " + ", ".join(f"{NOMBRES_MODALIDAD[m]}: {p}" for m, p in puntajes.items()))
    if (("hay_empate", SUJETO) in hechos):
        lineas.append("PERFIL: Multimodal (" + " / ".join(preferencias) + ")")
    else:
        lineas.append("PREFERENCIA PREDOMINANTE: " + ", ".join(preferencias))
    recursos = obtener_recursos()
    if recursos:
        lineas.append("RECURSOS ASOCIADOS (VARK):")
        for nombre, lista in recursos:
            lineas.append(f"  {nombre}: " + ", ".join(lista))
    lineas.append("")
    lineas.append("RECOMENDACIONES:")
    for i, (texto, fuente) in enumerate(recomendaciones, 1):
        lineas.append(f"  {i}. {texto}")
        lineas.append(f"     Fuente: {fuente}")
    lineas.append("")
    lineas.append(AVISO)
    return "\n".join(lineas)


def evaluar(respuestas, mostrar_trazas=False):
    """Función única que ejecuta todo el sistema (se reutiliza en tkinter)."""
    puntajes, contexto = contar_puntajes(respuestas)
    generar_hechos(puntajes, contexto)
    inferir(mostrar=mostrar_trazas)
    return puntajes, formatear_resultado(puntajes)