"""
this class is for handling all car output files so i can graph them 
"""

import csv
from datetime import date, datetime
from sqlite3 import Date
from uuid import uuid4
import numpy as np
import pandas as pd


data = pd.DataFrame(columns=('Source', 'General_Pos', 'Finer_Pos'))
file = None

'''
This is for creating iterating Data from car into A format for exel / Graphing Easly
''' 
def createDataFile(source,geneal,finer,i):
    predata = {'Source':str(source),'General_Pos': float(geneal), 'Finer_Pos': float(finer)}
    data.at[i,:] = predata


'''
Writes Data to The csv File
'''
def writeFile(filename):
    data.to_csv('collectedData/'+str(filename)+" "+datetime.now().strftime(
        "%Y_%m_%d-%I_%M_%S_%s")+'.csv', index=False)
