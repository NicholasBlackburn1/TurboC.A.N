""" 
this file is for graphing data thats been collected
"""


from asyncore import read
from cProfile import label

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import src.utils.datafileUwU as uwu
from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter
import logging as logger


def readavrogas():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/gone/")+str("gas")+".avro", "rb"), DatumReader())
    index = []
    finedata = []
    generaldata = []

    for gas in reader:
        logger.warn("UWU gas data")
        logger.info(gas)
        index.append(int(gas['name']))
        finedata.append(int(gas['finerPos']))
        generaldata.append(int(gas['generalPos']))

    reader.close()
    return index,finedata,generaldata
    

        
def readavrobreak():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/gone/")+str("break")+".avro", "rb"), DatumReader())
    index = []
    pos = []
    for gas in reader:
        logger.warn("UWU break data")
        logger.info(gas)
        index.append(int(gas['name']))
        pos.append(int(gas['Pos']))
        

    reader.close()
    return index,pos

def readavroStearing():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/gone/")+str("stearing")+".avro", "rb"), DatumReader())
    index = []
    finedata = []
    generaldata = []

    for gas in reader:
        logger.warn("UWU Stearing data")
        logger.info(gas)
        index.append(int(gas['name']))
        finedata.append(int(gas['finerPos']))
        generaldata.append(int(gas['generalPos']))

    reader.close()
    return index,finedata,generaldata
    

def graphStearing():

    stindex, stfiner,stgeneraldata = readavroStearing()

  
    fig, ax = plt.subplots()

 
    plt.plot(stindex, stfiner,color='pink',label="Stearing Finer Data")
    plt.plot(stindex, stgeneraldata,color='red',label="Stearing General Data")
    
    ax.set_ylabel("indexer counter")
    ax.set_xlabel("Tics Recording time")
    ax.legend()
    plt.title("Stearing Wheel Data")
    plt.show()



def graphGas():

    stindex, stfiner,stgeneraldata = readavrogas()

  
    fig, ax = plt.subplots()

 
    plt.plot(stindex, stgeneraldata,color='pink',label="Stearing Finer Data")
    plt.plot(stindex, stfiner,color='red',label="Stearing General Data")
    
    ax.set_ylabel("indexer counter")
    ax.set_xlabel("Tics Recording time")
    ax.legend()
    plt.title("Gas Wheel Data")
    plt.show()

def breakGraph():


    index,Pos = ()

    x = index
    y = Pos
    fig, ax = plt.subplots()

    # Using set_dashes() to modify dashing of an existing line
    line1, = ax.plot(x, y, label='Using set_dashes()')

    # Using plot(..., dashes=...) to set the dashing when creating a line
    line2, = ax.plot(x, y , label='Using the dashes parameter')

    plt.ylabel("indexer counter")
    plt.xlabel("Tics Recording time")
    plt.title("Break Wheel Data")
    plt.show()






graphGas()