import pandas as pd

df = pd.read_csv('Mycsvfile/Real_Estate_Sales_2001-2022_GL-Short (1).csv',delimiter=',')

print(df)

print(" the data type of the dataframe:")
print(df.dtypes)

print("the info of the dataset:")
print(df.info())

# Acess the first three rows
print("Acess the first three rows:")
print(df.head(3))

# Acess the last three rows
print(" the last three rows:")
print(df.tail(3))

# summary of the statistic of dataframe using describe function
print("the summary of the statsitic of the dataframe:",df.describe())

# count the rows and columns using the shape function
print("the shape of the df using shape function:",df.shape)

# Acess the single columns
Town = df['Town']
print("the acess of the single columns:")
print(Town)

# Acess the multiple columns
Town_sale = df[['Town','Sale Amount']]
print("the acess of the multiple columns:")
print(Town_sale)

# case1 use of the .loc
# select the single row
second_row = df.loc[1]
print("the selection of the single row:")
print(second_row)

#select the multiple rows
second_row2 = df.loc[[1,3]]
print("the selection of the multiple rows:")
print(second_row2)

# select the slice of the row
second_row3 = df.loc[3:5]
print("the slice of the row:")
print(second_row3)

# conditional selection of the rows
second_row4 = df.loc[df["Town"] == 'Avon']
print("the conditional selection of the rows:")
print(second_row4)

# select the single column
second_row5 = df.loc[:1,'Address']
print("the selection of the single columns:")
print(second_row5)

# selection of the multiple columns
second_row6 = df.loc[:1,['Town','Address']]
print("the selection of the multiple columns:")
print(second_row6)

# select the slice of the columns
second_row7 = df.loc[:1,'Town':'Sale Amount']
print("the selection of the slice of the columns: ")
print(second_row7)

# combined the row and columns
second_row8 = df.loc[df["Town"] == 'Avon','Town':'Sale Amount']
print("the combing of the rows and columns:")
print(second_row8)

# case2 using .loc with index col

df_index_col = pd.read_csv('Mycsvfile/Real_Estate_Sales_2001-2022_GL-short (1).csv',delimiter=',')

print(df_index_col)

print("the data type of the df:",df_index_col.dtypes)

print(df_index_col.info())

# select the single row
second_row = df_index_col.loc[3]
print("the selection of the single row:")
print(second_row)

# select the multiple rows
second_row2 = df_index_col.loc[[3,5]]
print("the selection of the multiple rows:")
print(second_row2)

# select the slice of the row
second_row3 = df_index_col.loc[2:8]
print("the slice of the rows of df_index_col:")
print(second_row3)

#coditional selection of the row
second_row4 = df_index_col.loc[df["Town"] == 'Avon','Town':'Sale Amount']
print("the coditional selection of the rows:")
print(second_row4)

# select the single columns
second_row5 = df_index_col.loc[:5,'Town']
print("the selection of the single columns:")
print(second_row5)

# select the multiple columns
second_row6 = df_index_col.loc[:5,['Town','Address']]
print("the selection of the multiple columns:")
print(second_row6)

# slice of the columns
second_row7 = df_index_col.loc[:5,'Town':'Sale Amount']
print("the slice of the columns is:")
print(second_row7)

# the combing of the rows and columns
second_row8 = df_index_col.loc[df["Town"] == 'Avon','Address':'Sale Amount']
print("the combing of the rows and columns:")
print(second_row8)

# case3 using iloc
#selecting single row
second_row = df_index_col.iloc[4]
print("the selection of the single row:")
print(second_row)

# select the multiple rows
second_row2 = df_index_col.iloc[[3,4,5]]
print("the selection of the multiple rows:")
print(second_row2)

# select the slice of the row
second_row3 = df_index_col.loc[2:6]
print("the slice of the row:")
print(second_row3)

# select the single columns
second_row4 = df_index_col.iloc[:,4]
print("the selection of the single columns:")
print(second_row4)

# selectio of the multiple columns
second_row5 = df_index_col.iloc[:,[3,6]]
print("the selection of the multiple row:")
print(second_row5)

# select the slice of the columns
second_row6 = df_index_col.iloc[2:6]
print("the slice of the columns:")
print(second_row6)

# the combined row and column
second_row7 = df_index_col.iloc[[3,4,5],2:6]
print(" the combined row and column are:")
print(second_row7)

# Remove the rows and columns of the dataframe
# remove the row
df.drop(2, axis=0,inplace=True)
# remove the row with index 3
df.drop(index=3,inplace=True)
#remove the multiple rows
df.drop([4,5],axis=0,inplace=True)
print("the modified dataframe remove the row and column:")
print(df)

# remove the columns
df.drop('Serial Number',axis=1,inplace=True)
# remove the column list year
df.drop(columns='List Year',inplace=True)
# remove the multiple columns
df.drop(['Date Recorded','Address'],axis=1,inplace=True)
print("the modified data after deleting thre rows and columns:")
print(df)

#Rename the columns
df.rename(columns={'Town':'ModelTown'},inplace=True)
# rename the multiple columns
df.rename(mapper={'Assessed Value':'Newvalue','Sale Amount':'Salepercentile'},axis=1,inplace=True)
print("the modified data:")
print(df)

# rename the rows
df.rename(index={0:3},inplace=True)
# rename the multiple rows
df.rename(mapper={2:4,3:6},axis=0,inplace=True)
print("the modefied data:")
print(df)

# query() select the data in pandas like more sql
slected_row = df.query('ModelTown == \'Avon\' or Newvalue > 170800')
print(slected_row.to_string())
print(len(slected_row))

# sorted the values
# sort dataframe by sale ratio
sorted_df = df.sort_values(by='Newvalue')
print(sorted_df.to_string(index=False))
# sort multiple values
df1 = df.sort_values(['Newvalue','Salepercentile'])
print(df1.to_string(index=False))

# pandas group
grouped = df.groupby('Newvalue')['Salepercentile'].sum()
print(grouped.to_string())
print('grouped:',len(grouped))

#clean the pandas
# remove the rows that have missing value
df_cleaned = df.dropna()
print("the clean data frame of the pandas:",df_cleaned)

# fill the nan values
df.fillna(0,inplace=True)
print("the data after filling the nan values:",df)

# create a list of the data
data = [2,4,6,8]
#create an array
array1 = pd.array(data)
print(array1)
# create an intiger array
int_array = pd.array([1,3,5,7,9],dtype='int')
print(int_array)