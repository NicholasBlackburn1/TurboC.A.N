
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
import matplotlib.pyplot as plt

breakschema = avro.schema.parse(
    open("/home/nicholas/Desktop/testarvo/shem/Test.avsc", "rb").read())
testwriter = DataFileWriter(
    open(str("/home/nicholas/Desktop/testarvo/output")+str("Test")+".avro", "wb"), DatumWriter(), breakschema)

      

def ReadbreakData():

    print("Reading  file..")

    reader = DataFileReader(
    open(str("/home/nicholas/Desktop/cardev/Graphing/output/")+str("break")+".avro", "rb"), DatumReader())
    print("Block count:"+str(reader.block_count)+"\n")
    print("IS eof:"+str(reader.is_EOF())+"\n")
    print("read header:"+" "+str(reader._read_header())+"\n")
    print("File length:"+" "+str(reader.file_length)+"\n")
    index = []
    pos = []
    logger.warn("reading file")
    for gas in reader:
        index.append(int(gas['name']))
        pos.append(int(gas['Pos']))
            
    reader.close()
    print("Index Number:"+str(index)+"\n")
    print("pos:"+" "+ str(pos)+"\n")
    return index,pos



def ReadgasData():

    print("Reading  file..")

    reader = DataFileReader(
    open(str("/home/nicholas/Desktop/cardev/Graphing/output/")+str("gas")+".avro", "rb"), DatumReader())
    print("Block count:"+str(reader.block_count)+"\n")
    print("IS eof:"+str(reader.is_EOF())+"\n")
    print("read header:"+" "+str(reader._read_header())+"\n")
    print("File length:"+" "+str(reader.file_length)+"\n")
    index = []
    generalpos = []
    finerpos = []
    logger.warn("reading file")
    for gas in reader:
        index.append(int(gas['name']))
        generalpos.append(int(gas['generalPos']))
        finerpos.append(int(gas['finerPos']))   
    reader.close()
    print("Index Number:"+str(index)+"\n")
    print("general:"+" "+ str(generalpos)+"\n")
    print("finerPos:"+" "+ str(finerpos))
    return index,generalpos,finerpos


def graphBreak():

    stindex, Pos = ReadbreakData()

  
    fig, ax = plt.subplots()

 
    plt.plot(stindex, Pos,color='red',label="Breaking General Data")
    
    ax.set_ylabel("Peddel Pos")
    ax.set_xlabel("Tics Recording time ")

    ax.legend()
    plt.title("Break Peddel Data")
    plt.show()



def graphGas():

    stindex, generlpos,finerpos = ReadgasData()

  
    fig, ax = plt.subplots()

 
    plt.plot(stindex, generlpos,color='red',label="Gas General Data")
    plt.plot(stindex, finerpos,color='pink',label="Gas Finer Data")
    
    ax.set_ylabel("Peddel Pos")
    ax.set_xlabel("Tics Recording time ")

    ax.legend()
    plt.title("Break Peddel Data")
    plt.show()



graphGas()