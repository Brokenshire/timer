from tkinter import *
import time
import tkinter.messagebox


class Countdown:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.running = False
        self.time1 = ''
        self.prevSec = ''
        self.mins = 10
        self.secs = 0
        self.hours = 0

        self.clock = Label(frame, width=7, font=('fixed', 20))
        self.clock.grid(row=1, columnspan=9, padx=5, pady=(5, 2))
        self.tick()

        self.plusButton = Button(frame, text="+", command=self.pluscountdown)
        self.plusButton.grid(row=2, column=1)

        self.minusButton = Button(frame, text="-", command=self.minuscountdown)
        self.minusButton.grid(row=2, column=2)

        self.startButton = Button(frame, text="Start", command=self.startcountdown)
        self.startButton.grid(row=2, column=3)

        self.stopButton = Button(frame, text="Stop", command=self.stopcountdown, state="disabled")
        self.stopButton.grid(row=2, column=4)

        self.resetButton = Button(frame, text="Reset", command=self.resetcountdown, state="disabled")
        self.resetButton.grid(row=2, column=5)

        self.quitButton = Button(frame, text="Quit", command=self.quitcountdown)
        self.quitButton.grid(row=2, column=6)

    def tick(self):
        if self.running == True:
            self.newSec = time.strftime('%H:%M:%S')
        else:
            self.newSec = ''
            self.prevSec = ''
        if self.newSec != self.prevSec:
            self.prevSec = self.newSec
            self.secs = self.secs - 1
            if self.secs < 0:
                self.secs = 59
                self.mins = self.mins - 1
                if self.mins < 0:
                    self.mins = 59
                    self.hours = self.hours - 1
                    if self.hours < 0:
                        self.hours = 0
                        self.mins = 0
                        self.secs = 0
                        self.plusButton.config(state="normal")
                        self.minusButton.config(state="normal")
                        self.startButton.config(state="normal")
                        self.stopButton.config(state="disabled")
                        self.resetButton.config(state="normal")
                        self.quitButton.config(state="normal")
        self.time2 = ('%02d:%02d:%02d' % (self.hours, self.mins, self.secs))
        if self.time2 != self.time1:
            self.time1 = self.time2
            self.clock.config(text=self.time2)
        self.clock.after(200, self.tick)

    def pluscountdown(self):
        self.mins = self.mins + 1
        if self.secs > 60:
            self.secs = 0
            self.mins = self.mins + 1
            if self.mins > 60:
                self.mins = 0
                self.hours = self.hours + 1
                if self.hours > 60:
                    self.hours = 0
                    self.mins = 0
                    self.secs = 0
        self.resetButton.config(state="normal")

    def minuscountdown(self):
        self.mins = self.mins - 1
        if self.secs < 0:
            self.secs = 60
            self.mins = self.mins - 1
            if self.mins < 0:
                self.mins = 60
                self.hours = self.hours - 1
                if self.hours < 0:
                    self.hours = 0
                    self.mins = 0
                    self.secs = 0
        self.resetButton.config(state="normal")

    def startcountdown(self):
        self.running = True
        self.plusButton.config(state="disabled")
        self.minusButton.config(state="disabled")
        self.startButton.config(state="disabled")
        self.stopButton.config(state="normal")
        self.resetButton.config(state="disabled")
        self.quitButton.config(state="disabled")

    def stopcountdown(self):
        self.running = False
        self.plusButton.config(state="normal")
        self.minusButton.config(state="normal")
        self.startButton.config(state="normal")
        self.stopButton.config(state="disabled")
        self.resetButton.config(state="normal")
        self.quitButton.config(state="normal")

    def resetcountdown(self):
        self.hours = 0
        self.mins = 10
        self.secs = 0
        self.prevSec = ''
        self.time1 = ''
        self.running = False
        self.plusButton.config(state="normal")
        self.minusButton.config(state="normal")
        self.startButton.config(state="normal")
        self.stopButton.config(state="disabled")
        self.resetButton.config(state="disabled")
        self.quitButton.config(state="normal")

    def quitcountdown(self):
        self.mExit = tkinter.messagebox.askokcancel(title="Quit", message="Are you sure?")
        print(self.mExit)
        if self.mExit > 0:
            root.destroy()
            return


root = Tk()
root.title("Scoreboard")
c = Countdown(root)
root.geometry("200x80+0+0")
root.resizable(0, 0)
root.mainloop()
