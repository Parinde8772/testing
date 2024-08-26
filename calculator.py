import tkinter as tk
from tkinter import ttk
from math import *

# Initialize variables
trig_functions = False  # Default state

def handle_trig_function(symbol):
    if trig_functions:
        # Handle inverse trigonometric functions separately
        expression = f"{symbol}("  # For example, tan⁻¹(5)
    else:
        expression = symbol

    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + expression)

# Add trig_functions toggle in evaluate_expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        store_ans(result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Modify the button_click function to call handle_trig_function
def button_click(symbol):
    if symbol in trig_operations + trig_inverse_operations:
        handle_trig_function(symbol)
    elif symbol != '=':
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + str(symbol))
    else:
        evaluate_expression()

def clear_entry():
    entry.delete(0, tk.END)

def toggle_operations():
    global trig_functions
    trig_functions = not trig_functions
    update_operation_buttons()

def store_ans(value):
    global ans_value
    ans_value = value

def retrieve_ans():
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(ans_value))

def get_operations():
    if trig_functions:
        return trig_inverse_operations
    else:
        return trig_operations

def update_operation_buttons():
    for btn, operation in zip(operation_buttons, get_operations()):
        btn.config(text=operation)




def update_trig_buttons():
    for btn, operation in zip(operation_buttons, trig_inverse_operations if trig_functions else trig_operations):
        btn.config(command=lambda op=operation: button_click(op), text=operation)

# Define trigonometric functions
trig_operations = ['tan', 'sin', 'cos']
trig_inverse_operations = ['tan⁻¹', 'sin⁻¹', 'cos⁻¹']

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x500")  # Set initial window size

# Apply a themed style
style = ttk.Style()
style.theme_use('clam')

# Set a custom style for the buttons
style.configure('TButton', padding=10, font=('Arial', 12))

# Create an entry widget for displaying the expression and results
entry = ttk.Entry(window, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=7, sticky="nsew", padx=10, pady=10)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('(', 1, 4), (')', 2, 4),
    ('log', 3, 4), ('e^', 5, 3)
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    btn = ttk.Button(window, text=text, style='TButton',
                     command=lambda t=text: button_click(t) if t != '=' else evaluate_expression() if t == '=' else retrieve_ans())
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Create a switch button
switch_button = ttk.Button(window, text='Shift', style='TButton', command=toggle_operations)
switch_button.grid(row=4, column=4, sticky="nsew", padx=5, pady=5)

# Create a Clear button
clear_button = ttk.Button(window, text='C', style='TButton', command=clear_entry)
clear_button.grid(row=5, column=4, sticky="nsew", padx=5, pady=5)

# Create operation buttons
operation_buttons = []
for i, operation in enumerate(get_operations()):
    btn = ttk.Button(window, text=operation, style='TButton', command=lambda op=operation: button_click(op))
    btn.grid(row=5, column=i, sticky="nsew", padx=5, pady=5)
    operation_buttons.append(btn)

# Configure row and column weights so that they expand proportionally
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Run the application
window.mainloop()