import pandas as pd
import numpy as np

df = pd.read_csv("HackUTD-2023-HomeBuyerInfo.csv")
df["Approval"] = 1

print(df.head())
disapprovals = 0

for row in range(0, len(df.index)):
    LTV = float(df.iloc[row, 7] / df.iloc[row, 5])
    DTI = float((df.iloc[row, 8] + df.iloc[row, 3] + df.iloc[row, 2]) / df.iloc[row, 1])
    FEDTI = float(df.iloc[row, 8] / df.iloc[row, 1])

    # FIRST CHECK
    if (df.iloc[row, 9]) < 640 or (LTV > 0.95) or (DTI > 0.43):
        df.iloc[row, 10] = 0
        # disapprovals = disapprovals + 1
        continue

    # SECOND CHECK

    if (FEDTI <= 0.28) and (DTI <= 0.36):
        df.iloc[row, 10] = 1

    if ((DTI >= 0.36) and (DTI <= 0.43)) and (FEDTI <= 0.28):
        df.iloc[row, 10] = 1

    if (LTV >= 0.80) and (LTV <= 0.95):
        df.iloc[row, 10] = 1

    if FEDTI > 0.28:
        df.iloc[row, 10] = 0
        # disapprovals = disapprovals + 1


print(df.head())
LTV = float(df.iloc[0, 7] / df.iloc[0, 5])
DTI = float((df.iloc[0, 8] + df.iloc[0, 3] + df.iloc[0, 2]) / df.iloc[0, 1])
FEDTI = float(df.iloc[0, 8] / df.iloc[0, 1])

# compression_opts = dict(method='zip',
           #            archive_name='out2.csv')

#df.to_csv('out.zip', index=False,
         # compression=compression_opts)

print("LTV: ", LTV, " ", "DTI: ", DTI, " ", "FEDTI: ", FEDTI)
# print(disapprovals)