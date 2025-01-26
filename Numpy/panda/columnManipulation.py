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

data = {"Name":["Tom", "nick", "krish", "jack"],
"age":[20, 21, 19, 1],
"Address":["USA", "Canada", "UK", "Africa"],
"Qualification":["Msc", "MA", "MCA", "Phd"]
}

df = pd.DataFrame(data, index = ["1", "2", "3", "4"])
print(df[["Name", "Qualification"]],"\n")

height = [5.1, 6.2, 5.1, 5.2]

df["Height"] = height

print(df,"\n")

df.drop("Qualification", axis = 1, inplace = True)

print(df,"\n")