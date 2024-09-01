




from datetime import datetime
# counstrucror= name inside it we but name,start date and if it comoleted or not
class Habit:
    def __init__(self, name, start_date=None, completed=False):
        self.name = name
        self.start_date = start_date if start_date else datetime.now().strftime("%Y-%m-%d")
        self.completed = completed

# we have here two functoion -- mark completed they return if i completred habit,2 str they will return name ,start date and completed of habit
    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.name},{self.start_date},{self.completed}"