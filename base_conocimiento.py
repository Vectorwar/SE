# -*- coding: utf-8 -*-
"""
Fase 2: Base de conocimiento.
Contiene los hechos (set compartido), las reglas SI-ENTONCES y los textos de salida.
"""

# ============================================================
# BASE DE CONOCIMIENTO
# ============================================================
# Los hechos tienen el mismo formato que en tu ejemplo:
#     (atributo, sujeto)   ->   ("predomina_visual", "usuario")
# Se guardan en un set (sin repetidos y búsqueda rápida).

SUJETO = "usuario"
hechos = set()   # Se llena con las respuestas del usuario y con la inferencia


# Cada regla es una tupla de 3 elementos:
#     (id, conclusion, condiciones)
# Es el mismo esquema "conclusion, condiciones" 
# pero con un id para poder identificar la regla.
#
# Las reglas se pueden ENCADENAR: la conclusión de una regla puede ser
# la condición de otra.

REGLAS = [
    # --- Preferencias (VARK) ---
    ("R1", "preferencia_visual", ("predomina_visual",)),
    ("R2", "preferencia_auditiva", ("predomina_auditivo",)),
    ("R3", "preferencia_kinestesica", ("predomina_kinestesico",)),
    ("R4", "preferencia_lectoescritura", ("predomina_lectoescritura",)),
    ("R5", "perfil_multimodal", ("hay_empate",)),

    # --- Recomendaciones según la preferencia ---
    ("R6", "rec_organizadores_graficos", ("preferencia_visual",)),
    ("R7", "rec_explicar_en_voz_alta", ("preferencia_auditiva",)),
    ("R8", "rec_ejercicios_practicos", ("preferencia_kinestesica",)),
    ("R9", "rec_notas_escritas", ("preferencia_lectoescritura",)),
    ("R10", "rec_combinar_estrategias", ("perfil_multimodal",)),

    # --- técnicas con evidencia (no dependen del estilo) ---
    ("R11", "rec_pruebas_de_practica", ("examen_proximo",)),
    ("R12", "rec_estudio_distribuido", ("varios_dias",)),
    ("R13", "rec_evitar_solo_releer", ("habito_releer_subrayar",)),
    ("R14", "rec_autoexplicacion", ("habito_releer_subrayar",)),

    # --- Reglas combinadas (estilo + contexto) ---
    ("R15", "rec_ejercicios_con_pruebas", ("preferencia_kinestesica", "examen_proximo")),
    ("R16", "rec_mapa_de_memoria", ("preferencia_visual", "examen_proximo")),
    ("R17", "rec_autoexplicacion_oral", ("preferencia_auditiva", "examen_proximo")),
    ("R18", "rec_preguntas_escritas", ("preferencia_lectoescritura", "examen_proximo")),
    ("R19", "rec_autoexplicacion_escrita", ("preferencia_lectoescritura", "habito_releer_subrayar")),
]

# FUENTES QUE SE MUESTRAN CON CADA RECOMENDACIÓN
# Referencias bibliográficas que se citan al usuario al final del cuestionario.
VARK = "VARK"
PASHLER = "Pashler et al. (2008)"
DUNLOSKY = "Dunlosky et al. (2013)"

FUENTES_REC = {
    "rec_organizadores_graficos":  (VARK,),
    "rec_explicar_en_voz_alta":    (VARK,),
    "rec_ejercicios_practicos":    (VARK,),
    "rec_notas_escritas":          (VARK,),
    "rec_combinar_estrategias":    (VARK, PASHLER),
    "rec_pruebas_de_practica":     (DUNLOSKY,),
    "rec_estudio_distribuido":     (DUNLOSKY,),
    "rec_evitar_solo_releer":      (DUNLOSKY,),
    "rec_autoexplicacion":         (DUNLOSKY,),
    "rec_ejercicios_con_pruebas":  (VARK, DUNLOSKY),
    "rec_mapa_de_memoria":         (VARK, DUNLOSKY),
    "rec_autoexplicacion_oral":    (VARK, DUNLOSKY),
    "rec_preguntas_escritas":      (VARK, DUNLOSKY),
    "rec_autoexplicacion_escrita": (VARK, DUNLOSKY),
}

# recomendación -> texto de la fuente, listo para mostrar (ej. "VARK; Dunlosky et al. (2013)")
FUENTE_DE_REC = {rec: "; ".join(fuentes) for rec, fuentes in FUENTES_REC.items()}

# Texto que se muestra al usuario por cada recomendación
TEXTOS = {
    "rec_organizadores_graficos":
        "Usa organizadores gráficos: mapas conceptuales, diagramas y esquemas de colores.",
    "rec_explicar_en_voz_alta":
        "Explica los contenidos en voz alta o estudia conversando con un compañero.",
    "rec_ejercicios_practicos":
        "Realiza ejercicios y actividades prácticas relacionadas con el tema.",
    "rec_notas_escritas":
        "Reescribe tus apuntes con tus propias palabras: elabora glosarios, listas y definiciones, y apóyate en libros y textos.",
    "rec_combinar_estrategias":
        "Tu perfil es mixto: combina esquemas, explicación oral y práctica según el tema.",
    "rec_pruebas_de_practica":
        "Haz cuestionarios y pruebas de práctica para repasar antes del examen.",
    "rec_estudio_distribuido":
        "Reparte tu estudio en varias sesiones en distintos días en lugar de una sola larga.",
    "rec_evitar_solo_releer":
        "Evita depender solo de releer y subrayar: por sí solos no suelen ser suficientes.",
    "rec_autoexplicacion":
        "Practica la autoexplicación: explica con tus palabras cada concepto y procedimiento.",
    "rec_ejercicios_con_pruebas":
        "Combina tu preferencia práctica con pruebas: resuelve ejercicios de exámenes anteriores.",
    "rec_preguntas_escritas":
        "Redacta tus propias preguntas del tema, respóndelas por escrito sin mirar los apuntes y luego corrígelas.",
    "rec_autoexplicacion_escrita":
        "En lugar de solo releer, escribe con tus palabras qué significa cada párrafo y por qué funciona.",
    "rec_mapa_de_memoria":
        "Dibuja de memoria un mapa conceptual del tema y compáralo con tus apuntes.",
    "rec_autoexplicacion_oral":
        "Graba o cuenta en voz alta el tema como si lo enseñaras y revisa qué te falta.",
}

NOMBRES_PREFERENCIA = {
    "preferencia_visual": "Visual",
    "preferencia_auditiva": "Auditiva",
    "preferencia_kinestesica": "Kinestésica",
    "preferencia_lectoescritura": "Lectura/Escritura",
}

# Cómo se llama cada preferencia dentro de HECHOS_DOMINIO (hechos F2 a F5),
SUJETO_VARK = {
    "preferencia_visual": "visual",
    "preferencia_auditiva": "auditiva",
    "preferencia_kinestesica": "kinestesica",
    "preferencia_lectoescritura": "lectura_escritura",
}

# Los ids de hechos.py van en snake_case sin acentos; aquí se acentúan los que lo necesitan
NOMBRES_RECURSO = {
    "representaciones_graficas": "representaciones gráficas",
    "actividades_practicas": "actividades prácticas",
}

NOMBRES_MODALIDAD = {
    "visual": "Visual",
    "auditivo": "Auditivo",
    "lectoescritura": "Lectura/Escritura",
    "kinestesico": "Kinestésico",
}

# La advertencia se apoya en el hecho F6 de hechos.py
AVISO = ("Nota: estos resultados son una orientación, no una clasificación definitiva. "
         f"La evidencia de {PASHLER} no demuestra que estudiar según un único "
         "estilo garantice mejores resultados.")
