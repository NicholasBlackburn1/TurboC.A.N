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

gasschema = avro.schema.parse(open("/home/nicholas/Desktop/cardev/src/utils/gas.avsc", "rb").read())
gaswriter = DataFileWriter(open(str("collectedData/")+str("gas")+".avro", "w+b"), DatumWriter(), gasschema)

breakschema = avro.schema.parse(open("/home/nicholas/Desktop/cardev/src/utils/break.avsc", "rb").read())
breakwriter = DataFileWriter(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("break")+".avro", "w+b"), DatumWriter(), breakschema)

Stearingschema = avro.schema.parse(open("/home/nicholas/Desktop/cardev/src/utils/stearing.avsc", "rb").read())
Stearingwriter = DataFileWriter(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("stearing")+".avro", "w+b"), DatumWriter(), Stearingschema)


def readavrogas():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("gas")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
    reader.close()

def readavrobreak():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("break")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
    reader.close()

def readavroStearing():
    reader = DataFileReader(open(str("/home/nicholas/Desktop/cardev/collectedData/")+str("stearing")+".avro", "rb"), DatumReader())
    for gas in reader:
        print (gas)
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

def gasdata(i, dataf,datag):
  
    print("gas data")

    
   
    dumpGasData(name="gas"+str(i),datafine=dataf,datagen=datag)
    
    i +=1 
    
    
    print("i: "+str(i))
    if i <= 2000:
        #gaswriter.close()
        
        #print("done with file reading gas file\n")
        #readavrogas()
        pass



        
         
def breakdata(data,i):
  
    print(" brake data")

    
   
    dumpbreakData(name="break"+str(i),data=data)
    
    i +=1 
    
    
    print("i: "+str(i))
    if i <= 2000:
        breakwriter.close()
        
        print("done with file reading break file\n")
        readavrobreak()()

       
def stearingdata(dataf,datag,i):
  
    print("stearing data")

    
    print({"name": str(), "finerPos": dataf,"generalPos": datag})
   # dumpStearingData(name=str("stearing"+str(i)),datafine=dataf, datagen= dataf)
    
  
    
    
    print("i: "+str(i))
    if i <= 2000:
        #Stearingwriter.close()
        
        #print("done with file reading break file\n")
        #readavroStearing()

        pass
    
    

    
    
