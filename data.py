import pandas as pd
import numpy as np

from upload_file import parse_contents


df = pd.read_excel('data/All_data.xlsx')
# Map all demographic values to labels
gender ={1: 'Male', 2: 'Female'}
df['survey/gender'] = df['survey/gender'].map(gender)

caste = {1: 'Brahmin/Chhetri', 2: 'Dalit', 3 : 'Janjati', 4: 'Newar', 5: 'Muslim', 95: 'Others'}
df['survey/caste'] = df['survey/caste'].map(caste)

family_type = {1: 'Nuclear', 2: 'Joint'}
df['survey/family_joint_nuclear'] = df['survey/family_joint_nuclear'].map(family_type)

# Respondent age group
bins = np.array([10,20,30,40,50,60,70,80,90,100])
df['Age'] = 2019 - (df['survey/Group1A/year'] - 57)
df['Age_group'] = pd.cut(df.Age,bins)
df['Age_group'] = df['Age_group'].astype(str)
# Municipality wise distinction
df_mun_1 = df[df.municipality == 1]
df_mun_2 = df[df.municipality == 2]
df_mun_3 = df[df.municipality == 3]

##### For all Municipality ####
# Function to make demographic bar graphs
def make_data(dataframe, column_name):
    df = pd.DataFrame(pd.value_counts(dataframe[column_name].values,sort=False))
    df.columns = ['Count']
    x = df.index
    y = df.Count
    df = pd.DataFrame({'x': x, 'y':y})
    return df
# Gender Dataframe
df_all_gender = make_data(df, 'survey/gender')
df_mun_1_gender = make_data(df_mun_1, 'survey/gender')
df_mun_2_gender = make_data(df_mun_2, 'survey/gender')
df_mun_3_gender = make_data(df_mun_3, 'survey/gender')
# Caste Dataframe
df_all_caste= make_data(df, 'survey/caste')
df_mun_1_caste = make_data(df_mun_1, 'survey/caste')
df_mun_2_caste = make_data(df_mun_2, 'survey/caste')
df_mun_3_caste = make_data(df_mun_3, 'survey/caste')
# Family_type dataframe
df_all_family_type = make_data(df, 'survey/family_joint_nuclear')
df_mun_1_ft = make_data(df_mun_1, 'survey/family_joint_nuclear')
df_mun_2_ft = make_data(df_mun_2, 'survey/family_joint_nuclear')
df_mun_3_ft = make_data(df_mun_3, 'survey/family_joint_nuclear')
# Age group of respondent
df_age_group = make_data(df, 'Age_group')
df_mun_1_ag = make_data(df_mun_1, 'Age_group')
df_mun_2_ag = make_data(df_mun_2, 'Age_group')
df_mun_3_ag = make_data(df_mun_3, 'Age_group')
print("This is funny{}".format(df_mun_1_ag['x'].dtype))







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
