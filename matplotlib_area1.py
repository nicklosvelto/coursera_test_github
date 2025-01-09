#Import Primary Modules:
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')  # optional: for ggplot-like style

df_can = pd.read_csv('Canada.csv')

# print(df_can.head())
# print(df_can.shape)
# print('Data read into a pandas dataframe!')
#Set the country name as index - useful for quickly looking up countries using .loc method.
df_can.set_index('Country', inplace=True)

# Let's view the first five elements and see how the dataframe was changed
# print(df_can.head())
# print('data dimensions:', df_can.shape)
# finally, let's create a list of years from 1980 - 2013
# this will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))
# In the last module, we created a line plot that visualized the top 5 countries that contribued the most immigrants 
# to Canada from 1980 to 2013. With a little modification to the code, we can visualize this plot as a cumulative plot, 
# also knows as a Stacked Line Plot or Area plot.

# print(years)
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head()

# transpose the dataframe
df_top5 = df_top5[years].transpose()

# print(df_top5.head())
# let's change the index values of df_top5 to type integer for plotting
df_top5.index = df_top5.index.map(int)
# The unstacked plot has a default transparency (alpha value) at 0.5. 
# We can modify this value by passing in the alpha parameter.
df_top5.plot(kind='area',
             alpha=0.25,  # 0 - 1, default value alpha = 0.5
             stacked=False,
             figsize=(20, 10))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()