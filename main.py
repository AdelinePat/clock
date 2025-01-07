#main.py
import tkinter as tk
from clockApp import ClockApp


if __name__ == "__main__":
        root = tk.Tk()
        app = ClockApp(root)
        root.mainloop()