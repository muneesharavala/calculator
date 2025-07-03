import tkinter as tk
from tkinter import messagebox

# --- Calculation Functions ---
def calculate():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = x + y
        elif operation == "Subtract":
            result = x - y
        elif operation == "Multiply":
            result = x * y
        elif operation == "Divide":
            if y == 0:
                result = "Error! Division by zero."
            else:
                result = x / y
        elif operation == "Percentage":
            result = (x * y) / 100
        elif operation == "Power":
            result = x ** y
        elif operation == "Floor Division":
            if y == 0:
                result = "Error! Division by zero."
            else:
                result = x // y
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x400")
root.config(padx=20, pady=20)

# --- Widgets ---
tk.Label(root, text="Enter First Number:").pack()
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack(pady=5)

tk.Label(root, text="Choose Operation:").pack(pady=10)

operation_var = tk.StringVar(root)
operation_var.set("Add")  # default

operations = [
    "Add", "Subtract", "Multiply", "Divide",
    "Percentage", "Power", "Floor Division"
]

tk.OptionMenu(root, operation_var, *operations).pack()

tk.Button(root, text="Calculate", command=calculate, font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=15)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.pack(pady=10)

# --- Run the GUI ---
root.mainloop()
