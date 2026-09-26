import pandas as pd

df = pd.read_csv('Mycsvfile/startup_growth_investment_data (1).csv',delimiter=',')

print(df)

print("the datatype of the dataframe:")
print(df.dtypes)

print("the info of the dataset:")
print(df.info())

# acess the first three rows
print("the acess of the first three rows:")
print(df.head(3))

# acess the last three rows
print("acess the last three rows of the df:")
print(df.tail(3))

# summary of the statistic of the dataframe using describe funtion
print(" the summmary of the statistic of the dataframe:")
print(df.describe())

# count the rows and columns
print("the shape of the dataframe in the form of tuple:")
print(df.shape)

# Acess the single columns
FunddingRound = df['Funding Rounds']
print("the acess of the single columns:")
print(FunddingRound)

# Acess the multiple columns
Fundval = df[['Funding Rounds','Valuation (USD)']]
print("the acess of the multiple columns:")
print(Fundval)

#case 1 using .loc
#select the single row
second_row = df.loc[2]
print("the selecion of the single row:")
print(second_row)

# select th emultiple rows
second_row2 = df.loc[[3,4]]
print("the selection of the multiple rows:")
print(second_row2)

# select the slice of the row
second_row3 = df.loc[3:6]
print("the slice of the row:")
print(second_row3)

# coditional selection of the row
second_row4 = df.loc[df['Industry'] == 'EdTech']
print("conditional selection of the row:")
print(second_row4)

# select the single column
second_row5 = df.loc[:1,'Industry']
print("the selection of the single column:")
print(second_row5)

# selection of the multiple columns
second_row6 = df.loc[:1,['Funding Rounds','Valuation (USD)']]
print("the selection of the multiple columns:")
print(second_row6)

#select the slice of the columns
second_row7 = df.loc[:1,'Industry':'Valuation (USD)']
print("the slice of the columns:")
print(second_row7)

# combined the rows and columns
second_row8 = df.loc[df["Industry"] == 'EdTech','Industry':'Valuation (USD)']
print("the combined rows and columns:")
print(second_row8)

# case2 using .loc with index_col

df_index_col = pd.read_csv('Mycsvfile/startup_growth_investment_data (1).csv', delimiter=',')

print(df_index_col)

print("the datatype of the dataframe is:")
print(df_index_col.dtypes)

print("the info of the dataframe is:")
print(df_index_col.info())

# select the single row
second_row = df_index_col.loc[3]
print("the selection of the single row:")
print(second_row)

# select the multiple rows
second_row2 = df_index_col.loc[[4,5]]
print("the selection of the multiple rows:")
print(second_row2)

# select the slie of the rows
second_row3 = df_index_col.loc[2:8]
print("the slice of the  rows:")
print(second_row3)

# conditional selection of the rows
second_row4 = df_index_col.loc[df["Industry"] == 'EdTech']
print("the conditional selection of the row:")
print(second_row4)

#select the single columns
second_row5 = df_index_col.loc[:1,'Industry']
print("the selection of the multiple columns:")
print(second_row5)

#select the multiple columns
second_row6 = df_index_col.loc[:5,['Funding Rounds','Valuation (USD)']]
print("the selection of the multiple columns:")
print(second_row6)

#select the slice of the columns
second_row7 = df_index_col.loc[:5,'Industry':'Valuation (USD)']
print("the slice of the columns:")
print(second_row7)

# combined the rows and columns
second_row8 = df_index_col.loc[df["Industry"] == 'EdTech','Industry':'Valuation (USD)']
print("combined the rows and columns:")
print(second_row8)

# case3 using iloc
# select the single row
second_row = df_index_col.iloc[3]
print("the selection of the single row:")
print(second_row)

#select the multiple rows
second_row2 = df_index_col.iloc[[4,5,6]]
print("the selection of the multiple rows:")
print(second_row2)

# select the slice of the row
second_row3 = df_index_col.iloc[2:8]
print("the slice of the row:")
print(second_row3)

# select the single columns
second_row4 = df_index_col.iloc[:,5]
print("the selection of the single column:")
print(second_row4)

# select the multiple coluns
second_row5 = df_index_col.iloc[6,7]
print("the selection of the multiple columns:")
print(second_row5)

# select the slice of the columns
second_row6 = df_index_col.iloc[2:8]
print("the slice of the columns:")
print(second_row6)

# combined the rows and column
second_row7 = df_index_col.iloc[[4,5,6],2:8]
print("the combining of the rows and columns:")
print(second_row7)

# Remove the rows and columns
# remove the single row
df.drop(1, axis=0, inplace=True)
#remove the row with index
df.drop(index=3,inplace=True)
# remove the multiple rows
df.drop([4,5],axis=0,inplace=True)
print("the modified dataframe:")
print(df)

# remove the columns
df.drop('Investment Amount (USD)',axis=1,inplace=True)
# remove the column  startup name
df.drop(columns='Startup Name',inplace=True)
# remove the multiple columns
df.drop(['Number of Investors','Growth Rate (%)'],axis=1,inplace=True)
print("the modified dataframe after the removel of the row and column:")
print(df)

#REname the rows and columns
# Rename the columns
df.rename(columns={'Industry':'Industries'},inplace=True)
# Rename the multiple columns
df.rename(mapper={'Year Founded':'Year_Founded','Indutry':'Industries'},axis=1,inplace=True)

# rename the row
df.rename(index={3:5},inplace=True)
# rename the multiple rows
df.rename(mapper={2:4,6:7},axis=0,inplace=True)
print("the modified data:")
print(df)

#query() select the data like more sql
slected_row = df.query("Industries == 'EdTech' or Year_Founded > 2010")
print(slected_row.to_string())
print(len(slected_row))

# sorted the values in assending order
sorted_value = df.sort_values(by='Funding Rounds')
print(sorted_value.to_string(index=False))
# sort multiple values
df1 = df.sort_values(['Funding Rounds','Valuation (USD)'])
print(df1.to_string(index=False))

# pandas grouped
grouped = df.groupby('Funding Rounds')['Valuation (USD)'].sum()
print(grouped.to_string())
print(len(grouped))

# clean the pandas
# remove the row that have missing value
cleaned_df = df.dropna()
print("the clean dataframe:",cleaned_df)

# fill the missing value
df.fillna(0,inplace=True)
print("the clean and modified dataframe:",df)

# create an array pandas
# create a list 
data = [2,4,6,8]
array_1 = pd.array(data)
print(array_1)
#create an intiger array
int_array = pd.array([1,2,3,4,5],dtype='int')
print(int_array)