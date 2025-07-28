import tkinter as tk

# Function to update the expression in the entry widget
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current + key)  # Append the key to the current expression

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)  # Show the result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Show error for invalid expressions

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)  # Clear the expression

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget where the expression will be displayed
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Create the buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 20), command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 20), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=lambda key=text: press(key))
    button.grid(row=row, column=col)

# Run the Tkinter event loop
root.mainloop()
