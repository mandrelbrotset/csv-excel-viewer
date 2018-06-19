import pandas as pd

x = pd.read_csv("test.csv")
print(x.loc[4][2])
