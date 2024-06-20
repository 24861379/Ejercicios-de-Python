print("Hola mundo") #permite imprimir mensajes
len("este es una mensaje") #Muestra el tamaño del texto, es como el .length() de java
type(45) #verufuca el tipo de dato
str(10)# Combierte números a texto
int("10")# lo combierte a un numero int
float(10)#lo combierte de integer a decimal
#input("ingrese su nombre: ")#recibe el ingreso de datos 

print("Algunos ejemplos de funciones")

#arrojar el número inferior
print(min(45, 15, 34, 54, 66,))#min me muestra el número menor

#arrojar el número mayor
print(max(45, 15, 34, 54, 66,))#min me muestra el número mayor

#con la función sum mostrar la suma total
print(sum([45, 15, 34, 54, 66,]))

#VARIABLES
first_name= "juan"
last_name= "Rodrigues"
country= "Colombia"
age =34
is_Married= False

skills=["HTTML", "CSS", "JS", "React","Python"]
person_info={
    'firstname':'juan',
   'lastname':'Rodrigues',
   'country':'Colombia'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_Married)
print('Skills: ', skills)
print('Person information: ', person_info)
