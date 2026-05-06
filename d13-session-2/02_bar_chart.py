import matplotlib.pyplot as plt

# Bar chart: salary by city
cities = ["NY", "LA", "Chicago", "Houston"]
salaries = [62500, 70000, 55000, 60000]

plt.bar(cities, salaries, color=["red", "green", "blue", "orange"])

plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Salary (USD)")

plt.show()
