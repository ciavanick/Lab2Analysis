#file to compute the mean and std of each PMT with all the different delays

import pandas as pd
from setup import paths, y, ye

def calib_all(df):
    column_mean = []
    column_std = []
    #computing the mean and std for each PMT
    for i in range(2, 5):
        col = df.iloc[:, i]  # Series of the i_th column
        # col = multiplyby4(col)
        print('mean:', col.mean(), 'std:', col.std())
        column_mean.append(col.mean())
        column_std.append(col.std())
    
    return column_mean, column_std


#function to write on a file
def writeonfile(x,xe,y,ye, name)->None:
    f = open("results/"+name+".txt", "w")
    for i in range(0,len(x)):
        f.write(str(x[i])+","+str(y[i])+","+str(xe[i])+","+str(ye[i])+"\n")
    f.close()

if __name__ == "__main__":
    xPMT1 = []
    xePMT1 = []
    xPMT2 = []
    xePMT2 = []
    xPMT3 = []
    xePMT3 = []
    #for each file we extract mean and std of each pmts
    for i in paths:
        df = pd.read_csv("csv/"+i)  # Produces a DataFrame type
        mean, std = calib_all(df)
        xPMT1.append(mean[0])
        xePMT1.append(std[0])
        xPMT2.append(mean[1])
        xePMT2.append(std[1])
        xPMT3.append(mean[2])
        xePMT3.append(std[2])
    writeonfile(xPMT1,xePMT1,y,ye,"PMT1")
    writeonfile(xPMT2,xePMT2,y,ye,"PMT2")
    writeonfile(xPMT3,xePMT3,y,ye,"PMT3")