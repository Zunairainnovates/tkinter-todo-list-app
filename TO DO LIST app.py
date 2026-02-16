import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task can't be empty!")

def delete_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_tasks():
    task_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
task_list = tk.Listbox(root, width=40)
task_list.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_task).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_tasks).pack(pady=5)

root.mainloop()