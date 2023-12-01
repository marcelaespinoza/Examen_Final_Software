from datetime import datetime
class cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = int(saldo)
        self.contactos = contactos
        self.operaciones = []

    def pagar(self, destino, Nvalor):
        if destino not in self.contactos:
            return "contacto no válido."
        if self.saldo < Nvalor:
            return "Saldo insuficiente para realizar la transferencia."
        self.saldo -= int(Nvalor)
        Operacion = operacion(destino, datetime.now(), Nvalor)
        self.operaciones.append(Operacion)
        return (Operacion.fecha)
        

    def historial(self):
        data = []
        for operacion in self.operaciones:
            data.append((operacion.numeroDestino, operacion.valor))
        return data





class operacion:
    def __init__(self, numeroD, fecha, valor):
        self.numeroDestino = numeroD
        self.fecha = fecha
        self.valor = valor
    
