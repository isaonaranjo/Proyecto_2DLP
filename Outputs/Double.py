# Este es el scanner que se generara con las reglas establecidas por ./Inputs/Double.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = ['while', 'do']

# characters disponibles
digit = "0123456789" 
digit  = character_read(digit)

tab = chr(9)
tab  = character_read(tab)

eol = chr(10)
eol  = character_read(eol)

blanco = eol+chr(13)+tab+' '
blanco  = character_read(blanco)

# Aqui se obtenemos cada uno de los tokens permitidos
number = digit+" (("+digit+")*)"
decnumber = digit+" (("+digit+")*) " +". "+digit+" (("+digit+")*)"
white = blanco+" (("+blanco+")*)"

# Nombres de las variables
names_automatas_keywords = []
names_automatas = ['number', 'decnumber', 'white']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = []
automata = [number,decnumber,white]
data_characters = [ chr(9), chr(10), eol+chr(13)+tab+' ']

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)