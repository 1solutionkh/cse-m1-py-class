import matplotlib.pyplot as plt

# Multiple plots in one figure: 1 row, 2 columns
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Left chart: line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
axes[0].plot(x, y, color="blue", marker="o")
axes[0].set_title("Squares (line)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("x²")

# Right chart: bar chart
cities   = ["NY", "LA", "Chicago"]
salaries = [62500, 70000, 55000]
axes[1].bar(cities, salaries, color="green")
axes[1].set_title("Salary by City (bar)")
axes[1].set_ylabel("Salary")

plt.tight_layout()       # nice spacing between subplots
plt.show()
