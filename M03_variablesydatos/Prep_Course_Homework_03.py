#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]: 
x=25
print(x)
25
# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))
<class 'float'>

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(x))
<class 'int'>

# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre= 'Marcela'


# 5) Crear una variable que contenga un número complejo

# In[3]:
m=5+5j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(m))
<class 'complex'>

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:

pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

var1='True'
var2= True
# son distintos tipos de datos la var1 es string y var2 es bool. 

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(var1))
pritn(type(var2))

'str'
'bool'

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

x=5+3.1

# 11) Realizar una operación de suma de números complejos

# In[2]:
x=4+1j
y=1+5j
z=x+y
print(z)

5+6j

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

x=7.5
y=2+3j
z=x+y
print(z)

9.5+3j

# 13) Realizar una operación de multiplicación

# In[5]:

x=5
y=7
z=x*y
print(z)

35

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

x=2**8
print(x)

256

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
x=27/4
print(x)

6.75


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print(int(x))

6

# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

print(27%4)

3

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

print(int(x)*4+(27%4))

27

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

'$ '+'# '+'@'

'$ # @'

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

"2"==2

False #"2" es un tipo de dato 'str' y 2 es un 'int'

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
num=int("2")
print(type(num))
num==2

<class 'int'>

True

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

could not convert string to float: '3,8'

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
x=3
x-=1
print(x)

2




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:





# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:






# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:



