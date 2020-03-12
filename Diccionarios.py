

Diccionario: dict={"clave": 4, "clave2": 8 }
print(Diccionario.items()) #imprime los valores
print(Diccionario.keys())   #imprime palabras
print(Diccionario.values())  #imprime los valores numeros
D2=Diccionario.copy()   #copia el diccionario
print(D2.clear())       #borrar los datos, dejandolo vacio
print(Diccionario)
print(D2)
Diccionario['clave']= "Nueva clave"  #remplaza y agrega otro valor
print(Diccionario)
D2['Clavek']="Ya no está vacía jajaj"
print(D2)
#Crear un diccionario a partir de una lista
Lista_D=['hay alguien', 'ahí'] #definir una lista
d = D2.fromkeys(Lista_D)  #el diccionario
print(d)
d['hay alguien']= 15434
print(d.get('hay alguien'))
r= len(d)       #nos dice cuantos elementos hay
print(r)
d.update({"clave": None})
print(d)
d.pop("hay alguien")
print(d)