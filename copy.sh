#!/bin/bash

echo "copying Dat from Car collection output to graphing pholder"
mkdir /home/nicholas/Desktop/cardev/Graphing/output/$((i+1))
mv /home/nicholas/Desktop/cardev/Graphing/output/*.avro  /home/nicholas/Desktop/cardev/Graphing/output/$((i+1))
cp -r /home/nicholas/Desktop/cardev/output/*.avro /home/nicholas/Desktop/cardev/Graphing/output/

echo "done copying files"