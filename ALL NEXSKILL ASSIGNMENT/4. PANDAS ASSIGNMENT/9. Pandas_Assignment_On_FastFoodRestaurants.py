import numpy as np
import pandas as pd

# =====================================================================
# 1. READ CSV FILE TO DATAFRAME
# =====================================================================
# Read csv file to DataFrame using comma delimiter for Fast Food data
df = pd.read_csv(
    "FastFoodRestaurants (3).csv",
    delimiter=",",
)
print(df)

print("df - data types", df.dtypes)
print("df.info():   ", df.info())

# display the last three rows
print("Last three Rows:")
print(df.tail(3))

# display the first three rows
print("First Three Rows:")
print(df.head(3))
print()

# Summary of Statistics of DataFrame using describe() method.
print(
    "Summary of Statistics of DataFrame using describe() method", df.describe()
)

# Counting the rows and columns in DataFrame using shape().
print("Counting the rows and columns in DataFrame using shape() : ", df.shape)
print()


# =====================================================================
# ACCESSING COLUMNS
# =====================================================================
# access the city column
city_column = df["city"]
print("access the city column: df : ")
print(city_column)
print()

# access multiple columns
city_province = df[["city", "province"]]
print("access multiple columns: df : ")
print(city_province)
print()


# =====================================================================
# CASE 1 : USING .loc - DEFAULT CASE
# =====================================================================
print("# Case 1 : using .loc - default case - starts here")

# Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

# Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

# Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

# Conditional selection of rows using .loc
# Filtering properties in Massena city
second_row4 = df.loc[df["city"] == "Massena"]
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

# Selecting a single column using .loc
second_row5 = df.loc[:1, "city"]
print("#Selecting a single column using .loc")
print(second_row5)
print()

# Selecting multiple columns using .loc
second_row6 = df.loc[:, ["city", "province"]]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

# Selecting a slice of columns using .loc
second_row7 = df.loc[:1, "address":"name"]
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

# Combined row and column selection using .loc
second_row8 = df.loc[df["city"] == "Massena", "address":"name"]
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 1 : using .loc - default case - ends here


# =====================================================================
# CASE 2 : USING .loc WITH index_col
# =====================================================================
print("# Case 2 : using .loc with index_col - starts here")

# Second cycle - with index_col as address
df_index_col = pd.read_csv(
    "FastFoodRestaurants (3).csv",
    delimiter=",",
    index_col="address",
)

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Selecting a single row using .loc via address index
try:
    first_address = df_index_col.index[0]
    second_row = df_index_col.loc[first_address]
    print("#Selecting a single row using .loc via address index")
    print(second_row)
except KeyError:
    pass
print()

# Selecting multiple rows using .loc via address labels
try:
    address1 = df_index_col.index[0]
    address2 = df_index_col.index[1]
    second_row2 = df_index_col.loc[[address1, address2]]
    print("#Selecting multiple rows using .loc via address index")
    print(second_row2)
except KeyError:
    pass
print()

# Conditional selection of rows using .loc on indexed DataFrame
second_row4 = df_index_col.loc[df_index_col["city"] == "Massena"]
print("#Conditional selection of rows using .loc with index dataframe")
print(second_row4)
print()

# Selecting a single column using .loc with index dataframe
second_row5 = df_index_col.loc[:, "city"]
print("#Selecting a single column using .loc with index dataframe")
print(second_row5.head())
print()

# Selecting multiple columns using .loc with index dataframe
second_row6 = df_index_col.loc[:, ["city", "province"]]
print("#Selecting multiple columns using .loc with index dataframe")
print(second_row6.head())
print()

# Combined row and column selection using .loc with index dataframe
second_row8 = df_index_col.loc[
    df_index_col["city"] == "Massena", "city":"name"
]
print("#Combined row and column selection using .loc with index dataframe")
print(second_row8.head())
print()

# Case 2 : using .loc with index_col - ends here


# =====================================================================
# CASE 3 : USING .iloc (POSITIONAL-BASED SELECTION)
# =====================================================================
print("# Case 3 : Using .iloc - starts here")

# Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

# Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3, 5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

# Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

# Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:, 2]
print("#Selecting a single column using .iloc")
print(second_row5.head())
print()

# Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:, [2, 4]]
print("#Selecting multiple columns using .iloc")
print(second_row6.head())
print()

# Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:, 2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7.head())
print()

# Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3, 5], 2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here


print("Next Run")


# =====================================================================
# PANDAS DATAFRAME MANIPULATION
# =====================================================================
# Add a New Row to a Pandas DataFrame
# Order:
# address,city,country,keys,latitude,longitude,name,postalCode,province,websites

df.loc[len(df.index)] = [
    "100 Main St",
    "San Juan",
    "US",
    "us/pr/sanjuan/100mainst",
    18.4655,
    -66.1057,
    "McDonald's",
    "00901",
    "PR",
    "http://mcdonalds.com",
]

print("Modified DataFrame - add a new row:")
print(df.tail(1))
print()


# Remove Rows/Columns from a Pandas DataFrame
# delete row with index 1
df.drop(1, axis=0, inplace=True)

# delete row with index 2
df.drop(index=2, inplace=True)

# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)

print("Modified DataFrame - Remove Rows:")
print(df.head())


# delete country column
df.drop("country", axis=1, inplace=True)

# delete keys column
df.drop(columns="keys", inplace=True)

# delete latitude and longitude columns
df.drop(["latitude", "longitude"], axis=1, inplace=True)

print("Modified DataFrame - delete columns :")
print(df.head())


# Rename Labels in a DataFrame
# rename column 'province' to 'province_nameChanged'
df.rename(
    columns={"province": "province_nameChanged"},
    inplace=True
)

# rename columns 'city' and 'name'
df.rename(
    mapper={
        "city": "city_Changed",
        "name": "restaurant_name_Changed"
    },
    axis=1,
    inplace=True,
)

print("Modified DataFrame - Rename Labels :")
print(df.head())


# Example: Rename Row Labels
df.rename(index={0: 7}, inplace=True)
print("Modified DataFrame - Rename Row - 0 >>> 7 Labels:")
print(df.head())


# =====================================================================
# QUERY AND SORTING DATA
# =====================================================================
# query() to Select Data using updated columns names
selected_rows = df.query(
    "city_Changed == 'Massena' or postalCode == '43160'"
)
print(selected_rows.to_string())
print(len(selected_rows))


# sort DataFrame by restaurant name in ascending order
sorted_df = df.sort_values(by="restaurant_name_Changed")
print(sorted_df.to_string(index=False))


# Sort Pandas DataFrame by Multiple Columns
# Sort DataFrame by 'restaurant_name_Changed' and then by 'city_Changed'
df1 = df.sort_values(
    by=["restaurant_name_Changed", "city_Changed"]
)

print(
    "Sorting by 'restaurant_name_Changed' (ascending) "
    "and then by 'city_Changed' (ascending):\n"
)
print(df1.to_string(index=False))


# =====================================================================
# PANDAS GROUPBY & DATA CLEANING
# =====================================================================
# group the DataFrame by the city column and calculate
# the count of restaurants in each city
grouped = df.groupby("city_Changed")["restaurant_name_Changed"].count()

print(grouped.to_string())
print("grouped :", len(grouped))


# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n", df_cleaned)

# =====================================================================
# PANDAS ARRAY CREATION
# =====================================================================
# create a list named data
data = [2, 4, 6, 8]
array1 = pd.array(data)
print(array1)


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype="int")
print(int_array)
print()


print (values"anything")