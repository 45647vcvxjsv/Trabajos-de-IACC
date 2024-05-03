# ingresar la calculadora 
primero = input("Ingrese el numero a comprobar")

try:
    primero = int(primero)
except:
    primero = "Hola"

if primero == "Aburrido chanchito":
    print("El valor ingresado, no es valido")
    exit()

segundo = input("Ingrese el segundo numero a evaluar")

try:
    segundo = int(segundo)
except:
    segundo = "Aburrido chanchito"
    exit()

if segundo == "Aburrido chanchito":
    print("el valor ingresado, no es valido")
else:
    print(primero + segundo)

# agregando funciones 

simbolo = input("Ingrese operacion a evaluar")
primero = float(input('Ingrese el primer numero'))
segundo = float(input('Ingrese el segundo numero'))

if simbolo == '+':
    print('suma :', primero + segundo)
elif simbolo == '-':
    print('resta:', primero - segundo)
elif simbolo == '*':
    print('Multi:', primero * segundo)
elif simbolo == '/':
    if segundo != 0:
        print('division:', primero / segundo)
    else: 
        print('No se puede dividir por cero')
else:
    print('la operacion, no es la adecuada')

# control de flujo 
usuarios = ['paquete', 'entregado', '11:00', 'a destino']

for usuarios in usuarios:
    if usuarios == 'entregado':
        break
    print(usuarios)

usuarios = 'paquete'

for c in usuarios:
    print(c)

for usuarios in usuarios:
    if usuarios == 'entregado':
        continue
    print(usuarios)

# rango 

for x in range(10):
    print(x)

for x in range(3,12,5):
    print(x)

else:
    print('pedido entregado')

edades = [12, 15, 8, 45, 33]

for usuarios in usuarios:
    for edad in edades:
        print(usuarios, edades)


# funciones 

def pasando_en_limpio():
    print(pasando_en_limpio)

pasando_en_limpio()

def imprimiendo(nombre):
    print('el nombre es: ', nombre[1])

imprimiendo_dato('ambriosio','dedo')

def indicando_nombre(nombre, apellido):
    print(nombre, apellido)

nombre_completo('nombre:' 'ambrosito', 'apellido:''dedo')

def nombre_completo2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

def miFuncion(argumento = 'calavera'):
    print(argumento)


mifuncion3('gatitos')
miFuncion4('belcebu')

def miFuncionlista(lista):
    for el in lista:
        print(el)

miFuncionlista(['casita', 'caribela'])

def concatenar_nombre(lista):
    i = ''
    for el in lista:
        i = i + ''
        return i

concatenar_nombre(['casita', 'holgada'])

# recursividad

def cuenta_numeros(i):
    if(i < 6):
        return i
    print(i)

cuenta_numeros(i-1)

#programacion orientada a objeto 

class pasajero:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido

    def saludar(self):
        print('Hola', 'Soy el pasajero: ', self.nombre, 'y mi apellido:', self.apellido)

class admin(pasajero):
    def superSaludo(self):
        print('Hola', 'Soy el administrador', self.nombre, self.apellido)

pasajero = pasajero('felipe', 'contreras')

pasajero.saludo()
pasajero.nombre = 'Jorge'
pasajero.saludar()

#del es para borrar el nombre y # del usuario

print(pasajero)

admin = admin('Felix', 'Bustos')

admin.saludar()
admin.superSaludo()

#pasajero.superSaludo()

# ejercicios 

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi gracia es', self.onomatopeya)
    
class Gato(Animal):
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        self.tipo = 'felino'
        print('Hola, soy una extensión de gato')

class Perro(Animal):
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        self.tipo = 'perro'
        print('Soy un perro')

class Canario(Animal):
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        self.tipo = 'ave'
        print('Soy un canario')


gato = Gato('Ternurita', 'Maullido')
gato.saludo()

perro = Perro('Cailo', 'Ladrido')
perro.saludo()

canario = Canario('Piolín', 'Pío')
canario.saludo()


# modulos 

'''
un modulo, puede ser considerado un set de instrucciones ' funciones o variables ' que se pueden incluir dentro de los 
archivos que estamos programando de esta manera se puede reutilizar el codigo que nosotros creemmos y que puedan ser 
descargados de internet 
'''

#creando el modulo.py

mascotas = ['Perro', 'Gato', 'Canario', 'Avestruz']

def saludo(nombre):
    print('Hola Soy', nombre)

import modulo

print(modulo.mascotas)


from camelcase import camelcase

c = camelcase()
s = 'Algo que comentar'

camelcase = c.humps(s)
print(camelcase)


#Gestion de archivos 

c.write()

c.close()

x = open('caracter.csv')
print(x.read())

import os

if os.path.exists('caracter.csv'):
    os.remove('caracter.csv')

os.rmdir('mi carpeta')










