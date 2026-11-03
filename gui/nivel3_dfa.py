import customtkinter as ctk
from models.dfa import AutomataFinito

class Nivel3Window(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Nivel 3 - Autómata Finito Determinista (DFA)")
        self.geometry("800x400")

        self.grid_columnconfigure(0, weight=1)

        # Controles
        self.frame_controles = ctk.CTkFrame(self)
        self.frame_controles.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        ctk.CTkLabel(self.frame_controles, text="Ingrese cadena a*b* (ej. aaabb):").pack(side="left", padx=10)
        self.entrada_cadena = ctk.CTkEntry(self.frame_controles, width=150)
        self.entrada_cadena.pack(side="left", padx=10)

        ctk.CTkButton(self.frame_controles, text="Cargar", command=self.cargar_cadena).pack(side="left", padx=5)
        self.btn_paso = ctk.CTkButton(self.frame_controles, text="Siguiente Paso", command=self.siguiente_paso, state="disabled")
        self.btn_paso.pack(side="left", padx=5)
        ctk.CTkButton(self.frame_controles, text="Limpiar", command=self.limpiar, fg_color="#C62828", hover_color="#b71c1c").pack(side="left", padx=5)

        # Visualización de Cinta y Estado
        self.frame_visual = ctk.CTkFrame(self)
        self.frame_visual.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.label_cinta = ctk.CTkLabel(self.frame_visual, text="Cadena restante: [ ]", font=("Courier", 18, "bold"))
        self.label_cinta.pack(pady=30)

        self.label_estado = ctk.CTkLabel(self.frame_visual, text="Estado Actual: q0", font=("Arial", 22, "bold"))
        self.label_estado.pack(pady=20)

        self.historial = []
        self.paso_actual = 0

    def cargar_cadena(self):
        cadena = self.entrada_cadena.get()
        dfa = AutomataFinito(cadena)
        self.historial = dfa.historial
        self.paso_actual = 0
        
        self.btn_paso.configure(state="normal")
        self.mostrar_estado_actual()

    def siguiente_paso(self):
        if self.paso_actual < len(self.historial) - 1:
            self.paso_actual += 1
            self.mostrar_estado_actual()
            
        if self.paso_actual == len(self.historial) - 1:
            self.btn_paso.configure(state="disabled")

    def mostrar_estado_actual(self):
        estado_datos = self.historial[self.paso_actual]
        self.label_cinta.configure(text=f"Cadena restante: [ {estado_datos['cinta']} ]")
        
        color = "green" if "Aceptada" in estado_datos['estado'] else "red" if "Rechazada" in estado_datos['estado'] else "white"
        self.label_estado.configure(text=f"Estado Actual: {estado_datos['estado']}", text_color=color)

    def limpiar(self):
        self.entrada_cadena.delete(0, "end")
        self.label_cinta.configure(text="Cadena restante: [ ]")
        self.label_estado.configure(text="Estado Actual: q0", text_color="white")
        self.btn_paso.configure(state="disabled")
        self.historial = []
        self.paso_actual = 0