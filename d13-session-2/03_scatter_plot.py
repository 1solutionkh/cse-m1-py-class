import matplotlib.pyplot as plt

# Scatter plot: age vs salary (each dot = one person)
ages     = [25, 30, 35, 28, 40, 22, 45, 33]
salaries = [50000, 60000, 75000, 55000, 80000, 48000, 90000, 65000]

plt.scatter(ages, salaries, color="purple", marker="o", s=80)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary (USD)")
plt.grid(True)

plt.show()
