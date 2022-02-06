import os

# Verzeichnis in dem sich die Dateien befinden.
# initialdir = b"'C:\Users\chvatdi00\Documents\Python Scripts\Spectro'"
initialdir = os.getcwdb()

# Log Files
wrapper_logfile = os.getcwd() + r"\data\wrapper.log"
oildata_logfile = os.getcwd() + r"\data\oildata.log"

# Das "Template" für das Auswertefile, in der Regel einfach die ersten beiden Zeilen deines Auswertefiles.
#template = 'C:/Users/chvatdi00/Documents/Python Scripts/Spectro/Auswertung_Susanne_Header.xlsx'
xltemplates = os.getcwd() + r'/templates.xlsx'
#spectro_template = os.getcwd() + '/Auswertung_Susanne_Header.xlsx'

# Name und Ort der temporären Datei.
tempfile = os.getcwd() + r'\data\temp.csv'

# Output File Name
# outfile = 'C:/Users/chvatdi00/Documents/Python Scripts/Spectro/csv_converted.xlsx'
outfile = os.getcwd() + r'/csv_converted.xlsx'
zoutfile = os.getcwd() + r'/Zusammenfassung.xlsx'

