# Este es el scanner que se generara con las reglas establecidas por ./Inputs/Hexnumber.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = ['while', 'do']

# characters disponibles
upletter  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upletter  = character_read(upletter)

downletter  = "abcdefghijklmnopqrstuvwxyz"
downletter  = character_read(downletter)

letter = "abcdefghijklmnopqrstuvwxyz" + upletter + downletter 
letter  = character_read(letter)

digit = "0123456789" 
digit  = character_read(digit)

hexdigit = digit + "ABCDEF"
hexdigit  = character_read(hexdigit)

hexterm = 'H'
hexterm  = character_read(hexterm)

tab = chr(9)
tab  = character_read(tab)

eol = chr(10)
eol  = character_read(eol)

whitespace = chr(13)+eol+tab+chr(13)
whitespace  = character_read(whitespace)

sign ='+'+'-'
sign  = character_read(sign)

# Aqui se obtenemos cada uno de los tokens permitidos
ident = letter+" (("+letter+"|"+digit+")*)"
hexnumber = hexdigit+" (("+hexdigit+")*) "+hexterm
number = digit+" (("+digit+")*)"
signnumber = "(("+sign+")*) "+digit+" (("+digit+")*)"
whitetoken = whitespace+" (("+whitespace+")*)"

# Nombres de las variables
names_automatas_keywords = ['ident', 'hexnumber']
names_automatas = ['number', 'signnumber', 'whitetoken']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = [ident,hexnumber]
automata = [number,signnumber,whitetoken]
data_characters = [ chr(9), chr(10), chr(13)+eol+tab+chr(13)]

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)