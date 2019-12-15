"""
Simple timer GUI application using tkinter.

Author: Jack Brokenshire
Date: 15/12/2019
"""

# Standard import
import time

# Third-party imports
import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
    """"Simple timer application using tkinter."""
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.build_interface()

    def build_interface(self):
        """The interface function."""
        self.clock = tk.Label(self)
        self.clock.grid(row=1)

        self.power_button = tk.Button(self, text="Start", command=lambda: self.timer(3600))
        self.power_button.grid(row=2, column=0)

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=2, column=1)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=2, column=3)

        root.bind("<Return>", lambda: self.timer(t=3600))

    def timer(self, t):
        """Calculates the time to be displayed"""
        while t:
            hours = t // 3600
            mins = (t // 60) % 60 
            secs = t % 60
            self.clock.config(text="{:02d}:{:02d}:{:02d}".format(hours, mins, secs))
            t -= 1
            self.clock.after(200, self.timer)

    def reset(self):
        """Resets the timer to 0."""
        self.clock["text"] = "00:00:00"

    def quit(self):
        """Ask user if they want to close program. If yes closes, if no goes back to timer."""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
   

if __name__ == "__main__":
    """Main loop which creates program."""
    root = tk.Tk()
    root.title("TIMER")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()