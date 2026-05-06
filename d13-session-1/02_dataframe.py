import pandas as pd

# DataFrame = 2D labeled table (rows + columns)
data = {
    "name":   ["Alice", "Bob", "Charlie", "Diana"],
    "age":    [25, 30, 35, 28],
    "city":   ["NY", "LA", "NY", "Chicago"],
    "salary": [50000, 60000, 75000, 55000],
}

df = pd.DataFrame(data)

print(df)
#       name  age     city  salary
# 0    Alice   25       NY   50000
# 1      Bob   30       LA   60000
# 2  Charlie   35       NY   75000
# 3    Diana   28  Chicago   55000

print(df.shape)        # (4, 4)        — rows, columns
print(df.columns)      # Index(['name', 'age', 'city', 'salary'], dtype='object')
print(df.dtypes)       # type of each column
print(df.head(2))      # first 2 rows
print(df.describe())   # stats summary for numeric columns
