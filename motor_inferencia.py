# -*- coding: utf-8 -*-
"""
Fase 3: Motor de inferencia.
Convierte las respuestas en hechos y aplica las reglas por encadenamiento hacia adelante.
"""
from cuestionario import PREGUNTAS, MODALIDADES
from base_conocimiento import hechos, REGLAS, SUJETO


# ============================================================
# PROCESAMIENTO DE RESPUESTAS -> HECHOS
# ============================================================
def contar_puntajes(respuestas):
    """
    respuestas: lista de valores elegidos (uno por pregunta, en orden).
    Devuelve un diccionario con los puntos de cada modalidad
    y la lista de hechos de contexto.
    """
    puntajes = {m: 0 for m in MODALIDADES}
    contexto = []
    for pregunta, valor in zip(PREGUNTAS, respuestas):
        if pregunta["tipo"] == "estilo":
            puntajes[valor] += 1
        elif valor is not None:
            contexto.append(valor)
    return puntajes, contexto


def generar_hechos(puntajes, contexto):
    """
    Convierte los puntajes en hechos. Aquí se define el criterio
    de "principalmente" que faltaba en el documento:
        - Predomina(es) la modalidad con el puntaje máximo.
        - Si dos o más modalidades empatan en el máximo -> hay_empate
          (perfil multimodal) y cada modalidad empatada también predomina.
    """
    hechos.clear()
    maximo = max(puntajes.values())
    ganadoras = [m for m, p in puntajes.items() if p == maximo]

    for m in ganadoras:
        hechos.add((f"predomina_{m}", SUJETO))
    if len(ganadoras) > 1:
        hechos.add(("hay_empate", SUJETO))

    for c in contexto:
        hechos.add((c, SUJETO))


# ============================================================
# MOTOR DE INFERENCIA (encadenamiento hacia adelante)
# ============================================================
def inferir(sujeto=SUJETO, mostrar=True):
    """
    Recorre las reglas una y otra vez hasta que ya no se pueda
    deducir nada nuevo. Esto permite encadenar reglas
    (la conclusión de una puede activar a otra).
    Devuelve la lista de reglas disparadas: [(id, conclusion, condiciones)]
    """
    disparadas = []
    hay_cambios = True

    while hay_cambios:
        hay_cambios = False
        for id_regla, conclusion, condiciones in REGLAS:
            ya_deducida = (conclusion, sujeto) in hechos
            if ya_deducida:
                continue
            if all((condicion, sujeto) in hechos for condicion in condiciones):
                hechos.add((conclusion, sujeto))
                disparadas.append((id_regla, conclusion, condiciones))
                hay_cambios = True
                if mostrar:
                    print(f"Regla cumplida: {id_regla}", condiciones)
                    print("  conclusion:", sujeto, "->", conclusion)
    return disparadas
