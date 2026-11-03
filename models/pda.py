class AutamataPila:
    def __init__(self, cadena):
        self.cadena = cadena
        self.historial = []
        self.simular()

    def simular(self):
        estado = "q0"
        pila = ["Z0"] # Z0 representa el fondo de la pila
        cinta = list(self.cadena)
        
        # Fotografía inicial
        self.historial.append({"estado": estado, "cinta": "".join(cinta), "pila": list(pila)})
        
        error = False
        for i, simbolo in enumerate(cinta):
            if estado == "q0" and simbolo == "a":
                pila.append("A") # Apila por cada 'a'
            elif estado == "q0" and simbolo == "b":
                estado = "q1" # Transición al leer la primera 'b'
                if pila[-1] == "A":
                    pila.pop() # Desapila
                else:
                    error = True; break
            elif estado == "q1" and simbolo == "b":
                if pila[-1] == "A":
                    pila.pop() # Sigue desapilando
                else:
                    error = True; break
            else:
                error = True; break
            
            # Fotografía tras cada símbolo procesado
            self.historial.append({"estado": estado, "cinta": "".join(cinta[i+1:]), "pila": list(pila)})
        
        # Verificación final de aceptación
        if not error and len(pila) == 1 and pila[0] == "Z0" and len(self.cadena) > 0:
            self.historial.append({"estado": "q2 (Aceptada)", "cinta": "", "pila": list(pila)})
        else:
            self.historial.append({"estado": "q_error (Rechazada)", "cinta": "", "pila": list(pila)})