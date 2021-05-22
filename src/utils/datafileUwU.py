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

gasschema = avro.schema.parse(open("src/utils/gas.avsc", "rb").read())
gaswriter = DataFileWriter(open(str("collectedData/")+str("gas")+".avro", "w+b"), DatumWriter(), gasschema)

breakschema = avro.schema.parse(open("src/utils/gas.avsc", "rb").read())
breakwriter = DataFileWriter(open(str("collectedData/")+str("break")+".avro", "w+b"), DatumWriter(), breakschema)


def dumpGasData(name, datafine, datagen):
   gaswriter.append({"name": name, "finerPos": datafine,"generalPos": datagen})
  
def dumpbreakData(name, data):
   breakwriter.append({"name": name, "Pos": data})
  
def readavrogas():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/")+str("gas")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
    reader.close()

def readavrobreak():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/")+str("break")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
    reader.close()


def gasdata(i, dataf,datag):
  
    print("testing data")

    
   
    dumpGasData(name="gas"+str(i),datafine=dataf,datagen=datag)
    
    i +=1 
    
    
    print("i: "+str(i))
    if i >= 2000:
        gaswriter.close()
        
        print("done with file reading gas file\n")
        readavrogas()



        
         
def breakdata(data,i):
  
    print("testing data")

    
   
    dumpbreakData(name="break"+str(i),data=data)
    
    i +=1 
    
    
    print("i: "+str(i))
    if i >= 2000:
        breakwriter.close()
        
        print("done with file reading break file\n")
        readavrobreak()()


    
    
