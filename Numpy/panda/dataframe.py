import pandas as pd

lst = ["Geeks", "For", "Geeks", "is",
"portal", "for", "Geeks"]

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df,"\n")

data = {"Name":["Tom", "nick", "krish", "jack"],
"Age":[20, 21, 19, 1]}

# Create DataFrame
df1 = pd.DataFrame(data)
print(df1)