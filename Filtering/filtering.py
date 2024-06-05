# The cleaning happens line by line:
# we decide to ACCEPT only the lines that don't show the following conditions:
# 1) ALL 3 measures with 4095 (nothing detected after trigger)
# 2) ALL 3 measures with a DIFFERENT value with respect to 4095 (triple coincidence, which CANNOT be an electron)
# 3) P2 & P3 have a signal: there is Iron between them
# 4) P1 & P3 have a signal: there is iron between them
# 4) without P1

import os, sys
import pandas as pd

# function to write on ftxt in the way we want


def readfromtxt(path)->float:
    file = open(path,"r")
    value = float(file.read())
    return value


def writeonfile(p, path):
    f = open(path, "w")
    for i in p:
        f.write(str(i)+"\n")
    f.close()


# function to filter every single pmt column, removing all 4095
def single_filter(p):
    p_filtered = []
    for i in p:
        if (i != 4095):
            p_filtered.append(i)

    return p_filtered


# function to convert from ticks to time in ns
def tmp_conv(p, a, t0, path):
    for i in range(0, len(p)):
        p[i] = p[i]*a + t0
    writeonfile(p, path)


# function for the coincidence between PMT1 and PMT2
def P1andP2(df, name_p1andp2):
    P1AndP2 = []
    for index, row in df.iterrows():
        flag = row["tP1"] != 4095 and row["tP2"] != 4095 and row["tP3"] == 4095
        if (flag == True):
            m1 = readfromtxt("calres/PMT1m.txt")
            q1 = readfromtxt("calres/PMT1q.txt")
            P1AndP2.append(int(row["tP1"])*m1 + q1)
            m2 = readfromtxt("calres/PMT2m.txt")
            q2 = readfromtxt("calres/PMT2q.txt")
            P1AndP2.append(int(row["tP2"])*m2 + q2)
    outpath =  "cleanandconv/" + name_p1andp2 + ".txt"
    writeonfile(P1AndP2, outpath)

def P1P2P3All(path, P1, P2, P3):
    P = P1 + P2 + P3
    writeonfile(P, path)

# function to filter the raw data
def filter(path , out , name_pmt1 , name_pmt2 , name_pmt3 , name_pmt1andpmt2, cleaningmode : bool):
    df = pd.read_csv(path)
    P1 = []
    P2 = []
    P3 = []
    for index, row in df.iterrows():
        if cleaningmode == True:
            flag1 = row["tstopP1"] == 4095 and row["tstopP2"] == 4095 and row["tstopP3"] == 4095
            flag2 = row["tstopP1"] != 4095 and row["tstopP2"] != 4095 and row["tstopP3"] != 4095
            flag3 = row["tstopP1"] == 4095 and row["tstopP2"] != 4095 and row["tstopP3"] != 4095
            flag4 = row["tstopP1"] != 4095 and row["tstopP2"] == 4095 and row["tstopP3"] != 4095
            flag5 =  row["tstopP1"] != 4095 and row["tstopP2"] == 4095 and row["tstopP3"] == 4095
            flag = flag1 or flag2 or flag3 or flag4
        else :
            flag1 = row["tstopP1"] == 4095 and row["tstopP2"] == 4095 and row["tstopP3"] == 4095
            flag = flag1
        if (flag == False):
            P1.append(int(row["tstopP1"]))
            P2.append(int(row["tstopP2"]))
            P3.append(int(row["tstopP3"]))
    dic = {"tP1": P1, "tP2": P2, "tP3": P3}
    df_filtered = pd.DataFrame(dic)
    outpath = "filtered/" + out + ".csv"
    df_filtered.to_csv(outpath, header=True, index=False)
    
    #saving on csv data, not converted
    #P1
    P1 = single_filter(P1)
    dicP1 = {"P1": P1}
    df_P1 = pd.DataFrame(dicP1)
    outpath = "filtered/" + name_pmt1 + ".csv"
    df_P1.to_csv(outpath, header=True, index=False)
    #P2
    P2 = single_filter(P2)
    dicP2 = {"P2": P2}
    df_P2 = pd.DataFrame(dicP2)
    outpath = "filtered/" + name_pmt2 + ".csv"
    df_P2.to_csv(outpath, header=True, index=False)
    #P3
    P3 = single_filter(P3)
    dicP3 = {"P3": P3}
    df_P3 = pd.DataFrame(dicP3)
    outpath = "filtered/" + name_pmt3 + ".csv"
    df_P3.to_csv(outpath, header=True, index=False)
    
    #Saving on txt file, converted value
    #P1
    m = readfromtxt("calres/PMT1m.txt")
    q = readfromtxt("calres/PMT1q.txt")
    outpath = "cleanandconv/" + name_pmt1 + ".txt"
    print("P1: m = " + str(m)+", q = "+str(q))
    tmp_conv(P1, m, q, outpath)
    #P2
    m = readfromtxt("calres/PMT2m.txt")
    q = readfromtxt("calres/PMT2q.txt")
    outpath = "cleanandconv/" + name_pmt2 + ".txt"
    print("P2: m = " + str(m)+", q = "+str(q))
    tmp_conv(P2, m, q, outpath)
    #P3
    m = readfromtxt("calres/PMT3m.txt")
    q = readfromtxt("calres/PMT3q.txt")
    outpath = "cleanandconv/" + name_pmt3 + ".txt"
    print("P3: m = " + str(m)+", q = "+str(q))
    tmp_conv(P3, m, q, outpath)
    P1andP2(df_filtered, name_pmt1andpmt2)
    outhpath =  "cleanandconv/" + name_pmt1 + name_pmt2 + name_pmt3 + "all.txt"
    P1P2P3All(outhpath, P1, P2, P3)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Error \nInput a FileName.csv')
        exit()
    path = sys.argv[1]
    mode = sys.argv[2]
    if (mode == "i"):
        P1 = "P1"
        P2 = "P2"
        P3 = "P3"
        P1andP2_var = "P1andP2"
        out = "filt"
        cleanmode = True
    elif (mode == "a"):
        P1 = "P1wir"
        P2 = "P2wir"
        P3 = "P3wir"
        P1andP2_var = "P1andP2wir"
        out = "filtwir"
        cleanmode = False
    else:
        print("We have a problem")
        exit() 
    filter(path, out, P1, P2, P3, P1andP2_var, cleanmode)
