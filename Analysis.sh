# This bash script Crun the analysis

#!/bin/bash

echo "PMT1..."
root -l -q 'Analysis.cpp("Filtering/cleanandconv/P1.txt","PMT1")'

echo "PMT2..."
root -l -q 'Analysis.cpp("Filtering/cleanandconv/P2.txt","PMT2")'

echo "PMT3..."
root -l -q 'Analysis.cpp("Filtering/cleanandconv/P3.txt","PMT3")'

echo "PMT1 && PMT2..."
root -l -q 'Analysis.cpp("Filtering/cleanandconv/P1AndP2.txt","PMT1_and_PMT2")'

echo "All..."
root -l -q 'Analysis.cpp("Filtering/cleanandconv/P1P2P3all.txt","all")'
