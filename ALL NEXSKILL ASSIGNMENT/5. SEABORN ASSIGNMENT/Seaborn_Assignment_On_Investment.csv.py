import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({'x':np.arange(100),'y':np.random.rand(100).cumsum()})

# set theme and create he plot
sns.set_theme(style='dark')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='darkgrid')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x',y='y',data=data)
plt.show()

# custamize the theme and create the plot
sns.set_theme(style='darkgrid', rc={'axes.facecolor':'white','grid.color':'gray'})
sns.lineplot(x='x',y='y',data=data)
plt.show()

# startup_Growth_investment_data based example
# load csv file of the data

df = pd.read_csv('Mycsvfile/startup_growth_investment_data (1).csv',delimiter=',')

print(df)
print("The data type of the dataframe",df.dtypes)
dffilter =  df.head(40)
dffilter100 = df.head(100)

# kind = hist
g = sns.displot(data=dffilter,x='Industry',y='Investment Amount (USD)',hue='Valuation (USD)',kind='hist')
g.figure.suptitle("The Displot of the data")
g.figure.show()

read = input("wait for me ......")

# kind = kde
g = sns.displot(data=dffilter,x='Valuation (USD)',y='Investment Amount (USD)',kind='kde')
g.figure.suptitle("The kdeplot of the data")
g.figure.show()

read = input("wait for me ....")

# kind = kde
g = sns.kdeplot(data=dffilter,x='Investment Amount (USD)')
g.figure.suptitle("The kdeplot of the data")
g.figure.show

read = input("wait for me .....")

# Histplot
g = sns.histplot(data=dffilter,x='Industry',y='Investment Amount (USD)',hue='Industry',multiple='stack')
g.figure.suptitle("The Histplot of the data")
g.figure.show()

read = input("wait for me ....")

# scaterplot
g = sns.scatterplot(data=dffilter,x='Industry',y='Investment Amount (USD)')
g.figure.suptitle("The Scatterplot of the data")
g.figure.show()

read = input("wait for me ....")

#barplot
g = sns.barplot(data=dffilter,x='Industry',y='Investment Amount (USD)')
g.figure.suptitle("The barplot of the data")
g.figure.show()

read = input("wait for me ....")

#lineplot
g = sns.lineplot(data=dffilter,x='Industry',y='Investment Amount (USD)')
g.figure.suptitle("The lineplot of the data ")
g.figure.show()

read = input("wait for me .......")

#catplot
g = sns.catplot(data=dffilter,x='Industry',y='Investment Amount (USD)')
g.figure.suptitle("The catplot of the data")
g.figure.show()

read = input("wait for me .....")

# HeatMapPlot
glue = dffilter.pivot(columns='Industry',values='Investment Amount (USD)')
g = sns.heatmap(glue)
g.figure.suptitle("The HeatMapplot of the data")
g.figure.show()

read = input("wait for me ......")