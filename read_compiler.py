''' Archivo que sirve para leer el lenguaje de COCOr'''

from Thompson.test_expre import string_to_list, list_to_string
from utils import str_list

def read_file(direction):
    list_data =  ['CHARACTERS', 'KEYWORDS', 'PRODUCTIONS']

    # guardamos los datos especificos en una lista correspondiente, estas son las que se requeriran para le creacion
    character = []
    keywords = []
    productions = []
    tokens = []
    data = []  # --> INDICA EL ENCABEZADO

    # manejador de archivo
    filename = []
    count = 0
    # leemos el archivo
    text_file = open(direction, 'r')
    for line in text_file.readlines():
        if line[-1:] == '\n':
            filename.append((line[:-1]))
        else:
            filename.append(line)
    text_file.close()

    for read_line in filename:
        if read_line.strip() == "TOKENS":
            count = 1
        if read_line.strip() == "CHARACTERS":
            count = 2
        if read_line.strip() == "KEYWORDS":
            count = 3
        if read_line.strip() == "PRODUCTIONS":
            count = 4
        
        # anadimos la linea leida para el archivo
        if count == 1:
            tokens.append(read_line)
        if count == 0:
            data.append(read_line)
        if count == 2:
            character.append(read_line)
        if count == 3:
            keywords.append(read_line)
        if count == 4:
            productions.append(read_line)
    
    return data, character, keywords, tokens, productions

# revisa si char | "CHR", es booleano solo para verificar que se encuentre
def evaluate_char(data):
    if ('chr(' in data) or ('CHR(' in data):
        return True
    else:
        return False

def create_file_compiler(data, character, keywords, tokens, productions):
    automata = []
    chars = []
    data_automata_keywords = []
    data_for_keywords = []
    names_ak = []
    names_automatas = []
    
    # verificamos el encabezado
    if data[0] != '':
        encabezado = data[0].split(' ')
        if encabezado[0] == 'COMPILER':
            # creamos el archivo que se generara
            filename = open('./Outputs/'+ encabezado[1] +'.py', 'w+',  encoding="utf-8")   # Creamos el archivo de compilacion
            # filename = open(encabezado[1] +'.py', 'w+')
    
    # comenzamos a escribir en el archivo
    filename.write('# Este es el scanner que se generara con las reglas establecidas por ./Inputs/%s.ATG' % encabezado[1])
    filename.write('\n')
    filename.write('import os')
    filename.write('\n')
    filename.write('import sys')
    filename.write('\n')
    filename.write('sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))')
    filename.write('\n')
    filename.write('from utils import character_read')
    filename.write('\n')
    filename.write('from scanner import scanner_data')
    filename.write('\n')
    filename.write('\n')
    filename.write('# Obtenemos los keywords')
   
    # recorremos la lista de keywords
    for i in range(len(keywords)):
        # leemos el indicador, y separamos los datos que estan en ese indicador
        if (keywords[i].strip() == 'KEYWORDS'):
            pass
        else:
            # miramos los espacios
            if keywords[i] != '':
                s0 = keywords[i].split('=')
                # chr(34) son las comillas --> ""
                s1 = s0[1].replace(chr(34), '')
                s1 = s1.replace(chr(39), '')
                s1 = s1.replace('.', '')
                '''
                print(s0)
                print(s1)
                '''
                data_for_keywords.append(s1.strip())
    
    filename.write('\n')
    filename.write('keywords = %s' % str(data_for_keywords))
    filename.write('\n')

    # obtenemos los characters
    filename.write('\n')
    filename.write('# characters disponibles')

    # recorremos la lista
    for i in range(len(character)):
        # indicador
        if character[i].strip() == 'CHARACTERS':
            pass
        else:
            index_char = character[i].rfind('.')
            new_character = character[i][:index_char] + '' + character[i][index_char+1:]
            # si esta vacio 
            if new_character != '':
                filename.write('\n')
                # quitamos el igual
                s0 = new_character.split('=')
                # print(s0)
                # verificamos si son char 
                if evaluate_char(s0[1]):
                    chars.append(s0[1].lower())
                    filename.write(new_character.lower())
                    filename.write('\n')
                    filename.write('%s = character_read(%s)' % (s0[0], s0[0].strip().lower()))
                    filename.write('\n')
                elif (s0[1].strip() == "'A' . 'Z'") or (s0[1].strip() == "'A' . 'Z'.") or (s0[1].strip()== chr(34)+"A"+chr(34)+ ".." +chr(34)+"Z"+chr(34)):
                    s0[1] = chr(34)+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+chr(34)
                    filename.write('%s = %s' % (s0[0], s0[1]))
                    filename.write('\n')
                    filename.write('%s = character_read(%s)' % (s0[0], s0[0].strip()))
                    filename.write('\n')
                elif (s0[1].strip() == "'a' . 'z'") or (s0[1].strip() == "'A' . 'Z'.") or (s0[1].strip()== chr(34)+"A"+chr(34)+ ".." +chr(34)+"Z"+chr(34)):
                    s0[1] = chr(34)+"abcdefghijklmnopqrstuvwxyz"+chr(34)
                    filename.write('%s = %s' % (s0[0], s0[1]))
                    filename.write('\n')
                    filename.write('%s = character_read(%s)' % (s0[0], s0[0].strip()))
                    filename.write('\n')
                else:
                    filename.write(new_character)
                    filename.write('\n')
                    filename.write('%s = character_read(%s)' % (s0[0], s0[0].strip()))
                    filename.write('\n')

    filename.write('\n')
    filename.write('# Aqui se obtenemos cada uno de los tokens permitidos')
    filename.write('\n')          

    # si encuentra un END se acaba
    # print(tokens[-1][0:3]) 
    if tokens[-1][0:3] == 'END':
        tokens.pop()
    # print(tokens)
    for i in range(len(tokens)):
        # indicador
        if tokens[i].strip() == 'TOKENS':
            pass
        else:
            if len(tokens[i]) != 0:
                # convertimos los datos a una lista
                data_list = string_to_list(tokens[i])
                # quitamos los puntos
                if data_list[len(data_list)-1] == '.':
                    data_list.pop()
                # print(data_list)
                
                # los datos evaluados anteriormente los pasamos a una lista
                data_list = list_to_string(data_list)
                data_list = data_list.strip()
                # cambiamos a plus
                data_list = data_list.replace(chr(34), '+')
                data_list = data_list.replace('(H)',chr(34) + 'H' + chr(34))
                data_list = data_list.replace("("," + "+chr(34)+" ("+chr(34)+"+")
                # data_list = data_list.replace('= ', '+')
                data_list = data_list.replace(")"," + "+chr(34)+")"+chr(34))
                data_list = data_list.replace("|"," + "+chr(34)+"|"+chr(34)+"+")
                data_list = data_list.replace(".", chr(34)+". "+chr(34))
                data_list = data_list.replace("{", " + "+chr(34)+" (("+chr(34)+"+")
                data_list = data_list.replace("[", " + "+chr(34)+" (("+chr(34)+"+")
                data_list = data_list.replace("}", " + "+chr(34)+")*) "+chr(34)+"+")
                data_list = data_list.replace("]", " + "+chr(34)+")*) "+chr(34)+"+")

                # EXCEPT KEYWORD
                ek = data_list.split()
                # print(ek)
                if len(ek)>2 and ek[len(ek)-1] == 'KEYWORDS' and ek[len(ek)-2] == 'EXCEPT':
                    ek.pop()
                    ek.pop()
                    names_ak.append(ek[0])
                    data_automata_keywords.append(ek[0])
                elif ek[len(ek)-2] == 'SET' and ek[len(ek)-3] == 'IGNORE':
                    ek.pop(len(ek)-3)
                    ek.pop(len(ek)-2)
                    # data_automata_keywords.append(ek[0])
                    continue
                else:
                    names_automatas.append(ek[0])
                    automata.append(ek[0])
                    # print(automata)
            
                # convertimos a lista y lo separamos por --> =
                ek = list_to_string(ek)
                ek = ek.split('=')
                
                # print(ek)
                ek[1]= ek[1].replace(")*)", ")*) ")
                
                 # signo plus
                if ek[1][0]== "+":
                    ek[1] = ek[1].replace("+","",1)
                if ek[1][-1] == "+":
                    ek[1] = ek[1][:-1]
                
                s1 = string_to_list(ek[1])

                # se observa espacios los vamos a quitar
                if s1[-2] == " ":
                    s1.pop(len(s1)-2)
                    
                for i in range(len(s1)):
                    if s1[i] == "." or s1[i] == ",":
                        s1.insert(i+1, " ")

                ek[1] = list_to_string(s1)
                convert = ek[0]+"="+list_to_string(ek[1])
                # print(convert)

                convert = convert.replace("((", " ((")
                convert = convert.replace("+++", " +")
                convert = convert.replace("++", " +")
                convert = convert.replace(chr(34)+"("+chr(34), chr(34)+" ("+chr(34))
                # print(convert)
                
                # separamos por simbolos
                space = convert.split("=")
                
                if string_to_list(space[1])[1] == " ":
                    x = string_to_list(space[1])
                    x.pop(1)
                    space[1] = list_to_string(x)
            
            
                convert = space[0]+" = "+list_to_string(space[1])
                filename.write(convert)
                filename.write("\n")

    # print(names)
    filename.write('\n')
    filename.write('# Nombres de las variables')
    filename.write('\n')
    filename.write('names_automatas_keywords = %s' % names_ak)
    filename.write('\n')
    filename.write('names_automatas = %s' % names_automatas)
    filename.write('\n')
    filename.write('\n')
    filename.write('# Si existe EXCEPT WORDS se agrega a esta lista')
    filename.write('\n')
    filename.write('data_automata_keywords = %s' % str_list(data_automata_keywords))
    filename.write('\n')
    filename.write('automata = %s' % str_list(automata))
    filename.write('\n')
    filename.write('data_characters = %s' % str_list(chars))
    filename.write('\n')
    filename.write('\n')
    filename.write('# Se scannea lo generado')
    filename.write('\n')
    filename.write('if __name__ == '+chr(39)+'__main__'+chr(39)+':')
    filename.write('\n')
    filename.write('\t')
    filename.write('scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)')

                



        
        
    
