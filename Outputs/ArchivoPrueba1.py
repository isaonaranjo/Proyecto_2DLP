# Este es el scanner que se generara con las reglas establecidas por ./Inputs/ArchivoPrueba1.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = ['if']

# characters disponibles
letra = "abcdefghi"
letra  = character_read(letra)

digito = "01"
digito  = character_read(digito)

# Aqui se obtenemos cada uno de los tokens permitidos
id = letra+" (("+letra+"|"+digito+")*)"
numero = digito+" (("+digito+")*)"

# Nombres de las variables
names_automatas_keywords = ['id']
names_automatas = ['numero']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = [id]
automata = [numero]
data_characters = []

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)