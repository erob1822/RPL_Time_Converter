import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
import threading

# List of common timezones
TIMEZONES = [
    'UTC',
    'America/New_York',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney',
    'Europe/Paris',
    'America/Los_Angeles',
    'Asia/Kolkata',
    'America/Chicago',
    'Europe/Berlin',
]

def get_time_in_timezone(tz_name):
    tz = pytz.timezone(tz_name)
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

def get_utc_time():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title('UTC & Local Time Clock')

        # Timezone dropdown
        self.tz_var = tk.StringVar(value='UTC')
        ttk.Label(root, text='Select Timezone:').grid(row=0, column=0, padx=5, pady=5)
        self.tz_menu = ttk.Combobox(root, textvariable=self.tz_var, values=TIMEZONES, state='readonly')
        self.tz_menu.grid(row=0, column=1, padx=5, pady=5)

        # UTC Time
        ttk.Label(root, text='UTC Time:').grid(row=1, column=0, padx=5, pady=5)
        self.utc_label = ttk.Label(root, text='')
        self.utc_label.grid(row=1, column=1, padx=5, pady=5)

        # Local Time
        ttk.Label(root, text='Local Time:').grid(row=2, column=0, padx=5, pady=5)
        self.local_label = ttk.Label(root, text='')
        self.local_label.grid(row=2, column=1, padx=5, pady=5)

        self.update_clock()

    def update_clock(self):
        utc_time = get_utc_time()
        local_time = get_time_in_timezone(self.tz_var.get())
        self.utc_label.config(text=utc_time)
        self.local_label.config(text=local_time)
        self.root.after(1000, self.update_clock)

def main():
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
