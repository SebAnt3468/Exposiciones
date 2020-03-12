#dos formas

Numeros={5,6,2,4,7,3} #forma 1
print(Numeros)
S = set("Computadora y ratones")  #forma 2
print(S)
t= len(S)  #cuenta
print(t)
r = 6 in Numeros  #para saber si un número pertenece al set
print(r)
p = 4 not in Numeros
print(p)

A = S.add("sw")
print(S)

Numeros.remove(4)
print(Numeros)

#Operadores de intersección y unión

a={3,6,5,7,4}
u={4,6,8,9,10}
print(a&u)  #Operadores de intersección
print(a|u)  #Operadores de unión

print(a-u) #diferencia entre conjuntos

print(a^u)  #los elementos que estan en s o u.  pero  no en ambos

print(a<=u)
print(u<=a)

print(a.isdisjoint(u)) #inndica si dos conjuntos son disconexos
