#!/bin/bash

# This bash script CONVERTS txt to csv, SPACES to ',' and HEX to DEC

path=$1
filename="${path%.*}"
extension="${path#*.}"
csvpath="csv/${filename}.csv"

echo "Converting txt to csv..."
sed 's/ /,/g' raw/$path > $csvpath # Converts SPACES to ','

echo "Converting Hex to Dec..."
python3 FromHextoDEC.py $csvpath