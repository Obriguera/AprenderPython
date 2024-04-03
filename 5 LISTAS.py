lista_vacia = [1,2,3,4,5]

#Modificacion de elemento de lista
print(lista_vacia[0])
lista_vacia[0] = 233
print(lista_vacia[0])


# Agregar un elemento al final de la lista
lista_vacia.append(6)
print(lista_vacia)  

# Insertar un elemento en una posición específica
lista_vacia.insert(1, 99)  # Insertar el número 5 en la posición 1
print(lista_vacia)

#remover elemento 233
lista_vacia.remove(233)
print(lista_vacia) 
#remover elemento en la posición
lista_vacia.pop(0)
print(lista_vacia) 

#Borro esta variable
del lista_vacia 