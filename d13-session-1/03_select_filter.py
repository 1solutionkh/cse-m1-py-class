import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Diana"],
    "age":    [25, 30, 35, 28],
    "city":   ["NY", "LA", "NY", "Chicago"],
    "salary": [50000, 60000, 75000, 55000],
})

# Select a single column -> Series
print(df["name"])

# Select multiple columns -> DataFrame
print(df[["name", "salary"]])

# Select rows by position
print(df.iloc[0])      # first row
print(df.iloc[1:3])    # rows 1 and 2

# Select rows by label (here labels are 0..3)
print(df.loc[0, "name"])   # Alice

# Filter rows by condition
print(df[df["age"] > 28])
#       name  age city  salary
# 1      Bob   30   LA   60000
# 2  Charlie   35   NY   75000

# Combine conditions: age > 25 AND city == "NY"
print(df[(df["age"] > 25) & (df["city"] == "NY")])
