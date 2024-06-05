def readfromtxt(path)->float:
    file = open(path,"r")
    value = float(file.read())
    return value
    
v = readfromtxt("calres/PMT1q.txt")
print(v)