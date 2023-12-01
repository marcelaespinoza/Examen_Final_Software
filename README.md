# Examen_Final_Software

## Pregunta 1
En caso de visualizar historial, realizar previamente (y sin cancelar) el pago para obtener resultados esperados
## Pregunta 2
En el directorio, para las pruebas unitarias, ejecutar python -m unittest routes.py
## Pregunta 3
### Qué cambiaría en el código (Clases / Métodos)
Agregaría un atributo a la clase cuenta llamado límite, y al momento de hacer un pago este se iría sumando con el valor a pagar y en caso de llegar al límite la operación no se realizaría. (OJO: esto implica modificar un poco (agregar condicional) el metodo pagar)
### Nuevos casos de prueba a adicionar.
- Validar que el límite incremente por cada pago realizado
- Validar que si llega al límite establecido la función pagar no se ejecute, es decir que el saldo se mantenga y que no se agregue ninguna operación
- Validar que si se supera el límite establecido en la función pagar no se ejecute la función
### Cuánto riesgo hay de “romper” lo que ya funciona?
No hay mucho riesgo, porque es solo agregar un condicional dado un atributo. El agregar este cambio solo afecta la función pagar y si se rompe el límite realmente no pasa nada, solo no se ejecuta (realiza ningún cambio).


