import json
import os

FILEPATH = "planner.json"

# Days and periods
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
PERIODS = ['morning', 'afternoon', 'evening']

# Default structure
default_planner = {day: {period: [] for period in PERIODS} for day in DAYS}

def get_planner(filepath=FILEPATH):
    """Returns the planner dict from file, or creates a default one if not found."""
    if not os.path.exists(filepath):
        save_planner(default_planner, filepath)
        return default_planner
    with open(filepath, 'r') as file:
        return json.load(file)

def save_planner(planner_dict, filepath=FILEPATH):
    """Writes the planner dict to a file."""
    with open(filepath, "w") as file:
        json.dump(planner_dict, file, indent=4)

def is_valid_day_period(day, period):
    """Helper to check if the day and period are valid."""
    return day.lower() in DAYS and period.lower() in PERIODS

def add_task_to_specific_day(planner_dict, day, period, task_to_add):
    """Adds a task to a given day and period."""
    day, period = day.lower(), period.lower()
    if is_valid_day_period(day, period):
        planner_dict[day][period].append(task_to_add)

def access_specific_todos(planner_dict, day, period):
    """Returns the list of tasks for a specific day and period."""
    day, period = day.lower(), period.lower()
    if is_valid_day_period(day, period):
        return planner_dict[day][period]
    return []

def remove_task(planner_dict, day, period, task):
    """Removes a task from a specific day and period."""
    day, period = day.lower(), period.lower()
    if is_valid_day_period(day, period):
        try:
            planner_dict[day][period].remove(task)
        except ValueError:
            pass  # Task wasn't in list — fail silently or log