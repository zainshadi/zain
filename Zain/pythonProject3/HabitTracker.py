
from Habit import Habit
# in self habit [] we store all habits
class HabitTracker:
    def __init__(self):
        self.habits = []
# we have here 3 functoin
    def add_habit(self, name):
        habit = Habit(name)
        self.habits.append(habit)


    def remove_habit(self, name):
        self.habits = [habit for habit in self.habits if habit.name != name]

    def mark_habit_completed(self, name):
        for habit in self.habits:
            if habit.name == name:
                habit.mark_completed()

    def save_to_file(self, filename="data.txt"):
        with open(filename, 'a') as file:
            for habit in self.habits:
                file.write(f"{habit.name},{habit.start_date},{habit.completed}\n")

    def load_from_file(self, filename="data.txt"):
        try:
            with open(filename, 'r') as file:
                self.habits = []
                for line in file:
                    name, start_date, completed = line.strip().split(',')
                    habit = Habit(name, start_date, completed == 'True')
                    self.habits.append(habit)
        except FileNotFoundError:
            pass
