import os, sys
sys.path.insert(0, os.path.abspath(".."))
from Calibration import FromHextoDEC as htd



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Error \nInput a FileName.csv to FromHextoDEC.py')
        exit()
    path = sys.argv[1]
    c = htd.conversion(path)
    c.printdf()
    c.fromHtoD()  