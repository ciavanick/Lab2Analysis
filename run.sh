#!/bin/bash
bash settings.sh
cd Calibration/
dir="raw/"
for i in raw/*.txt
do 
    path=${i#"$dir"}
    bash conversion.sh $path
done

bash calib.sh

cd ..
cd Filtering/
echo "Setting calibration values on filtering code..."
bash settings.sh
echo "Filtering..."
text1=$1
bash fromtxttocsv.sh $text1 i

cd ..
bash Analysis.sh