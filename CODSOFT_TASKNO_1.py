from tkinter import *

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
            else:
                result = num1 / num2
        else:
            result_label.config(text="Invalid operator")
            return

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = Tk()
window.title("Simple Calculator")
window.geometry("300x200")

# Create labels and entry fields
label1 = Label(window, text="Number 1:")
label1.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1)

label2 = Label(window, text="Number 2:")
label2.grid(row=1, column=0)
entry2 = Entry(window)
entry2.grid(row=1, column=1)

# Create operator selection
operator_var = StringVar(window)
operator_var.set("+")  # Default operator
operator_menu = OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=2, column=0)

# Create calculate button
calculate_button = Button(window, text="=", fg="blue", command=calculate)
calculate_button.grid(row=2, column=1)

# Create result label
result_label = Label(window, text="Result:")
result_label.grid(row=3, column=0, columnspan=2)

# Run the GUI
window.mainloop()