class AutomataFinito:
    def __init__(self, cadena):
        self.cadena = cadena
        self.historial = []
        self.simular()

    def simular(self):
        estado = "q0"
        cinta = list(self.cadena)
        
        # Fotografía inicial
        self.historial.append({"estado": estado, "cinta": "".join(cinta)})
        
        for i, simbolo in enumerate(cinta):
            if estado == "q0":
                if simbolo == "a":
                    estado = "q0"
                elif simbolo == "b":
                    estado = "q1"
                else:
                    estado = "q_error"
            elif estado == "q1":
                if simbolo == "b":
                    estado = "q1"
                else:
                    estado = "q_error"
            else:
                estado = "q_error"
                
            self.historial.append({"estado": estado, "cinta": "".join(cinta[i+1:])})
            
            if estado == "q_error":
                break
                
        # Evaluación de aceptación (q0 y q1 son estados finales válidos)
        estado_final = self.historial[-1]["estado"]
        if estado_final in ["q0", "q1"]:
            self.historial[-1]["estado"] = f"{estado_final} (Aceptada)"
        else:
            self.historial[-1]["estado"] = "q_error (Rechazada)"