# script to convert from hexadecimal to decimal

import pandas as pd
import sys

# class to handle the conversion from hexadecimal to decimal


class conversion:
    def __init__(self, path):
        df = pd.read_csv(path, dtype=str, header=None)
        self.df = df
        self.flag = int(0)
        self.path = path

    # private method to transform from hexadecimal to decimal
    def __HexToDec(self, col):
        new_column = []
        if self.flag < 3:
            self.flag += 1
            for element in col:
                element = str(element)
                element_to_dec = int(element, 16)
                new_column.append(element_to_dec)
            col = pd.Series(data=new_column)
            return col
        else:
            print('Error \nAlready converted')
            exit()

    def fromHtoD(self):
        for i in range(3, 6):
            col = self.df.iloc[:,i]  # Series of the i_th Hex column
            col = self.__HexToDec(col)
            del self.df[i]
            self.df.insert(i, i, col)
        if (self.df.iloc[0, 0] == '_'):
            del self.df[0]  # delete first column _
            self.df.columns = ['Event', 'tTrigger',
                               'tstopP1', 'tstopP2', 'tstopP3']
            self.df.to_csv(self.path, header=True, index=False)

    def printdf(self):
        print(self.df)

    def get(self):
        return self.df


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Error \nInput a FileName.csv to FromHextoDEC.py')
        exit()
    path = sys.argv[1]
    c = conversion(path)
    c.printdf()
    c.fromHtoD()
    c.printdf()
