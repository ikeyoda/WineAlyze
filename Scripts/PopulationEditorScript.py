import pandas as pd
df = pd.read_csv("populationFINAL.csv")
dfNew = pd.DataFrame(columns=['CountryName', 'Year', 'Population'])
dfColumnCount = 1
for i in range(0, len(df.index)):
    for j in range(2, len(df.columns)):
        dfColumnCount += 1
        dfNew = dfNew.append({'CountryName' : df.iat[i, 1], 'Year' : df.columns[j], 'Population' : df.iat[i, j]},
                     ignore_index=True)
dfNew.to_csv('populationClean.csv', index = False)
df_saved_file = pd.read_csv('populationClean.csv')




