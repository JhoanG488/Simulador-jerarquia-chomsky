class AutomataLinealAcotado:
    def __init__(self, cadena):
        self.cadena = cadena
        self.historial = []
        self.simular()

    def simular(self):
        # La cinta del LBA está delimitada estrictamente por [ y ]
        cinta = ['['] + list(self.cadena) + [']']
        cabezal = 1
        estado = "q0"
        
        self.registrar_paso(estado, cinta, cabezal)
        
        while True:
            simbolo = cinta[cabezal]
            estado_previo = estado
            
            if estado == "q0":
                if simbolo == 'a': cinta[cabezal] = 'X'; cabezal += 1; estado = "q1"
                elif simbolo == 'Y': cabezal += 1; estado = "q4"
                else: estado = "q_error"
            
            elif estado == "q1":
                if simbolo in ['a', 'Y']: cabezal += 1
                elif simbolo == 'b': cinta[cabezal] = 'Y'; cabezal += 1; estado = "q2"
                else: estado = "q_error"
                
            elif estado == "q2":
                if simbolo in ['b', 'Z']: cabezal += 1
                elif simbolo == 'c': cinta[cabezal] = 'Z'; cabezal -= 1; estado = "q3"
                else: estado = "q_error"
                
            elif estado == "q3":
                if simbolo in ['a', 'b', 'Y', 'Z']: cabezal -= 1
                elif simbolo == 'X': cabezal += 1; estado = "q0"
                else: estado = "q_error"
                
            elif estado == "q4":
                if simbolo in ['Y', 'Z']: cabezal += 1
                elif simbolo == ']': estado = "q_aceptacion"
                else: estado = "q_error"
            
            self.registrar_paso(estado, cinta, cabezal)
            
            if estado in ["q_aceptacion", "q_error"] or estado_previo == estado and estado == "q_error":
                break

    def registrar_paso(self, estado, cinta, cabezal):
        self.historial.append({
            "estado": estado,
            "cinta": list(cinta),
            "cabezal": cabezal
        })