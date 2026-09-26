import numpy as np
import pandas as pd

# =====================================================================
# 1. READ CSV FILE TO DATAFRAME
# =====================================================================
#  Read csv file to DataFrame using comma delimiter for RealEstate data
df = pd.read_csv(
    "RealEstate-USA (3).csv",
    delimiter=",",
    parse_dates=["prev_sold_date"],
    date_format="%Y-%m-%d",
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
city_state = df[["city", "state"]]
print("access multiple columns: df : ")
print(city_state)
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

# Conditional selection of rows using .loc (Filtering properties in Ponce city)
second_row4 = df.loc[df["city"] == "Ponce"]
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

# Selecting a single column using .loc
second_row5 = df.loc[:1, "city"]
print("#Selecting a single column using .loc")
print(second_row5)
print()

# Selecting multiple columns using .loc
second_row6 = df.loc[:, ["city", "state"]]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

# Selecting a slice of columns using .loc
second_row7 = df.loc[:1, "price":"street"]
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

# Combined row and column selection using .loc
second_row8 = df.loc[df["city"] == "Ponce", "price":"street"]
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


# =====================================================================
# CASE 2 : USING .loc WITH index_col
# =====================================================================
print("# Case 2 : using .loc with index_col - starts here")
# Second cycle - with index_col as street (acting as the ID row indicator)
df_index_col = pd.read_csv(
    "RealEstate-USA (3).csv",
    delimiter=",",
    parse_dates=["prev_sold_date"],
    date_format="%Y-%m-%d",
    index_col="street",
)

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Selecting a single row using .loc (Targeting street label 1962661)
try:
    second_row = df_index_col.loc[1962661]
    print("#Selecting a single row using .loc via street index")
    print(second_row)
except KeyError:
    pass
print()

# Selecting multiple rows using .loc via street labels
try:
    second_row2 = df_index_col.loc[[1962661, 1902874]]
    print("#Selecting multiple rows using .loc via street index")
    print(second_row2)
except KeyError:
    pass
print()

# Conditional selection of rows using .loc on indexed DataFrame
second_row4 = df_index_col.loc[df_index_col["city"] == "Ponce"]
print("#Conditional selection of rows using .loc with index dataframe")
print(second_row4)
print()

# Selecting a single column using .loc with index dataframe
second_row5 = df_index_col.loc[:, "city"]
print("#Selecting a single column using .loc with index dataframe")
print(second_row5.head())
print()

# Selecting multiple columns using .loc with index dataframe
second_row6 = df_index_col.loc[:, ["city", "state"]]
print("#Selecting multiple columns using .loc with index dataframe")
print(second_row6.head())
print()

# Combined row and column selection using .loc with index dataframe
second_row8 = df_index_col.loc[
    df_index_col["city"] == "Ponce", "price":"house_size"
]
print("#Combined row and column selection using .loc with index dataframe")
print(second_row8.head())
print()
# Case 2 : using .loc with index_col  -  ends here


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
# Add a New Row to a Pandas DataFrame match real estate columns order
# Order: brokered_by,status,price,bed,bath,acre_lot,street,city,state,zip_code,house_size,prev_sold_date
df.loc[len(df.index)] = [
    103378,
    "for_sale",
    250000,
    4,
    3,
    0.25,
    1962665,
    "San Juan",
    "Puerto Rico",
    901,
    1850,
    "2026-08-13",
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

# delete status column
df.drop("status", axis=1, inplace=True)
# delete brokered_by column
df.drop(columns="brokered_by", inplace=True)
# delete zip_code and acre_lot columns
df.drop(["zip_code", "acre_lot"], axis=1, inplace=True)
print("Modified DataFrame - delete columns :")
print(df.head())

# Rename Labels in a DataFrame
# rename column 'state' to 'state_nameChanged'
df.rename(columns={"state": "state_nameChanged"}, inplace=True)
# rename columns 'bed' and 'bath'
df.rename(
    mapper={"bed": "bedrooms_Changed", "bath": "bathrooms_Changed"},
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
selected_rows = df.query("city == 'Ponce' or price > 500000")
print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by="price")
print(sorted_df.to_string(index=False))

# Sort Pandas DataFrame by Multiple Columns
# Sort DataFrame by 'price' and then by 'street'
df1 = df.sort_values(by=["price", "street"])
print("Sorting by 'price' (ascending) and then by 'street' (ascending):\n")
print(df1.to_string(index=False))


# =====================================================================
# PANDAS GROUPBY & DATA CLEANING
# =====================================================================
# group the DataFrame by the city column and calculate the sum of price
grouped = df.groupby("city")["price"].sum()
print(grouped.to_string())
print("grouped :", len(grouped))

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n", df_cleaned)

# filling NaN values with 0
df.fillna(0, inplace=True)
print("\nData after filling NaN with 0:\n", df)


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
