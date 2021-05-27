""" 
this file is for graphing data thats been collected
"""


from asyncore import read
from cProfile import label
import os

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import src.utils.datafileUwU as uwu
from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter
import logging as logger




Location = str("Tyquando_2021-05-26/")
StorePath = "/home/nicholas/Desktop/cardev/collectedData/"


def readavrogas():
    if(os.path.isfile((StorePath+"Test"+".avro"))):
        reader = DataFileReader(open(StorePath+"gas"+".avro", "rb"), DatumReader())
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
    else:
        return 0,0,0
        

        
def readavrobreak():
    if(os.path.isfile((StorePath+"break"+".avro"))):
        reader = DataFileReader(open(StorePath+"break"+".avro", "rb"), DatumReader())
        index = []
        pos = []
        for gas in reader:
            logger.warn("UWU break data")
            logger.info(gas)
            index.append(int(gas['name']))
            pos.append(int(gas['Pos']))
            

        reader.close()
        return index,pos
    else:
        return 0,0

def readavroStearing():
    if(os.path.isfile((StorePath+"stearing"+".avro"))):
        reader = DataFileReader(open(StorePath+"stearing"+".avro", "rb"), DatumReader())
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
    else: 
        return 0,0,0
    

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

 
    plt.plot(stindex, stgeneraldata,color='pink',label="Gas Peddle Finer Data")
    plt.plot(stindex, stfiner,color='red',label="Gas Peddle General Data")
    
    ax.set_ylabel("Peddel Pos")
    ax.set_xlabel("Tics Recording time ")

    ax.legend()
    plt.title("Gas Peddel Data")
    plt.show()

def graphBreak():

    stindex, Pos = readavrobreak()

  
    fig, ax = plt.subplots()

 
    plt.plot(stindex, Pos,color='red',label="Breaking General Data")
    
    ax.set_ylabel("Peddel Pos")
    ax.set_xlabel("Tics Recording time ")

    ax.legend()
    plt.title("Break Peddel Data")
    plt.show()







print(readavrobreak())