# Este es el scanner que se generara con las reglas establecidas por ./Inputs/ArchivoPrueba2.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = ['if', 'IF', 'for']

# characters disponibles
letra = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letra  = character_read(letra)

digito = "01234567890"
digito  = character_read(digito)

digitoHex = digito + "ABCDEF"
digitoHex  = character_read(digitoHex)

tab = chr(9)
tab  = character_read(tab)

# Aqui se obtenemos cada uno de los tokens permitidos
identificador = letra+" (("+letra+"|"+digito+")*)"
numero = digito+" (("+digito+")*)"
numeroHex = digitoHex+" (("+digitoHex+")*) " +"H"
tabulador = tab

# Nombres de las variables
names_automatas_keywords = ['identificador']
names_automatas = ['numero', 'numeroHex', 'tabulador']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = [identificador]
automata = [numero,numeroHex,tabulador]
data_characters = [ chr(9)]

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)