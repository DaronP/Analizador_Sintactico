from libs import *
from tqdm import tqdm

EPSILON = 'ε'
#trans: lista de nodos; estados de transicion
#strt_end, lim: nodos de inicio/fin
def subconjuntos(trans, strt_end):
    
    #Simbolos de la expresion
    symbols = []

    for i in range(len(trans)):
        if trans[i][1] != EPSILON and trans[i][1] not in symbols:
            symbols.append(trans[i][1])

    

    estados = []
    new_lim = []
    tabla_trans = []

    #Calculando la cerradura-e de las transiciones de Thomson
    estados_raw = []
    estados_raw = cerr_e(trans, strt_end[0][0])
    estados.append(estados_raw)
    new_lim.append(estados_raw)

    #Calculando la cerradura-e de la funcion Move() de cada transicion por simbolo
    estado = 0
    while estado < len(estados):
        for symbol in symbols:
            #move(T, a)
            move_res = move(trans, estados[estado], symbol)
            #Cerradura-e de move(T, a)
            e_move = cerr_e(trans, move_res)
            tabla_trans.append([estados[estado], symbol, e_move])

            #Appendeando nuevos limites de DFA
            for nodo in strt_end:
                if nodo[1] in e_move:
                    new_lim.append(e_move)
            #Appendenado nuevos estados que no sean vacios
            if e_move not in estados and e_move is not None:
                estados.append(e_move)
        estado += 1
    
    #Eliminando estados vacios
    estado = 0
    while estado < len(tabla_trans):
        if len(tabla_trans[estado][0]) == 0 or len(tabla_trans[estado][2]) == 0:
            tabla_trans.pop(estado)
            estado -= 1
        estado += 1

    print("\nTabla de transicion ")
    #print(tabla_trans)

    tabla_estados = []
    end = []

    #Estados a letas
    for tran in tabla_trans:
        if tran[0] in estados and tran[2] in estados:
            tabla_estados.append([chr(65 + estados.index(tran[0])), tran[1], chr(65 + estados.index(tran[2]))])
    #Estados iniciales/finales
    lista_estados = []

    for item in tabla_estados:
        lista_estados.append([item[0], item[2]])

    #convietiendo a estados "puros"
    estados_dict = dict()
    for item in lista_estados:
        if (item[0] in estados_dict.keys()) and (item[1] not in estados_dict[item[0]]):
            estados_dict[item[0]].append(item[1])
        else:
            estados_dict[item[0]] = [item[1]]

    #Calculando el minimo
    print("calculando minimo")
    minimo = []
    keys = list(estados_dict.keys())
    vals = list(estados_dict.values())
    
#    for key in tqdm(range(len(keys))):
#        for v in range(len(vals)):
#            if keys[key] not in vals[v]:
#                for key2 in range(len(keys)):
#                    if keys[key2] in vals[key]:
#                        key2 += 1
#                    else:
#                        for w in vals[v]:
#                            try:
#                                sym = tabla_estados[lista_estados.index([keys[key], w])][1]
#                                m = [keys[key], sym, keys[key2]]
#                                
#                                minimo.append(m)
#                            except:
#                                continue

    
    for key in tqdm(range(len(keys))):
        if keys[key] not in vals[:key]:
            for key2 in vals[:key]:
                for val in key2:
                    if val in vals[key]:
                        try:
                            #print(keys[key])
                            #print(lista_estados.index([keys[key], val]))
                            sym = tabla_estados[lista_estados.index([keys[key], val])][1]
                            minimo.append([keys[key], sym, val])
                        except:
                            continue

    print("minimo calculado")
    
    #Eliminar duplicados
    print("Eliminando duplicados")
    minimoo = []
    for i in tqdm(range(len(minimo))):        
        if(minimo[i] in minimoo):
            pass
        else:
            minimoo.append(minimo[i])

    min_end = []
    for item in minimo:
        min_end.append([item[0], item[2]])

    print("retornando resultados...")
    return(tabla_estados, lista_estados, minimoo, min_end)

    

    
    
