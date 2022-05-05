''' Tiene las funciones utiles para realizar el analizador '''

from Thompson.test_expre import string_to_list, list_to_string, change_data, regex
from Thompson.operations import get_operation, delete_parentesis
from dfa1.dfa import subset
from graphviz import Digraph

# funcion para convertir letra 
def str_list(data):
    lista = []
    lista.append('[')
    for i in range(len(data)):
        lista.append(data[i])
        if i != len(data)-1 :
            lista.append(',')
    lista.append(']')
    return list_to_string(lista)

# juntamos la informacion con su operador
def join_data(lst, operator):
    result = [operator] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

# leemos cada uno de los simbolos
def character_read(data):
    data = string_to_list(data)
    parse = False
    new_data = []
    for i in data:
        if (i == '('):
            parse = True
    if (parse == False):
        data = string_to_list(data)
        data = join_data(data, '|')
        data = string_to_list(data)
        data.append(')')
        data.insert(0, '(')
        return list_to_string(data)
    
    while_counter = False
    if (parse == True):
        new_data = []
        for i in data:
            if (i == '('):
                while_counter = True
            if (i == ')'):
                while_counter = False
            # si es True
            if (while_counter == True):
                if (i == '(') or (i == ')'):
                    pass
                else:
                    new_data.append(i)
            elif (while_counter == False):
                if i == ')':
                    pass
                else:
                    new_data.append(i)
                new_data.append('|')
        
        if new_data[len(new_data)-1] == '|':
            new_data.pop()
        if new_data[len(new_data)-1] == ' ':
            new_data.pop()
            new_data.pop()
        
        # print(new_data)
        new_data.append(')')
        new_data.insert(0, '(')
        # print(list_to_string(new_data))
        return list_to_string(new_data)

# funcion para graficar el automata
def graphic(exp, data, name):
    dot = Digraph(name='Automata')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')

    for i in range(len(data)):
        dot.node(str(data[i][1]))
        
    dot.attr('node', shape='circle')

    for i in range(len(exp)):
        dot.edge(str(exp[i][0]), str(exp[i][2]), label= str(exp[i][1]))
    
    dot.render(name + '.gv', view=True)

# funcion para crear el automata AFD
def create_automata(data):
    expresion = regex(data)
    exp, data = get_operation(expresion)
    automata, new_state = subset(exp, data)
    # print(new_state)
    # print(automata)
    return new_state, automata
    




