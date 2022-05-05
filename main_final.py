from read_compiler import read_file, create_file_compiler
archivo = input('Ingrese el nombre del archivo: ')

data, character, keywords, tokens, productions = read_file(archivo)
'''
print(data)
print(character)
print(keywords)
print(tokens)
'''

create_file_compiler(data, character, keywords, tokens, productions)