import pandas as pd

df = pd.read_excel('data/All_data.xlsx')

## For Ward counts ###
df_1 = pd.DataFrame(df.groupby(['ward'])['ward'].count())
x = df_1.index
y = df_1.ward
df_2 = pd.DataFrame({'x': x, 'y': y})
# municipality count
df_3 = pd.DataFrame(df.groupby(['municipality'])['municipality'].count())
x = df_3.index
y = df_3.municipality
df_3 = pd.DataFrame({'x': x, 'y': y})
######### Surveyor count#####
df_4 = pd.DataFrame(df.groupby(['surveyor_id'])['surveyor_id'].count())
x = df_4.index
y = df_4.surveyor_id
df_4 = pd.DataFrame({'x': x, 'y': y})