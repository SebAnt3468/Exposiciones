from _collections import deque   #definir colas
cola = deque()
print(cola)

cola=deque(["Azul", "morado"]) #definir lista
print(cola)

cola.append("Turqueza")  #agregar elemento
print(cola)

print(cola.popleft())   #quita el primer elemento
print(cola)

import queue         #
cola2 = queue.Queue(maxsize=2)
cola2.put("Azul")
print(list(cola2.queue)) 

cola2.get()
print(list(cola2.queue))
