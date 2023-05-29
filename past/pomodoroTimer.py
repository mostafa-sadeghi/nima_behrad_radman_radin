import tkinter as tk
from tkinter import ttk
from collections import deque


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("pomodoroTimer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        timer_frame = Timer(container)
        timer_frame.grid(row=0, column=0, sticky="nsew")


class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_time = tk.StringVar(value="01:10")
        self.timer_running = False
        self._timer_decrement_job = None
        self.timer_order = ["Pomodoro",
                            "short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        self.current_timer_label = tk.StringVar(value=self.timer_schedule[0])
        timer_description = ttk.Label(
            self, textvariable=self.current_timer_label)
        timer_description.grid(row=0, column=0, sticky="w")

        button_container = ttk.Frame(self)
        button_container.grid(column=0, row=2, sticky="ew")

        self.start_button = ttk.Button(
            button_container, text="start", command=self.start_timer, cursor="hand2")
        self.start_button.grid(row=0, column=0, sticky="ew")
        self.stop_button = ttk.Button(
            button_container, text="stop", command=self.stop_timer, cursor="hand2", state="disable")
        self.stop_button.grid(row=0, column=1, sticky="ew")
        reset_button = ttk.Button(
            button_container, text="reset", command=self.reset_timer, cursor="hand2")
        reset_button.grid(row=0, column=2, sticky="ew")

        timer_frame = ttk.Frame(self, height="100")
        timer_frame.grid(pady=(10, 0), sticky="nsew", column=0, row=1)
        timer_counter = ttk.Label(timer_frame, textvariable=self.current_time)
        timer_counter.grid()
        # self.decrement_time()

    def reset_timer(self):
        self.stop_timer()
        self.current_time.set("01:00")
        self.timer_schedule = deque(self.timer_order)
        self.current_timer_label.set(self.timer_schedule[0])

    def start_timer(self):
        self.timer_running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "enabled"
        self.decrement_time()

    def stop_timer(self):
        self.timer_running = False
        self.start_button["state"] = "enabled"
        self.stop_button["state"] = "disabled"
        if self._timer_decrement_job:
            self.after_cancel(self._timer_decrement_job)
            self._timer_decrement_job = None

    def decrement_time(self):
        current_time = self.current_time.get()
        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1

            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self._timer_decrement_job = self.after(1000, self.decrement_time)

        elif self.timer_running and current_time == "00:00":
            self.timer_schedule.rotate(-1)
            next_up = self.timer_schedule[0]
            self.current_timer_label.set(next_up)
            if next_up == "Pomodoro":
                self.current_time.set("01:00")
            elif next_up == "short Break":
                self.current_time.set("00:30")
            elif next_up == "Long Break":
                self.current_time.set("15:00")
            self._timer_decrement_job = self.after(1000, self.decrement_time)


app = PomodoroTimer()
app.mainloop()
