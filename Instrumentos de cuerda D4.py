first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh

#FORMATO DE CADENA
nombre= 'Carlos'
Apellido = 'Rodrigues'
lenguaje = 'python'
'''formato_de_cadena= 'soy %s %s. y estoy trabajando con %s' %(nombre, Apellido, lenguaje)
print(formato_de_cadena)'''
#--------------------------------------------------------------------------------------
#str.format
formato_de_cadena = 'soy {}{}.. y estoy trabajando con {}'.format(nombre, Apellido, lenguaje)
#--------------------------------------------------------------------------------------
#STRINGS Y NUMEROS
radio = 10
pi = 3.14
area = pi * radio **2
formato_de_CADENA='El area del circulo es de %d es %.2f' %(radio, area)

#------------------------------------------------------------------------------------------
#MÉTODOS DE CADENAS
challenge = 'treinta días de python'
print(challenge.capitalize()) # --> convierte el primer caracter de la cadena en letra mayúscula

#endswith() --> comprueba si la cadena termina en una palabra especifica
print(challenge.endswith('as')) #false
print(challenge.endswith('on')) #true

#expandtabs() --> reemplaza el caracter de espacio por tabulación el cual tiene 8 espacios
Challenge = 'treinta\tdías\tde\tpython'
print(Challenge.expandtabs()) #treinta días    de      python
print(Challenge.expandtabs(10)) #treinta   días      de        python

#isalnumber() --> Comprueba caracteres alfanuméricos
reto ='treintadíasdepython'
print(reto.isalnum())#true
Reto = '30díasdepython'
print(reto.isalnum()) #true
REto='treinta días de python'
print(reto.isalnum()) #true
RETo='treinta días de python 2024'
print(reto.isalnum()) #true
#replace() --> reemplaza la subcadena con una cadena dada
print(challenge.replace('python', 'programación'))