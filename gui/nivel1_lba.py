import customtkinter as ctk
from models.lba import AutomataLinealAcotado

class Nivel1Window(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Nivel 1 - Autómata Linealmente Acotado (LBA)")
        self.geometry("800x400")

        self.grid_columnconfigure(0, weight=1)

        # Controles
        self.frame_controles = ctk.CTkFrame(self)
        self.frame_controles.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        ctk.CTkLabel(self.frame_controles, text="Ingrese a^n b^n c^n (ej. aabbcc):").pack(side="left", padx=10)
        self.entrada_cadena = ctk.CTkEntry(self.frame_controles, width=150)
        self.entrada_cadena.pack(side="left", padx=10)

        ctk.CTkButton(self.frame_controles, text="Cargar", command=self.cargar_cadena).pack(side="left", padx=5)
        self.btn_paso = ctk.CTkButton(self.frame_controles, text="Siguiente Paso", command=self.siguiente_paso, state="disabled")
        self.btn_paso.pack(side="left", padx=5)
        ctk.CTkButton(self.frame_controles, text="Limpiar", command=self.limpiar, fg_color="#C62828", hover_color="#b71c1c").pack(side="left", padx=5)

        # Visualización de Cinta Bidireccional
        self.frame_visual = ctk.CTkFrame(self)
        self.frame_visual.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.label_cinta = ctk.CTkLabel(self.frame_visual, text="Cinta: ", font=("Courier", 24, "bold"))
        self.label_cinta.pack(pady=20)
        
        self.label_indicador = ctk.CTkLabel(self.frame_visual, text="", font=("Courier", 24, "bold"), text_color="yellow")
        self.label_indicador.pack(pady=5)

        self.label_estado = ctk.CTkLabel(self.frame_visual, text="Estado Actual: -", font=("Arial", 22, "bold"))
        self.label_estado.pack(pady=20)

        self.historial = []
        self.paso_actual = 0

    def cargar_cadena(self):
        cadena = self.entrada_cadena.get()
        lba = AutomataLinealAcotado(cadena)
        self.historial = lba.historial
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
        paso = self.historial[self.paso_actual]
        cinta_str = " ".join(paso['cinta'])
        self.label_cinta.configure(text=f"Cinta: {cinta_str}")
        
        # Crear un indicador (^) debajo de la posición del cabezal
        espacios_previos = " " * 7 + "  " * paso['cabezal'] # Ajuste manual de espaciado para alinear con la fuente Courier
        self.label_indicador.configure(text=f"{espacios_previos}^")
        
        color = "green" if "aceptacion" in paso['estado'] else "red" if "error" in paso['estado'] else "white"
        self.label_estado.configure(text=f"Estado Actual: {paso['estado']}", text_color=color)

    def limpiar(self):
        self.entrada_cadena.delete(0, "end")
        self.label_cinta.configure(text="Cinta: ")
        self.label_indicador.configure(text="")
        self.label_estado.configure(text="Estado Actual: -", text_color="white")
        self.btn_paso.configure(state="disabled")
        self.historial = []
        self.paso_actual = 0