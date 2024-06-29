"""
Escriba un script que solicite al usuario 
que ingrese la base y la altura del triángulo 
y calcule el área de este triángulo.
(perimetro = a + b + c)
"""
print('Vamos a calcular el perimetro de una triangulo\n Ingrese el lado "a"')
side_a= int(input())

print('Ingrese el lado "b"')
side_b= int(input())

print ('Ingrese el la dos "c"')
side_c= int(input())

perimetro = side_a + side_b + side_c

print('El resultado de hallar el perimetro es: ', perimetro)
