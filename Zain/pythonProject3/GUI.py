import tkinter as tk
from tkinter import messagebox
from HabitTracker import HabitTracker

class HabitTrackerApp:
    def __init__(self, root):
        self.tracker = HabitTracker()
        self.root = root
        self.root.title("Habit Tracker")

        self.habit_name_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):



        tk.Label(self.root, text="Habit Name:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.habit_name_var).grid(row=0, column=1)

        tk.Button(self.root, text="Add Habit", command=self.add_habit).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Mark Completed", command=self.mark_habit_completed).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Remove Habit", command=self.remove_habit).grid(row=3, column=0, columnspan=2)
        tk.Button(self.root, text="Save Habits", command=self.save_habits).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Load Habits", command=self.load_habits).grid(row=5, column=0, columnspan=2)

        self.habits_listbox = tk.Listbox(self.root)
        self.habits_listbox.grid(row=6, column=0, columnspan=2)

    def add_habit(self):
        habit_name = self.habit_name_var.get()
        if habit_name:
            self.tracker.add_habit(habit_name)
            self.habits_listbox.insert(tk.END, habit_name)
            self.habit_name_var.set("")
        else:
            messagebox.showwarning("Warning", "Habit name cannot be empty.")

    def mark_habit_completed(self):
        selected_habit_index = self.habits_listbox.curselection()
        if selected_habit_index:
            habit_name = self.habits_listbox.get(selected_habit_index)
            self.tracker.mark_habit_completed(habit_name)
            messagebox.showinfo("Info", f"{habit_name} marked as completed.")
        else:
            messagebox.showwarning("Warning", "Select a habit to mark as completed.")

    def remove_habit(self):
        selected_habit_index = self.habits_listbox.curselection()
        if selected_habit_index:
            habit_name = self.habits_listbox.get(selected_habit_index)
            self.tracker.remove_habit(habit_name)
            self.habits_listbox.delete(selected_habit_index)
            messagebox.showinfo("Info", f"{habit_name} removed.")
        else:
            messagebox.showwarning("Warning", "Select a habit to remove.")

    def save_habits(self):
        self.tracker.save_to_file()
        messagebox.showinfo("Info", "Habits saved successfully.")

    def load_habits(self):
        self.tracker.load_from_file()
        self.habits_listbox.delete(0, tk.END)
        for habit in self.tracker.habits:
            self.habits_listbox.insert(tk.END, habit.name)

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()