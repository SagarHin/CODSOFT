from tkinter import *
import random
import string

def generate_password():
    """Generates a random password based on user input."""
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            result_label.config(text="Password length must be greater than 0.")
            return

        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for _ in range(password_length))
        result_label.config(text="Generated Password: " + password)

    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry("300x150")

# Create labels and entry fields
length_label = Label(window, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = Entry(window)
length_entry.grid(row=0, column=1)

# Create generate button
generate_button = Button(window, text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2)

# Create result label
result_label = Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2)

# Run the GUI
window.mainloop()