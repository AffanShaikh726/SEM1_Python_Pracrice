import pandas as pd
import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
clear_terminal()

data = pd.read_csv("nba.csv",index_col="Name")  

firstRow = data.loc["Avery Bradley"]
print(firstRow)
 
print(data.head(10))

new_row = pd.DataFrame({'Team':'Boston', 'Number':3, 'Position':'PG', 'Age':25, 'Height':'6-2', 'Weight':180, 'College':'Texas', 'Salary':1000000}, index =["Geeks"])

# simply concatenate both dataframes
data = pd.concat([new_row, data])

# print(data.head(5))

data.drop(["Avery Bradley", "John Holland", "R.J. Hunter", "R.J. Hunter"], inplace = True)

print(data.head(5))

