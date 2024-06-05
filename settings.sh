#!/bin/bash


makedirectory () {
    if [ ! -d "$1" ]; then
      echo "$1 does not exist."
      echo "Creating $1"
      mkdir $1
    else 
      echo "$1 does exist."
    fi

}

echo "Going in Calibration/"
cd Calibration/
CDIRECTORYRAW="raw/"
CDIRECTORYCSV="csv/"
CDIRECTORYPDF="pdf/"
CDIRECTORYRESULTS="results/"
CDIRECTORYCALRES="calres/"

makedirectory $CDIRECTORYRAW
makedirectory $CDIRECTORYCSV
makedirectory $CDIRECTORYPDF
makedirectory $CDIRECTORYRESULTS
makedirectory $CDIRECTORYCALRES
cd ..

echo "Going in Filtering/"
cd Filtering/
CDIRECTORYRAW="raw/"
CDIRECTORYCSV="csv/"
CDIRECTORYFILT="filtered/"
CDIRECTORYRESULTS="cleanandconv/"
CDIRECTORYCALRES="calres/"

makedirectory $CDIRECTORYRAW
makedirectory $CDIRECTORYCSV
makedirectory $CDIRECTORYFILT
makedirectory $CDIRECTORYRESULTS
makedirectory $CDIRECTORYCALRES
cd ..

CDIRECTORYRES="Results/"
makedirectory $CDIRECTORYRES

pathdata=$PWD"/Data/."
cd Filtering/
cp -a $pathdata raw/
cd ..

pathcaldata=$PWD"/CalData/."
pathsetup=$PWD"/setup.py"
cd Calibration/
cp -a $pathcaldata raw/

if [ -f setup.py ]; then
    echo 'setup.py exist... removing setup.py'
    rm -r setup.py
else
    echo 'setup.py does not exist'
fi
cd ..
cp $pathsetup Calibration/