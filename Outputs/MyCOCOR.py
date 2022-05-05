# Este es el scanner que se generara con las reglas establecidas por ./Inputs/MyCOCOR.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = [')']

# characters disponibles
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnÒopqrstuvwxyz"
letter  = character_read(letter)

digit = "0123456789"
digit  = character_read(digit)

ignore = chr(13)+chr(10)+chr(9)+'.'
ignore  = character_read(ignore)

comillas = '"'
comillas  = character_read(comillas)

stringletter = ANY-comillas-ignore
stringletter  = character_read(stringletter)

operadores = "+-=()[]{}|.<>"
operadores  = character_read(operadores)

MyANY = "."+ANY-operadores
MyANY  = character_read(MyANY)

# Aqui se obtenemos cada uno de los tokens permitidos
ident = letter+" (("+letter+"|"+digit+")*)"
string = comillasstringletter+" (("+stringletter+")*) "+comillas
operador = operadores
char = '+" ((" +/ +")*) "+letter+'
charnumber = CHR+" (" +digit+" (("+digit+")*) " +")"
charinterval = CHR+" (" +digit+" (("+digit+")*) " +")" +". "". " +CHR+" (" +digit+" (("+digit+")*) " +")"
startcode = +" (" +". "
nontoken = MyANY

# Nombres de las variables
names_automatas_keywords = ['ident']
names_automatas = ['string', 'operador', 'char', 'charnumber', 'charinterval', 'startcode', 'nontoken']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = [ident]
automata = [string,operador,char,charnumber,charinterval,startcode,nontoken]
data_characters = [ chr(13)+chr(10)+chr(9)+'.']

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)