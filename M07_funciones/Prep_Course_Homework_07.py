#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True



# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    return primos

primos=[1,2,3,4,5,6,7,8,9,10,11]
lista_de_primos=filtrar_primos(primos)
print(lista_de_primos)


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def numero_mas_repetido(lista):
    frecuencias = {}
    for x in lista:
        if x in frecuencias:
            frecuencias[x] += 1
        else:
            frecuencias[x] = 1
    
    numero_mas_repetido = None
    repeticiones = 0
    for x, frecuencia in frecuencias.items():
        if frecuencia > repeticiones:
            numero_mas_repetido = x
            repeticiones = frecuencia
    
    return numero_mas_repetido, repeticiones

x = [1,2,4,5,9,4,4,7,8,2,2,5,6,0,4,4]
resultado = numero_mas_repetido(x)
print(resultado[0])
print(resultado[1])


# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def conversion_temperatura(valor,origen,destino):
    if origen=='C' and destino=='F':
        conversion=(valor*9/5)+32
    elif origen=='C' and destino=='K':
        conversion= valor+273,15
    elif origen=='F' and destino=='C':
        conversion= (valor-32)*(5/9)
    elif origen== 'K' and destino== 'C':
        conversion=valor-273,15
    elif origen== 'F' and destino== 'K':
        conversion=((valor-32)*(5/9))+273,15
    elif origen== 'K' and destino== 'F':
        conversion=((valor-273,15)*(9/5))+32
    else:
        conversion=valor  
    return conversion 

valor=35
origen='C'
destino='F'
conversion=conversion_temperatura(valor,origen,destino)
print(f" {valor} {origen} es igual a {conversion} {destino}")

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

Temperatura=['C','F','K']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado', Temperatura[i], 'a', Temperatura[j], ':', conversion_temperatura(1, Temperatura[i], Temperatura[j]))


# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial (numero):
    if not (numero, int) or numero <= 0:
        return 'No tiene factorial'
    elif (numero>1):
        numero=numero*factorial(numero-1)
    return numero


