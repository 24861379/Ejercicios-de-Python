#Hay dos formas de hacer una lista
#Forma 1 

lista = list() #--> esta lista está vacia

#Forma 2 
Lista =[]

frutas = ['banano', 'naranja', 'mango', 'limon']
vegetales = ['tomate', 'papas','lechuga','cebolla', 'zanahoria']
animal_products = ['leche', 'carne', 'mantequilla','yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']

print('las frutas son : ',frutas)
print('la longitud de la lista es de: ', len(frutas))

print('Los vegetales son: ',vegetales)
print('La cantidad de vegetales son: ', len(vegetales))

#Separar elementos de una lista
todas_las_frutas = frutas[0:4] #Devuelve todos los elementos
todas_las_frutas = frutas[0:] # retorna todo porque no se le especifico hasta donde parar
ejemplo2 = frutas[1:3] # solo retorna los elementos con el indice  1 y 3
ejemplo3 = frutas[1:] #retorna desde el elemento con el indice 1 hasta el ultimo
ejemplo4 = frutas[::2] # retorna cada segundo elemento (cada n elemento)

#Modificación de listas
frutas[0]= 'aguacate' #--> cambie banano por aguacate
print(frutas)

frutas[1] = 'manzana'
print(frutas)

ultimo_indice= len(frutas)-1
frutas[ultimo_indice] = 'lima'
print(frutas)

#Comprobar si un elemento existe
print('****Comprobando si un elemento existe.****')
existe = 'pajaro' in frutas
print(existe)

existe = 'lima' in frutas
print(existe)

#Agregar elementos
frutas.append('naranja') #append añade un elemento a la ultima posicion
print(frutas)

#Insertar elementos 
frutas.insert(3, 'banano')
print(frutas)

#eliminar elementos de una lista con remove()
frutas.remove('banano')
frutas.remove('lima')
frutas.remove('aguacate')
print(frutas)

#eliminar con el método .pop()
frutas.append('banano')
frutas.append('aguacate')
frutas.pop()
print(frutas)

frutas.pop(0)
print(frutas)

#eliminar elementos con del

