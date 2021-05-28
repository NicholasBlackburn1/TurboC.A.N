
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
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random

breakschema = avro.schema.parse(
    open("/home/nicholas/Desktop/testarvo/shem/Test.avsc", "rb").read())
testwriter = DataFileWriter(
    open(str("/home/nicholas/Desktop/testarvo/output")+str("Test")+".avro", "wb"), DatumWriter(), breakschema)


# Reads Break Data
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
    print("pos:"+" " + str(pos)+"\n")
    return index, pos


# Reads Gas Data from File
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
    print("general:"+" " + str(generalpos)+"\n")
    print("finerPos:"+" " + str(finerpos))
    return index, generalpos, finerpos


# Reads the Stearing Data
def ReadStearingData():

    print("Reading  file..")

    reader = DataFileReader(
        open(str("/home/nicholas/Desktop/cardev/Graphing/output/")+str("stearing")+".avro", "rb"), DatumReader())
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
    print("general:"+" " + str(generalpos)+"\n")
    print("finerPos:"+" " + str(finerpos))
    return index, generalpos, finerpos



# Reads the Stearing Data
def ReadRpmData():

    print("Reading  file..")

    reader = DataFileReader(
        open(str("/home/nicholas/Desktop/cardev/Graphing/output/")+str("rpm")+".avro", "rb"), DatumReader())
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
        generalpos.append(int(gas['rpm']*256/4))
        finerpos.append(int(gas['peddelpos']*256/4))
    reader.close()
    print("Index Number:"+str(index)+"\n")
    print("general:"+" " + str(generalpos)+"\n")
    print("finerPos:"+" " + str(finerpos))
    return index, generalpos, finerpos


"""
This graphs and reads the Brak Data From file 
"""


def graphBreak():

    stindex, Pos = ReadbreakData()

    fig, ax = plt.subplots()

    plt.plot(stindex, Pos, color='red', label="Breaking General Data")

    ax.set_ylabel("Peddel Pos")
    ax.set_xlabel("Tics Recording time ")

    ax.legend()
    plt.title("Break Peddel Data")
    plt.show()


"""
This graphs and reads the Gas Data From file 
"""


def graphGas():

    stindex, generlpos, finerpos = ReadgasData()

    fig, ax = plt.subplots()

    plt.plot(stindex, finerpos, color='pink', label="Gas Finer Data")
    plt.plot(stindex, generlpos, color='red', label="Gas General Data")

    ax.set_ylabel("Peddle pos")
    ax.set_xlabel("Tics Recording time ")

    ax.legend()
    plt.title("Gas Peddel Data")
    plt.show()


"""
This graphs and reads the Stearing Data From file 
"""


def graphStearing():

    stindex, generlpos, finerpos = ReadStearingData()

    fig, ax = plt.subplots()

    plt.plot(stindex, finerpos, color='pink', label="Stearing Finer Data")
    plt.plot(stindex, generlpos, color='red', label="Stearing General Data")

    ax.set_ylabel("Wheel Pos")
    ax.set_xlabel("Tics Recording time ")
    
    ax.legend()
    plt.title("Steering Peddel Data")
    plt.yticks(1000)
    plt.show()




def graphrpm():

    stindex, rpm, ped = ReadRpmData()
    
    fig, ax = plt.subplots()

  
    plt.plot(stindex, rpm, color='pink', label="Raw Unprossed rpm")
    plt.plot(stindex, ped, color='red', label="Main Rpm Data")
    ax.set_ylabel("RPM")
    ax.set_xlabel("Tics Recording time ")
    
    ax.legend()
    plt.title("RPM  Data i think")
    plt.show()



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Turbo C.A.N Graphs'
        self.width = 1920
        self.height = 1080
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        gas = PlotGas(self, width=5, height=5)
        brake = PlotBreak(self,width=5, height=5)
        brake.move(0,500)
        gas.move(0,0)


        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)
        button.resize(140,100)

        self.show()


class PlotBreak(FigureCanvas):

    def __init__(self, parent=None, width=10, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('1')
        self.draw()

class PlotGas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        stindex, generlpos, finerpos = ReadgasData()

        ax = self.figure.add_subplot()

        ax.plot(stindex, finerpos, color='pink', label="Gas Finer Data")
        ax.plot(stindex, generlpos, color='red', label="Gas General Data")

        ax.set_ylabel("Peddle pos")
        ax.set_xlabel("Tics Recording time ")

        ax.legend()
        ax.set_title('Gas Peddle Data')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())