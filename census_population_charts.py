# %% [markdown]
# This notebook will document the creation of a population pyramid for England and Wales using publicly available data from the 2021 census 

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import numpy as np

df = pd.read_excel('census2021firstresultsenglandwales1.xlsx', 'P03', skiprows=7, usecols='B,D:AO')
df

#importing the required columns of the dataset and printing it to assess how it looks 


# %%
popdata = df.head(1)
popdata

#in this case, only the top row is needed as it contains the required data 

# %%
popdata_transposed = popdata.T
popdata_transposed
new_header = popdata_transposed.iloc[0] 
popdata_transposed = popdata_transposed[1:] 
popdata_transposed.columns = new_header


popdata_transposed = popdata_transposed.reset_index()
popdata_transposed = popdata_transposed.rename(columns={'index': 'Group', 'England and Wales': 'Population'})

popdata_transposed = popdata_transposed.rename_axis(None, axis=1)

popdata_transposed

female_data = popdata_transposed[popdata_transposed['Group'].str.contains('Females')]
male_data = popdata_transposed[popdata_transposed['Group'].str.contains('Males')]

female_data, male_data

#transposing the row and splitting it up into two datasets (male and female)

# %%
female_data.loc[:, 'Group'] = female_data.loc[:, 'Group'].str.replace('Females:\nAged','').str.replace('\n[note 12]',' ')
male_data.loc[:, 'Group'] = male_data.loc[:, 'Group'].str.replace('Males:\nAged','').str.replace('\n[note 12]',' ')

female_data, male_data

#cleaning up the category labels 

# %%
plt.barh(y = female_data['Group'], width = female_data['Population'], color = '#ee7a87')
plt.barh(y = female_data['Group'], width = male_data['Population'], left = -male_data['Population'], color = '#4682b4')
plt.xlabel('Population')
plt.ylabel('Age range')
plt.xlim(xmin=-2500000, xmax = 2500000)
plt.xticks(ticks=[-2000000, -1000000, 0, 1000000, 2000000],
labels=['2,000,000', '1,000,000', '0', '1,000,000', '2,000,000'])

#creating the plot, with male data in blue, and female in pink 

# %%



