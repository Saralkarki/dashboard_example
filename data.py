import pandas as pd

from upload_file import parse_contents


df = pd.read_excel('data/All_data.xlsx')
df_mun_1 = df[df.municipality == 1]
df_mun_2 = df[df.municipality == 2]
df_mun_3 = df[df.municipality == 3]

##### For all Municipality ####
# Respondent Gender indicator
df_all_gender = pd.DataFrame(pd.value_counts(df['survey/gender'].values, sort=False))
df_all_gender.columns = ['Count']
x = df_all_gender.index
y = df_all_gender.Count
df_all_gender = pd.DataFrame({'x': x, 'y': y})
print(df_all_gender)

#####
df_mun_1_gender = pd.DataFrame(pd.value_counts(df_mun_1['survey/gender'].values, sort=False))
df_mun_1_gender.columns = ['Count']
x = df_mun_1_gender.index
y = df_mun_1_gender.Count
df_mun_1_gender = pd.DataFrame({'x': x, 'y': y})
######
df_mun_2_gender = pd.DataFrame(pd.value_counts(df_mun_2['survey/gender'].values, sort=False))
df_mun_2_gender.columns = ['Count']
x = df_mun_2_gender.index
y = df_mun_2_gender.Count
df_mun_2_gender = pd.DataFrame({'x': x, 'y': y})
######
df_mun_3_gender = pd.DataFrame(pd.value_counts(df_mun_3['survey/gender'].values, sort=False))
df_mun_3_gender.columns = ['Count']
x = df_mun_3_gender.index
y = df_mun_3_gender.Count
df_mun_3_gender = pd.DataFrame({'x': x, 'y': y})
######



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
##
