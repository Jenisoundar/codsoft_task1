import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.pack(pady=10)
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.task_list = tk.Listbox(self.master, width=50)
        self.task_list.pack(pady=10)
        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        self.populate_tasks()
    
    def populate_tasks(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.populate_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")
    
    def update_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[index] = updated_task
                self.populate_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter an updated task.")
        else:
            messagebox.showerror("Error", "Please select a task to update.")
    
    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.populate_tasks()
        else:
            messagebox.showerror("Error", "Please select a task to delete.")

# Create main window
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
