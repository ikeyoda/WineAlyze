import pandas as pd
df = pd.read_csv("WineImportFINAL.csv")
dfNew = pd.DataFrame(columns=['CountryName', 'Year', 'Population'])
dfColumnCount = 1
for j in range(0, len(df.columns)-1):
    for i in range(0, len(df.index)):
        dfColumnCount += 1
        dfNew = dfNew.append({'CountryName' : df.columns[j+1], 'Year' : df.iat[i, 0], 'Population' : df.iat[i, j+1]},
                     ignore_index=True)
dfNew.to_csv('WineImportClean.csv', index = False)




