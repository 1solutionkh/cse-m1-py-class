print("--- Read and Count Words ---")

filename = input("Enter file name to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    print("\n--- File Content ---")
    print(content)

    words = content.split()
    lines = content.splitlines()
    characters = len(content)

    print("\n--- Statistics ---")
    print("Total lines:     ", len(lines))
    print("Total words:     ", len(words))
    print("Total characters:", characters)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print("Unexpected error:", e)
