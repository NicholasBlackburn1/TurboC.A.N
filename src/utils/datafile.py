"""
this class is for handling all car output files so i can graph them 
"""

import csv
from uuid import uuid4
import numpy as np
import pandas as pd


data = pd.DataFrame(columns=('Source', 'General_Pos', 'Finer_Pos'))

'''
This is for creating iterating Data from car into A format for exel / Graphing Easly
''' 
def createDataFile(source,geneal,finer,i):
    predata = {'Source':str(source),'General_Pos': float(geneal), 'Finer_Pos': float(finer)}
    data.at[i,:,:,:] = predata
    data.to_csv('collectedData/'+'my_new_file.csv', index=False)
