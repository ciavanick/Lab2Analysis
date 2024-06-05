# This bash script CONVERTS txt to csv, SPACES to ',' and HEX to DEC and filter

#!/bin/bash

path=$1 #path of file
mode=$2
filename="${path%.*}"
extension="${path#*.}"
csvpath="csv/${filename}.csv"

echo "Converting txt to csv..."
sed 's/ /,/g' raw/$path > $csvpath # Converts SPACES to ','

echo "Coversion..."
python3 conversion.py $csvpath

echo "Filtering..."
python3 filtering.py $csvpath $mode
# rm $path