"""
Calcular la longitud y el ancho de un rectángulo mediante un comando. 
Calcular su área (área = longitud * ancho) y su perimetro (perimetro= 2 * (longitud + ancho))
"""
print('Ingrese la longitud del recatngulo: ')
Long= int(input())

print('Ingrese el ancho del rectangulo: ')
ancho= int(input())

area= Long * ancho
perimetro =2 * (Long + ancho)

print('el area del rectangulo es de: ', area, 'y el perimetro del rectagulo es de: ', perimetro)