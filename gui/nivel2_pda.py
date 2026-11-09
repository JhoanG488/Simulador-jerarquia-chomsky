import customtkinter as ctk
from models.pda import AutamataPila # Agrega esta importación

class Nivel2Window(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        # ... (Mantén todo el código del __init__ exactamente igual) ...
        super().__init__(master, **kwargs)
        self.title("Nivel 2 - Autómata de Pila (PDA)")
        self.geometry("1200x500")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Panel superior: Entrada y Controles
        self.frame_controles = ctk.CTkFrame(self)
        self.frame_controles.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.label_instruccion = ctk.CTkLabel(self.frame_controles, text="Ingrese cadena a^n b^n (ej. aabb):")
        self.label_instruccion.pack(side="left", padx=10)

        self.entrada_cadena = ctk.CTkEntry(self.frame_controles, width=150)
        self.entrada_cadena.pack(side="left", padx=10)

        self.btn_procesar = ctk.CTkButton(self.frame_controles, text="Cargar", command=self.cargar_cadena)
        self.btn_procesar.pack(side="left", padx=5)

        self.btn_paso = ctk.CTkButton(self.frame_controles, text="Siguiente Paso", command=self.siguiente_paso, state="disabled")
        self.btn_paso.pack(side="left", padx=5)

        self.btn_limpiar = ctk.CTkButton(self.frame_controles, text="Limpiar", command=self.limpiar, fg_color="#C62828", hover_color="#b71c1c")
        self.btn_limpiar.pack(side="left", padx=5)
        
        # --- Botón de Ejemplos sugeridos ---
        self.combo_ejemplos = ctk.CTkOptionMenu(
            self.frame_controles, 
            values=["Ejemplos sugeridos:", "🟢 aabb (Válida)", "🟢 aaabbb (Válida)", "🔴 aab (Inválida)", "🔴 baab (Inválida)"], 
            command=self.usar_ejemplo
        )
        self.combo_ejemplos.pack(side="left", padx=15)
        # ---------------------------------------

        # Panel central: Cinta (Entrada)
        self.frame_cinta = ctk.CTkFrame(self)
        self.frame_cinta.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.label_cinta = ctk.CTkLabel(self.frame_cinta, text="Cinta: [ ]", font=("Courier", 18, "bold"))
        self.label_cinta.pack(pady=20)

        # Panel inferior: Pila y Estado
        self.frame_pila = ctk.CTkFrame(self)
        self.frame_pila.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.label_estado = ctk.CTkLabel(self.frame_pila, text="Estado Actual: q0", font=("Arial", 16, "bold"))
        self.label_estado.pack(pady=10)

        self.label_titulo_pila = ctk.CTkLabel(self.frame_pila, text="Memoria Pila (LIFO)", font=("Arial", 14))
        self.label_titulo_pila.pack()

        self.vista_pila = ctk.CTkTextbox(self.frame_pila, width=150, height=300, font=("Courier", 18), state="disabled")
        self.vista_pila.pack(pady=10)

        # Variables de control
        self.historial = []
        self.paso_actual = 0

    # REEMPLAZA ESTOS MÉTODOS
    def cargar_cadena(self):
        cadena = self.entrada_cadena.get()
        pda = AutamataPila(cadena)
        self.historial = pda.historial
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
        
        self.label_cinta.configure(text=f"Cinta: [ {estado_datos['cinta']} ]")
        
        color_estado = "green" if "Aceptada" in estado_datos['estado'] else "red" if "Rechazada" in estado_datos['estado'] else "white"
        self.label_estado.configure(text=f"Estado Actual: {estado_datos['estado']}", text_color=color_estado)
        
        self.actualizar_pila(estado_datos['pila'])

    def limpiar(self):
        self.entrada_cadena.delete(0, "end")
        self.label_cinta.configure(text="Cinta: [ ]")
        self.label_estado.configure(text="Estado Actual: q0", text_color="white")
        self.btn_paso.configure(state="disabled")
        self.actualizar_pila([])
        self.historial = []
        self.paso_actual = 0

    def actualizar_pila(self, elementos):
        self.vista_pila.configure(state="normal")
        self.vista_pila.delete("1.0", "end")
        for elem in reversed(elementos):
            self.vista_pila.insert("end", f" | {elem} |\n")
            self.vista_pila.insert("end", " +---+\n")
        self.vista_pila.configure(state="disabled")
        
        
        #BOTON EJEMPLOS SUGERIDOS
    def usar_ejemplo(self, choice):
        if choice != "Ejemplos...":
            cadena = choice.split(" ")[1] 
            self.entrada_cadena.delete(0, "end")
            self.entrada_cadena.insert(0, cadena)
        self.combo_ejemplos.set("Ejemplos...")