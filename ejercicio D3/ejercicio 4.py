"""
Obtenga el radio de un círculo mediante 
un mensaje. Calcular el área (área = pi *r*r) y 
la circunferencia (c = 2 * pi * r) donde pi = 3,14.
"""
print('Ingrese el radio del un circulo')
radio= int(input())

#hallar el area del circulo
pi = 3.14
area = pi * (radio ** 2)

#hallar la circunferencia del circulo
C = 2 * pi * radio

print('El área del circulo es de: ', area, '\nLa circunferencia del circulo es de: ',C)


