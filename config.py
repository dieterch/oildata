import os

# Verzeichnis in dem sich die Dateien befinden.
initialdir = os.getcwdb()

# Log Files
wrapper_logfile = os.getcwd() + r"\data\wrapper.log"
oildata_logfile = os.getcwd() + r"\data\oildata.log"

# Das "Template" für das Auswertefile, in der Regel einfach die ersten beiden Zeilen deines Auswertefiles.
xltemplates = os.getcwd() + r'/templates.xlsx'

# Name und Ort der temporären Datei.
tempfile = os.getcwd() + r'\data\temp.csv'

# Output File Names
outfile = os.getcwd() + r'/csv_converted.xlsx'
zoutfile = os.getcwd() + r'/Zusammenfassung.xlsx'

