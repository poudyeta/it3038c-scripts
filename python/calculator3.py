import tkinter as tk
from tkinter import ttk

#Calculate function which handles the equation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_var.set(result)

        #Log to log file
        with open("log.txt", "a") as log_file:
            log_file.write(f"{expression} = {result}\n")
    except Exception as e:
        result_var.set("Error")

#clear when C is clicked
def clear():
    entry.delete(0, tk.END)
    result_var.set("")

#Adds new operation to current equation when nunbers/operations clicked
def extend(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

#create main window
app = tk.Tk()
app.title("TP Calculator")

# Entry widget for input
entry = ttk.Entry(app, justify="right", font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Result Var
result_var = tk.StringVar()

# Label to display the result
result_label = ttk.Label(app, textvariable=result_var, font=('Arial', 14))
result_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_val = 2
col_val = 0

#Places buttons
for button in buttons:
    ttk.Button(app, text=button, command=lambda b=button: extend(b)).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

#Clear Teext
ttk.Button(app, text="C", command=clear).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

# Calculate result
ttk.Button(app, text="=", command=calculate).grid(row=row_val + 1, column=col_val, columnspan=4, sticky="nsew", padx=5, pady=5)

#Make window expand proportioportionally
for i in range(6):
    app.grid_rowconfigure(i, weight=1)
    app.grid_columnconfigure(i, weight=1)

# Run the application
app.mainloop()
