# This bash script compute the calibration

#!/bin/bash

echo "Computing mean and std..."
python3 Calib.py

echo "Calibration..."
root -l -q cal.cpp
# rm $path