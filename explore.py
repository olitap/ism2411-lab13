# ISM2411 Lab 13


# SELF-ASSESSMENT REFLECTIONS
#
# 1. A boolean filter checks whether certain conditions are true or false.
# It allows you to select only the rows that meet specific requirements.
#
# 2. df["revenue"] returns a Series, which is one column of data.
# df[["revenue"]] returns a DataFrame, which keeps the column in
# DataFrame format. This matters when working with multiple columns
# or when a function requires a DataFrame.
#
# 3. I would choose pandas because it makes it easier to organize,
# filter, and analyze large amounts of data. It can also perform
# calculations quickly without having to manually work through
# thousands of rows like you might in Excel.




# Exercise 1: Load the data

import pandas as pd

# Load the retail sales CSV file
df = pd.read_csv('data/retail_sales.csv')

# Print the first 5 rows
print(df.head())

# Print the number of rows and columns
print(df.shape)

# Print the column names
print(df.columns.tolist())

# Print the data types
print(df.dtypes)


# Exercise 2: Filter by region

south = df[df['region'] == 'South']

print(len(south))
print(south.head())


# Exercise 3: Top 5 by revenue

top5 = df.sort_values('revenue', ascending=False).head(5)

print(top5)


# Exercise 4: Two-condition filter

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())


# Exercise 5: A new column

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())

print(df['per_unit'].mean())

# Exercise 6: Unique values

print(df['region'].unique())

print(df['region'].value_counts())


# Exercise 7: Select columns

selected = df[['region', 'product', 'revenue']]

print(selected)
print(selected.shape)


# Exercise 8: Save

df.to_csv('data/explored.csv', index=False)

print("File saved successfully!")
