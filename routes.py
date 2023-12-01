from clases import cuenta, operacion
from fastapi import APIRouter
from datetime import datetime
import unittest

#Base de datos 

BD = []

BD.append(cuenta("21345", "Arnaldo", 200, ["123", "456"]))
BD.append(cuenta("123", "Luisa", 400, ["456"]))
BD.append(cuenta("456", "Andrea", 300, ["21345"]))


#Funciones para el endpoint 

def getContactos(minumero):
    #DATABASE
    temp = []
    contactos = {}
    #obtener contactos de minumero
    for i in range (len(BD)):
        if(BD[i].numero == minumero):
            temp = BD[i].contactos

    #obtener nombres de contacto    

    for contacto in temp:
        for i in range (len(BD)):
            if(BD[i].numero == contacto):
                contactos[contacto] =  BD[i].nombre
    return contactos


def getHistorial(minumero):
    mensajes= []
    temp = []
    for cuenta in BD:
        if(minumero == cuenta.numero):
            temp = cuenta.historial()
    for cuenta in BD:    
        for i in range (len(temp)): #operaciones
            if temp[i][0] == cuenta.numero:
                mensajes.append("Pago realizado de "+ str(temp[i][1])+ " a " + cuenta.nombre)
            if temp[i][0] == str("D"+cuenta.numero):
                mensajes.append("Pago recibido de "+ str(temp[i][1])+ " de " + cuenta.nombre)

    return mensajes


def realizarPago(minumero, numeroDestino, valor):
    mensaje = ""
    for cuenta in BD:
        if cuenta.numero == minumero:
            mensaje = cuenta.pagar(numeroDestino, valor)
        if cuenta.numero == numeroDestino:
            cuenta.saldo += valor  
            cuenta.operaciones.append(operacion(str("D"+minumero), datetime.now(), valor)) #Modifica para el numeroDestino Tenga un D antes del numero esto implicaria que es ingreso

    return mensaje



#Definir rutas 
routes_billetera = APIRouter()

@routes_billetera.get('/contactos/{minumero}')
def get_contactos(minumero:str):
    return getContactos(str(minumero))

@routes_billetera.put('/pagar/{minumero}/{numeroDestino}/{valor}')
def Pagar(minumero:str, numeroDestino:str, valor: int):
    return realizarPago(minumero, numeroDestino, valor)  

@routes_billetera.get('/historial/{minumero}')
def historial(minumero:str):
    return getHistorial(minumero)    





#pruebas unitarias
class TestBilletera(unittest.TestCase):
    def setUp(self):
        pass

    def test_getContactos_exitoso(self):
        # Caso de prueba de éxito para obtener contactos
        resultado_esperado = {'123': 'Luisa', '456': 'Andrea'}
        resultado_real = getContactos("21345")
        self.assertEqual(resultado_real, resultado_esperado)

    def test_realizarPago_error_saldo_insuficiente(self):
        # Caso de prueba de error por saldo insuficiente al realizar un pago
        resultado_esperado = "Saldo insuficiente para realizar la transferencia."
        resultado_real = realizarPago("21345", "123", 500)
        self.assertEqual(resultado_real, resultado_esperado)

    def test_realizarPago_error_destino_no_contacto(self):
        # Caso de prueba de error por destino no siendo un contacto válido
        resultado_esperado = "contacto no válido."
        resultado_real = realizarPago("21345", "789", 50)
        self.assertEqual(resultado_real, resultado_esperado)


    def test_historial_sin_operaciones(self):
        # Caso de prueba para historial sin operaciones
        cuenta_nueva = cuenta("789", "Juan", 100, [])
        BD.append(cuenta_nueva)
        resultado_esperado = []
        resultado_real = cuenta_nueva.historial()
        self.assertEqual(resultado_real, resultado_esperado)    


if __name__ == '__routes__':
    unittest.main()        