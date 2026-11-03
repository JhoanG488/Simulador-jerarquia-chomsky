class MaquinaTuring:
    def __init__(self, cadena):
        self.cadena = cadena
        self.historial = []
        self.simular()

    def simular(self):
        # La cinta de la Máquina de Turing es infinita. La inicializamos con Blancos (B) a los lados.
        cinta = ['B', 'B'] + list(self.cadena) + ['B', 'B']
        cabezal = 2 # Inicia en el primer carácter de la entrada
        estado = "q0"
        
        self.registrar_paso(estado, cinta, cabezal)
        
        while True:
            # Expansión dinámica de la cinta infinita si el cabezal llega a los extremos
            if cabezal == 0:
                cinta = ['B'] + cinta
                cabezal = 1
            elif cabezal == len(cinta) - 1:
                cinta.append('B')
                
            simbolo = cinta[cabezal]
            estado_previo = estado
            
            # Lógica de transiciones para suma unaria
            if estado == "q0":
                if simbolo == '1': cabezal += 1
                elif simbolo == '+': cinta[cabezal] = '1'; cabezal += 1; estado = "q1"
                else: estado = "q_error"
                
            elif estado == "q1":
                if simbolo == '1': cabezal += 1
                elif simbolo == 'B': cabezal -= 1; estado = "q2"
                else: estado = "q_error"
                
            elif estado == "q2":
                if simbolo == '1': cinta[cabezal] = 'B'; cabezal -= 1; estado = "q_aceptacion"
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