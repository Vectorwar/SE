# -*- coding: utf-8 -*-
"""Hechos del sistema experto
Se usaran tuplas por que un hecho no cambia una vez registrado, debido
a su inmutabilidad. Se guardan en un set para que no haya repetidos y
estas cuentan con la forma (id, relacion, sujeto, objeto).

Este modulo NO depende de otros archivos del proyecto: lo importa salida.py.
"""

# Hechos de dominio (se agregan al iniciar el programa)
# Son los que obtuvimos de las fuentes bibliograficas

HECHOS_DOMINIO = {

    #Estas son las tuplas que representan los hechos del dominio del sistema experto. Cada hecho tiene un identificador único, 
    #una relación, un sujeto y un objeto. Los hechos se utilizan para inferir conclusiones sobre las preferencias de aprendizaje 
    #y las técnicas de estudio.

    # F1: el modelo VARK clasifica las preferencias de aprendizaje.
    ("F1", "clasifica_en", "VARK",
        ("visual", "auditiva", "lectura_escritura", "kinestesica")),

    # F2: la preferencia visual se relaciona con recursos gráficos.
    ("F2", "se_relaciona_con", "visual",
        ("diagramas", "esquemas", "representaciones_graficas")),

    # F3: la preferencia auditiva se relaciona con la comunicación oral.
    ("F3", "se_relaciona_con", "auditiva",
        ("escuchar_explicaciones", "conversar_sobre_los_temas")),

    # F4: la preferencia kinestésica se relaciona con la práctica.
    ("F4", "se_relaciona_con", "kinestesica",
        ("actividades_practicas", "experiencias", "ejemplos")),

    # F5: la modalidad lectura/escritura se relaciona con las palabras y el texto.
    ("F5", "se_relaciona_con", "lectura_escritura",
        ("palabras", "textos")),

    # F6: no hay evidencia suficiente de que enseñar según un solo estilo mejore resultados.
    ("F6", "sin_evidencia_suficiente_de", "adaptar_ensenanza_a_un_solo_estilo",
        "mejores_resultados"),

    # F7: las pruebas de práctica ayudan a recordar y reforzar lo aprendido.
    ("F7", "ayuda_a", "pruebas_de_practica",
        ("recordar", "reforzar_conocimientos")),

    # F8: distribuir el estudio en varias sesiones mejora el aprendizaje.
    ("F8", "es_util_para", "estudio_distribuido",
        "mejorar_el_aprendizaje"),

    # F9: definición de autoexplicación.
    ("F9", "consiste_en", "autoexplicacion",
        "explicar_con_palabras_propias_conceptos_y_procedimientos"),

    # F10: releer y subrayar no siempre bastan.
    ("F10", "no_siempre_es_suficiente_para", "releer_y_subrayar",
        "aprendizaje_efectivo"),
}


# Funciones de consulta

def _numero(hecho):
    """Orden natural de los ids: F1, F2, ..., F10 (no F1, F10, F2)."""
    return int(hecho[0][1:])


def buscar(relacion=None, sujeto=None):
    """Nos devolvera los hechos del dominio que coinciden con la relacion y el sujeto.
    Si un parametro es None, no se filtra por el."""
    encontrados = [h for h in HECHOS_DOMINIO
                   if (relacion is None or h[1] == relacion)
                   and (sujeto is None or h[2] == sujeto)]
    return sorted(encontrados, key=_numero)


def objetos_de(hecho):
    """El objeto de un hecho puede ser una tupla o un solo texto;
    esta funcion siempre lo devuelve como tupla."""
    objeto = hecho[3]
    return objeto if isinstance(objeto, tuple) else (objeto,)


# Prueba de funcionamiento (solo se ejecuta con:  python hechos.py)

if __name__ == "__main__":
    # Ejemplos de hechos de usuario, solo para pruebas
    hechos_prueba = {
        ("predomina_visual", "Jose"),
        ("examen_proximo", "Irma"),
        ("varios_dias", "Annete"),
    }

    if ("predomina_visual", "Jose") in hechos_prueba:
        print("Jose tiene preferencia visual\n")

    print("Hechos sobre la preferencia visual:")
    for h in buscar("se_relaciona_con", "visual"):
        print(" ", h[0], "->", h[3])
