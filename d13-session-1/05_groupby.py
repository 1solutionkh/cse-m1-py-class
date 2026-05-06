import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
    "city":   ["NY", "LA", "NY", "Chicago", "LA", "NY"],
    "age":    [25, 30, 35, 28, 40, 22],
    "salary": [50000, 60000, 75000, 55000, 80000, 48000],
})

# Average salary per city
print(df.groupby("city")["salary"].mean())
# city
# Chicago    55000.0
# LA         70000.0
# NY         57666.7

# Multiple aggregations at once
print(df.groupby("city")["salary"].agg(["min", "max", "mean", "count"]))

# How many people in each city?
print(df["city"].value_counts())

# Group by city and get the oldest person's age in each
print(df.groupby("city")["age"].max())

# Total salary across the whole company
print("Total salary:", df["salary"].sum())
