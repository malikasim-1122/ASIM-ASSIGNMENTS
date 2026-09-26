import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# sample data

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})


# set the theme
sns.set_theme(style= "darkgrid")

# create a plot

sns.lineplot(x= "x" , y= "y" , data=data)
plt.show()

# other theme set similarly

sns.set_theme(style= "whitegrid")
sns.lineplot( x= "x" , y= "y" , data=data)
plt.show()

sns.set_theme(style= "dark")
sns.lineplot( x= "x" , y= "y" , data=data)
plt.show()

sns.set_theme(style= "white")
sns.lineplot( x="x" , y="y" , data=data)
plt.show()


sns.set_theme(style= "ticks")
sns.lineplot( x= "x" , y="y" , data=data)
plt.show()

# how to customize the theme

sns.set_theme(style= "darkgrid" , rc={"axes.facecolor" : "grey" , "grid.color" : "white"})
sns.lineplot( x= "x" , y= "y" , data=data)
plt.show()

# realestate based example
df = pd.read_csv('RealEstate-USA (3).csv', delimiter=",", parse_dates=[11], date_format={'date_added': '%m-%d-%Y'})


print(df.dtypes)

dffilter= df.head(40)
dffilter100= df.head(100)


sns.set(style="whitegrid")

g=sns.displot(data=dffilter, x="bed" , y="price" , hue="bath",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=bed , y=price , hue=bath,  kind='hist'  )"  )

# display that plot
plt.show()

read = input("Wait for me....")

g=sns.displot(data=dffilter, x="bed" , y="price" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=bed , y=price , kind='kde'  )"  )

plt.show()


read = input("Wait for me....")

g=sns.kdeplot(data=dffilter, x="bed")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=bed)"  )

plt.show()

read = input("Wait for me....")

g = sns.histplot(data=dffilter, x='bed', y='price', hue='bath', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='bed', y='price', hue='bath', multiple=stack)"  )


# display the plot



plt.show()

read = input("Wait for me....")

# use seaborn to create a plot

g = sns.scatterplot(x='bed', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='bed', y='price', data=dffilter)"  )
plt.show()
read = input("Wait for me....")


g=sns.lineplot(data=dffilter, x="bed" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=bed , y=price  )"  )
# Display the plot
plt.show()
read = input("Wait for me....")



g=sns.barplot(data=dffilter, x="bed", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=bed, y=price, legend=False)"  )
# Display the plot
plt.show()
read = input("Wait for me....")


g=sns.catplot(data=dffilter, x="bed", y="price")
g.figure.suptitle("sns.catplot(data=df, x=bed, y=price)"  )
# Display the plot
plt.show() 
read = input("Wait for me....")



glue = dffilter.pivot(columns="bed", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=agency, values=price)"  )
# Display the plot
plt.show()
read = input("Wait for me....")




