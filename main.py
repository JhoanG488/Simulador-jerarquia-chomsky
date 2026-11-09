import customtkinter as ctk
from gui.nivel2_pda import Nivel2Window
from gui.nivel3_dfa import Nivel3Window
from gui.nivel1_lba import Nivel1Window
from gui.nivel0_tm import Nivel0Window

# Configuración inicial de la apariencia
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class SimuladorChomsky(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simulador Jerarquía de Chomsky")
        self.geometry("1200x400")
        self.resizable(False, False)

        # Contenedor principal
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=40, fill="both", expand=True)

        # Título y descripción
        self.label_titulo = ctk.CTkLabel(self.frame, text="Jerarquía de Chomsky", font=("Arial", 24, "bold"))
        self.label_titulo.pack(pady=20)

        self.label_desc = ctk.CTkLabel(self.frame, text="Selecciona el nivel que deseas simular:", font=("Arial", 14))
        self.label_desc.pack(pady=10)

        # Botones para cada nivel
        self.btn_nivel3 = ctk.CTkButton(self.frame, text="Nivel 3: Lenguajes Regulares (DFA)", height=40, command=self.abrir_nivel3)
        self.btn_nivel3.pack(pady=10, fill="x", padx=20)

        self.btn_nivel2 = ctk.CTkButton(self.frame, text="Nivel 2: Libres de Contexto (PDA)", height=40, command=self.abrir_nivel2)
        self.btn_nivel2.pack(pady=10, fill="x", padx=20)

        self.btn_nivel1 = ctk.CTkButton(self.frame, text="Nivel 1: Sensibles al Contexto (LBA)", height=40, command=self.abrir_nivel1)
        self.btn_nivel1.pack(pady=10, fill="x", padx=20)

        self.btn_nivel0 = ctk.CTkButton(self.frame, text="Nivel 0: Recursivamente Enumerables (MT)", height=40, command=self.abrir_nivel0)
        self.btn_nivel0.pack(pady=10, fill="x", padx=20)

        # Variable para controlar ventanas secundarias abiertas
        self.ventana_actual = None

    def abrir_nivel3(self): 
        
         if self.ventana_actual is None or not self.ventana_actual.winfo_exists():
            self.ventana_actual = Nivel3Window(self)
            self.ventana_actual.grab_set()
         else:
            self.ventana_actual.focus()
    def abrir_nivel2(self):
        if self.ventana_actual is None or not self.ventana_actual.winfo_exists():
            self.ventana_actual = Nivel2Window(self)
            self.ventana_actual.grab_set()  # Enfoca la nueva ventana
        else:
            self.ventana_actual.focus()

    def abrir_nivel1(self):
        
            if self.ventana_actual is None or not self.ventana_actual.winfo_exists():
                self.ventana_actual = Nivel1Window(self)
                self.ventana_actual.grab_set()
            else:
                self.ventana_actual.focus()

    def abrir_nivel0(self):
        if self.ventana_actual is None or not self.ventana_actual.winfo_exists():
            self.ventana_actual = Nivel0Window(self)
            self.ventana_actual.grab_set()
        else:
            self.ventana_actual.focus()
            
    
if __name__ == "__main__":
    app = SimuladorChomsky()
    app.mainloop()