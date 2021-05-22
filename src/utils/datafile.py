"""
this class is for handling all car output files so i can graph them 
"""

import csv
import datetime
import datetime
from os import mkdir, path, write
from sqlite3 import Date
from uuid import uuid4
import numpy as np
import pandas as pd
import pathlib

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


def dumpGasData(name, datafine, datagen):
    schema = avro.schema.parse(open("/home/nicholas/Desktop/Car dev/schems/stearing.avsc", "rb").read())


    writer = DataFileWriter(open(str("/home/nicholas/Desktop/Car dev/collectedData")+str("stearing")+".avro", "w+b"), DatumWriter(), schema)
    writer.append({"name": name, "finerPos": datafine,"generalPos": datagen})
    writer.close()
  
    

def readavro():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/Car dev/collectedData")+str("stearing")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
    reader.close()

def main():
  
            
    i = 0
    z= 0
    while True:
      
        
        print("testing data")
        dumpGasData(name="gas"+str(i),datafine=i,datagen=i)
        i +=1 
        if i >= 100:
            print("done with file")
            readavro()
            break
            
    

main()