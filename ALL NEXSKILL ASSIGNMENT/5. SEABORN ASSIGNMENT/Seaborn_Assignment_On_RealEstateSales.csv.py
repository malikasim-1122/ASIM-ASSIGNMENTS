import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# sample data
data = pd.DataFrame({'x':np.arange(100),'y':np.random.rand(100).cumsum()})

# set theme
sns.set_theme(style='darkgrid')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x',y='y',data=data)
plt.show()

# custamize the theme and create the plot
sns.set_theme(style='darkgrid', rc={'axes.facecolor':'gray','grid.color':'white'})
sns.lineplot(x='x',y='y',data=data)
plt.show()

# load data from csv file of the RealEstate_Sale

df = pd.read_csv('Mycsvfile/Real_Estate_Sales_2001-2022_GL-Short (1).csv',delimiter=',')

print(df)

print("the data type of the df:",df)
dffilter = df.head(40)
dffilter100 = df.head(100)

# kind = hist
g = sns.displot(data=dffilter,x='Town',y='Sale Amount',hue='Sales Ratio',kind='hist')
g.figure.suptitle("The histplot of RealEstateSale")
g.figure.show()

read = input("wait for me ....")

# kind =kde
g = sns.displot(data=dffilter,x='Sales Ratio',y='Sale Amount',kind='kde')
g.figure.suptitle("The displot of the data")
g.figure.show()

read = input("wait for me ...")

#kind = kde
g = sns.kdeplot(data=dffilter,x='Sale Amount')
g.figure.suptitle("The kde plot of the data")
g.figure.show()

read = input("wait for me .....")

# Histplot
g = sns.histplot(data=dffilter,x='Town',y='Sale Amount',hue='Sale Amount',multiple='stack')
g.figure.suptitle("The histplot of the RealEstate Sale")
g.figure.show()

read = input("wait for me .....")

# scatter plot
g = sns.scatterplot(data=dffilter,x='Town',y='Sale Amount')
g.figure.suptitle("The Scatter plot of the data")
g.figure.show()

read = input("wait for me .....")

# barplot
g = sns.barplot(data=dffilter,x='Town',y='Sale Amount')
g.figure.suptitle("The barplot of the data")
g.figure.show()

read = input("wait for me .....")

# line plot
g = sns.lineplot(data=dffilter,x='Town',y='Sale Amount')
g.figure.suptitle("The lineplot of the data")
g.figure.show()

read = input("wait for me ....")

# catplot
g = sns.catplot(data=dffilter,x='Town',y='Sale Amount')
g.figure.suptitle("The catplot of the data")
g.figure.show()

read = input("wait for me .....")

# Heatmap plot
glue = dffilter.pivot(columns='Town',values='Sale Amount')
g = sns.heatmap(glue)
g.figure.suptitle("The heatmap plot")
g.figure.show()

read = input("wait for me .....")
