#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

ciudades_del_mundo=['Venecia','Roma','Vancouver','Toronto','Barcelona','Villa Regina','Cordoba']
print(ciudades_del_mundo)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(ciudades_del_mundo[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(ciudades_del_mundo[1:5])


# 4) Visualizar el tipo de dato de la lista

# In[12]:

type(ciudades_del_mundo)


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(ciudades_del_mundo[2:])


# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(ciudades_del_mundo[:4])

    
# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

ciudades_del_mundo.append('Toronto','Munich')
Print(ciudades_del_mundo)

TypeError: list.append() takes exactly one argument (2 given). El metodo append agrega solo un elemento y aqui se agregan dos.


# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

ciudades_del_mundo.insert(3,'Munich')
print(ciudades_del_mundo)


# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

ciudades_del_mundo.extend(['Sevilla','Ushuaia','Berlin'])
print(ciudades_del_mundo)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

ciudades_del_mundo.index('Toronto')
Me da el indice del lugar donde esta la ciudad por primera vez, no me da el Indice del agregado.


# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

ciudades_del_mundo.index('Bahia Blanca')
ValueError: 'Bahia Blanca' is not in list


# 12) Eliminar un elemento de la lista

# In[25]:

ciudades_del_mundo.remove('Toronto')
print(ciudades_del_mundo)


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

ciudades_del_mundo.remove('Bariloche')
print(ciudades_del_mundo)

ValueError: list.remove(x): x not in list


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

ultima_ciudad=ciudades_del_mundo.pop()
print(ultima_ciudad)


# 15) Mostrar la lista multiplicada por 4

# In[29]:

lista_multiplicada=ciudades_del_mundo*4
print(lista_multiplicada)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

mi_tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(mi_tupla[10:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

20 in mi_tupla
30 in mi_tupla


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

ciudades_del_mundo=['Venecia','Roma','Vancouver','Toronto','Barcelona','Villa Regina','Cordoba'] 
tupla_ciudades_del_mundo=tuple(ciudades_del_mundo)
print(tupla_ciudades_del_mundo)
'Paris'in tupla_ciudades_del_mundo #False porque Paris no esta en la lista
nueva_ciudad='Paris' #Agregar paris a la lista
nueva_tupla=tupla_ciudades_del_mundo,nueva_ciudad
print(nueva_tupla) #Paris, aparece fuera de tupla_ciudades_del_mundo.
'Paris' in nueva_tupla   #True


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

ciudades_lista=['Venecia', 'Roma', 'Vancouver', 'Munich', 'Toronto', 'Munich', 'Barcelona', 'Villa Regina', 'Cordoba', 'Toronto', 'Toronto', 'Munich']
ciudades_lista.count('Toronto')
ciudades_tupla=tuple(ciudades_lista)
ciudades_tupla.count('Toronto')


# 21) Convertir la tupla en una lista

# In[52]:

ciudades_lista1=list(ciudades_tupla)
print(ciudades_lista1)
type(ciudades_lista1)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

primera_v=ciudades_tupla[0]
segunda_v=ciudades_tupla[1]
tercera_v=ciudades_tupla[2]
print(primera_v)
print(segunda_v)
print(tercera_v)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

diccionario_ciudades={'Ciudades':ciudades_del_mundo,'Paises':['Italia','Canada','Espana','Argentian','Alemania'], 'Continente':['Europea','Americano']}
print(diccionario_ciudades)


# 24) Imprimir las claves del diccionario

# In[59]:

print(diccionario_ciudades.keys())


# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(diccionario_ciudades['Ciudades'])


