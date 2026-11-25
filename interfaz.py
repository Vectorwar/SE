# -*- coding: utf-8 -*-
"""
Interfaz gráfica (tkinter) del sistema experto.
Reutiliza el cuestionario (cuestionario.py) y el motor de inferencia a través de
salida.evaluar(), así la lógica no se duplica: solo cambia la forma de pedir datos
y mostrar el resultado.

Se abre desde main.py (python main.py) o directamente con:  python interfaz.py
"""
import tkinter as tk
from tkinter import ttk, messagebox

from cuestionario import PREGUNTAS
from salida import evaluar


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Técnicas de estudio - Sistema experto JAI")
        self.geometry("700x600")
        self.resizable(False, False)

        self.indice = 0          # pregunta actual
        self.respuestas = []     # número de la opción elegida en cada pregunta (0, 1, 2...)
        self.opcion = tk.IntVar(value=-1)   # opción seleccionada (radio buttons)

        # --- Widgets fijos ---
        self.lbl_progreso = ttk.Label(self, font=("Arial", 10))
        self.lbl_progreso.pack(pady=(15, 5))

        self.barra = ttk.Progressbar(self, length=500, maximum=len(PREGUNTAS))
        self.barra.pack()

        self.lbl_pregunta = ttk.Label(self, font=("Arial", 14, "bold"),
                                      wraplength=560, justify="center")
        self.lbl_pregunta.pack(pady=20)

        # Aquí se colocan los radio buttons de cada pregunta
        self.marco_opciones = ttk.Frame(self)
        self.marco_opciones.pack(pady=5)

        # Botón para volver atrás en caso de que el usuario quiera cambiar su respuesta
        self.marco_botones = ttk.Frame(self)
        self.marco_botones.pack(pady=20)

        self.btn_atras = ttk.Button(self.marco_botones, text="Atrás", command=self.atras)
        self.btn_atras.pack(side="left", padx=10)

        self.btn_siguiente = ttk.Button(self.marco_botones, text="Siguiente", command=self.siguiente)
        self.btn_siguiente.pack(side="left", padx=10)

        # Área de resultados (se usa al final)
        self.marco_resultado = ttk.Frame(self)
        self.txt_resultado = tk.Text(self.marco_resultado, wrap="word", font=("Arial", 11),
                                     height=24, width=78)
        self.scroll = ttk.Scrollbar(self.marco_resultado, command=self.txt_resultado.yview)
        self.txt_resultado.config(yscrollcommand=self.scroll.set)

        # --- Instrucciones (parte de abajo de la ventana) ---
        self.lbl_instrucciones = ttk.Label(
         self,
        text="Instrucciones: elige una opción que mejor te describa y presiona «Siguiente». "
         "Si quieres cambiar una respuesta anterior, usa el botón «Atrás».",
        font=("Arial", 9),
        foreground="black",
        wraplength=640,
        justify="center",
)
        self.lbl_instrucciones.pack(side="top", pady=10)
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        """Dibuja la pregunta actual y sus opciones."""
        pregunta = PREGUNTAS[self.indice]
        self.lbl_progreso.config(text=f"Pregunta {self.indice + 1} de {len(PREGUNTAS)}")
        self.barra["value"] = self.indice
        self.lbl_pregunta.config(text=pregunta["texto"])

        # Limpiar opciones anteriores
        for widget in self.marco_opciones.winfo_children():
            widget.destroy()

        # Si ya respondió esta pregunta antes (volvió con Atrás), se marca su respuesta
        if self.indice < len(self.respuestas):
            self.opcion.set(self.respuestas[self.indice])
        else:
            self.opcion.set(-1)

        # En la primera pregunta no hay a dónde regresar
        self.btn_atras.config(state="disabled" if self.indice == 0 else "normal")

        for i, (texto, _) in enumerate(pregunta["opciones"]):
            ttk.Radiobutton(self.marco_opciones, text=texto,
                            variable=self.opcion, value=i).pack(anchor="w", pady=4)

        es_ultima = self.indice == len(PREGUNTAS) - 1
        self.btn_siguiente.config(text="Ver resultado" if es_ultima else "Siguiente")

    def siguiente(self):
        """Valida la respuesta, la guarda y avanza (o evalúa si ya es la última)."""
        if self.opcion.get() == -1:
            messagebox.showwarning("Falta respuesta", "Selecciona una opción para continuar.")
            return

        eleccion = self.opcion.get()
        if self.indice < len(self.respuestas):
            self.respuestas[self.indice] = eleccion     
        else:
            self.respuestas.append(eleccion)            # respuesta nueva
        self.indice += 1

        self.lbl_instrucciones.pack_forget()  # desaparece al llegar a la última pregunta

        if self.indice < len(PREGUNTAS):
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado()

    def atras(self):
        """Permite al usuario regresar a la pregunta anterior para cambiar su respuesta."""
        if self.indice > 0:
            self.indice -= 1
            self.mostrar_pregunta()

    def mostrar_resultado(self):
        """Ejecuta el sistema experto y muestra la salida."""
        # Se convierten los números de opción en los valores que espera el motor
        valores = [PREGUNTAS[i]["opciones"][idx][1] for i, idx in enumerate(self.respuestas)]
        _, texto = evaluar(valores)

        # Ocultar las preguntas
        self.lbl_progreso.pack_forget()
        self.barra.pack_forget()
        self.lbl_pregunta.config(text="Resultado")
        self.marco_opciones.pack_forget()
        self.marco_botones.pack_forget()      # oculta Atrás y Siguiente juntos

        self.marco_resultado.pack(padx=15, pady=5)
        self.scroll.pack(side="right", fill="y")
        self.txt_resultado.pack(side="left")
        self.txt_resultado.insert("1.0", texto)
        self.txt_resultado.config(state="disabled")

        ttk.Button(self, text="Reiniciar", command=self.reiniciar).pack(pady=8)

    def reiniciar(self):
        """Reabre la aplicación desde cero."""
        self.destroy()
        App().mainloop()


if __name__ == "__main__":
    App().mainloop()