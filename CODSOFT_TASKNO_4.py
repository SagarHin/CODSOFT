from tkinter import *

def add_task():
    """Adds a new task to the list and updates the GUI."""
    new_task = task_entry.get()
    if new_task:
        tasks.append(new_task)
        task_list.insert(END, new_task)
        task_entry.delete(0, END) 

def remove_task():
    """Removes the selected task from the list and updates the GUI."""
    try:
        selected_index = task_list.curselection()[0]
        del tasks[selected_index]
        task_list.delete(selected_index) 
    except IndexError:
        pass

# Create the main window
window = Tk()
window.title("To-Do List")

# Create a listbox to display tasks
tasks = [] 
task_list = Listbox(window, selectmode=SINGLE)
task_list.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

# Create an entry field for new tasks
task_entry = Entry(window, width=30)
task_entry.grid(row=0, column=1, padx=10, pady=10)

# Create buttons
add_button = Button(window, text="Add Task", command=add_task)
add_button.grid(row=1, column=1)

remove_button = Button(window, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=1)

# Run the GUI
window.mainloop()