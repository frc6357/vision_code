#!/bin/bash

g++ -ggdb Main.cpp ImageCap.cpp ImageManipulation.cpp ImageProcessing.cpp -o Main `pkg-config --cflags --libs opencv` -std=c++11
./Main