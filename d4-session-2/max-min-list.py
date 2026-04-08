n = int(input("Enter number of elements: "))

numbers = []
for i in range(n):
    val = float(input("Enter a number: "))
    numbers.append(val)

print("List:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
