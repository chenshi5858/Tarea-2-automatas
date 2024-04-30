
with open('nfa4.txt', 'r') as file:
    automata = file.readlines()
########################################EXTRACCIÓN DE DATOS##################################################
estados = []
estado_inicial = None
estados_finales = []
alfabeto = []
copia_automata = [line for line in automata]
transiciones = []

for line in automata:
    if line == automata[0]:
        copia_automata.remove(line)
        continue
    if line[0] == ">":
        estado_inicial = line[1]
        estados.append(line[1])
    elif line[0] == "*":
        estados_finales.append(line[1])
        estados.append(line[1])
    elif line == "Alfabeto\n":
        copia_automata.remove(line)
        automata = [line for line in copia_automata]
        break
    else: 
        estados.append(line[0])
    copia_automata.remove(line)

for line in automata:
    if line == 'Transiciones\n':
        copia_automata.remove(line)
        automata = [line for line in copia_automata]
        break
    alfabeto.append(line[0])
    copia_automata.remove(line)

for line in automata:
    transiciones.append(((line[0], line[2]), line[7]))

# print(alfabeto)
# print(estado_inicial)
# print(estados)
# print(estados_finales)
# print(transiciones)
###########################################FORMAR LOS ESTADOS FINALES####################################################
estados_finales = []

for camino in alfabeto:
    ...

# for transicion_1 in transiciones:
#     estado=[]
#     if transicion_1[1] not in estado:
#         estado.append(transicion_1[1])

#     for transicion_2 in transiciones:
#         if transicion_1[0] == transicion_2[0] and (transicion_2[1] not in estado):
#             estado.append(transicion_2[1])

#     if estado not in estados_finales:
#         estados_finales.append(estado)

# print(estados_finales)


    

