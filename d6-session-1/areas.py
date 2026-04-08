
def area_rectangle(length, width):
    return length * width


def area_triangle(base, height):
    return 0.5 * base * height


print("--- Area Calculator ---")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Choose a shape: ")

if choice == "1":
    r = float(input("Enter radius: "))
    print("Area of circle:", area_circle(r))

elif choice == "2":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle:", area_rectangle(l, w))

elif choice == "3":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of triangle:", area_triangle(b, h))

else:
    print("Invalid choice.")
