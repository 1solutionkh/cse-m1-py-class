import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")  # width x height

# Add a label
label = tk.Label(window, text="Hello, World!")
label.pack(pady=10)

# Add a button


def on_click():
    label.config(text="Button clicked!")


button = tk.Button(window, text="Click Me", command=on_click)
button.pack()

# Start the event loop
window.mainloop()
