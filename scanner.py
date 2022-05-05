'''
 Archivo para hacer que scanee el archivo generado

'''

from utils import create_automata
from dfa1.simulacion import simulate_dfa

# variables necesarios
key = []
automata = []
automata_keywords = []
characters = []
tokens_list = []
names_ak = []
names_automata = []

# funcion que recorra lo generado en el compilador
def scanner_data(keywords, tokens, data, character, names_automatas_keywords, names_automatas):
    print('Escaneandooo.....\nSe estan creando los automatas')
    key.append(keywords)
    characters = character
    names_ak = names_automatas_keywords
    names_automata = names_automatas
    # print(key)
    
    # creamos el automatas solo si existe un EXCEPT WORDS
    if len(data) != 0:
        for i in range(len(data)):
            # creamos el automata con el algoritmo de subcojuntos
            new_state, table = create_automata(data[i])
            automata_keywords.append([table, new_state])
    # print(automata_keywords)

    if len(tokens) != 0:
        for i in range(len(tokens)):
            # creamos el automata con el algoritmo de subcojuntos
            new_state, table = create_automata(tokens[i])
            automata.append([table, new_state])
    # print(automata)
    
    # tokens_list.append(tokens)
    count = True
    while count:
        m_file = input('Ingrese el archivo a evaluar: ')
        test = open_file(m_file)
        evaluate(test)
        op = input('¿Desea evaluar otro archivo? S/N ')
        if op == 'N':
            count = False

# leemos el archivo txt
def open_file(data):
    m_file = open(data, 'r')
    archivo = []
    for line in m_file:
        archivo.append(line)
    m_file.close()
    return archivo

# data es la lista de lo generado
def evaluate(data):
    print(data)
    # recorremos el archivo
    for i in range(len(data)):
        lines = data[i].split(' ')
        # print(lines)
        for j in range(len(lines)):
            yes = 0
            count = 0
            # revisamos espacios
            if len(lines)-1 == j and lines[j][-1] == '\n':
                word = 0
                # contador para los keywords
                kw = 0
                # contador para los tokens
                tk = 0
                linea = lines[j].replace('\n', '')
                # print(linea)
                if linea in key[0]:
                    print('Keyword: %s' % linea)
                    kw += 1
                else:
                    # evaluacion del automata con except word
                    for k in range(len(automata_keywords)):
                        evaluate_linea = simulate_dfa(linea, automata_keywords[k][0], automata_keywords[k][1])
                        # print(evaluate_linea)
                        if evaluate_linea == 'SI':
                            tk +=1
                        evaluate_linea_second = simulate_dfa('\n', automata_keywords[k][0], automata_keywords[k][1])
                        # print(evaluate_linea_second)
                        if evaluate_linea_second == 'SI':
                            word += 1

                # evaluamos el automata 
                for h in range(len(automata)):
                    linea = lines[j].replace('\n', '')
                    evaluate_linea = simulate_dfa(linea, automata[h][0], automata[h][1])
                    if evaluate_linea == 'SI':
                        tk +=1
                    evaluate_linea_second = simulate_dfa('\n', automata[h][0], automata[h][1])
                    # print(evaluate_linea_second)
                    if evaluate_linea_second == 'SI':
                        word += 1
                
                # si no hay nada en los contadores entonces no pertenece
                if (tk == 0) and (kw == 0):
                    print('Esta palabra %s no pertenece al automata' % linea)
                elif (tk == 0) and (tk >= 1):
                    print('Tokens: %s' % linea)
                
                if evaluate_linea_second == 'NO':
                    print('No existe una linea \n entonces los demas no pertenece')
                elif evaluate_linea_second == 'SI':
                    print('Tokens: NUEVA LINEA')
            else:
                if lines[j] in key[0]:
                    print('Keyword: %s' % lines[j])
                    count += 1
                else:
                    for s in range(len(automata_keywords)):
                        evaluate_line = simulate_dfa(lines[j], automata_keywords[s][0], automata_keywords[s][1])
                        if evaluate_line == 'SI':
                            yes += 1
                for u in range(len(automata)):
                    evaluate_line = simulate_dfa(lines[j], automata[u][0], automata[u][1])
                    if evaluate_line == 'SI':
                        yes += 1
                
                # añadimos tokens
                if yes >= 1:
                    print('Tokens: %s' % lines[j])
                elif count >=1:
                    pass
                else:
                    print('ERROR! Esta palabra %s no pertence' % lines[j])
    # print(lines)

if __name__ == '__main__':
    test = input('Ingrese el archivo: ')
    m_file = open_file(test)
    print(m_file)
    