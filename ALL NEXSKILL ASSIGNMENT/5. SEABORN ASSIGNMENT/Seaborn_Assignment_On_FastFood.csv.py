import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({'x':np.arange(100),'y':np.random.rand(100).cumsum()})

# set the theme and create the plot
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

df = pd.read_csv('Mycsvfile/FastFoodRestaurants (2).csv',delimiter=',')
print(df)
print(df.dtypes)
dffilter = df.head(40)
dffilter100 = df.head(100)

# kind = histplot
g = sns.displot(data=dffilter,x='city',y='longitude',hue='latitude',kind='hist')
g.figure.suptitle("the histplot of the FastFood")
g.figure.show()

read = input("wait for me ......")

# kind = kde
g = sns.displot(data=dffilter,x='longitude',y='latitude',kind='kde')
g.figure.suptitle("The displot of the FastFood")
g.figure.show()

read = input("wait for me ......")

# kde plot
g = sns.kdeplot(data=dffilter,x='longitude')
g.figure.suptitle("The kde plot of the FastFood")
g.figure.show()

read = input("wait for me .....")

# histplot
g = sns.histplot(data=dffilter,x='city',y='longitude',hue='city',multiple='stack')
g.figure.suptitle("the histplot of the fast food")
g.figure.show()

read = input("wait for me .....")

# scatter plot
g = sns.scatterplot(data=dffilter,x='city',y='longitude')
g.figure.suptitle("The scatterplot of FastFood")
g.figure.show()

read = input("wait for  me ...")

# barplot
g = sns.barplot(data=dffilter,x='city',y='longitude')
g.figure.suptitle("The barplot of the FastFood")
g.figure.show()

read = input("wait for me ....")

# lineplot
g = sns.lineplot(data=dffilter,x='city',y='longitude')
g.figure.suptitle("The lineplot of the FastFood")
g.figure.show()

read = input("wait for me ....")

# catplot
g = sns.catplot(data=dffilter,x='city',y='longitude')
g.figure.suptitle("The catplot of the FastFood")
g.figure.show()

read = input("wait for me .....")

# Heatmap plot
glue = dffilter.pivot(columns='city',values='longitude')
g = sns.heatmap(glue)
g.figure("Heatmap Plot")
g.figure.show()

read = input("wait for me .....")