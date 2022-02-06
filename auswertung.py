from email import header
from unittest import result
import pandas as pd
from pprint import pprint as pp
import helpers
import logging
import os
import config
import datetime

def summary(filename, oil_name):
    result = {
        'Datum': pd.Timestamp.now(),
        'Datei':os.path.basename(filename),
        'Öl':oil_name,
        }
    fields = ['Unique Code','General Description','Oil/Fluid Long Name','Unit Hours','Oil/Fluid Hours'] # auf die benötigten Felder beschränken
    xdf = pd.read_excel(filename)[fields]
    new_xdf = xdf.applymap(helpers.corr) # correct the contents
    new_xdf = new_xdf[new_xdf['Oil/Fluid Long Name'] == oil_name] # nur die Zeilen mit 'oil_name' ausfiltern
    uniquecodes = new_xdf['Unique Code'].unique() # Alle Unique Codes der Motoren auslesen - nur unterschiedliche codes kommen in die Liste
    No_of_Engines = len(uniquecodes)
    result.update({
        'Zeilen': new_xdf.shape[0],
        'Eindeutige Motoren': No_of_Engines
    })
    if new_xdf.shape[0] == 0: #no enties found
        raise ValueError(f"kein Öl mit Namen '{oil_name}' in '{os.path.basename(filename)}' gefunden.")
    oil_sum = 0
    count_sum = 0
    for u in uniquecodes:
        df = new_xdf[new_xdf['Unique Code'] == u].sort_values(by = ['Unit Hours'],ascending=[True])
        try: #try to calculate oil running hours
            oil_age = df['Unit Hours'].max() - df['Unit Hours'].min() + df.iloc[0]['Oil/Fluid Hours']
            if oil_age == oil_age: #this is a trick to check for NAN
                oil_sum += oil_age
                count_sum += 1
        except Exception:
            pass # do nothing on entry rows with missing parameters.
    result.update({
        'gültige Motoren': count_sum,
        'Kumulierte Öl Stunden': int(f"{oil_sum:0.0f}"),
        'Mittlere Öl Stunden pro gültigem Motor': int(f"{oil_sum / count_sum:0.0f}")
    })
    rdf = pd.DataFrame.from_dict(result, orient='index')
    logging.info(f"Exporting Zusammenfassung to {config.zoutfile}.")
    rdf.to_excel(config.zoutfile, header=False)
    print(rdf)
    #os.startfile(config.zoutfile)





















    logging.info(f"Counting unique 'Unique Code' in: {filename}")
    xl_file = filename.split('/')[-1]
    xdf = pd.read_excel(filename)
    ne = xdf['Unique Code'].nunique()
    logging.info(f"Number of unique 'Unique Code' in {filename}: {ne}")
    
    
    
    
    
    
    return f"Number of unique 'Unique Code' fields: {ne}"
