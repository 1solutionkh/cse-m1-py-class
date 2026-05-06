import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Diana"],
    "age":    [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000],
})

# Add a new column from a calculation
df["bonus"] = df["salary"] * 0.10
print(df)

# Add a new column from a condition
df["senior"] = df["age"] >= 30
print(df)

# Modify an existing column (give everyone a 5% raise)
df["salary"] = df["salary"] * 1.05
print(df)

# Rename a column
df = df.rename(columns={"name": "employee"})
print(df.columns)

# Drop a column
df = df.drop(columns=["bonus"])
print(df)

# Sort by salary, highest first
print(df.sort_values("salary", ascending=False))
