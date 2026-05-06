import matplotlib.pyplot as plt

# Simple line chart: y = x squared
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, color="blue", linestyle="--", marker="o", label="y = x²")

plt.title("Line Plot Example")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid(True)

plt.show()
