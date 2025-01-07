import tkinter as tk
import time

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")

        # Interface graphique
        self.label = tk.Label(root, font=('Arial', 80), foreground='cyan', background='black')
        self.label.pack(anchor='center', pady=20)

        self.label_alarm = tk.Label(root, font=('Arial', 20), foreground='red', background='black')
        self.label_alarm.pack(anchor='center', pady=10)

        self.create_time_controls()
        self.create_alarm_controls()
        self.create_buttons()

    def create_time_controls(self):
        """Create the fields to set the time."""
        frame_time = tk.Frame(self.root)
        frame_time.pack(pady=10)
        tk.Label(frame_time, text="Set Time (HH:MM:SS):").grid(row=0, column=0)
        self.entry_hour = tk.Entry(frame_time, width=5)
        self.entry_hour.grid(row=0, column=1)
        self.entry_minute = tk.Entry(frame_time, width=5)
        self.entry_minute.grid(row=0, column=2)
        self.entry_second = tk.Entry(frame_time, width=5)
        self.entry_second.grid(row=0, column=3)
        tk.Button(frame_time, text="Set Time", command=self.set_time).grid(row=0, column=4)

    def create_alarm_controls(self):
        """Create the fields to set the alarm."""
        frame_alarm = tk.Frame(self.root)
        frame_alarm.pack(pady=10)
        tk.Label(frame_alarm, text="Set Alarm (HH:MM:SS):").grid(row=0, column=0)
        self.entry_alarm_hour = tk.Entry(frame_alarm, width=5)
        self.entry_alarm_hour.grid(row=0, column=1)
        self.entry_alarm_minute = tk.Entry(frame_alarm, width=5)
        self.entry_alarm_minute.grid(row=0, column=2)
        self.entry_alarm_second = tk.Entry(frame_alarm, width=5)
        self.entry_alarm_second.grid(row=0, column=3)
        tk.Button(frame_alarm, text="Set Alarm", command=self.set_alarm).grid(row=0, column=4)

    def create_buttons(self):
        """Create the buttons to select the format and pause the clock.."""
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        self.format_choice_var = tk.StringVar()
        self.format_choice_var.set("24h")
        format_menu = tk.OptionMenu(frame_buttons, self.format_choice_var, "12h", "24h")
        format_menu.grid(row=0, column=0)
        tk.Button(frame_buttons, text="Pause/Start", command=self.toggle_pause).grid(row=0, column=1)

    def set_time(self):
        """Dummy function to simulate setting the time"""
        pass

    def set_alarm(self):
        """Dummy function to simulate setting the alarm"""
        pass

    def toggle_pause(self):
        """Dummy function to simulate pausing the clock"""
        pass


