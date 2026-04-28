import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("350x400")
window.resizable(False, False)

# Entry widget to display numbers and results
display = tk.Entry(window, font=("Arial", 20), borderwidth=2,
                   relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10,
             ipady=10, sticky="we")

# Function to handle button clicks


def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

# Function to clear the display


def clear():
    display.delete(0, tk.END)

# Function to calculate the result


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button layout: (text, row, column)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3),
]

# Create number and operator buttons
for (text, row, col) in buttons:
    btn = tk.Button(window, text=text, font=("Arial", 16),
                    width=5, height=2,
                    command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=2, pady=2)

# Equals button
equals_btn = tk.Button(window, text="=", font=("Arial", 16),
                       width=5, height=2, bg="lightblue",
                       command=calculate)
equals_btn.grid(row=4, column=2, padx=2, pady=2)

# Clear button (spans across the bottom)
clear_btn = tk.Button(window, text="Clear", font=("Arial", 16),
                      bg="salmon", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=2, pady=5,
               sticky="we")

# Start the GUI
window.mainloop()
