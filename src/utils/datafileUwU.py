"""
this class is for handling all car output files so i can graph them 
"""

import csv
import datetime
import datetime
from sqlite3 import Date
from uuid import uuid4
import numpy as np
import pandas as pd
import pathlib
import logging as logger
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from time import sleep

StorePath = "/home/nicholas/Desktop/cardev/collectedData/Tyquando_2021-05-26/"

gasschema = avro.schema.parse(open("/home/nicholas/Desktop/cardev/src/utils/gas.avsc", "rb").read())
gaswriter = DataFileWriter(open(str(StorePath)+str("gas")+".avro", "w+b"), DatumWriter(), gasschema)

breakschema = avro.schema.parse(open("/home/nicholas/Desktop/cardev/src/utils/break.avsc", "rb").read())
breakwriter = DataFileWriter(open(str(StorePath)+str("break")+".avro", "w+b"), DatumWriter(), breakschema)

Stearingschema = avro.schema.parse(open("/home/nicholas/Desktop/cardev/src/utils/stearing.avsc", "rb").read())
Stearingwriter = DataFileWriter(open(str(StorePath)+str("stearing")+".avro", "w+b"), DatumWriter(), Stearingschema)


def readavrogas():
    reader = DataFileReader(open(str(StorePath)+str("gas")+".avro", "rb"), DatumReader())
    for gas in reader:
        logger.warn("UWU gas data")
        logger.info(gas)
        print (gas)
    reader.close()

def readavrobreak():
    reader = DataFileReader(open(str(StorePath)+str("break")+".avro", "rb"), DatumReader())
    for gas in reader:
        logger.warn("UWU break data")
        logger.info(gas)
        print (gas)
    reader.close()

def readavroStearing():
    reader = DataFileReader(open(str(StorePath)+str("stearing")+".avro", "rb"), DatumReader())
    for gas in reader:
        logger.warn("UWU Stearing data")
        logger.info(gas)
        print (gas)
        return gas
    reader.close()

def dumpGasData(name, datafine, datagen):
   gaswriter.append({"name": str(name), "finerPos": datafine,"generalPos": datagen})
   #print({"name": str(name), "finerPos": datafine,"generalPos": datagen})

def dumpbreakData(name, data):
   breakwriter.append({"name": str(name), "Pos": data})
   #print({"name": str(name), "Pos": data})


  
def dumpStearingData(name, datafine,datagen):
   Stearingwriter.append({"name": str(name), "finerPos": datafine,"generalPos": datagen})
   #print({"name": str(name), "finerPos": datafine,"generalPos": datagen})

    
    
