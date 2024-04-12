#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:


x=7
if (x<0):
  print('Es menor que cero')
elif (x>0):
  print('Es mayor que cero')
else:
  print('Es igual a cero')

Es mayor que cero

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

variable1=7
variable2='Maria'
if type(variable1) == type(variable2):
  print('Las variables son del msimo tipo')
else:
  print('Las variables no son del mismo tipo')

Las variables no son del mismo tipo


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range (1,21):
    if i%2==0:
        print(i,"Es un numero par")
    else:
        print(i,"Es un numero impar")


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:


for i in range(0,6):
    print(i,'**3=',i**3)


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:


cantidad_de_ciclos=10
for i in range(cantidad_de_ciclos):
    print(i,'este es el numero de ciclos=', i+1)


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:


numero=20
if numero > 0:
    divisor = 2
    print("Los factores de", numero, "son:")
    while numero > 1:
        if numero % divisor == 0:
            print(divisor)
            numero //= divisor
        else:
            divisor += 1
else:
    print("La variable no contiene un número entero mayor a 0.")


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:


x=2
while x<5:
    x +=1
    print('in while', x)
    for i in range(1,4):
        print('in for',i)


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:


for i in range (1,4):
    npar=2*i
    print(npar,'Es par')
    x=0
    while x<i:
        print('fin del ciclo',x)
        x +=1


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:


for i in range(0, 31):  
    es_primo = True  
    divisor = 2
    while divisor * divisor <= i:  
        if i % divisor == 0:  
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(i, end=" ")

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:


Use la sencencia break en el ejercicio anterior.


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:


def encontrar_primos(n):
   compuestos = [False] * (n+1)
   primos = []
    for i in range(2, n+1):
        if not compuestos[i]:
            primos.append(i)
            for j in range(i*i, n+1, i):
                compuestos[j] = True
    return primos
primos_hasta_30 = encontrar_primos(30)
print("Los números primos entre 0 y 30 son:", primos_hasta_30)

# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:


numero = 100
while numero <= 300:
    if numero % 12 != 0:  
        numero += 1
        continue  
    print(numero)  
    numero += 1


# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


numero = 100
while numero <= 300:
    if numero % 3 == 0 and numero % 6 == 0:
        print("El primer número divisible por 3 y múltiplo de 6 en el rango de 100 a 300 es:", numero)
        break
    numero += 1
