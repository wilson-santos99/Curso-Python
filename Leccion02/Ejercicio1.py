"""
Instrucciones de la tarea:
-En el siguiente ejercicio se solicita calcular el área y el perímetro de un rectángulo,
para ello deberemos crear las siguientes variables:

alto (int)
ancho (int)

- El usuario debe proporcionar los valores de largo y ancho,
y despues se debe imprimir el resultado en el siguiente formato

(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

Proporciona el alto:
Proporciona el ancho:
Area=<area>
Perimetro: <perimetro>"""


alto=int(input('Proporciona el alto: '))
ancho=int(input('Proporciona el ancho: '))

Area=alto*ancho
Perimetro=(alto+ancho)*2
print('Proporciona el alto:',Area)
print('Proporciona el ancho:',Perimetro)
