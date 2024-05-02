entrada = input("Ingrese direccion del archivo que contiene al automata: ")
with open(entrada, 'r') as file:
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
        if line[1]=="*":
            estado_inicial = line[2]
            estados_finales.append(line[2])
            estados.append(line[2])
        else:
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

# print("alfabeto: ",alfabeto)
# print("estado_inicial: ",estado_inicial)
# print("estados: ", estados)
# print("estados_finales: ",estados_finales)
# print("transiciones: ",transiciones)
###########################################FORMAR LOS ESTADOS FINALES####################################################
estados_DFA = [[estado_inicial]]

for camino in alfabeto:
    estado = []
    for transicion in transiciones:
        if transicion[0] == (estado_inicial, camino):
            estado.append(transicion[1])
    if estado not in estados_DFA:
        estados_DFA.append(estado)


#este for sirve para sacar los estados de DFA
for estado in estados_DFA:
    #dic[str(estado)] = []
    for camino in alfabeto:
        tupla = []
        for sub_estado in estado:
            for transicion in transiciones:
                if transicion[0] == (sub_estado, camino) and (transicion[1] not in tupla):
                    tupla.append(transicion[1])
            if tupla not in estados_DFA:
                estados_DFA.append(tupla)
            #dic[str(estado)].append(tuple(tupla))

dic = {}
#esto es para evaluar a donde va cada estado del DFA
for camino in alfabeto:
    for estado in estados_DFA:
        if str(estado) not in dic:
            dic[str(estado)] = []
        estado_dfa = []
        for mini_estado in estado:
            for transicion in transiciones:
                if transicion[0] == (mini_estado, camino) and (transicion[1] not in estado_dfa):
                    estado_dfa.append(transicion[1])
        dic[str(estado)].append(tuple(estado_dfa))

# print(transiciones,"\n\n\n")
# print(dic)
salida = input("Ingrese el nombre con el que quiere guardar el archivo que contiene al DFA (debe agregar la extension): ")
archivo_DFA = open(salida, 'w')

archivo_DFA.write("Estados\n")
final_e_inicial=False
final = False

for estado in estados_DFA:
    if estado_inicial == (str(estado)[2:-2]):
        
        for estado_final in estados_finales:
            if estado_final in estado:
                archivo_DFA.write(">"+"*" + str(estado).replace('\'','').replace('[', '{').replace(']', '}').replace(",}", "}")+"\n")
                final_e_inicial = True
                break
        if not final_e_inicial:
            archivo_DFA.write(">" + str(estado).replace('\'','').replace('[', '{').replace(']', '}').replace(",}", "}")+"\n")
        continue
    for estado_final in estados_finales:
        if estado_final in estado:
            archivo_DFA.write("*"+ str(estado).replace('\'','').replace('[', '{').replace(']', '}').replace(",}", "}")+"\n")
            final = True
            break
    if not final:
        archivo_DFA.write(str(estado).replace('\'','').replace('[', '{').replace(']', '}').replace(",}", "}")+"\n")
    final=False


archivo_DFA.write("Alfabeto\n")

for camino in alfabeto:
    archivo_DFA.write(camino+"\n")

archivo_DFA.write("Transiciones\n")

for key, value in dic.items():
    for i in range(len(value)):
        archivo_DFA.write(f'{key.replace('\'','').replace('[', '{').replace(']', '}').replace(",}", "}")} {i} -> {str(value[i]).replace('\'','').replace('(', '{').replace(')', '}').replace(",}", "}")}\n')


archivo_DFA.close()

    
    