import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_task():
    task = entry.get()
    if task:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        listbox.insert(tk.END, f"{task} (Created: {current_time})")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all_tasks():
    listbox.delete(0, tk.END)

def update_task():
    selected_task = listbox.curselection()
    updated_task = entry.get()

    if selected_task and updated_task:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        listbox.delete(selected_task)
        listbox.insert(tk.END, f"{updated_task} (Updated: {current_time})")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task and enter an update.")

def track_progress():
    selected_task = listbox.curselection()
    if selected_task:
        task_text = listbox.get(selected_task)
        messagebox.showinfo("Task Progress", f"Task Information:\n{task_text}")
    else:
        messagebox.showwarning("Warning", "Please select a task to track.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create widgets
entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
clear_button = tk.Button(root, text="Clear All", command=clear_all_tasks)
update_button = tk.Button(root, text="Update Task", command=update_task)
track_button = tk.Button(root, text="Track Progress", command=track_progress)
listbox = tk.Listbox(root, selectmode=tk.SINGLE)

# Place widgets in the window
entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)
update_button.pack(pady=5)
track_button.pack(pady=5)
listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
