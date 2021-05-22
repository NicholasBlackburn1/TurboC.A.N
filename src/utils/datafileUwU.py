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

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from time import sleep

gasschema = avro.schema.parse(open("/home/nicholas/Desktop/Car dev/schems/stearing.avsc", "rb").read())
gaswriter = DataFileWriter(open(str("/home/nicholas/Desktop/Car dev/collectedData")+str("stearing")+".avro", "w+b"), DatumWriter(), gasschema)

def dumpGasData(name, datafine, datagen):
   gaswriter.append({"name": name, "finerPos": datafine,"generalPos": datagen})
   
  
    

def readavro():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/Car dev/collectedData")+str("stearing")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
    reader.close()

def data(i, dataf,datag):
  
    print("testing data")

    
   
    dumpGasData(name="gas"+str(i),datafine=dataf,datagen=datag)
    i +=1 
    
    
    print("i: "+str(i))
    if i >= 2000:
        gaswriter.close()
        print("done with file")
        readavro()
         

    
    
