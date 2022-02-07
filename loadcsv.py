import os
import sys
import tempfile
import pandas as pd
import numpy as np
from pprint import pprint as pp
import subprocess
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
import config
import re
import logging
import helpers

def lookup(key, tmpl, df):
    if key in tmpl:
        erg = [v for v in tmpl[key] if v in df.columns]
        #print(erg)
        return erg[0] if erg else np.nan
    else:
        return np.nan

def load(filename):
    # File in utf-8 umwandeln, Fehler im CSV korrigieren
    checkedfile = helpers.checkfile(filename)
    logging.info(f"Pre Check File {filename} completed.")
    
    # analyze encoding and delimiter
    analysis = helpers.analyze_file(checkedfile)

    # Spectro Daten in ein pandas DataFrame einlesen: 
    sdf = pd.read_csv(checkedfile, sep=analysis['delimiter'], encoding=analysis['encoding'], index_col=False)
    logging.info(f"CSV {filename} loaded.")

    # Quick check: is key 'Unique Code' in the CSV ?
    #if 'Unique Code' not in sdf.columns:
    #    raise ValueError(f"Cannot convert file {os.path.basename(filename)},\nQuick Check, key 'Unique Code' not found.")

    # Das Header File der Auswertung als "Template" einlesen
    xdf = pd.read_excel(config.xltemplates)
    logging.info(f"Template Excel {os.path.basename(config.xltemplates)} loaded.")

    # die lookup table - templates einlesen
    tmpl = xdf.to_dict(orient='list')
    lookup_table = {k:lookup(k, tmpl, sdf) for k in xdf}

    # jetzt für jede Spalte im Template die Daten aus Spectro übertragen.
    # Falls keine Daten vorhanden sind eine leere Spalte einfügen, damit copy & paste möglich bleibt.
    _df = pd.DataFrame([])
    # for col in xdf.columns:
    #     if col in sdf.columns:
    #         _df[col] = sdf[col]
    #     else:
    #         _df[col] = ""
    for col in xdf.columns:
        if lookup_table[col] in sdf.columns:
            _df[col] = sdf[lookup_table[col]]
        else:
            _df[col] = ""

    logging.info(f"CSV and Excel Template successfully merged.")
    
    # die Zellen in Zahlen umwandeln, wo möglich
    new_df = _df.applymap(helpers.corr)
    logging.info(f"All cells have correct type for Excel now, special characters '<?*' have been removed.")

    # jetzt Daten als Excel abspeichern und user verständigen.
    logging.info(f"Exporting to {config.outfile}.")
    new_df.to_excel(config.outfile, index=False)
    if sys.platfrom == 'win32':
        os.startfile(config.outfile)
    else:
        print(new_df)


