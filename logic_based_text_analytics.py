# -*- coding: utf-8 -*-
"""
Created on September 20 2018
"""
'''
Author: Vamsee Achanta
Date Updated: 2018-09-20
Objective: To generate clean data from mixed text
Run instructions with:
 Default yml file : python APISTD2RD.py
 Update default yml with parameters in 12.yml: python APISTD2RD.py 12.yml
 Outputs: JSON file and ASCII DataFrame with outputs

 UPDATES:
 Input YML: Relocate Spacing to PlotSettings
 Rename Summary "Hangoff" to "HangOffToSag"

References:
 https://docs.python.org/3/library/re.html
 https://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string

'''
import logging
import os

import pandas as pd

from common.application_configuration import application_configuration
from common.data import FromString, ReadData
from common.set_logging import set_logging

# Data preparation
basename = os.path.basename(__file__).split('.')[0]
cfg = application_configuration(basename)

# Overwrite flag
if cfg['default']['config']['overwrite']['output'] == True:
    cfg['Analysis']['file_name'] = cfg['Analysis']['file_name_for_overwrite']

# Set logging
set_logging(cfg)
logging.info(cfg)

read_data = ReadData()
from_string = FromString()

df_array = []
for file_index in range(0, len(cfg['files']['from_xlsx'])):
    df_array.append(read_data.from_xlsx(cfg, file_index))

result_text_df = pd.DataFrame(columns = cfg['Analysis']['result_df_columns'])
result_numerals_df = pd.DataFrame(columns = cfg['Analysis']['result_df_columns'])

df_index = 0
for df_row in range(0, len(df_array[0])):
# for df_row in range(0, 20):
    row_text_array = []
    row_numeral_array = []
    string_to_process = df_array[df_index].loc[df_row, cfg['files']['from_xlsx'][df_index]['column']]
    if string_to_process is not float('nan') and string_to_process is not float:
        # print(string_to_process)
        row_text_array.append(string_to_process)
        row_numeral_array.append(string_to_process)
        # for regex_index in range(0, 1):
        for regex_index in range(0, len(cfg['regular_expressions'])):
            ref_text = cfg['regular_expressions'][regex_index]['regex_find_first']
            regex_found = from_string.using_regex(ref_text, string_to_process)
            row_text_array.append(regex_found)

            string_array = cfg['regular_expressions'][regex_index]['remove']
            regex_numeral = from_string.remove_strings(regex_found, string_array)

            if regex_numeral is not None:
                regex_numeral=regex_numeral.replace('-', ' ')
                regex_numeral=regex_numeral.replace('½', '.5')
                regex_numeral=regex_numeral.replace('¾', '.75')
                regex_numeral=regex_numeral.replace(':', '/')

            if regex_index == 0 or regex_index == 1 :
                try:
                    row_numeral_array.append(from_string.convert_fraction_to_float(regex_numeral))
                except:
                    try:
                        row_numeral_array.append(float(regex_numeral))
                    except:
                        row_numeral_array.append(regex_numeral)
            else:
                try:
                    row_numeral_array.append(float(regex_numeral))
                except:
                    row_numeral_array.append(regex_numeral)

            if regex_index == 0 and isinstance(regex_numeral, float):
                if regex_numeral >=200:
                    regex_numeral = regex_numeral/100
        # print(row_text_array)
        # print(row_numeral_array[0])
        # print(row_numeral_array[1:])
        result_text_df.loc[len(result_text_df)] = row_text_array
        result_numerals_df.loc[len(result_numerals_df)] = row_numeral_array
        # print(df_row)

result_text_df.to_csv(cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'] + 'text.csv')
result_numerals_df.to_csv(cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'] + 'numerals.csv')
print(result_numerals_df.count(numeric_only=False))