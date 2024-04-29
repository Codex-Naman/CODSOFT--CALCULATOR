import tkinter as tk
import math

# Function to calculate square root
def calculate_sqrt(expr):
    if '√' in expr:
        expr = expr.replace('√', math.sqrt)
        return eval(expr)
    else:
        return None

# Function to evaluate the expression
def calculate():
    try:
        expr = expression.get()
        result = calculate_sqrt(expr)
        if result is None:
            result = eval(expr)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Result: Error")

# Function to clear the expression
def clear():
    expression.set("")
    result_label.config(text="Result: ")

# Function to delete the last character
def backspace():
    current_expression = expression.get()
    expression.set(current_expression[:-1])

# Function to add character to expression
def add_to_expression(char):
    current_expression = expression.get()
    if char == '√':
        expression.set(current_expression + char)
    else:
        expression.set(current_expression + char)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.config(bg="black")
root.geometry("680x486+100+100")

# Entry widget to display the expression
expression = tk.StringVar()
entry = tk.Entry(root, textvariable=expression, bg="grey", font=('Arial', 20), bd=5, relief=tk.GROOVE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Labels to display the result
result_label = tk.Label(root, text="Result: ", bg="grey", fg="white", font=('Arial', 14), bd=5, relief=tk.GROOVE, anchor=tk.W)
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

# Buttons for numbers and operations
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), 
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, bg="grey", font=('Arial', 16), width=5, height=2,
                       command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button
clear_button = tk.Button(root, text="C", bg="red", font=('Arial', 16), width=5, height=2,
                         command=clear)
clear_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

# Backspace button
backspace_button = tk.Button(root, text="DEL", bg="red", font=('Arial', 16), width=5, height=2,
                             command=backspace)
backspace_button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

# Equal button
equal_button = tk.Button(root, text="=", font=('Arial', 16), bg="orange", width=5, height=2,
                         command=calculate)
equal_button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

# Configuring row and column weights
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()

