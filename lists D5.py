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
print('***Usando \'del\' para eliminar elementos.***')
print(vegetales)
del vegetales[3] #cuando a del se le especifica el indice del elemento elimina el elemento
print(vegetales)
del vegetales[1]
print(vegetales)
#cuando no le especificamos el indice del elimina toda la lista
#del vegetales #--> esto devuelve: NameError: name 'vegateles' is not defined
#print(vegetales)  

#Borrar elementos con clear()
print('***Usando el método  \'clear()\' para eliminar elementos.***'.upper())
animal_products.clear()
print(animal_products)

#Copiar una lista
print('***Usando el método  \'copy()\' para copiar una lista.***'.upper())
web_techs_copia = web_techs.copy()
print(web_techs_copia)

#UNIR LISTAS
print('***Usando \'concatenacion y el método extend()\' para unir listas.***'.upper())
vector= [1, 2, 3]
vec_cero=[0]
vector2 = [-3, -2,-1]

Concatenar= vector2 + vec_cero+ vector
print(Concatenar)
web_techs_copia.extend(frutas)
print(web_techs_copia)

#Contar la cantidad de elementos de una lista
print('***Usando \'el método count()\' para contar la cantidad de un elemento en las listas.***'.upper()) 
edades = [14, 30, 15, 14, 60, 20, 20, 20, 20, 34]
print(edades.count(20))

#invertir una lista
print('***Usando \'el método reverse()\' para invertir una lista.***'.upper()) 
web_techs.reverse()
print(web_techs)



