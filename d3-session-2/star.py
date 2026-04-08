n = int(input("Enter number of rows: "))

# Right triangle
print("Right Triangle:")
for i in range(1, n + 1):
    print("*" * i)

# Inverted triangle
print("\nInverted Triangle:")
for i in range(n, 0, -1):
    print("*" * i)

# Pyramid
print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
