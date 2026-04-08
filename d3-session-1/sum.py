n = int(input("Enter a number: "))

total = int(input("Enter total: "))

for i in range(1, n + 1):
    print(i)
    total += i

print("Sum of 1 to", n, "is:", total)
