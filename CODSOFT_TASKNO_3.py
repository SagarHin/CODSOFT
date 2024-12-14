from tkinter import *
import random

def play_game():
    """Plays a single round of Rock-Paper-Scissors."""
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text=result_label.cget("text") + "\nIt's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text=result_label.cget("text") + "\nYou win!")
    else:
        result_label.config(text=result_label.cget("text") + "\nYou lose!")

# Create the main window
window = Tk()
window.title("Rock-Paper-Scissors")
window.geometry("300x200")

# Create labels and options
user_choice_var = StringVar(window)
user_choice_var.set("rock")  # Default choice

choice_label = Label(window, text="Choose:")
choice_label.grid(row=0, column=0)

choice_menu = OptionMenu(window, user_choice_var, "rock", "paper", "scissors")
choice_menu.grid(row=0, column=1)

play_button = Button(window, text="Play", command=play_game)
play_button.grid(row=1, column=0, columnspan=2)

result_label = Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2)

# Run the GUI
window.mainloop()