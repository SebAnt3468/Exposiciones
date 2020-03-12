lista_1 = [4, 'life', 'eternal']   # definir lista
print(lista_1)
lista_1[2]=4
print(lista_1) #cambiar el orden


lista_1.append('life')   #agregar elementos
print(lista_1)

print(lista_1.count('life')) #contador de elementos


lista_1.extend(range(3,12)) #agregar otra lista
print(lista_1)


print(lista_1.index(11)) #la poscición de un elemento de la lista

lista_1.insert(5,'nel') #inserta UN ELEMENTO donde lo indicamos en el range
print(lista_1)

print(lista_1.pop()) #quitar elementos  de la lista
print(lista_1)

lista_1.remove(4) #quitar un elemento
print(lista_1)

lista_1.reverse()  #invierte los elementos
print(lista_1)

lista_1.remove('nel')
lista_1.remove('life')
lista_1.remove('life')

print(lista_1)

lista_1.sort()  #ordena
print(lista_1)