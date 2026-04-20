print("--- File Error Handling ---")

filename = input("Enter file name to read: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("--- File Content ---")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")

except IsADirectoryError:
    print(f"Error: '{filename}' is a folder, not a file.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("No file to close.")
