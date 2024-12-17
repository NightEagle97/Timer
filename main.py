from tkinter import messagebox
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTk, set_appearance_mode, set_default_color_theme
import time

def convert_to_seconds(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def notify_task(task, duration):
    time.sleep(duration)
    tasks.remove((task, duration))
    tasks.append((task, duration))
    messagebox.showinfo("TIMES UP!!", f"It's Time To Do {task}")

def exit_program():
    root.destroy()

def update_count_label():
    count_label.configure(text=f"Tasks Added: {len(tasks)}")

def add_task():
    if not all((task_entry.get(), hour_entry.get(), min_entry.get(), sec_entry.get())):
        messagebox.showwarning("Input Error", "Please enter values for all fields")
        return

    tasks.append((task_entry.get(), convert_to_seconds(int(hour_entry.get()), int(min_entry.get()), int(sec_entry.get()))))
    update_count_label()

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = CTk()
root.title("Task Notifier")
root.geometry("400x500")

tasks = []

task_label = CTkLabel(root, text="Enter the Task to Notify For:")
task_label.pack()

task_entry = CTkEntry(root)
task_entry.pack()

hour_label = CTkLabel(root, text="Hours:")
hour_label.pack()

hour_entry = CTkEntry(root)
hour_entry.pack()

min_label = CTkLabel(root, text="Minutes:")
min_label.pack()

min_entry = CTkEntry(root)
min_entry.pack()

sec_label = CTkLabel(root, text="Seconds:")
sec_label.pack()

sec_entry = CTkEntry(root)
sec_entry.pack()

add_button = CTkButton(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

count_label = CTkLabel(root, text="Tasks Added: 0")
count_label.pack()

notify_button = CTkButton(root, text="Notify Me!", command=lambda: [notify_task(task, duration) for task, duration in tasks] if tasks else messagebox.showinfo("Input Error", "Please enter values for all fields"))
notify_button.pack(pady=20)

exit_button = CTkButton(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

root.mainloop()
