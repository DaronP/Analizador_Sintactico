from operator import itemgetter
from collections import Counter
from libs import *
from tqdm import tqdm

EPSILON = 'ε'
def thomson(exp_posfix, alfa):

    nodos = []
    pila_fin = []
    num = 1

    prim = []
    
    for i in tqdm(range(len(exp_posfix))):
        if exp_posfix[i] in alfa or exp_posfix[i] == EPSILON:
            nodos.append([num, exp_posfix[i], num + 1])
            pila_fin.append([num, num + 1])
            num += 2

        if exp_posfix[i] == '*':           
            ultim = pila_fin[-1][0]
            penultim = pila_fin[-1][1]

            n1 = [num, EPSILON, ultim]
            n2 = [penultim, EPSILON, ultim]

            ultim = num
            num += 1

            n3 = [penultim, EPSILON, num]
            n4 = [ultim, EPSILON, num]

            penultim = num

            vert = nodos.pop()
            
            nodos.append([vert, n1, n2, n3, n4])

            pila_fin.pop()
            pila_fin.append([ultim, penultim])
            num += 1

        if exp_posfix[i] == '|':
            ultim = nodos.pop()
            penultim = nodos.pop()

            n1 = [num, EPSILON, pila_fin[-2][0]]
            n2 = [num, EPSILON, pila_fin[-1][0]]
            n3 = [pila_fin[-2][1], EPSILON, num + 1]
            n4 = [pila_fin[-1][1], EPSILON, num + 1]

            nodos.append([ultim, penultim, n1, n2, n3 ,n4])

            inicio = num
            num += 1
            final = num
            num += 1

            #prim = pila_fin.pop()
            pila_fin.pop()
            pila_fin.pop()
            pila_fin.append([inicio, final])

        if exp_posfix[i] == '_':
            
            ultim = nodos.pop()
            penultim = nodos.pop()

            ultim_nodo = pila_fin.pop()
            penultim_nodo = pila_fin.pop()

            '''
            try:
                ultim_nodo = pila_fin[-1]
                penultim_nodo = pila_fin[-2]
            except:                
                ultim_nodo = pila_fin.pop()
                penultim_nodo = prim
            
            for no_se in range(len(pila_fin)):
                pila_fin.pop()
            '''
            limpias = sacar_lista(penultim)

            for val in limpias:
                for v in range(0, 3):
                    if limpias[limpias.index(val)][v] == ultim_nodo[1]:
                        limpias[limpias.index(val)][v] = penultim_nodo[0]
                
            pila_fin.append([penultim_nodo[0], ultim_nodo[1]])
            nodos.append([limpias, ultim])

            #Corrigiendo concatenaciones
            #if exp_posfix[i - 1] == '|' or exp_posfix[i - 1] == '*' or exp_posfix[i - 1] == '_':
            try:
                #Si nodos tiene solo un nivel
                li = []
                for l in nodos[0][-1]:
                    for l2 in l:
                        if type(l2) is int:
                                li.append(l2)
                li = sorted(li)

                '''
                for w in range(len(li) - 1, - 1, - 1):        
                    if(li[w] in li[:w]):
                        del(li[w])'''

                lii = []
                for w in range(len(li)):
                    if li[w] in lii:
                        pass
                    else:
                        lii.append(li[w])

                if nodos[0][0][-1][-1] != lii[-2]:
                    nodos[0][0].append([nodos[0][0][-1][-1], EPSILON, lii[-2]])
            except:
                try:
                    #Si nodos tiene dos niveles
                    li = []
                    for l in nodos[0][-1]:
                        if type(l) is int:
                            li.append(l)

                    li = sorted(li)

                    if nodos[0][0][-1][-1] != li[-2]:
                        nodos[0][0].append([nodos[0][0][-1][-1], EPSILON, li[-2]])

                    buff = []
                    for l in nodos[0][0]:
                        buff.append(l)
                    buff2 = []
                    for l2 in nodos[-1][0]:
                        buff2.append(l2)
                                            
                    if nodos[-1][0][-1][0] not in buff or nodos[-1][0][-1][0] not in buff2:
                        if nodos[-1][0][-1][-1] not in buff or nodos[-1][0][-1][-1] not in buff2:
                            li = []
                            for l in nodos[-1][-1]:
                                if type(l) is list:
                                    for l2 in l:
                                        if type(l2) is list:
                                            for l3 in l2:
                                                if type(l3) is int:
                                                    li.append(l3)
                                        else:
                                            if type(l2) is int:
                                                li.append(l2)
                                else:
                                    if type(l) is int:
                                        li.append(l)
                            li = sorted(li)

                            '''
                            for w in range(len(li) - 1, - 1, - 1):        
                                if(li[w] in li[:w]):
                                    del(li[w])'''

                            lii = []
                            for w in range(len(li)):
                                if li[w] in lii:
                                    pass
                                else:
                                    lii.append(li[w])

                            if exp_posfix[i - 1] not in alfa:
                                if nodos[0][-1][-1] != nodos[-1][0][-1][0]:
                                    nodos[0][0].append([nodos[0][-1][-1], EPSILON, nodos[-1][0][-1][0]])
                            
                            if nodos[-1][0][-1][-1] != lii[-2]:
                                nodos[0][0].append([nodos[-1][0][-1][-1], EPSILON, lii[-2]])
                except:
                    pass

                       
            '''
            if exp_posfix[i-1] == '*' or exp_posfix[i-1] == '|':
                last = sorted(ultim, key=itemgetter(0))
                nodos.append([limpias[-1][-1], 'wasd', last[-1][0]])
            '''
            
    respuesta = sorted(sacar_lista(nodos), key=itemgetter(0))

    #Eliminar duplicados
    '''
    for i in range(len(respuesta) - 1, - 1, - 1):        
        if(respuesta[i] in respuesta[:i]):
            del(respuesta[i])'''

    wasd = []
    for i in range(len(respuesta)):
        if respuesta[i] in wasd:
            pass
        else:
            wasd.append(respuesta[i])

    

    return wasd, pila_fin



