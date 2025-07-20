task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
message = f"{task}"

match priority:
    case "high":
        message += " is a high priority task"
    case "medium":
        message += " is a medium priority task"
    case "low":
        message += " is a low priority task"
    case _:
        message += " has an unknown priority"
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += " Consider completing it when you have free time."
print(f"Reminder: {message}") 