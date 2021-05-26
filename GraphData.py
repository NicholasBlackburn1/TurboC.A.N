""" 
this file is for graphing data thats been collected
"""


from asyncore import read
import numpy as np
import matplotlib.pyplot as plt
import src.utils.datafileUwU as uwu
from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter
import logging as logger


def readavrogas():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("gas")+".avro", "rb"), DatumReader())
    for gas in reader:
        logger.warn("UWU break data")
        logger.info(gas)
        print(gas)
        return gas
    reader.close()

        
def readavrobreak():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("break")+".avro", "rb"), DatumReader())
    for gas in reader:
        logger.warn("UWU break data")
        logger.info(gas)
        print (gas)
    reader.close()

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
    


index, finer,generaldata = readavroStearing()

x = index
y = generaldata
fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y, label='Using set_dashes()')

# Using plot(..., dashes=...) to set the dashing when creating a line
line2, = ax.plot(x, y , label='Using the dashes parameter')

plt.ylabel("indexer counter")
plt.xlabel("Tics Recording time")
plt.title("Stearing Wheel Data")
plt.show()