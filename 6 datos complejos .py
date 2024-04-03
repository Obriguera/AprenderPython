#MULTILISTA
array_variado = ["ñocci", 1, 1.0 , False]
array_variado[3] = True
print(array_variado[3])

array_variado3 = ("ñocci", 1, 1.0 , False) #No modificable 
print(array_variado3[1])

conjunto = {"ñocci", 1, 1.0 , False,1} #Esta cosa no permite elementos repetidos
#No lo voy a poder mostrar un elemento con el índice, pero se puede mostrar todo
print(conjunto)


#Dict o diccionario
diccionario = {
    'Nombre' : "Roberto",
    'edad' : 3,
    'nose' : "soy como un json",
    'KEY' : "VALUE"
}
print(diccionario["KEY"])