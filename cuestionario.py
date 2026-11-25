# -*- coding: utf-8 -*-
"""
Fase 1: Cuestionario (entradas del usuario).
Solo contiene datos: las preguntas, sus opciones y las modalidades VARK usadas.
"""

# ============================================================
# CUESTIONARIO (entradas del usuario)
# ============================================================
# Cada opción es una tupla: (texto_mostrado, valor)
#   - En las preguntas de tipo "estilo", valor es la modalidad VARK
#     que suma un punto: "visual", "auditivo", "lectoescritura" o "kinestesico".
#   - En las preguntas de tipo "contexto", valor es el hecho que se
#     agrega a la base de conocimiento (o None si no agrega nada).

PREGUNTAS = [
    # ---------- Preguntas de estilo (suman puntos) ----------
    {
        "tipo": "estilo",
        "texto": "Cuando tienes que aprender un tema nuevo, prefieres:",
        "opciones": [
            ("Ver diagramas, esquemas o mapas conceptuales", "visual"),
            ("Escuchar la explicación de alguien", "auditivo"),
            ("Leer un texto o artículo sobre el tema", "lectoescritura"),
            ("Probarlo con ejercicios o ejemplos prácticos", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "Para recordar información, normalmente:",
        "opciones": [
            ("Imagino cómo se veía en mi cuaderno o en la pizarra", "visual"),
            ("Me la repito en voz alta o la converso con alguien", "auditivo"),
            ("Recuerdo lo que escribí o leí sobre el tema", "lectoescritura"),
            ("Recuerdo lo que hice al practicarla", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "Si no entiendes un concepto, lo que más te ayuda es:",
        "opciones": [
            ("Que me lo dibujen o me lo muestren en una gráfica", "visual"),
            ("Que me lo expliquen hablando", "auditivo"),
            ("Leer su definición o una explicación por escrito", "lectoescritura"),
            ("Resolver un problema donde se use", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "En una clase te sientes más cómodo cuando:",
        "opciones": [
            ("Hay presentaciones con imágenes y esquemas", "visual"),
            ("Se permite preguntar y debatir los temas", "auditivo"),
            ("Se entregan lecturas o apuntes para leer y tomar notas", "lectoescritura"),
            ("Hay laboratorios o actividades prácticas", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "Al preparar apuntes prefieres:",
        "opciones": [
            ("Usar colores, flechas y cuadros", "visual"),
            ("Grabar la clase o estudiar con un compañero", "auditivo"),
            ("Escribir listas, definiciones y párrafos completos", "lectoescritura"),
            ("Hacer ejemplos y ejercicios resueltos", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "Cuando armas algo nuevo (un mueble, un programa):",
        "opciones": [
            ("Miro primero el diagrama o las imágenes del instructivo", "visual"),
            ("Pido que alguien me explique los pasos", "auditivo"),
            ("Leo con calma el manual o la documentación", "lectoescritura"),
            ("Empiezo a armarlo y aprendo sobre la marcha", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "Para entregar un trabajo o presentar un tema, prefieres:",
        "opciones": [
            ("Hacer una infografía o una presentación visual", "visual"),
            ("Exponerlo hablando frente a otras personas", "auditivo"),
            ("Redactar un informe o ensayo", "lectoescritura"),
            ("Mostrar una demostración o un prototipo funcionando", "kinestesico"),
        ],
    },
    {
        "tipo": "estilo",
        "texto": "Si tienes que buscar información, lo que más usas es:",
        "opciones": [
            ("Imágenes, gráficos o videos con esquemas", "visual"),
            ("Podcasts, audios o preguntar a alguien que sepa", "auditivo"),
            ("Artículos, libros o páginas con texto", "lectoescritura"),
            ("Tutoriales donde se haga el ejemplo paso a paso", "kinestesico"),
        ],
    },
    # ---------- Preguntas de contexto (agregan hechos) ----------
    {
        "tipo": "contexto",
        "texto": "¿Tienes un examen próximo para el cual necesitas repasar?",
        "opciones": [
            ("Sí", "examen_proximo"),
            ("No", None),
        ],
    },
    {
        "tipo": "contexto",
        "texto": "¿Cuántos días tienes disponibles para estudiar?",
        "opciones": [
            ("Hoy o mañana (1 a 2 días)", None),
            ("Tres días o más", "varios_dias"),
        ],
    },
    {
        "tipo": "contexto",
        "texto": "¿Cómo sueles estudiar normalmente?",
        "opciones": [
            ("Releo y subrayo mis apuntes", "habito_releer_subrayar"),
            ("Hago preguntas, ejercicios o resúmenes con mis palabras", None),
        ],
    },
]

# Modalidades VARK que el sistema puntúa (V-A-R-K)
MODALIDADES = ("visual", "auditivo", "lectoescritura", "kinestesico")
