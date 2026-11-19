# ISM2411 Lab 13
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
