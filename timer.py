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
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        """The interface function."""
        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=0)

        self.clock = tk.Label(self, text="00:00:00", font=("Courier", 15), width=10)
        self.clock.grid(row=1, column=1)

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=2, column=0)

        self.stop_button = tk.Button(self, text="Stop", command=lambda: self.stop())
        self.stop_button.grid(row=2, column=1)

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=2, column=2)

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=2, column=3)

        self.master.bind("<Return>", lambda: self.start())

    def timer(self):
        """Calculates the time to be displayed"""
        if self.running == True:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
            else:
                self.hours = self.time // 3600
                self.mins = (self.time // 60) % 60 
                self.secs = self.time % 60
                self.clock.configure(text="{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs))
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        """Begins the timer"""
        self.time = int(self.time_entry.get())
        self.power_button.configure(text ="Stop", command=lambda: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text ="Start", command=lambda: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 0."""
        self.running = False
        self.clock["text"] = "00:00:00"

    def quit(self):
        """Ask user if they want to close program."""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
   

if __name__ == "__main__":
    """Main loop which creates program."""
    root = tk.Tk()
    root.title("TIMER")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()